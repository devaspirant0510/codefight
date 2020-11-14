#=========================================#
# https://blog.naver.com/nova020510/222111050473 #
#=========================================#
# case 1:
def boxBlur(image):
    width,height=len(image),len(image[0]) # image 크기(높이,너비)
    filter_width,filter_height=width-3+1,height-3+1 # 필터링된 이미지 크기 (w-f+1) * (h-f+1)

    pooling=[ [0 for i in range(filter_height)]for j in range(filter_width)] # 필터링된 이미지 행렬 초기화
    for i in range(filter_width):
        for j in range(filter_height):
            pooling[i][j]=avg_pooling(image,i,j) #i행 j열마다 avg_pooling한 값 반환
    return pooling

def avg_pooling(m,r,c):# 3x3행렬의 요소를 다 더하고 평균값을 구해주는 함수
    su=0
    # boxBlur에서 i와 j값을 인자값으로 받아 i+3,j+3 만큼의 합을 구함
    for i in range(r,r+3):
        for j in range(c,c+3):
            su+=m[i][j]

    return su//9 # 평균값 => 9로 나눈값 반환
#=========================================#
# case 2:
def boxBlur(image):
    r = []
    for i in range(len(image)-2):
        r.append([])
        for j in range(len(image[0])-2):
            r[i].append(sum(image[i][j:j+3] + image[i+1][j:j+3] + image[i+2][j:j+3])/9//1)
    return r
