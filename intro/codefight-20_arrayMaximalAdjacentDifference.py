#=========================================#
# https://blog.naver.com/nova020510/222106635715 #
#=========================================#
# case 1:
def arrayMaximalAdjacentDifference(s):
    st=[-1] # 초기 배열
    for i in range(len(s)-1): 
        absoul=(lambda a,b:(a-b)*-1 if a-b<0 else a-b)(s[i],s[i+1]) # (abs로 대체 가능) 람다함수 + 삼항연산자 => 두수의 차가 음수가 될경우 +로 바꿔줌
        if st[0] < absoul: # 처음 선언한 배열의 값보다 두 이웃한 수의 절대값이 클때
            st.pop() # st의 값 삭제
            st.append(absoul) # st에 absoul값 추가
    return st[0]
#=========================================#
# case 2:
def arrayMaximalAdjacentDifference(s):
    li=[]
    for i in range(len(s)-1):
        li.append(abs(s[i]-s[i+1]))
    return max(li)
#=========================================#
# case 3:
def arrayMaximalAdjacentDifference(s):
    return max([abs(s[i]-s[i+1]) for i in range(len(s)-1)])
