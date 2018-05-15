import json
import requests
from src.Module.Sentence import Sentence
from src.Module.Pattern import *

class LtpParser:
    def __init__(self):
        self.api_url = "https://api.ltp-cloud.com/analysis/"
        self.api_key = "s52646d6PKwzcMAJEt7zlU1yYFEzxLAZ2Eax1uAI"

    def analysis(self, sentence, pattern="all", form="json"):
        grammar_tree = self.get_grammar_tree(sentence, pattern, form)
        parent_child = {}
        root = -1
        for item in grammar_tree:
            if parent_child.get(item['parent']):
                parent_child[item['parent']].append(item['id'])
            else:
                parent_child[item['parent']] = [item['id']]
            if item['parent'] == -1:
                root = item['id']

        # 开始分析模板
        # 模板1: xx的xx是/在xx 《机械设计基础》这本书的作者是谁？
        # ATT SVB HED VOB 模式 和 SVB HED ATT VOB模式
        # 1,2,3
        pattern4 = Pattern4()
        pattern3 = Pattern3(pattern4)
        pattern2 = Pattern2(pattern3)
        pattern1 = Pattern1(pattern2)
        res = pattern1.handle(grammar_tree, parent_child, root)
        if res:
            attribute, entity = res[0], res[1]
            return attribute, entity

    def get_grammar_tree(self, sentence, pattern="all", form="json"):
        sentence = Sentence(sentence).drop_punctuation().dropWrap().sentence
        url = self.api_url + "?" + "api_key=" + self.api_key + "&text=" + sentence + "&pattern=" + pattern + "&format=" + form
        res = requests.get(url)
        decoder = json.JSONDecoder()
        return decoder.decode(res.text)[0][0]

