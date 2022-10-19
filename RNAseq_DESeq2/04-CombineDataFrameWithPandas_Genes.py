### all the files are in the same order, no need to match rows.
import os
import pandas as pd

def GeneCounts(inFs=[], ouF='', DIR='.'):
    ### first columns
    DF = pd.DataFrame()
    df = pd.read_table(DIR + '/' + inFs[0], header=0, comment='#')
    DF['GeneID'] = df.iloc[:,0]

    ### following columns
    for F in inFs:
        sample = F.split('_Genes')[0]
        df = pd.read_table(DIR + '/' + F, header=0, comment='#')
        DF[sample] = df.iloc[:, 6]

    if ouF.endswith('.gz'):
        DF.to_csv(ouF, header=True, index=False, sep='\t', compression='gzip')
    else:
        DF.to_csv(ouF, header=True, index=False, sep='\t')

inFs = []
inFile = open('SampleList.txt')
for line in inFile:
    line = line.strip()
    f = line
    inFs.append(f)
inFile.close()


GeneCounts(inFs, 'Calcoco2_GenesExp')

