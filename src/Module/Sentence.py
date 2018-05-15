import jieba.posseg as pseg

class Sentence:
    def __init__(self, sentence):
        self.sentence = sentence

    def __str__(self):
        return self.sentence

    def drop_punctuation(self):
        new_sentence = ''
        words = pseg.cut(self.sentence)
        for word, flag in words:
            if (flag[0:1] not in ("x", "w")) or (flag[0:1] in ("，", "。", ",", "。")):
                new_sentence += word
        return Sentence(new_sentence)

    def dropWrap(self):
        drop_words = ["你说", "你知道","能告诉我","告诉我","请问","大家知道","请问一下","能问下","能问一下","问一下","请告诉我"]
        drop_words.extend(["吗","呢","呀","啊"])
        new_sentence = self.drop_punctuation().sentence
        for word in drop_words:
            new_sentence = new_sentence.strip(word)
        return Sentence(new_sentence)


# sentence = Sentence("你知道《机械设计基础》这本书的作者是谁吗?")
# sentence = sentence.dropWrap()
# print(sentence)