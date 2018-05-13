from Config import Config


class StopWordsReader:
    @staticmethod
    def readAllStopWords():
        file = open(Config.getRootPath()+'data/stopwords.txt')
        words = []
        for line in file:
            line = line.strip('')
            words.append(line)
        file.close()
        return words
