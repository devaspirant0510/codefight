#=========================================#
# https://blog.naver.com/nova020510/222116835499 #
#=========================================#
# case 1:
def alphabeticShift(inputString):
    result=[] # 결과값 출력할 리스트
    for i in inputString:
        if i=='z': # z일경우 a 삽입
            result.append('a')
        else:
            result.append(chr(ord(i)+1)) # z가 아닌경우 ord함수로 문자 -> 정수 +1 한 상태에서  chr()함수로 문자열로 만들어서 삽입
    return "".join(result) # join 함수로 리스트 -> 문자열
#=========================================#
# case 2:
def alphabeticShift(inputString):
    return "".join([ 'a' if i=='z' else chr(ord(i)+1) for i in inputString
#=========================================#
# case 3:
def alphabeticShift(s):
    return "".join(chr((ord(i)-96)%26+97) for i in s) # 아스키 코드값 이용해 구함
