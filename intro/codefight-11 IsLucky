#=================================================
# https://blog.naver.com/nova020510/222095850574 #
#=================================================
# case :1 
def isLucky(n):
    n=str(n) # 정수 => 문자열
    mid=len(n)//2 # 중앙값 구함
    lucknum=0 # mid~n[-1] 까지의 합계
    su=0 # 전체 합계
    for i in range(len(n)):
  
        su+=int(n[i]) # n[i]의 합계
        if i>=mid: # i 값이 mid보다 클때 lucknum 값에 더함
            lucknum+=int(n[i])
    if lucknum*2==su:# lucknum의 두배가 전체 합계랑 같은지 판단
        return True
    else:
        return False
#=================================================
# case :2 
  def isLucky(n):
    s = str(n)
    pivot = len(s)//2
    left, right = s[:pivot], s[pivot:] # 중앙을 기준으로 왼쪽과 오른쪽으로 슬라이싱
    return sum(map(int, left)) == sum(map(int, right)) # map함수로 문자열 => 정수형 => 합계 => left와 right가 같은지 판단
