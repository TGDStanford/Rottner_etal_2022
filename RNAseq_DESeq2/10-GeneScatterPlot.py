from pyst import *

def GenePlot(inF, Gene = ['ZMIZ1'], CONS=['siNT', 'siCCO2'], COLORS=['C0','C1','C2','C3','C4','C5','C6']):
    df = pd.read_table(inF, header=0)
    df_sub = df.loc[df.iloc[:, 1].isin(Gene), :]
    LT = []
    for i in range(0, df_sub.shape[0]):
        for j in range(2, df_sub.shape[1]):
            expr = df_sub.iloc[i, j]
            gene = df_sub.iloc[i, 1]
            sample = df_sub.columns[j]
            condition = sample.split('_')[-1]
            cell_line = sample.split('_')[0]
            LT.append([gene, sample, condition,  cell_line, expr])

    LT = pd.DataFrame(LT)
    LT.columns = ['Gene', 'Sample', 'Condition', 'CellLine', 'Expression']
    print(LT)

    if len(Gene) == 1:
        g = sns.FacetGrid(LT, col='Gene', col_wrap=2, sharex = False, sharey=False, col_order=Gene, legend_out=True, height=5)
    else:
        g = sns.FacetGrid(LT, col='Gene', col_wrap=2, sharex = False, sharey=False, col_order=Gene, legend_out=True)

    g.map_dataframe(sns.barplot, x='Condition', y='Expression', order=CONS, capsize=0.1, palette=['C0', 'C1'], alpha=1)
    g.map_dataframe(sns.swarmplot, x='Condition', y='Expression', order=CONS, hue='CellLine', palette=['C4', 'C9'], size=8)
    g.set_ylabels('Normlized Expression')
    for ax in g.axes:
        ax.tick_params(labelsize=8)
        ax.set_xlabel('')
    #    ax.set_yticklabels(ax.get_yticklabels(), fontsize=4)
    
    #g.set_xticklabels(size=8)
    #if len(Gene) == 1:
    plt.legend()


    plt.savefig(inF.split('.tsv')[0] + '.' + '_'.join(Gene) + '.BarPlot.pdf')
    plt.savefig(inF.split('.tsv')[0] + '.' + '_'.join(Gene) + '.BarPlot.svg')






GenePlot('Calcoco2_GenesExp_GeneName_Norm', Gene = ['CALCOCO2', 'TSPAN2', 'GCNT1', 'B4GALT5'])





