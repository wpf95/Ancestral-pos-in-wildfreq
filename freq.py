# time：2023/4/15 15:04
# name：Wangpf
# encoding：utf-8

#usage:python freq.py [wild.freq] [vcf.freq] [out.file]

import sys
fo1=open(sys.argv[1],"r")
fo2=open(sys.argv[2],"r")
out=open(sys.argv[3],"w")

out.write("CHROM"+"\t"+"POS"+"\t"+"ref"+"\t"+"alt"+"\n")
for line in fo1:
    if line.startswith("CHROM"):
        pass
    else:
        line = line.strip().split()
        bs1 = line[4].split(":")[0]
        bs2 = line[5].split(":")[0]
        fq1 = line[4].split(":")[1]
        fq2 = line[5].split(":")[1]
        if fq1== '-nan':
            for i in fo2:
                if i.startswith("CHROM"):
                    pass
                else:
                    i = i.strip().split()
                    pos1=line[0]+"_"+line[1]
                    pos2=i[0]+"_"+i[1]
                    if pos1 == pos2:
                        b1 = i[4].split(":")[0]
                        b2 = i[5].split(":")[0]
                        f1 = i[4].split(":")[1]
                        f2 = i[5].split(":")[1]
                        if f1 > f2:
                            out.write(i[0]+"\t"+i[1]+"\t"+b1+"\t"+b2+"\n")
                            break
                        elif f1 < f2:
                            out.write(i[0]+"\t"+i[1]+"\t"+b2+"\t"+b1+"\n")
                            break
                        elif f1 == f2:
                            out.write(i[0]+"\t"+i[1]+"\t"+b1+"\t"+b2+"\n")
                            break
        elif fq1 > fq2:
            out.write(line[0]+"\t"+line[1]+"\t"+bs1+"\t"+bs2+"\n")
        elif fq1 < fq2:
            out.write(line[0]+"\t"+line[1]+"\t"+bs2+"\t"+bs1+"\n")
        elif fq1 == fq2:
            out.write(line[0]+"\t"+line[1]+"\t"+bs1+"\t"+bs2+"\n")

fo1.close()
fo2.close()
out.close()
