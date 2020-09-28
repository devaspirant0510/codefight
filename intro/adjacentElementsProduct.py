#=========================================
https://blog.naver.com/nova020510/222085968276
#=========================================
# case 1
def adjacentElementsProduct(inputArray):
    su=[]# 빈리스트 생성
    
    for i in range(len(inputArray)-1):
        su.append(inputArray[i]*inputArray[i+1])#이웃한 두수의 곱 리스트에 추가
    #리스트중에서 가장 큰값 리턴
    return max(su)  
#=========================================
# case 2    
def adjacentElementsProduct(inputArray):
    # 위 코드 한줄로 줄임
    return max([inputArray[i] * inputArray[i+1] for i in range(len(inputArray)-1)])
