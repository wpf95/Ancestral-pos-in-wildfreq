# Ancestral-pos-in-wildfreq   
Use wild outgroup freq and vcf freq to exact ancestral pos   

Warning:the file vcf.freq pos must contain all the the pos of wild.freq , if not , this script can not use correctly , it just like  the 'yield' function in python ,so must strict in formate in input file.  

1.You need to use vcftools '--keep' to extract wild outgroup than run vcftools '--freq' to get the wild.freq   
2.Than you see some pos is not in wild.freq,You need to run the vcf.file '--freq' to get the vcf.freq  
3.Usage : python freq.py [wild.freq] [vcf.freq] [out.file]

