for i in Proteins/PSSM_testing/*.fasta
do
psiblast -query $i -db /home/u2341/SwissProt/uniprot_sprot.fasta -evalue 0.001  -num_iterations 3 -out $i.out -out_ascii_pssm $i.pssm
done
