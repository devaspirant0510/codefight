#https://blog.naver.com/nova020510/222083443195
#=================================================
#case1
def add(param1, param2):#기본적인 함수
    return param1+param2

#=================================================
#case2
def  add(a,b): # 람다 함수
    return (lambda x, y: x + y)(a, b)
