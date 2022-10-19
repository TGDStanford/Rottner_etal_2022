from pyst import *

def BarPlot(inF):
    df = pd.read_table(inF, header=0)
    print(df)

    df_sub = df.loc[df['Feature'] == 'Number of input reads', ]
    df_sub['Number of input reads'] = [int(x)/1e6 for x in df_sub['Value']]

    CL = []
    for x in df_sub['Sample']:
        cl = 'C0'
        if x.endswith('siNT'):
            cl = 'C0'
        else:
            cl = 'C1'
        CL.append(cl)
    
    fig = plt.figure()
    ax = fig.add_subplot()
    sns.barplot(x='Sample', y='Number of input reads', ax=ax, data=df_sub, palette=CL)
    print('median number of input reads: %s'%df_sub['Number of input reads'].median())
    ax.set_xticklabels(ax.get_xticklabels(), rotation=0, fontsize=6)
    ax.set_xlabel('')
    ax.set_ylabel('Number of reads (million)')
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.savefig(inF.split('.txt')[0] + '_NumReads.pdf')
    plt.savefig(inF.split('.txt')[0] + '_NumReads.svg')


    df_sub = df.loc[df['Feature'] == 'Uniquely mapped reads %', ]
    fig = plt.figure()
    ax = fig.add_subplot()
    df_sub['Uniquely mapped reads (%)'] = [float(x.strip('%')) for x in df_sub['Value']]
    sns.barplot(x='Sample', y='Uniquely mapped reads (%)', ax=ax, data=df_sub, palette=CL)
    print('median mapping rate: %s'%df_sub['Uniquely mapped reads (%)'].median())
    ax.set_xticklabels(ax.get_xticklabels(), rotation=0, fontsize=6)
    ax.set_xlabel('')
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.savefig(inF.split('.txt')[0] + '_MappingRate.pdf')
    plt.savefig(inF.split('.txt')[0] + '_MappingRate.svg')


BarPlot('MappingStatSTAR.txt')

