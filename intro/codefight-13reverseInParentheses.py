#================================================#
# https://blog.naver.com/nova020510/222099715525 #
#================================================#
def reverseInParentheses(s):
    for i in range(len(s)):
        if s[i] == "(": # 괄호 여는부분이 있을때
            start = i # start로 값을 인덱스 값으로 지정
        if s[i] == ")": # 괄호 닫는 부분이 있을때
            end = i # end 값을 인덱스 값으로 지정
            return reverseInParentheses(s[:start] + s[start+1:end][::-1] + s[end+1:]) #괄호부분 바깥쪽은 그대로 두고 괄호 안쪽부분은 괄호만 제거하고 역순한 리스트 리턴
    return s
