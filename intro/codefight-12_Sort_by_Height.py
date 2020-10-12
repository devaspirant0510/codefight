#================================================#
# https://blog.naver.com/nova020510/222096179302 #
#================================================#
# case :1 
def sortByHeight(a):
    minus_index_li=[] # -1이 있는 index 위치 저장 할 리스트
    numli=[] # -1을 제외한 양수 저장 할 리스트
    for n,i in enumerate(a): # enumerate로 인덱스위치도 같이 구함
        if i==-1: # i가 -1일땐 minus_index에 인덱스 위치를 추가
            minus_index_li.append(n)
        else: # -1이 아닌경우 numlist에 i 값 추가
            numli.append(i)
    sortnum=sorted(numli)# numli 정렬

    for i in minus_index_li:
        sortnum.insert(i,-1)# 정렬된 numli에 원래 위치에 있는 -1을 삽입
    return sortnum
#================================================#
# case :2
def sortByHeight(a):
    l = sorted([i for i in a if i > 0]) # i가 0 이상인 경우만 정렬
    for n,i in enumerate(a): # 원본리스트를 돌면서 i가 -1일때
        if i == -1:
            l.insert(n,i)# 정렬된 리스트 l에 -1삽입
    return l

    
