#================================================#
# https://blog.naver.com/nova020510/222094780621 #
#================================================#
# case :1 
def commonCharacterCount(s1, s2):
    su=set(s1) & set(s2) # s1과 s2 의 공통으로 들어가는 엘리먼트 구합 => 공집합
    answer=0
    for i in su: # 공통으로 들어가는 집합 포문 돌면서
        answer+=min(s1.count(i),s2.count(i)) #s1과 s2중에 작은값 더함 
    return answer
