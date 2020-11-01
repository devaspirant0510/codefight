#=========================================#
# https://blog.naver.com/nova020510/222104637538 #
#=========================================#
# case 1:
def palindromeRearranging(inputString):
    li=[]
    su=len(inputString) #문자열의 크기 => 문자열의 크기 홀짝에따라 로직이 달라짐
    setli=set(inputString) # 각 엘리먼트의 원소개수 세기 위해 셋
    od=0 # 홀수가 몇개 있는지 판단
    for i in setli: #엘리먼트 개수세기
        if inputString.count(i)%2==1: #엘리먼트 개수가 홀수일때 
            od+=1
            if su%2==0: # 입력한 문자열의 크기가 짝수인데 홀수가 들어가면 펠린드롬문자열이 안됨 => 리턴 False
                return False
            else: # 입력한 문자열의 크기가 홀수일경우 정중앙에 홀수개의 문자열이 들어갈수 있음 
                if od>1: # 단 엘리먼트의 갯수가 홀수경우가 두번이상 나올경우 리턴 False
                    return False
    return True
#=========================================#
# case 2:
def palindromeRearranging(inputString):
    return sum([inputString.count(i)%2 for i in set(inputString)]) <= 1
