#================================================#
# https://blog.naver.com/nova020510/222092574836 #
#================================================#
# case :1
def allLongestStrings(inputArray):
    li=[]
    # 문자열의 크기를 li에 저장
    for i in inputArray:
        li.append(len(i))
    # 크기가 가장 큰 문자열을 ma로 지정
    ma=max(li)
    answer=[]
    # inputArray 돌면서 ma와 i의 크기가 같은지 비교
    for i in inputArray:
        if len(i)==ma:
            # 크기가 같다면 answer에 추가
            answer.append(i)
    return answer
#================================================#
# case :2
def allLongestStrings(inputArray):
    m = max(len(s) for s in inputArray) #포문 돌면서 크기가 가장 큰값을 구함 => case1코드 간략화
    r = [s for s in inputArray if len(s) == m] # len(s)와 m이 값은지 비교 => case1코드 간략화
    return r
