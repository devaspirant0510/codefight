#================================================#
# https://blog.naver.com/nova020510/222100942442 #
#================================================#
# case: 1
def addBorder(picture):
    row=len(picture)+2 # picture의 행에 +2
    col=len(picture[0])+2 # picture의 열에 +2
    answer=[i for i in range(row)] # 정답 리스트 초기화
    for i in range(row):
        if i==0 or i==len(picture)+1: # 1번째행이거나 마지막 행일때 *을 row만큼 추가
            answer[i]="*"*col
        else:
            answer[i]=f"*{picture[i-1]}*"# #나머지 경우 원래 데이터 양끝에 *추가
    
    return answer
#================================================#
# case:2
def addBorder(picture):
    l=len(picture[0])+2
    return ["*"*l]+[x.center(l,"*") for x in picture]+["*"*l] #center 함수 이용
