# 需要加载的数据
# 1. word embeddings
# 2. entity embeddings
# 3. stop words
# 4. qa pairs
# 5. kb

# 预检查
# 1. kb的所有歧义entity
# 结论：目前的语料库将mention一样的实体都放在了一起，分不出来

# 进行的检查有
# 1. 是否 question 的所有词都有对应的 word embedding
# 2. 检查 kb 的所有属性是否都有对应的 word embedding

# 预检查
# 1. 歧义entity检查
# from src.Helper.KBReader import KBReader
# kb = KBReader.readAllRecords()
# for item in kb:
#     print(item.keys())
#     break
# mention_entities = {}
# entityid_mention = []
# entity_id = 0
# counter = 0
# for item in kb:
#     try:
#         counter += 1
#         if counter % 10000 == 0:
#             print("已遍历 " + str(counter) + " 个 entity")
#         entity_name = list(item.keys())[0]
#         entityid_mention.append(entity_name)
#         if mention_entities.get(entity_name):
#             mention_entities[entity_name].append(entity_id)
#         else:
#             mention_entities[entity_name] = [entity_id]
#         entity_id += 1
#     except:
#         pass

# 检查question的所有词、kb的属性词 是否都有embedding
from src.Helper.QAReader import QAReader
from src.vecModel.BaikeModel import BaikeVecModel
from src.Helper.KBReader import KBReader
import jieba
import time

print("数据准备阶段开始，正在加载 knowledge base...")
data_prepare_start = time.time()

kb = KBReader.readAllRecords()

print("\n正在加载 qa 对...")
qaReader = QAReader()
qa_pairs = qaReader.readAllPair('train')

print("\n正在加载 word embedding...")
baike_model = BaikeVecModel()
word_embeds = baike_model.loadAllWords()

data_prepare_end = time.time()
print("数据加载完毕，共耗时 "+ str(int(data_prepare_end - data_prepare_start)) + " 秒")

print("开始查找 kb 中没有 embedding 的属性")
kb_start = time.time()
un_encoded_words_attr = {}
# 1. kb的属性词是否有embedding
for item in kb:
    entity_name = list(item.keys())[0]
    entity      = item[entity_name]
    for attr in entity:
        if attr not in word_embeds:
            un_encoded_words_attr[attr] =  "【实体】"+entity_name
ques_start = time.time()
print("kb查找完毕，耗时" + str(int(ques_start - kb_start)) + " s, 共找到 " + str(len(un_encoded_words_attr)) + " 个没有embeddings的属性")
# 2. question的词是否有embedding
un_encoded_words_ques = {}
for pair in qa_pairs:
    question, answer = pair[0], pair[1]
    word_list = list(jieba.cut(question))
    for word in word_list:
        if word not in word_embeds:
            un_encoded_words_ques[word] = "【问题】" + question
ques_end = time.time()
print("question-answer pair 查找完毕，耗时" + str(int(ques_end - ques_start)) + " s, 共找到 " + str(len(un_encoded_words_ques)) + " 个没有embeddings的词")

attr_file = open('attr_unencoded.txt', 'w')
for attr in un_encoded_words_attr:
    attr_file.write(attr + ", " + un_encoded_words_attr[attr] + "\n")
attr_file.close()

ques_file = open('ques_unencoded.txt', 'w')
for ques in un_encoded_words_ques:
    ques_file.write(ques + ", "+un_encoded_words_ques[ques] + "\n")
ques_file.close()