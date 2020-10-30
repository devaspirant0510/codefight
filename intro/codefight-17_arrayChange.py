#=========================================#
# https://blog.naver.com/nova020510/222103831358 #
#=========================================#
# case 1:
def arrayChange(li):
    su=0
    for i in range(len(li)-1): 
        # i번째 값과 i+1번째 값을 비교해서 
        # i번째 값이 i+1번째 값보다 크거나 같을경우
        if li[i]>=li[i+1]:
            su+=li[i]+1-li[i+1]#최소한의 수를 구해야됨 => i번째 값 +1
            li[i+1]=li[i]+1  #변경된 값 적용

    return su  
#=========================================#
# case 2:
def arrayChange(inputArray):
    target  = inputArray[0] - 1
    steps = 0
    
    for i in inputArray:
        if i > target: 
            target = i
        else:
            target = target + 1
            steps += target - i
            
    return steps
