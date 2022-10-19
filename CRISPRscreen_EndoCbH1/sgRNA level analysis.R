
library(tidyverse)
library(data.table)



Gene<-read.table("RRApaired_screen.gene_summary.txt", header=TRUE)
sgRNA<-read.table("RRApaired_screen.sgrna_summary (1).txt", header=TRUE) 
sgRNA <- subset(sgRNA,subset=(sgRNA$control_count>=10)) 
sgRNA <- subset(sgRNA,subset=(sgRNA$treatment_count>=10)) 

sgRNA <- subset(sgRNA,subset=(sgRNA$Gene!="LacZ"))
sgRNA <- subset(sgRNA,subset=(sgRNA$Gene!="luciferase"))
sgRNA <- subset(sgRNA,subset=(sgRNA$Gene!="EGFP"))

sgRNAFDR <- subset(sgRNA,subset=(sgRNA$FDR<=1.00E-01))
sgRNAFDR[,1] <- sub("_+.*", "", sgRNAFDR[,1])

sgRNAPOS <- subset(sgRNAFDR,subset=(sgRNAFDR$LFC>0))
POSREP <- sgRNAPOS[sgRNAPOS$sgrna %in% sgRNAPOS$sgrna[duplicated(sgRNAPOS$sgrna)],] 
POSREP2 <- POSREP[duplicated(POSREP$sgrna), ] 
POSREP3 <- POSREP2[POSREP2$Gene %in% POSREP2$Gene[duplicated(POSREP2$Gene)],]

POSREP4 <- POSREP3[duplicated(POSREP3$Gene), ] 
MOREP2 <- POSREP4[duplicated(POSREP4$Gene), ] 
MOREP3 <- MOREP2[duplicated(MOREP2$Gene), ] 


sgRNANEG <- subset(sgRNAFDR,subset=(sgRNAFDR$LFC<0)) 
NEGREP <- sgRNANEG[sgRNANEG$sgrna %in% sgRNANEG$sgrna[duplicated(sgRNANEG$sgrna)],] 
NEGREP2 <- NEGREP[duplicated(NEGREP$sgrna), ]
NEGREP3 <- NEGREP2[NEGREP2$Gene %in% NEGREP2$Gene[duplicated(NEGREP2$Gene)],] 
NEGREP4 <- NEGREP3[duplicated(NEGREP3$Gene), ] 

MOREN2 <- NEGREP4[duplicated(NEGREP4$Gene), ] 
MOREN3 <- MOREN2[duplicated(MOREN2$Gene), ]  

`%notin%` <- Negate(`%in%`)

POS2 <- POSREP4[POSREP4$Gene %notin% MOREP2$Gene,]
POS3 <- MOREP2[MOREP2$Gene %notin% MOREP3$Gene,]
POS4 <- MOREP3

NEG2 <- NEGREP4[NEGREP4$Gene %notin% MOREN2$Gene,]
NEG3 <- MOREN2[MOREN2$Gene %notin% MOREN3$Gene,]

POS <- rbind(POS2,POS3,POS4)
NEG <- rbind(NEG2,NEG3)
POS[POS$Gene%in%NEG$Gene,]

HITS <- rbind(POS,NEG)
HITS <- subset(HITS,subset=(HITS$Gene!="NDUFS6"))

Endo <- read.table("EndoC_islet_expression lookup table.txt",h=T) ##EndoC-bH1 expression data
Endo_not <- Endo[Endo[,3]<1, "GeneName"]

HITS$Expression <- ifelse(HITS$Gene %in% Endo_not,"FALSE","TRUE")
HITS_expr <- subset(HITS, HITS$Expression=="TRUE")

write.table(HITS_expr,file="CRISPRHits.txt",sep="\t",row.names=FALSE,quote=FALSE)
