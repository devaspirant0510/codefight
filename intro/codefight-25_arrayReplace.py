def arrayReplace(inputArray, elemToReplace, substitutionElem):
    for i in range(len(inputArray)): #포문 돌면서 i가 elemToReplace인지 판단
        if inputArray[i]==elemToReplace:
            inputArray[i]=substitutionElem # i가 elemToReplace일경우 substitutionElem 으로 바꿈
    return inputArray
