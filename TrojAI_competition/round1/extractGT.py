#extract ground truth given 
import pandas
import os

DM_gt=[]
with open("/mnt/nfs/ml-shared/trojai_data/ABS/TrojAI_competition/round1/densenetModelNames100.txt") as f:
    densenums=f.read().splitlines()
    nistbasepath='/mnt/nfs/ml-shared/trojai_data/dl/round1train/models/'
    #outputbasepath='/mnt/nfs/ml-shared/trojai_data/ABS/TAI_debug_batch/'
    #ExperimentName='absPTrandom_dense'
    for modelid in densenums:
        gt_filepath=os.path.join(nistbasepath,modelid,'ground_truth.csv')
        with open(gt_filepath,mode='r') as file:
            csvee=pandas.read_csv(file)
            for line in csvee:
                DM_gt.append(line)
f.close

RM_gt=[]
with open("/mnt/nfs/ml-shared/trojai_data/ABS/TrojAI_competition/round1/resnetModelNames100.txt") as f:
    resnums=f.read().splitlines()
    nistbasepath='/mnt/nfs/ml-shared/trojai_data/dl/round1train/models/'
    #outputbasepath='/mnt/nfs/ml-shared/trojai_data/ABS/TAI_debug_batch/'
    #ExperimentName='absPTrandom_dense'
    for modelid in resnums:
        gt_filepath=os.path.join(nistbasepath,modelid,'ground_truth.csv')
        with open(gt_filepath,mode='r') as file:
            csvee=pandas.read_csv(file)
            for line in csvee:
                RM_gt.append(line)
f.close

with open(result_filepath+'/'+ExperimentName+'/'+ modelName+'/output.pkl', 'wb') as f:
    pickle.dump(RM_gt, f)

with open(result_filepath+'/'+ExperimentName+'/'+ modelName+'/output.pkl', 'wb') as f:
    pickle.dump(RM_gt, f)