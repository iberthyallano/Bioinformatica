import re

fileName = 'Database/rosalind_rna.txt';
dataset = open(fileName, 'r').read();

codon_table = {
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

# Forma 01
dataset = re.split("(\S{3})", dataset);
for i in dataset:
    if(i == ''):
        dataset.remove(i);

forma01 = [codon_table[j] for j in dataset];
forma01.remove('Stop');
forma01 = "".join(forma01);
print(forma01);
#-----------------------------------#


# Forma 02
forma02 = list(zip(dataset));# tem um erro nessa linha- --> froma correta --> list(zip(*[iter(dataset)]*3));
# forma02 = list(zip(*[iter(dataset)]));# tem um erro nessa linha- --> froma correta --> list(zip(*[iter(dataset)]*3));
result = "";
for i in forma02:
    aux = "".join(i);
    protein = codon_table[aux];
    if protein == "Stop":
        break;
    result += protein;
forma02 = result;
print(forma02);
#-----------------------------------#