class Solution:
    #@param A and B: sorted integer array A and B.
    #@return: A new sorted integer array
    def mergeSortedArray(self, A, B):
        # write your code here
        res = [];
        i = j = 0;
        while i < len(A) and j < len(B):
            if (A[i] < B[j]):
                res.append(A[i]);
                i = i + 1;
            else:
                res.append(B[j]);
                j = j + 1;
        if (i < len(A)):
            res = res + A[i:];
        else:
            res = res + B[j:];
        return res;

def main():
    A = [1,3,5,7];
    B = [2,4,6,8];
    sp = Solution();
    res = sp.mergeSortedArray(A,B);
    print(res);

if __name__ == "__main__":
    main();
    
