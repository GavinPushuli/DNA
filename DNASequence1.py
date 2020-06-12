import importlib

MName = input("DNAfile.txt")


importlib.import module(module)
inputfile = "DNAfile.txt"
f = open(inputfile,"r")

DNA_seq = f.read()
DNA_seq = DNA_seq.replace("\n","")
DNA_seq = DNA_seq.replace("\r","")


def translate(DNA_seq):
    AMINO_ACIDS = {
        'ATT':'I','ATC':'I','ATA':'I',
        'CTT':'L','CTC':'L','CTA':'L',
        'TTA':'L','TTG':'L','TTT':'F',
        'TTC':'F','GTT':'V','GTC':'V',
        'GTA':'V','GTG':'V','ATG':'M',
    }
    
    AMINO_ACIDS = ""
        if len(NM)%3 == 0:
        for i in range(0, len(seq),3):
            codon = seq[i:i + 3]
            AMINO_ACIDS+=table[codon]
        return AMINO_ACIDS
    
    def mutant(inputfile):
        with open(inputfile, "r") as f:
            DNA_seq = f.read()
            DNA_seq = DNA_seq.replace("\n","DNAfile.txt")
            DNA_seq = DNA_seq.replace("\r","DNAfile.txt")
            DNA_seq = DNA_seq.replace("a","A")
            return DNA_seq
            
    
    print(mutant(normalDNA.txt))
    print(mutant(mutantDNA.txt))
    
    def txtTranslate():
        with open("normalDNA.txt","r") as f:
            noDNA f.read()
        with open("mutantDNA.txt","r") as g:
            muDNA = g.read()
            
            return translate(noDNA)
            return translate(muDNA)
        
        txtTranslate()