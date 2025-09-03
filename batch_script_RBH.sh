#!/bin/bash

python3 script_hits.py -S1 dbs/Dre_query_Hsa_db.txt -S2 dbs/Hsa_query_Dre_db.txt -B1 /projects/bgmp/shared/Bi623/PS1/biomart/dre_114_biomart.tsv -B2 /projects/bgmp/shared/Bi623/PS1/biomart/hsa_114_biomart.tsv -o RBH_results/Human_Zebrafish_RBH.tsv
python3 script_hits.py -S1 dbs/Hsa_query_Eel_db.txt -S2 dbs/Eel_query_Hsa_db.txt -B1 /projects/bgmp/shared/Bi623/PS1/biomart/hsa_114_biomart.tsv -B2 /projects/bgmp/shared/Bi623/PS1/biomart/eel_114_biomart.tsv -o RBH_results/Human_ElectricEel_RBH.tsv
python3 script_hits.py -S1 dbs/Hsa_query_Pka_db.txt -S2 dbs/Pka_query_Hsa_db.txt -B1 /projects/bgmp/shared/Bi623/PS1/biomart/hsa_114_biomart.tsv -B2 /projects/bgmp/shared/Bi623/PS1/biomart/pka_114_biomart.tsv -o RBH_results/Human_ElectricBabyWhale_RBH.tsv
python3 script_hits.py -S1 dbs/Dre_query_Eel_db.txt -S2 dbs/Eel_query_Dre_db.txt -B1 /projects/bgmp/shared/Bi623/PS1/biomart/dre_114_biomart.tsv -B2 /projects/bgmp/shared/Bi623/PS1/biomart/eel_114_biomart.tsv -o RBH_results/Zebrafish_ElectricEel_RBH.tsv
python3 script_hits.py -S1 dbs/Dre_query_Pka_db.txt -S2 dbs/Pka_query_Dre_db.txt -B1 /projects/bgmp/shared/Bi623/PS1/biomart/dre_114_biomart.tsv -B2 /projects/bgmp/shared/Bi623/PS1/biomart/pka_114_biomart.tsv -o RBH_results/Zebrafish_ElectricBabyWhale_RBH.tsv
python3 script_hits.py -S1 dbs/Eel_query_Pka_db.txt -S2 dbs/Pka_query_Eel_db.txt -B1 /projects/bgmp/shared/Bi623/PS1/biomart/eel_114_biomart.tsv -B2 /projects/bgmp/shared/Bi623/PS1/biomart/pka_114_biomart.tsv -o RBH_results/ElectricEel_ElectricBabyWhale_RBH.tsv
