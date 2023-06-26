def merge(leftPart, rightPart):
    foo = []
    left = 0
    right = 0
    while left != len(leftPart) or right != len(rightPart):
        if left == len(leftPart):
            foo.append(rightPart[right])
            right += 1
            continue
        if right == len(rightPart):
            foo.append(leftPart[left])
            left += 1
            continue
        if leftPart[left][1] > rightPart[right][1]:
            foo.append(leftPart[left])
            left += 1
        else:
            foo.append(rightPart[right])
            right += 1
    return foo


def split(L):
    return L if len(L)<=1 else merge(split(L[:len(L)//2]),  split(L[len(L)//2:]))

def mergesort(L):
    return split(L)

print(mergesort([("Interstellar", 13), ("James Bond", 76), ("La La Land", 77), ("Ziemlich beste Freunde", 78), ("Inception", 40), ("Herr der Ringe", 85)]))
