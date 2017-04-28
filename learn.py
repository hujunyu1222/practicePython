# test
import sys;

def process(s):
    st = [];
    rcnt = ycnt = bcnt = 0;
    for i in range(0,len(s)):
        if (s[i][0] == '#'):
            if(s[i][1] == '/'):
                st.pop();
            else:
                st.append(s[i]);
        elif (st[-1] == "#yellow"):
            ycnt += len(s[i]);
        elif (st[-1] == "#blue"):
            bcnt += len(s[i]);
        elif (st[-1] == "#red"):
            rcnt += len(s[i]);
    print("%d %d %d"%(rcnt, ycnt, bcnt));

def main():
    infile = open("1.txt");
    s = infile.readline();
    s = s.replace(' ','').replace('<'," #").replace('>',' ').split();
    process(s);
                
    
if __name__ == "__main__":
    main();
