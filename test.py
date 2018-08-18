
import numpy as np
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
def loadDna(path):
    f = open(path,"r");
    Dna = f.read();
    f.close()
    return Dna;
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
def Noncoding(Dna,bounds):
    Dna = Dna.upper();
    ans= []
    for i in range(len(bounds)-1):
        endf = bounds[i][1];
        satrtn = bounds[i+1][0]
        if (satrtn -endf) > 127:
            cut =Dna[endf:satrtn-50]
        ans.extend(GCcontent(cut));
    return ans;
def StatsOf ( inlist ):
    vec = np. array ( inlist )
    return vec . mean () , vec .std ()

print ("***********noncoding*********")
print(Noncoding(loadDna("sequence ch18.txt"),loadBound("a.txt")))
print("**********state of noncoding *********************")
print(StatsOf(Noncoding(loadDna("sequence ch18.txt"),loadBound("a.txt"))))
