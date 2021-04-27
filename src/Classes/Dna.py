from collections import Counter;

class Dna:
    def __init__(self, input):
       self.ribbon = input;
       self.complement = {
            "A" : "T",
            "C" : "G",
            "G" : "C",
            "T" : "A",
        }
    
    def complementing(self):
        ribbon_complement = [self.complement[i] for i in self.ribbon][::-1];
        return ribbon_complement;

    def count(self):
        accounted = Counter(self.ribbon);
        return accounted.most_common();
    
    # def count_mutations(self, ribbon_complement):
    # return 'In progress';

    def search_motif(self, motif):
        motif_list = []
        for i in range(len(self.ribbon) - len(motif) + 1):
            if self.ribbon[i : i+len(motif)] == motif:
                motif_list.append(str(i + 1));
        return motif_list;

    def transcribing_into_rna(self):
        rna = self.ribbon.replace('T', 'U');
        return rna;

    def toString(self):
        print(self.ribbon);