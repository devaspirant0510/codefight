#=========================================#
# https://blog.naver.com/nova020510/222115789470 #
#=========================================#
# case 1:
def variableName(name):
    for num,i in enumerate(name):
        if num==0 and i.isdigit():# 첫번째 인덱스가 숫자일경우 False 리턴
            return False
        if i.isalpha()==False and i.isdigit()==False: # i가 숫자도 아니고 문자도 아닐경우 => 특수문자인경우 
            if i=='_': # 언더바인경우는 예외
                continue
            return False 
    return True
#=========================================#
# case 2:
def variableName(name):
    return name.isidentifier()
            
