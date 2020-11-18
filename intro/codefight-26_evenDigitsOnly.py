#==========================================#
# https://blog.naver.com/nova020510/222114727183  #
#==========================================#
# case 1:
def evenDigitsOnly(n):
    for i in str(n):#int => str
        if int(i)%2==1: # 나머지가 1인경우 바로리턴
            return False
    return True
#==========================================#
# case 2:
def evenDigitsOnly(n):
    return all([int(i)%2==0 for i in str(n)])
