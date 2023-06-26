# TODO: Implementieren Sie die beiden Funktionen wie in der Aufgabenstellung beschrieben!
# Verändern Sie das Dictionary "languagePopularity" nicht!

languagePopularity = {"JavaScript": 1, "Java": 2, "Python": 3, "CSS": 4, "PHP": 5, "Ruby": 6, "C++": 7, "C": 8, "Shell": 9, "C#": 10}

# Hilfsfunktion: soll das Tupel (i,j) zurückgeben
def teile(L, low, high): 
    p = (low + high)//2
    s = L[p]
    i = low
    j = high

    # for l in L:
    #     if not l in languagePopularity:
    #         languagePopularity[l]= len(languagePopularity)
    #         print(languagePopularity)
        

    print(i, j)
    while not i > j:
        while languagePopularity[L[i]] < languagePopularity[s]:
            i += 1
        while languagePopularity[L[j]] > languagePopularity[s]:
            j -= 1
        if i <= j:
            (L[i], L[j]) = (L[j], L[i])
            i += 1
            j -= 1
    return (i,j)

def quicksort(L, low, high):
    if L == []:
        return L

    p = teile(L, low, high)

    if low < p[1]:
        quicksort(L, low, p[1])
    if p[0] < high:
        quicksort(L, p[0], high)
    return L

def start(L):
    return quicksort(L, 0, len(L)-1)
