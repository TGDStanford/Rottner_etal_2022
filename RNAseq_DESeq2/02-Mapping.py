import os 

GenomeRef = 'GRCh38'

D = {}
ouFile = open('02-Mapping.sh', 'w')
ouFile.write('#!/usr/bin/bash\n\n')
for F in sorted(os.listdir('.')):
    if F.endswith('.fq.gz'):
        sample = F.split('_1')[0].split('_2')[0].split('_R1')[0].split('_R2')[0]
        D.setdefault(sample, [])
        D[sample].append(F)

for sample in D:
    D[sample].sort()
    ouFile.write('STAR --runThreadN 4 --runMode alignReads --genomeDir %s --readFilesIn %s --readFilesCommand zcat --outFileNamePrefix %s --outSAMtype BAM SortedByCoordinate --outReadsUnmapped Fastx --outSAMattributes NH HI AS nM XS\n\n'%(GenomeRef, ' '.join(D[sample]), sample + '_'))
ouFile.close()
