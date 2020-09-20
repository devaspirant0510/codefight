#https://app.codesignal.com/arcade/intro/level-1/egbueTZRRL5Mm4TXN
def centuryFromYear(year):
    if year%100==0:#100으로 나누어 떨어질경우 몫만 구함
        return year//100
    else:#100으로 나누어 떨어지지 않을경우 몫에다 1 더함
        return year//100+1      
