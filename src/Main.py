from Classes.Dna import Dna
from Classes.Rna import Rna

fileName = '/home/iberthy/Documentos/Bioinformatica/src/Database/rosalind_dna.txt';
dataset = open(fileName, 'r').read().upper();

dna = Dna(dataset);
dna.toString();
print(dna.count());
aux_complement = "".join(dna.complementing());
print(aux_complement);
print("\n");
print(dna.transcribing_into_rna());
print(dna.search_motif('GAAGAT'));
rna = Rna(dna.transcribing_into_rna());
print(rna.transcribing_into_protein());