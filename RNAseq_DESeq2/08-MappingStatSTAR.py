def MappingStat(inFs, ouF='MappingStatSTAR.txt'):
    ouFile = open(ouF, 'w')
    ouFile.write('Sample\tFeature\tValue\n')
    for F in inFs:
        sample = D[F.split('_Log')[0]]
        inFile = open(F)
        head1 = inFile.readline()
        head2 = inFile.readline()
        head3 = inFile.readline()
        head4 = inFile.readline()

        for line in inFile:
            line = line.strip()
            if line:
                fields = line.split('|\t')
                ouFile.write('\t'.join([sample] + [x.strip() for x in fields]) + '\n')

        inFile.close()
    ouFile.close()



inFs = []
D = {}
inFile = open('SampleAnnot.txt')
head = inFile.readline()
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    inFs.append('%s_Log.final.out'%fields[0])
    D[fields[0]] = fields[0]
inFile.close()

MappingStat(inFs)
