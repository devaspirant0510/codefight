#=========================================#
# https://blog.naver.com/nova020510/222105611659 #
#=========================================#
# case 1:
def areEquallyStrong(yourLeft, yourRight, friendsLeft, friendsRight):
    # 내 양쪽팔의 힘과 친구의 양쪽팔의 힘이 같은지 확인
    return sorted([yourLeft,yourRight]) == sorted([friendsLeft,friendsRight])
