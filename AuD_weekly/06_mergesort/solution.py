# TODO: Implementieren Sie die Funktionen wie in der Aufgabenstellung beschrieben!

def merge(leftPart, rightPart):
    L = []
    i = j = 0
    while i != len(leftPart) or j != len(rightPart):
        if (i == len(leftPart)):
            L.append(rightPart[j])
            j += 1
        elif (j == len(rightPart)):
            L.append(leftPart[i])
            i += 1
        elif (leftPart[i][1] > rightPart[j][1]):
            L.append(leftPart[i])
            i += 1
        else:
            L.append(rightPart[j])
            j += 1
    return L

def split(L):
    m = len(L)//2
    if(len(L) > 1):
        leftPart = L[m:]
        rightPart = L[:m]
        return merge(split(leftPart), split(rightPart))
    else:
        return L

def mergesort(L):
    return split(L)
