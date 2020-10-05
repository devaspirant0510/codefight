#=================================================
# https://blog.naver.com/nova020510/222090207692 #
#=================================================

def almostIncreasingSequence(sequence): # 리스트에서 엘리먼트 하나를 제거했을때 오름차순이 나오는지 판별하는 문제
    c = 0
    for i in range(len(sequence)-1):
        if sequence[i] >= sequence[i+1]: 
            c += 1
        if i+2 < len(sequence) and sequence[i] >= sequence[i+2]: 
            c += 1
    return c < 3
