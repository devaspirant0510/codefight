#========================================================
# blog : https://blog.naver.com/nova020510/222087081788 #
#========================================================
# case 1 
def shapeArea(n):
    return n*n+(n-1)*(n-1) #택시기하학
#========================================================
# case 2
def shapeArea(n):
    result = 1
    for i in range(n):
        result += 4 * i
    return result
