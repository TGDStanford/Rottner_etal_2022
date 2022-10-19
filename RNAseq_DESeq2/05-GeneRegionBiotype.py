def id2region(inF):
    D = {}
    inFile = open(inF)
    ouFile = open(inF.split('.gtf')[0] + '.GeneRegionType', 'w')
    for line in inFile:
        if line[0] != '#':
            fields = line.split('\t')
            if fields[2] == 'gene':
                info = fields[8].split(';')
                for item in info:
                    if item.find('gene_id') != -1:
                        gene_id = item.split('"')[1]
                        gene_name = gene_id
                    elif item.find('gene_name') != -1:
                        gene_name = item.split('"')[1]
                    elif item.find('gene_biotype') != -1:
                        gene_biotype = item.split('"')[1]
                D.setdefault(gene_id, [])
                D[gene_id].append('\t'.join([gene_name, fields[0], fields[3], fields[4], fields[6], gene_biotype]))
    inFile.close()
    d = sorted(D.items(), key = lambda x : x[0])
    for item in d:
        if len(set(item[1])) != 1:
            print('Warning:gene_id to multiple gene_name')
        else:
            ouFile.write(item[0] + '\t' + item[1][0] + '\n')

    ouFile.close()

d2region('Homo_sapiens.GRCh38.101.gtf')
