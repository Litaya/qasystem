from Config import Config
import re

class QAReader:
    def __init__(self):
        self.test_file = open(Config.getRootPath() + "data/qa/kbqa.testing-data", encoding='utf-8')
        print(self.test_file)
        self.train_file = open(Config.getRootPath() + "data/qa/kbqa.training-data", encoding='utf-8')

    def __del(self):
        self.test_file.close()
        self.train_file.close()

    def readOneQAPair(self, file):
        q, a = "", ""
        counter = 0
        for line in file:
            if not line:
                return None
            match_res = re.match('<.*?>', line)
            if not match_res:
                break
            match_str = match_res.group()
            line_split = line.split('\t')
            if 'question' in match_str:
                q = line_split[1].strip()
            if 'answer' in match_str:
                a = line_split[1].strip()
        return q,a

    def readOnePairFromTrain(self):
        return self.readOneQAPair(self.train_file)

    def readOnePairFromTest(self):
        return self.readOneQAPair(self.test_file)

    def readAllPair(self, t):
        qa_pairs = []
        if t not in ['train', 'test']:
            return None
        counter = 0
        while 1:
            counter += 1
            if type == 'train':
                res = self.readOnePairFromTrain()
            else:
                res = self.readOnePairFromTest()
            if res and res[0] !='' :
                qa_pairs.append([res[0], res[1]])
            else:
                print("共加载 "+str(counter)+" 条 question-answer pair")
                break
        return qa_pairs






