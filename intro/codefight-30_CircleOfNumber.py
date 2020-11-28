#=========================================#
# https://blog.naver.com/nova020510/222118438410 #
#=========================================#
# case 1:
def circleOfNumbers(n, firstNumber):
    # 입력받은 n/2 를한후 firstNumber에 n/2 를 더한다
    # 더한 값이 n보다 커질경우 n을 빼주고
    # 아닐경우 그냥 그대로 둔
    return (lambda a,b:(a//2+b)-a if (a//2+b)>=a else a//2+b )(n,firstNumber)
#=========================================#
# case 2:
def circleOfNumbers(n, firstNumber):
    return (firstNumber + n/2)%n
