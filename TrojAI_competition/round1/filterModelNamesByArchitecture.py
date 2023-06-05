import pandas as pd
df=pd.read_csv('/home/nnichols/Documents/Projects/trojai/ABS/TrojAI_round1/METADATA.csv')
filterlist=df[df['model_architecture']!= "inceptionv3"]
filterlist.shape

type(filterlist.model_architecture)
filterlist.model_architecture.unique()

ResnetModels=df[df["model_architecture"]=='resnet50']
DenseNetModels=df[df["model_architecture"]=='densenet121']
#DenseNetModels.model_architecture.unique()

resnetModelNames=ResnetModels.model_name
densenetModelNames=DenseNetModels.model_name

type(resnetModelNames)
resnetModelNames.tolist()
densenetModelNames.tolist()

with open('/home/nnichols/Documents/Projects/trojai/ABS/TrojAI_competition/round1/resnetModelNames.txt', 'w+') as f:    
    # write elements of list
    for items in resnetModelNames:
        f.write('%s\n' %items)    
    print("File written successfully")
f.close()

with open('/home/nnichols/Documents/Projects/trojai/ABS/TrojAI_competition/round1/densenetModelNames.txt', 'w+') as f:    
    # write elements of list
    for items in densenetModelNames:
        f.write('%s\n' %items)    
    print("File written successfully")
f.close()