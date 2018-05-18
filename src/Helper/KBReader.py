import sys

from Config import Config

class KBReader:
    @staticmethod
    def readAllRecords():
        file = open(Config.getRootPath() + 'data/kb/KB-original/kbqa.kb', encoding='utf-8')
        entity_name = ''
        entity = {}
        entities = {}
        counter = 0
        for line in file:
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
                if counter % 100000 == 0:
                    print("已加载 "+str(counter)+" 个实体")
        print("共加载 "+str(counter)+" 个实体")
        file.close()
        return entities