#=========================================#
# https://blog.naver.com/nova020510/222107790940 #
#=========================================#
# case 1:
def isIPv4Address(s):
    s=s.split('.') # .을 기준으로 쪼갬
    li=[]
    if len(s)==4: # s의 길이가  4일경우
        # i가 숫자가 아닌경우 걸러내는 부분
        for i in s: # for 문 돌면서 첫번째 값부터 4번째 값까지 확인
            if i=='': # i값이 공백일경우 리턴 False
                return False
            for j in i: # 2중포문 돌면서 텍스트를 하나하나비교
                if j.isalpha():# 알파벳이 나올경우 리턴 False
                    return False
        # i가 숫자인 경우 범위를 벗어날시 걸러내는 부분
        for i in s:
            if i[0]=='0' and len(i)>1: # 03 012 이렇게 앞쪽에 0이 있고 뒤에 정수가 올경우 리턴 False
                return False
            if int(i)<0 or int(i)>255: # i가 0~255 범위를 벗어날시 리턴 False
                return False
        return True
    else: # s의 길이가 4가 아닌경우  바로 리턴 False
        return False
#=========================================#
# case 2:
def isIPv4Address(s):
    p = s.split('.') # . 을 기준으로 분활 
    return len(p) == 4 and all(n.isdigit() and 0 <= int(n) < 256 for n in p) # 분활한 값이 0~256사이에 있는지 판단
