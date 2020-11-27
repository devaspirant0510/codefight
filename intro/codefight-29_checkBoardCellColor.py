#=========================================#
# https://blog.naver.com/nova020510/222117752665 #
#=========================================#
# case 1:
def chessBoardCellColor(cell1, cell2):
    ax,ay=ord(cell1[0])-64,int(cell1[1]) # a 체스의 x좌표 y좌표
    bx,by=ord(cell2[0])-64,int(cell2[1]) # b 체스의 x좌표 y좌표
    abx=bx-ax # a와 b좌표가 x 축에서 떨어진 거리
    aby=by-ay # a와 b좌표가 y 축에서 떨어진 거리
    if (abx%2==0 and aby%2==0) or (abx%2==1 and aby%2==1): # 떨어진거리가 둘다 홀수거나 둘다 짝수일경우 True 리턴
        return True
    else: # 아닐경우 False 리턴
        return False  
#=========================================#
# case 2:
def chessBoardCellColor(cell1, cell2):
    return (sum(map(ord,cell1+cell2)))%2 == 0
