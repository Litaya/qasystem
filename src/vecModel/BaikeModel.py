import sys
import os
sys.path.append(os.path.abspath('../'))
print(sys.path)
from Config import Config
from src.Helper.BinaryReader import BinaryReader


class BaikeVecModel:

    def __init__(self):
        self.data_path = Config.getRootPath() + 'data/' + 'vectors/vectors_word'
        self.file = open(self.data_path, 'rb')
        self.words_num = int(BinaryReader.readStringWithoutBlank(self.file))
        self.vec_size  = int(BinaryReader.readStringWithoutBlank(self.file))

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance = super(BaikeVecModel, cls).__new__(cls)
        return cls.instance

    def __del__(self):
        self.file.close()

    def refreshFilePointer(self):
        self.file.close()
        self.file = open(self.data_path, 'rb')

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
