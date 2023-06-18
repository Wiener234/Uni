# TODO: Implementieren Sie die beiden Funktionen wie in der Aufgabenstellung beschrieben! 

def binSearch(L, n, start, end):
    m = (start + end) // 2
    if (L[m] == n):
        return True
    if (L[m] > n and m > start):
        return binSearch(L,n,start,m-1)
    if (L[m] < n and m < end):
        return binSearch(L,n,m+1,end)
    else:
        return False

def isSubset(A, B):
    if(type(B) != list):
        return False
    for i in B:
        if(len(A) == 0):
            boolen = False
        else:
            boolen = binSearch(A,i,0,len(A)-1)
        if(boolen ==False):
            return False
    return True
