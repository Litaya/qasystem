from src.Module.LtpParser import LtpParser
from src.Helper.QAReader import  QAReader

parser = LtpParser()

qaReader = QAReader()
pairs = qaReader.readAllPair('test')
counter = 1
matched = 0
for q, a in pairs:
    if counter % 20  == 0:
        break
    print(q)
    res = parser.analysis(q)
    if res:
        matched += 1
    print(res)
    counter+=1

print("共匹配 "+str(matched)+"条")