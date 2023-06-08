import abs_pytorch_round1_extraOutputs
def main(model_filepath, result_filepath, scratch_dirpath, examples_dirpath, modelName, ExperimentName, example_img_format='png',):
    with open("/mnt/nfs/ml-shared/trojai_data/ABS/TrojAI_competition/round1/denseResNetModelNames50.txt") as f:
          modelnums=f.read().splitlines()
          print(modelnums)  
    for i in modelnums:
            try:
                 print("helloooooo")
                 abs_pytorch_round1_extraOutputs(model_filepath+i+'/model.pt', result_filepath, scratch_dirpath, examples_dirpath +i+'/example_data/', i , ExperimentName)
            except:
                 print("model:"+i+ "failed")



if __name__=="__main__":
    import argparse

    parser = argparse.ArgumentParser(description='Fake Trojan Detector to Demonstrate Test and Evaluation Infrastructure.')
    parser.add_argument('--model_filepath', type=str, help='File path to the pytorch model file to be evaluated.', default='./model.pt')
    parser.add_argument('--result_filepath', type=str, help='File path to the file where output result should be written. After execution this file should contain a single line with a single floating point trojan probability.', default='./output')
    parser.add_argument('--scratch_dirpath', type=str, help='File path to the folder where scratch disk space exists. This folder will be empty at execution start and will be deleted at completion of execution.', default='./scratch')
    parser.add_argument('--examples_dirpath', type=str, help='File path to the folder of examples which might be useful for determining whether a model is poisoned.', default='./example')
    parser.add_argument('--modelName', type=str, help='base name of the NIST assigned model number' )
    parser.add_argument('--ExperimentName', type=str, help='base name of the batch of accros which an ROC can be computed' )
    """
    if len(sys.argv)>1:
        ExperimentName= sys.argv[1]
        modelfilename=sys.argv[2]
        if not os.path.exists('./'+ExperimentName):
            os.makedirs('./'+ExperimentName +'/'+modelfilename+'/deltas')
            os.makedirs('./'+ExperimentName +'/'+modelfilename+'/imgs')
            os.makedirs('./'+ExperimentName +'/'+modelfilename+'/masks')
            os.makedirs('./'+ExperimentName +'/'+modelfilename+'/temp')
    """
    args = parser.parse_args()

    main(args.model_filepath, args.result_filepath, args.scratch_dirpath, args.examples_dirpath, args.modelName, args.ExperimentName)
