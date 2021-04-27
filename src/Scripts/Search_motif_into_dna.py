fileName = 'Database/rosalind_motif_in_dna.txt';
dataset = open(fileName, 'r').read().split('\n');

# Forma 01
forma01 = dataset[0];
motif = dataset[1];

result = []
for i in range(len(forma01) - len(motif) + 1):
  if forma01[i : i+len(motif)] == motif:
    result.append(str(i + 1));

forma01 = " ".join(result);
print(forma01);
#-----------------------------------#