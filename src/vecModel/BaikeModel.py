import sys
import os
sys.path.append(os.path.abspath('../'))
print(sys.path)
from Config import Config
from src.Helper.BinaryReader import BinaryReader
import time


class BaikeVecModel:

    def __init__(self):
        self.data_path = Config.getRootPath() + 'data/' + 'vectors/vectors_word'
        self.file = open(self.data_path, 'rb')
        self.words_num = int(BinaryReader.readStringWithoutBlank(self.file))
        self.vec_size  = int(BinaryReader.readStringWithoutBlank(self.file))
        self.vectors   = {}

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance = super(BaikeVecModel, cls).__new__(cls)
        return cls.instance

    def __del__(self):
        self.file.close()

    def refreshFilePointer(self):
        self.file.close()
        self.file = open(self.data_path, 'rb')
        self.words_num = int(BinaryReader.readStringWithoutBlank(self.file))
        self.vec_size = int(BinaryReader.readStringWithoutBlank(self.file))

    def getDataSize(self):
        return self.words_num, self.vec_size

    def readOneWordEmbedding(self):
        try:
            vec  = []
            word = BinaryReader.readStringWithBlank(self.file)
            for i in range(0, self.vec_size):
                vec.append(BinaryReader.readFloat(self.file))
            BinaryReader.readStringWithoutBlank(self.file)
            return word, vec
        except EOFError:
            return ['', []]
            pass

    def loadAllWords(self):
        try:
            print('开始加载embeddings，预计需要加载 '+ str(self.words_num) + ' 条数据')
            start_time = time.time()
            self.refreshFilePointer()
            self.vectors = {}
            counter = 0
            while 1:
                word, vec = self.readOneWordEmbedding()
                if word != '':
                    self.vectors[word] = vec
                    counter += 1
                    if counter %10000 == 0:
                        print("已加载 "+str(counter) + " 个vector")
                else:
                    break
            end_time = time.time()
            print('\n加载结束, 期望加载 ' + str(self.words_num) + ' 条数据， 实际加载 ' + str(counter) + '条,共耗时 '+ str(int(end_time - start_time)) + ' s')
        except EnvironmentError:
            pass

