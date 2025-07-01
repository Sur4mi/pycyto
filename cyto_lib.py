from dic_aa import IUPAC_AMINO_DIC
from dic_aa import CODONS_DIC

# Return an aa if present in the codon dictiorary

def find_aa_by_codon_in_dic(dic, codon):
    for aa, codon_list in dic.items():
        if codon in codon_list:
            return aa

# Return the sequence of the trasnlated protein (ORF1)

def get_codon(sequence):
    translated_prot =''
    for i in range(len(sequence)//3):
        codon = sequence[3*i:(3*i)+3]
        aa = find_aa_by_codon_in_dic(CODONS_DIC, codon)
        translated_prot += aa
    return translated_prot
      