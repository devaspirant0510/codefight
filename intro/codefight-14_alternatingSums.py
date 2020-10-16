#================================================#
# https://blog.naver.com/nova020510/222100053315 #
#================================================#
# case:1
def alternatingSums(a):
    team=[0,0] # 짝수와 홀수의 합을 담을 리스트
    for i in range(len(a)):
        if i%2==0: # 짝수일경우
            team[0]+=a[i] # i의 값을 team의 0번째 값에 저장
        else: # 홀수일경우 
            team[1]+=a[i] # i의 값을 team의 1번째 값에 저장
    return team
    
#================================================#    
# case:2
def alternatingSums(a):
    return [sum(a[::2]),sum(a[1::2])] # 0번째 부터 스텝을 2만큼 슬라이싱,1번째 부터 스텝을 2만큼 슬라이싱

