#=========================================#
# https://blog.naver.com/nova020510/222112203351 #
#=========================================#
#  case 1:
def Number_Of_Mine(result,r,c): # i행j열을 제외한 8방향에 1씩 더해주는 함수
    # m*n 행렬이 (m+2)*(n+2) 행렬로 바뀌기 때문에 행과 열에 1씩 더해줌 ( 위 그림 참고)
    r=r+1
    c=c+1
    
    for i in range(r-1,r+2): # -1,0,1 
        for j  in range(c-1,c+2): # -1,0,1 위치에 1씩더함

            result[i][j]+=1
            if (i,j)==(r,c): # 지뢰가 있는 위치는 제외
                result[i][j]-=1 
    return result
def minesweeper(matrix):
    row=len(matrix) # 입력된 리스트의 높이
    col=len(matrix[0]) # 입력된 리스트의 너비
    result=[[ 0 for i in range(col+2)] for j in range(row+2)] # 테두리크기가 1인 빈 리스트

    for i in range(row):
        for j in range(col):
            if matrix[i][j]==True: # i행 j열에 지뢰(True)가 있을경우
                Number_Of_Mine(result,i,j) # 위에서 선언한 테두리 크기가 1인 빈리스트와 현재 행과 열을 전달
    
    result=[result[1:-1][i][1:-1] for i in range(row)] # 결과값에서 테두리를 제거
    return result
#=========================================#
# case 2:
def minesweeper(matrix):
    r=len(matrix)
    c=len(matrix[0])
    m=[[] for x in range(r)]
    for x in range(r):
        for y in range(c):
            count=0
            if r>x-1>=0 and c>y-1>=0 and matrix[x-1][y-1]==True:
                count+=1
            if r>x>=0 and c>y-1>=0 and matrix[x][y-1]==True:
                count+=1
            if r>x+1>=0 and c>y-1>=0 and matrix[x+1][y-1]==True:
                count+=1
            if r>x-1>=0 and c>y>=0 and matrix[x-1][y]==True:
                count+=1
            if r>x+1>=0 and c>y>=0 and matrix[x+1][y]==True:
                count+=1
            if r>x-1>=0 and c>y+1>=0 and matrix[x-1][y+1]==True:
                count+=1
            if r>x>=0 and c>y+1>=0 and matrix[x][y+1]==True:
                count+=1
            if r>x+1>=0 and c>y+1>=0 and matrix[x+1][y+1]==True:
                count+=1
            m[x].append(count)
    return(m)
