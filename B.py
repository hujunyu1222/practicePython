# problem B

import sys;

global INT_MAX
INT_MAX = 999999999;

def dfs(a, s, e):
    if (s > e):
        return;
    if (s == e):
        print(a[s], end = ' ');
        return;
    minN = INT_MAX;
    for i in range(s,e+1):
        if (a[i] < minN):
            minN = a[i];
            idx = i;
    print(a[idx], end = ' ');
    dfs(a, s, idx - 1);
    dfs(a, idx + 1, e);
    
def main(): 
    N = int(input());
    a = [];
    for i in range(N):
        a.append(int(input()));
    dfs(a, 0, N - 1);

if __name__ == "__main__":
    main();


