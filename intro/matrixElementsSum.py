#================================================#
# https://blog.naver.com/nova020510/222091333865 #
#================================================#
# case 1:
def matrixElementsSum(matrix):
    # 행렬의 행값
    row=len(matrix)
    # 행렬의 열값
    col=len(matrix[0])
    # 손님수
    guest=0
    # 2중포문으로 행렬 전체 탐색
    for i in range(row):
        for j in range(col):
            if matrix[i][j]==0: # 행렬(i,j) 가 0이 아니면서
                if i<row-1: # i 행이 row -1이 아닐때 => ex) 행이 3행일때 내위치가 3행이면 index out이 되서 -1을 해줌
                    matrix[i+1][j]=0 # 아랫행을 0으로 바꿈
            else:
                guest+=matrix[i][j] # 0이 아닌경우 각 행렬(i,j)를 guest에 더함
    return guest
 #================================================#
 # case 2:
 def matrixElementsSum(m):
    # 행렬 정의
    r = len(m)
    c = len(m[0])
    total=0
    for j in range(c):
        for i in range(r):
            if m[i][j]!=0: # 행렬(i,j)가 0이 아닌경우
                total+=m[i][j] # total 값에 행렬(i,j) 더함
            else:
                break # 0인경우 그냥 break =>0이 나오면 그 밑에행은 손님이 들어갈수 없기때문에 볼 필요가 없음
    return total
