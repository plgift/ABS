#each time this runs, it writes a new random 50 files. 
import random
resnetmodel25=[]
densenetmodel25=[]
with open("/home/nnichols/Documents/Projects/trojai/ABS/TrojAI_competition/round1/resnetModelNames.txt") as f:
          res=f.read().splitlines()

resnetmodel25=random.sample(res,25)

with open("/home/nnichols/Documents/Projects/trojai/ABS/TrojAI_competition/round1/densenetModelNames.txt") as f:
          dense=f.read().splitlines()

densenetmodel25=random.sample(dense,25)

denseresnetmodels50=resnetmodel25+densenetmodel25

type(resnetmodel25)
print(resnetmodel25)
len(resnetmodel25)
"""
file=open("/home/nnichols/Documents/Projects/trojai/ABS/TrojAI_competition/round1/denseResNetModelNames50.txt",'w')
for each in denseresnetmodels50:
        file.write(each+"\n")
file.close 
"""
