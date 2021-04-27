fileName = 'Database/rosalind_dna.txt';
dataset = open(fileName, 'r').read();

# Formas de se ler e contar uma sequencia de DNA

# Forma_01
# O(N)
from collections import defaultdict;

forma01 = defaultdict(int);
for x in dataset:
  forma01[x] += 1;
print(forma01);
#-----------------------------------#

# Forma_02
# O(N)
from collections import Counter;

forma02 = Counter(dataset);
print(forma02);
#-----------------------------------#

# Forma_03
# O(4*N)
count_a = dataset.count('A');
count_c = dataset.count('C');
count_g = dataset.count('G');
count_t = dataset.count('T');
print(count_a,count_c,count_g,count_t);
#-----------------------------------#
