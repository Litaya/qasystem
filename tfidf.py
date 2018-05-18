# 使用tfidf抽取中心词
import jieba
from sklearn import feature_extraction
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
from src.Helper.QAReader import QAReader
from src.Helper.KBReader import KBReader
from src.Module.Entity import Entity
from src.Helper.StopWordsReader import StopWordsReader
from src.vecModel.BaikeModel import BaikeVecModel

def dropWordFromList(corpus_item, drop_word):
    words = corpus_item.split(' ')
    new_words = []
    for word in words:
        if word != drop_word and word not in stop_words:
            new_words.append(word)
    return new_words

stop_words= StopWordsReader.readAllStopWords()

vecModel = BaikeVecModel()
word_embeddings = vecModel.loadAllWords()

kbReader = KBReader()
kb = kbReader.readAllRecords()

counter = 0
for entity_name in kb:
    jieba.add_word(entity_name)
    counter += 1
    if counter % 100000 == 0:
        print("已添加 "+str(counter)+" 个词")

qaReader = QAReader()
pairs = qaReader.readAllPair('test')

corpus = []
for q, a in pairs:
    words = jieba.cut(q)
    corpus.append(" ".join(words))

vectorizer  = CountVectorizer()
transformer = TfidfTransformer()
tfidf=transformer.fit_transform(vectorizer.fit_transform(corpus))

words   = vectorizer.get_feature_names()
weights = tfidf.toarray()

entity_tfidf_result = open('log/entity_tfidf_result.txt', 'w')
entity_names = []
for i in range(0, len(weights)):
    max_weight = 0
    max_index  = -1
    for j in range(0, len(weights[0])):
        if weights[i][j] > max_weight:
            max_weight = weights[i][j]
            max_index  = j
    entity_tfidf_result.write(corpus[i]+"\n")
    entity_tfidf_result.write(words[max_index] + "\n\n")
    entity_names.append(words[max_index])
entity_tfidf_result.close()

no_entity_file    = open('log/no_entity_result.txt')
no_attribute_file = open('log/no_attribute_file.txt')
good_result_file  = open('log/good_result_file.txt')
for i in range(0, len(pairs)):
    entity_name = entity_names[i]
    if kb.get(entity_name):
        entity = kb[entity_name]
        entity_obj = Entity(entity)
        target_attributes = dropWordFromList(corpus[i], entity_name)
        res = entity_obj.getAnswerFromMultiTarget(target_attributes, word_embeddings)
        if not res:
            no_attribute_file.write("【问题】"+pairs[i][0]+'\n')
            no_attribute_file.write("【目标实体】"+entity_name + "\n")
            no_attribute_file.write("【全部属性】"+"\n")
            for att in entity:
                no_attribute_file.write("\t"+att+","+entity[att]+"\n")
        else:
            attribute, value, similarity = res
            good_result_file.write("【问题】" + pairs[i][0] + '\n')
            good_result_file.write("【目标实体】" + entity_name + "\n")
            good_result_file.write("【全部属性】" + "\n")
            for att in entity:
                good_result_file.write("\t" + att + "," + entity[att] + "\n")
            good_result_file.write("【匹配属性】" + attribute + ","+ value + ",\n")
            good_result_file.write("【相似度】"+str(similarity)+"\n")
    else:
        no_entity_file.write("【问题】" + pairs[i][0] + '\n')

no_entity_file.close()
no_attribute_file.close()
good_result_file.close()



