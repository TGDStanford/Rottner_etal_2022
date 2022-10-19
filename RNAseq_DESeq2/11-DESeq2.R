CountTable = 'Calcoco2_GenesExp_GeneName'
SampleTable = 'SampleAnnot.txt'

library(DESeq2)
#library("BiocParallel")
#register(MulticoreParam(8))

geneCounts = read.table(CountTable, header=T)
sampleAnnot = read.table(SampleTable, header=T, sep='\t')
rownames(geneCounts) = paste0(geneCounts[,1], '\t', geneCounts[,2])
geneCounts = geneCounts[,3:(ncol(geneCounts))]

sampleAnnot$Condition = relevel(as.factor(sampleAnnot$Condition), 'siNT')
print(sampleAnnot)

###
dds = DESeqDataSetFromMatrix(geneCounts, sampleAnnot, design=formula('~Condition'))
dds = DESeq(dds)

res = results(dds)

res = data.frame(cbind(rownames(res), res))
colnames(res)[1]='GeneID\tGeneName'
res = res[order(res$padj), ]

ouF = paste0('Calcoco2_GenesExp_siCCO2-siNT.txt')
write.table(res, file=ouF, quote = FALSE, sep = "\t",  row.names = F, col.names= T)
