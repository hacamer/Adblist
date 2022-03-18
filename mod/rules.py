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

resultb = []
ffob = open("adp-mo.txt")
fob = open("adp-mo-test.txt", "w")
resultb=list(set(ffob.readlines()))
resultb.sort()
fob.writelines(resultb)
fob.close()
ffob.close()
os.remove("adp-mo.txt")
os.rename("adp-mo-test.txt","adp-mo.txt")

resultc = []
ffoc = open("adp-pc.txt")
foc = open("adp-pc-test.txt", "w")
resultc=list(set(ffoc.readlines()))
resultc.sort()
foc.writelines(resultc)
foc.close()
ffoc.close()
os.remove("adp-pc.txt")
os.rename("adp-pc-test.txt","adp-pc.txt")

resultd = []
ffod = open("adp.txt")
fod = open("adp-test.txt", "w")
resultd=list(set(ffod.readlines()))
resultd.sort()
fod.writelines(resultd)
fod.close()
ffod.close()
os.remove("adp-edentw.txt")
os.rename("adp-edentw-test.txt","adp-edentw.txt")

resulte = []
ffoe = open("adp2.txt")
foe = open("adp2-test.txt", "w")
resulte=list(set(ffoe.readlines()))
resulte.sort()
foe.writelines(resulte)
foe.close()
ffoe.close()
os.remove("adp2.txt")
os.rename("adp2-test.txt","adp2.txt")

result = []
ffog = open("adp3.txt")
fog = open("adp3-test.txt", "w")
resultg=list(set(ffog.readlines()))
resultg.sort()
fog.writelines(resultg)
fog.close()
ffog.close()
os.remove("adp3.txt")
os.rename("adp3-test.txt","adp3.txt")
