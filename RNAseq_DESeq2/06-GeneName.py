D = {}
inFile = open('Homo_sapiens.GRCh38.101.GeneRegionType')
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    D[fields[0]] = fields[1]
inFile.close()

def Symbol(inF):
    inFile = open(inF)
    ouFile = open(inF + '_GeneName', 'w')
    head = inFile.readline().strip().split('\t')
    ouFile.write('GeneID\tGeneName\t'+'\t'.join([x.split('.bam')[0] for x in head[1:]])+'\n')
    for line in inFile:
        line = line.strip()
        fields = line.split('\t')
        if fields[0] in D:
            ouFile.write(fields[0] + '\t' + D[fields[0]] + '\t' + '\t'.join(fields[1:]) + '\n')
        else:
            ouFile.write(fields[0] + '\t' + fields[0] + '\t' + '\t'.join(fields[1:]) + '\n')

    inFile.close()
    ouFile.close()

Symbol('Calcoco2_GenesExp')
