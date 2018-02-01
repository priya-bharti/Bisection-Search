num = -25
epsilon = 0.01
numGuesses = 0
low = -1.0
high = num
ans = (high+low)/2.0
while abs(ans**3 - num) >= epsilon:
    print("low = ", low, " high = ", high, " ans = ", ans)
    numGuesses += 1
    if ans**3 < num:
        high = ans
    else:
        low = ans
    ans = (high+low)/2.0
print("Number of Guesses = ", numGuesses)
print(ans, " is the close cube root of ", num)
