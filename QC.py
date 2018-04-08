#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#尝试用最简单的字符串匹配解决属性词隐藏在特殊疑问词的问题
from enum import Enum, unique
import re

@unique
class QC(Enum):
    Location = 0 #地点
    Artifact = 1 #东西
    Time = 2 #时间
    Person = 3 #人
    Causality = 4 #原因
    Amount = 5 # 数量

def question_classification(question):
    if re.search('哪年', question) != None:
        return QC.Time
    elif  re.search('哪月', question) != None:
        return QC.Time
    elif  re.search('哪天', question) != None:
        return QC.Time
    elif re.search('哪日', question) != None:
        return QC.Time
    elif  re.search('哪里', question) != None:
        return QC.Location
    elif  re.search('哪儿', question) != None:
        return QC.Location
    elif  re.search('哪', question) != None:
        return QC.Location
    elif re.search('什么', question) != None:
        return QC.Artifact
    elif  re.search('啥', question) != None:
        return QC.Artifact
    elif re.search('谁', question) != None:
        return QC.Person
    elif re.search('为什么', question) != None:
        return QC.Causality
    elif re.search('多少', question) != None:
        return QC.Amount
    else:
        return "无匹配"


def test():
    category = question_classification('清华大学在哪儿？')
    print(category)

if __name__=='__main__':
    test()