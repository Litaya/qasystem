from src.Module.LtpParser import LtpParser
from src.Helper.QAReader import  QAReader
from src.Helper.KBReader import KBReader
from src.Module.Entity import Entity
from src.vecModel.BaikeModel import BaikeVecModel
import jieba
import json

parser = LtpParser()

vecModel = BaikeVecModel()
word_embeddings = vecModel.loadAllWords()

qaReader = QAReader()
pairs = qaReader.readAllPair('test')

kbReader = KBReader()
kb = kbReader.readAllRecords()

counter = 0
matched = 0
right   = 0
unmatched_file = open('log/unmatched.txt', 'w')
no_entity_file = open('log/no_entity.txt', 'w')
no_answer_file = open('log/no_answer.txt', 'w')
for q, a in pairs:
    counter += 1
    if counter % 50 == 0:
        break
    res = parser.analysis(q)
    if res and res[0] != '':
        # print(res)
        matched += 1
        entity_name, attribute = res[0], res[1]
        if kb.get(entity_name):
            entity = kb[entity_name]
            entity_obj = Entity(entity)
            answer_res = entity_obj.getAnswer(attribute, word_embeddings)
            # 目标匹配成功，但未找到answer
            if not answer_res:
                no_answer_file.write("【问题】：" + q + "\n")
                no_answer_file.write("【抽取结果】：" + entity_name + ", " + attribute+'\n' )
                no_answer_file.write("【匹配到的实体】: " + entity_name + "\n")
                for attribute in entity:
                    no_answer_file.write("\t" + attribute + "："+entity[attribute] + "\n")
                no_answer_file.write("======================\n")
                continue
            print(q)
            print(entity_name, attribute, answer_res)
            right += 1
        else:
            no_entity_file.write("【问题】"+q+"\n【抽取结果】"+res[0]+","+res[1]+"\n")
    else:
        unmatched_file.write(q+"\n")
print("accuracy: "+str(float(right)/float(matched)) + "\nrecall:"+str(float(right)/float(counter)))
print("共匹配 "+str(matched)+"条")