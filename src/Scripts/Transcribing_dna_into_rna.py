fileName = 'Database/rosalind_dna_in_rna.txt';
dataset = open(fileName).read();

# Forma 01
dataset = dataset.replace('T', 'U');
print(dataset);
#-----------------------------------#

# Forma 02
result = '';
for i in dataset:
    if i == 'T':
        result += 'U';
        continue
    result += i;
print(result);
#-----------------------------------#
