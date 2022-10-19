#!/usr/bin/bash

wget ftp://ftp.ensembl.org/pub/release-101/fasta/homo_sapiens/dna/Homo_sapiens.GRCh38.dna.primary_assembly.fa.gz
wget ftp://ftp.ensembl.org/pub/release-101/gtf/homo_sapiens/Homo_sapiens.GRCh38.101.gtf.gz

REF=Homo_sapiens.GRCh38.dna.primary_assembly.fa
GTF=Homo_sapiens.GRCh38.101.gtf
GenomeDIR=GRCh38
STAR --runThreadN 4 --runMode genomeGenerate --genomeDir $GenomeDIR --genomeFastaFiles $REF --sjdbGTFfile $GTF --sjdbOverhang 100
