def quesako(mot):
    tom=""
    for k in range(len(mot)):
        tom=tom+mot[len(mot)-k-1]
    return tom

quesako("informatique")
