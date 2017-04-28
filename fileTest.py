import sys;
import string;

#to process inputFile

def process(infilePath):
    infile = open(infilePath);
    line = infile.readline().split();
    start = int(line[-7] + line[-6], 16);
    
    cnt = 1;
    miss = 0;
    while True:
        line = infile.readline();
        if not line:
            end = idx;
            break;
        cnt = cnt + 1;
        line = line.split();
        idx = int(line[-7] + line[-6], 16);
    infile.close();
    return cnt / ((end - start + 1)*1.0);


infilePath = "D:\\python_Code\\" + sys.argv[1];

PRR = process(infilePath);
print("PRR is %.2f%%"%(PRR*100));

               
        
    
    

