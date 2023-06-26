# TODO: Implementieren Sie die Funktion wie in der Aufgabenstellung beschrieben! 
# Nur rekursive Lösungen werden akzeptiert!

def transformToUppercase(s):
    if not s:
        return ''
    char = s[0]
    return char.upper() + transformToUppercase(s[1:])
