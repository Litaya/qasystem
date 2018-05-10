from src.Helper.QAReader import QAReader
from src.vecModel.BaikeModel import BaikeVecModel
import jieba

qaReader = QAReader()
qa_pairs = qaReader.readAllPair('test')

baikeModel      = BaikeVecModel()
word_embeddings = baikeModel.loadAllWords()

un_encoded_words = []
for pair in qa_pairs:
    question, answer = pair[0], pair[1]
    word_list = []
    word_list.extend(list(jieba.cut(question)))
    for word in word_list:
        if word not in word_embeddings:
            un_encoded_words.append(word)
    # break

result_file = open('un_encoded_words.txt', 'w')
for word in un_encoded_words:
    result_file.write(word+'\n')
result_file.close()