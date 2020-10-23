#================================================#
# https://blog.naver.com/nova020510/222102299371 #
#================================================#
# case 1:
def areSimilar(a, b):
    dif_a=[] # 새로 담을 a배열 리스트 
    dif_b=[] # 새로 담을 b배열 리스트 
    if a==b: # a와 b가 같을시 바로 리턴
        return True
    for i in range(len(a)):# 배열의 크기만큼 for 문
        if a[i]!=b[i]: ai번째의 엘리먼트와 bi의 엘리먼트가 서로 다를때 
            dif_a.append(a[i]) # 각각의 엘리먼트를  리스트에 추가
            dif_b.append(b[i])
        
        if len(dif_a)>2: # 추가된 리스트의 크기가 3이상일경우 => 한번의 스왑만 혀용되기때문에 다른값이 두번 있는건 상관없음
            return False # 리턴 False
    return sorted(dif_a)==sorted(dif_b) # 두리스트를 정렬해서 비교 => 두 값이 스왑했을때 같아야 하기떄문에 두 배열의 요소가 같아야됨
#================================================#
# case 2:
def areSimilar(A, B):
    return sorted(A)==sorted(B) and sum([a!=b for a,b in zip(A,B)])<=2 # 정렬된 배열이 같으면서 a와 b의 요소들을 서로 비교해 a!=b인 값이 두개 이하인경우
                                                                      
