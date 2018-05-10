from src.Helper.QAReader import QAReader
from src.vecModel.BaikeModel import BaikeVecModel
from src.Helper.KBReader import KBReader
import jieba

qaReader = QAReader()
qa_pairs = qaReader.readAllPair('test')

baikeModel      = BaikeVecModel()
word_embeddings = baikeModel.loadAllWords()

un_encoded_words = []
counter = 0
print("\n================== 开始查找question的词embedding ==================")
for pair in qa_pairs:
    counter += 1
    if counter % 1000 == 0:
        print("已对比 "+ str(counter) + " 条qa对")
    question, answer = pair[0], pair[1]
    word_list = []
    word_list.extend(list(jieba.cut(question)))
    for word in word_list:
        if word not in word_embeddings:
            un_encoded_words.append(word)
    # break
print("结束查找，共对比 " + str(counter) + " 条qa对\n")

result_file = open('un_encoded_words.txt', 'w')
for word in un_encoded_words:
    result_file.write(word+'\n')
result_file.close()
#
# kbReader = KBReader()
# kbReader.readAllRecords()