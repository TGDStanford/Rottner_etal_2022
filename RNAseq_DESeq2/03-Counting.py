import os
Fs = sorted([x for x in os.listdir('.') if x.endswith('.bam')])

def FC(GTF='Homo_sapiens.GRCh38.91.gtf', nT=4, MinQ=30, Strand=0):
    ouFile = open('03-Counting.sh', 'w')
    ouFile.write('#!/usr/bin/bash\n\n')
    for F in Fs:
        sample = F.split('_Aligned.sortedByCoord.out.bam')[0]
        ouFile.write('featureCounts -p -T %s -a %s -Q %s -s %s -o %s_Genes %s\n'%(nT, GTF, MinQ, Strand, sample, F))
        ouFile.write('gzip %s_Genes\n'%sample)
        ouFile.write('\n')
    ouFile.close()

FC(GTF='Homo_sapiens.GRCh38.101.gtf', nT=4, Strand=0)

