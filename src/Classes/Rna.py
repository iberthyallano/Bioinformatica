class Rna:
    def __init__(self, input):
        self.ribbon = input;
        self.codon_table = {
            'UUU':'F', 'CUU':'L', 'AUU':'I', 'GUU':'V',
            'UUC':'F', 'CUC':'L', 'AUC':'I', 'GUC':'V',
            'UUA':'L', 'CUA':'L', 'AUA':'I', 'GUA':'V',
            'UUG':'L', 'CUG':'L', 'AUG':'M', 'GUG':'V',
            'UCU':'S', 'CCU':'P', 'ACU':'T', 'GCU':'A',
            'UCC':'S', 'CCC':'P', 'ACC':'T', 'GCC':'A',
            'UCA':'S', 'CCA':'P', 'ACA':'T', 'GCA':'A',
            'UCG':'S', 'CCG':'P', 'ACG':'T', 'GCG':'A',
            'UAU':'Y', 'CAU':'H', 'AAU':'N', 'GAU':'D',
            'UAC':'Y', 'CAC':'H', 'AAC':'N', 'GAC':'D',
            'CAA':'Q', 'AAA':'K', 'GAA':'E', 'CAG':'Q',
            'AAG':'K', 'GAG':'E', 'UGU':'C', 'CGU':'R',
            'AGU':'S', 'GGU':'G', 'UGC':'C', 'CGC':'R',
            'AGC':'S', 'GGC':'G', 'CGA':'R', 'AGA':'R',
            'GGA':'G', 'UGG':'W', 'CGG':'R', 'AGG':'R',
            'GGG':'G', 'UAA':'Stop', 'UGA':'Stop', 'UAG':'Stop'
        }

    def transcribing_into_protein(self):
        protein = 'In progress';
        return protein;

    def toString(self):
        print(self.ribbon);