num = -25
epsilon = 0.01
numGuesses = 0
low = 1.0
b = 0
if num<0:
    num = -num
    b = 1
high = num
ans = (high+low)/2.0
while abs(ans**3 - num) >= epsilon:
    print("low = ", low, " high = ", high, " ans = ", ans)
    numGuesses += 1
    if ans**3 < num:
        low = ans
    else:
        high = ans
    ans = (high+low)/2.0
print("Number of Guesses = ", numGuesses)
if b==1:
    ans = -ans
    num = -num
print(ans, " is the close cube root of ", num)
