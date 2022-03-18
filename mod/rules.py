# -*- coding:gbk -*-
import os

result = []
ffo = open("adp.txt")
fo = open("adp-test.txt", "w")
result=list(set(ffo.readlines()))
result.sort()
fo.writelines(result)
fo.close()
ffo.close()
os.remove("adp.txt")
os.rename("adp-test.txt","adp.txt")
