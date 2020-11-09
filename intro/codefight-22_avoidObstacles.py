#=========================================#
# https://blog.naver.com/nova020510/222109402686 #
#=========================================#
#  case 1:
def avoidObstacles(s):
    s=sorted(s)
    full=[i for i in range(2,max(s)+1)] # x%1=0 이 항상 성립하기때문에 2부터 max(s)까지 오름차순리스트 생성
    an=[]                       
    for i in range(len(full)): # 불필요한 계산을 줄이기 위해 s에 포함된 엘리먼트 제거
        if full[i] in s:
            pass
        else:
            an.append(full[i])

    for i in range(len(an)):
        result=list(map(lambda x:x%an[i],s)) # s에서 x%a[i]의 값을 각각 계산 
        if not 0 in result: # 계산한 result에 0이 포함되지 않을경우 현재 an[i]값 리턴
            return an[i]
    return max(s)+1  # an의 정답이 없는경우 => s에서 가장 큰값에다 1을 더한값 리턴
#=========================================#
# case 2:
def avoidObstacles(inputArray):
    c = 2
    while True:
        if sorted([i%c for i in inputArray])[0]>0:
            return c
        c += 1
