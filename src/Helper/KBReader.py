import sys

from Config import Config

class KBReader:
    def __init__(self):
        self.file = open(Config.getRootPath()+'data/kb/KB-small/kbqa.kb', encoding='utf-8')

    def __del__(self):
        self.file.close()

    def readAllRecords(self):
        entity_name = ''
        entity = {}
        entities = {}
        counter = 0
        for line in self.file:
            line = line.strip()
            line_split = line.split(' ||| ')
            if entity_name == line_split[0]:
                entity[line_split[1]] = line_split[2]
            else:
                if entity_name != '':
                    entities[entity_name] = entity
                counter += 1
                entity_name = line_split[0]
                entity = {
                    line_split[1]: line_split[2]
                }
            if counter % 10000 == 0:
                print("已加载 "+str(counter)+" 个实体")