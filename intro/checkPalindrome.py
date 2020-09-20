#https://blog.naver.com/nova020510/222084476012

#case1
#==========================================
def checkPalindrome(inputString):
    if inputString==inputString[::-1]:#슬라이싱으로 역순 한 값과 원래 값이 같을때 True
        return True
    else:#같지않다면 False
        return False

#==========================================
#case2
def checkPalindrome(inputString):
    pal=[]#빈리스트 생성
    for i in range(len(inputString)-1,-1,-1):#포문 역순으로 
        pal.append(inputString[i])#pal에 역순으로 엘리먼트 저장
    if list(inputString)==pal: # 역순으로 저장된 pal과 원래 리스트가 같을때 True 반환
        return True
    else:
        return False
