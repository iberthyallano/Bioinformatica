fileName = 'Database/rosalind_revc.txt';
dataset = open(fileName, 'r').read();

# utilizado em 3 formas, então, globalizar é importante
complement = {
    "A" : "T",
    "C" : "G",
    "G" : "C",
    "T" : "A",
}

# Formas de se ler e saber o complemento de uma sequencia de DNA

# Forma 01
forma01 = '';
for i in dataset:
    if(i == 'A'):
        forma01 += 'T';
    elif(i == 'C'):
        forma01 += 'G';
    elif(i == 'G'):
        forma01 += 'C';
    else:
        forma01 += 'A';

forma01 = forma01[::-1];
print(forma01);
#-----------------------------------#

# Forma 02
forma02 = '';
for j in dataset:
    forma02 += complement[j];

forma02 = forma02[::-1];
print(forma02);
#-----------------------------------#

# Forma 03
forma03 = [complement[j] for j in dataset][::-1];
forma03 = "".join(forma03);
print(forma03);
#-----------------------------------#

# Forma 04
def complementor(base):
    return complement[base];

forma04 = list(map(complementor, dataset));
forma04.reverse();
forma04 = "".join(forma04);
print(forma04);
#-----------------------------------#

# fileName = 'Database/rosalind_revc.txt';
# fita01 = open(fileName, 'r').read();

# def fitaToString(fita):
# 	text = "".join(fita);
# 	return text;

# complement = {
#     "A" : "T",
#     "C" : "G",
#     "G" : "C",
#     "T" : "A",
# }

# fita02 = [complement[j] for j in fita01][::-1];
# print(fitaToString(fita02));
