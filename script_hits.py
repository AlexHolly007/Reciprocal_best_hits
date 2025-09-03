import argparse
import re

#ONLY WORKS WITH SORTED SPECIES FILES
def main(species1_file, species2_file, biomart_species1, biomart_species2, output_file):
    #This keeps all the proteins of species1, and is filled with species 2 matching, and its eval
    #The number of times seen is kept so that after its second time seen, it can start skipping the protein name when its found
        #It needs to be found twice (two top e-vals), to verify that the top 2 are not equal
    #Valid. This is 1(true) of 0(false). going through every line in file2, if dict[P2][0] == P1 then that dict1 entry is valid. 
    dict1 = {} #{Protein1: Protein2}
    dict2 = {} #{Protein2: Protein1}

    p1_times_seen = {} #{Protein1: [Times seen, Eval]}
    p2_times_seen = {} #{Protein2: [Times seen, Eval]}


#######################################
    #TODO protein id is the same to two equal evalues.
    #TODO, just open github and make directory for this assignment, manually add all files
##########################################

    with open(species1_file, 'r') as f1:
        for line in f1:
            entries = line.strip().split()
            entries = [entry.strip() for entry in entries]
            #if the protein is already in the dict
            if entries[0] in p1_times_seen:
                #check if its been seen twice already
                if p1_times_seen[entries[0]][0] == 2:
                    continue

                else:
                    #if its the same protein again
                    if entries[1] == dict1[entries[0]][0]:
                        #if evalue is the same, and protein name the same, we want to keep looking
                        if p1_times_seen[entries[0]][1] != float(entries[10]):
                            p1_times_seen[entries[0]][0] = 2

                    #its only been seen once, check if e-values are the same
                    else:
                        p1_times_seen[entries[0]][0] = 2
                        if p1_times_seen[entries[0]][1] == float(entries[10]):
                            del dict1[entries[0]]

            #its not already in dict1
            else:
                dict1[entries[0]] = [entries[1]]
                p1_times_seen[entries[0]] = [1, float(entries[10])]

            
    #now check file2
    with open(species2_file, 'r') as f2:
        for line in f2:
            entries = line.strip().split()
            entries = [entry.strip() for entry in entries]
            #if the protein is already in the dict
            if entries[0] in p2_times_seen:
                #check if its been seen twice already
                if p2_times_seen[entries[0]][0] == 2:
                    continue

                else:
                    #if its the same protein again
                    if entries[1] == dict2[entries[0]][0]:
                        #if evalue is the same, and protein name the same, we want to keep looking
                        if p2_times_seen[entries[0]][1] != float(entries[10]):
                            p2_times_seen[entries[0]][0] = 2

                    #its only been seen once, check if e-values are the same
                    else:
                        p2_times_seen[entries[0]][0] = 2
                        if p2_times_seen[entries[0]][1] == float(entries[10]):
                            del dict2[entries[0]]

            #its not already in dict1
            else:
                dict2[entries[0]] = [entries[1]]
                p2_times_seen[entries[0]] = [1, float(entries[10])]

    final_dict = {}
    #sort the two dicts
    for entry in dict1:
        if dict1[entry][0] in dict2:
            if dict2[dict1[entry][0]][0] == entry:
                final_dict[entry] = [dict1[entry][0], ' ', ' ', ' ', ' ']
            
            

    #GET THE NAMES AND ID OF THE GENES
    #from the biomart files
    #first grab all from the biomart species 2 files
    S2_lines = open(biomart_species2, 'r').readlines()

    #for each line in biomart 1
    with open(biomart_species1, 'r') as b1:
        _ = b1.readline()
        for line in b1:
            entries = line.split()
            #if there is more than 1 peice of information, important because biomart files could be missing proteinid, and name
            if len(entries) > 1:
                #check if col2 in biomart is in dict: this will be proteinid if it exists, if pid is missing and its the gene name, it wont be in the dict
                if entries[1] in final_dict:
                    final_dict[entries[1]][1] = entries[0]
                    #if it has three entries, the last will be the gene name
                    if len(entries) > 2:
                        final_dict[entries[1]][2] = entries[2]

                    #NEST LOOP :(, now go through the species 2 lines to find the protein id that matches, grab the gene id and gene name, if name exists
                    for lineS2 in S2_lines:
                        if final_dict[entries[1]][0] in lineS2:
                            S2_entries = lineS2.split()
                            final_dict[entries[1]][3] = S2_entries[0]
                            if len(S2_entries) > 2:
                                final_dict[entries[1]][4] = S2_entries[2]
    

    #RBH OUTPUT: Species 1 Gene ID, Species 1 Protein ID, Species 1 Gene Name, Species 2 Gene ID, Species 1 Protein ID, Species 2 Gene Name**
    with open(output_file, 'w') as fo:
        fo.write("Species 1 Gene ID\tSpecies 1 Protein ID\tSpecies 1 Gene Name\tSpecies 2 Gene ID\tSpecies 1 Protein ID\tSpecies 2 Gene Name\n")
        for Pro in final_dict:
            fo.write(f"{final_dict[Pro][1]}\t{Pro}\t{final_dict[Pro][2]}\t{final_dict[Pro][3]}\t{final_dict[Pro][0]}\t{final_dict[Pro][4]}\n")
        


def get_args():
    parser = argparse.ArgumentParser(description="This is a script to find the best hits betwee two species. It requires blastp comparisons to already be done. \
        The files should contain every protein, and the top proteins that relate to that one")
    parser.add_argument("-S1","--species1",required=True)
    parser.add_argument("-S2","--species2",required=True)
    parser.add_argument("-B1","--biomart1",required=True)
    parser.add_argument("-B2","--biomart2",required=True)
    parser.add_argument("-o", '--output', required=True)
    return parser.parse_args()


#python3 script
#python3 script_hits.py -S1 TEST_INPUT_DRE_2_HSA._txt_ -S2 TEST_INPUT_HSA_2_DRE._txt_ -B1 TEST_BM_DRE.tsv -B2 TEST_BM_HSA.tsv -o TEST_OUTPUT_RBH.tsv
if __name__ == "__main__":
    args = get_args()
    main(args.species1, args.species2, args.biomart1, args.biomart2, args.output)
