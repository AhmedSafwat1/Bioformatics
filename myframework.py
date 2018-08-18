# this imoprt lib
import re
import numpy as np
#my codon table
def codonTable(codon):
    codon = codon.upper()
    table = {"UUU": "F", "UUC": "F", "UUA": "L", "UUG": "L",
           "UCU": "S", "UCC": "s", "UCA": "S", "UCG": "S",
           "UAU": "Y", "UAC": "Y", "UAA": "STOP", "UAG": "STOP",
           "UGU": "C", "UGC": "C", "UGA": "STOP", "UGG": "W",
           "CUU": "L", "CUC": "L", "CUA": "L", "CUG": "L",
           "CCU": "P", "CCC": "P", "CCA": "P", "CCG": "P",
           "CAU": "H", "CAC": "H", "CAA": "Q", "CAG": "Q",
           "CGU": "R", "CGC": "R", "CGA": "R", "CGG": "R",
           "AUU": "I", "AUC": "I", "AUA": "I", "AUG": "M",
           "ACU": "T", "ACC": "T", "ACA": "T", "ACG": "T",
           "AAU": "N", "AAC": "N", "AAA": "K", "AAG": "K",
           "AGU": "S", "AGC": "S", "AGA": "R", "AGG": "R",
           "CAU": "V", "GUC": "V", "GUA": "V", "GUG": "V",
           "GCU": "A", "GCC": "A", "GCA": "A", "GCG": "A",
           "GAU": "D", "GAC": "D", "GAA": "E", "GAG": "E",
           "GGU": "G", "GGC": "G", "GGA": "G", "GGG": "G", }
    return table[codon];

#for Test codon table
def Test_codon_table(Dna):
    Protein = ""
    Dna = Dna.upper()
    Dna.strip();
    start = Dna.find("AUG")
    if start != -1 :
        while start + 2 < len(Dna):
            codon = codonTable(Dna[start:start + 3])
            if codon == "STOP":
                break;
            els0.0.e:
             Protein += codon;
             start += 3
    return Protein


# make Dna to Rna
def transcription(DNA):
    DNA = DNA.upper();
    x=DNA.replace("T","U");
    return x


#make Dna frpm RNA
def make_DNA_From_RNA(RNA):
    RNA = RNA.upper()
    return RNA.replace("U","T");

#mke coplemrnt for rna
def Complement_RNA(RNA):
    RNA = RNA.upper()
    g = RNA.maketrans("GCAU","CGUA");
    x= RNA.translate(g);
    return x
def Rev_Coplement_RNA(RNA):
    Coomlemt = Complement_RNA(RNA)
    REV_Coplement = Coomlemt[ : :-1]
    return REV_Coplement;




#*****************************************************************

# count the number of word in file
def count(filePath):
     total = 0
     lines_list = []
     line_reduce = []
     f = open(filePath,"r")
     lines = f.readlines()
     print(lines_list)
     for i in lines:
         if emptyline(i) == True:
             continue
         else:
             x=i.split(" ");
             print(x);

             total += len(x)- x.count('')
     return  total



# count the number of word in file
def count_Word(file):
    list_word= []
    list_freq = []
    out = {};
    f = open(file,"r");
    in_text = f.read().lower();
    list_word = re.findall(r' (\b [a-z]{3,15}\b)',in_text)
    print(in_text)
    print(list_word)


def emptyline(line):
        if line[0] == "\n" and len(tuple(line))== 1:
           return True
        return False



# first programm 1books reed file 1


def loadDna(path):
    f = open(path,"r");
    Dna = f.read();
    f.close()
    return Dna;



# load bound from the file 2

def loadBound(path):
    f =open(path,"r");
    raws = f.readlines();
    f.close();
    bounds = []
    for raw in raws:
        if len(raw) > 1:
            start,stop,cflag = raw.split("\t")
            start = int(start);
            stop = int(stop);
            cflag = int(cflag)
            bounds.append((start,stop,cflag))
    return bounds
'''
  for check the bounde true
  ((start -1 ) - end )/3
'''


# complemnt Dna 3
def Dna_Complement(Dna):
    Dna = Dna.upper();
    rule = Dna.maketrans("ATCG","TAGC");
    x = Dna.translate(rule);
    return x;


# gcontent
def GCcontent(instr, window=128, step=32):
    answ = []
    for i in range(0, len(instr), step):
        cut = instr[i:i + window].lower()
        a = cut.count('a')
        g = cut.count('g')
        c = cut.count('c')
        t = cut.count('t')
        r = float(c + g) / (a + c + g + t)
        answ.append(r)
    return answ

# check bad codon in file 4


def CheckForStartsStops(Dna,bounds):
    n =  len(bounds);
    Dna = Dna.upper()
    bads = []
    for i in range(n):
        start,stop,cfg=bounds[i];
        cut = Dna[start-1:stop];
        if cfg:
            cut = Dna_Complement(cut);
        startcodon =cut[0:3];
        endcodon = cut[-3:];
        m =((start-1)-stop)%3;
        if m == 0 and (startcodon == "ATG" or startcodon == "GTG" or startcodon == "TTG") and (endcodon == "TAG" or endcodon == "TAA" or endcodon == "TGA"):
            pass
        else:
            bads.append((start,stop,cfg))
    return bads;



# Gcontant 5




# noncodiong region 6
def Noncoding(Dna,bounds):
    Dna = Dna.upper();
    ans= []
    for i in range(len(bounds)-1):
        endfirst = bounds[i][1];
        satrtnext = bounds[i+1][0]
        if (satrtnext -endfirst) > 127:
            cut =Dna[endfirst:satrtnext-50]
        ans.extend(GCcontent(cut));
    return ans;


# state noncoding 7

def StatsOf ( inlist ):
    vec = np. array ( inlist )
    return vec . mean () , vec .std ()



# coding 8
def Coding(indna, bounds):
    answ = []
    for k in range(len(bounds)):
        start, stop, cflag = bounds[k]
        if cflag == 0 and stop - start > 128:
            answ.extend(GCcontent(indna[start: stop]))
    return answ

'''

can calculate the  stat also

'''

# prcodong 9


def Precoding ( indna , bounds ):
    answ = []
    for k in range ( len( bounds )-1):
        stop = bounds [k ][1] # stop of first gene
        start = bounds [k +1][0] # start of next gene
        cflag = bounds [k +1][2]
        if start-stop >50 and cflag ==0:
            cut = indna [ start-50: start ]
            answ . extend ( GCcontent ( cut ) )
    return answ


# read dna from fasta file
def loadDnaFast(path):
    f = open(path,"r");
    x = f.readlines();
    f.close()
    print(x[0])
    Dna ="".join(x[1:]);
    Dna = Dna.replace('\n',' ')
    return Dna;



'''
   haming distance
   for two strings and calc the different
'''
def haming(str1,str2):
    h = 0
    try:
        if len(str1) != len(str2):
            raise ValueError("the length must be equal for two varibel")
        if type(str1) != str or type(str2) != str:
            raise ValueError("must enter the two varible str")
        for i in range(len(str2)):
            if str2[i] != str1[i]:
                h +=1
        return h
    except ValueError as e:
        print("errror.....",e)
