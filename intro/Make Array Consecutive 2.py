#================================================
#https://blog.naver.com/nova020510/222087905915 #
#================================================
# case 1
#================================================

# 머지소트
def merge_sort(li):
    if len(li)<=1:
        return li
    else:
        mid=len(li)//2
        # 중앙을 기준으로 분활
        left=merge_sort(li[:mid])
        right=merge_sort(li[mid:])
        # 분활된 엘리먼트를 합치면서 정렬
        return merge(left,right)
# 머지
def merge(left,right):
    i=j=0
    s=[]
    # left와 right 첫번째 엘리멘트부터 비교
    # i나 j 중 하나라도 left나 right크기를 넘길경우 빠져나옴 
    while i<len(left) and j<len(right):
        # left가 작다면 left[i]값을 더하고
        # i값 1증가
        if left[i]<right[j]:
            s.append(left[i])
            i+=1
        else:
            s.append(right[j])
            j+=1
    # left와 right중 비어있는 리스트 그대로 대입
    if i<len(left):
        s+=left[i:]
    else:
        s+=right[j:]
    return s
def makeArrayConsecutive2(statues):
    sorts=merge_sort(statues) #머지소트로 statues 정렬
    answer=0
    for i in range(len(sorts)-1):
        if sorts[i]!=sorts[i+1]+1:#1씩 증가하는 배열이 아닐경우
            answer+=sorts[i+1]-sorts[i]-1 #i+1 값에서 i번째 값을 빼고 -1을 함 ex> 2 3 6 8 -> 6-3-1=2 -> 3 (4) (5) 6

    return answer
#================================================
# case 2
#================================================
def makeArrayConsecutive2(statues):
    # 1씩 증가하는 배열을 만들어야 되니
    # statuse의 최솟값과 statues의 최댓값을 for문에 넣음
    sorts=[i for i in range(min(statues),max(statues)+1)]
    # 정렬된 배열 크기 - 원래 배열 크기
    return len(sorts)-len(statues)

