from vecModel.BaikeModel import BaikeVecModel

model = BaikeVecModel()
# word_num, vec_size = model.getDataSize()
# print(word_num, vec_size)
# for i in range(0, word_num):
#     if i == 10:
#         break
#     word, vec = model.readOneWordEmbedding()
#     print(word, vec)

model.loadAllWords()
