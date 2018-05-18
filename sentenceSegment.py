import jieba
import jieba.posseg as posg
from src.Helper.KBReader import KBReader
from src.Helper.QAReader import QAReader

kbReader = KBReader()
qaReader = QAReader()

# 将所有的实体名都添加到 jieba 的词典中
kb = kbReader.readAllRecords()
counter = 0
for entity_name in kb:
    jieba.add_word(entity_name)
    if counter % 100000 == 0:
        print("已添加 " + str(counter) + " 个词")
    counter += 1

# 可以考虑把所有的实体属性也加到jieba的词典中

# 遍历qa对，查看分词结果
qa_result_file = open('log/qa_result_file.txt', 'w')
pairs   = qaReader.readAllPair('test')
counter = 0
for q,a in pairs:
    words = posg.cut(q)
    for word, flag in words:
        qa_result_file.write(word + " ")
    qa_result_file.write("\n")
    counter += 1
    if counter % 50 == 0:
        print(counter)
qa_result_file.close()