fileName = 'Database/rosalind_mutations_in_dna.txt';
dataset = open(fileName, 'r').read().split('\n');

#The Hamming distance, nesse problema descobrimos onde as strings se diferem 

# Forma 01
fita01 = dataset[0];
fita02 = dataset[1];

result = 0;
for i in range(len(fita01)):
  if(fita01[i] == fita02[i]):
    result += 1;

forma01 = len(fita01)-result;
print(forma01);
#-----------------------------------#