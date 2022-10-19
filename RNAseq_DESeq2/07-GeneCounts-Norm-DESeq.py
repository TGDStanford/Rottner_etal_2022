import pandas as pd
import numpy as np


def Norm(inF):
    ouF =  inF.split('.tsv')[0].split('.txt')[0] + '_Norm'
    

    df = pd.read_table(inF, header=0)
    df.columns = [x.split('Aligned.sortedByCoord.out')[0] for x in df.columns]
    df_mat=df.iloc[:,2:]

    df2 = np.log(df_mat)
    rowMean=np.mean(df2.T)
    SizeFactor = []
    for i in range(df2.shape[1]):
        s = (df_mat.iloc[:,i] > 0) & (np.isfinite(rowMean))
        sf = np.exp(np.median((df2.iloc[:,i] - rowMean)[s]))
        SizeFactor.append(sf)
    print(SizeFactor)

    df_norm = df_mat/SizeFactor

    df_norm.insert(0, df.columns[0], df.iloc[:,0])
    df_norm.insert(1, df.columns[1], [x.split('.')[0] for x in df.iloc[:,1]])

    df_norm.to_csv(ouF, sep='\t', index=False, header=True, float_format='%.2f')

Norm('Calcoco2_GenesExp_GeneName')
