low = 0
high = 100
mid = (int)((low+high)/2)
print("Please think of a number between 0 ans 100!")
while(True):
    print("Is your secret number ", mid, "?")
    ch = str(input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly."))
    if(ch == "c"):
        print("Game over. Your secret number was: ", mid)
        break;
    elif(ch == "l"):
        low = mid
    elif(ch == 'h':
        high = mid
    else:
         print("Sorry I failed to understand your message!")
         break
    mid = (int)((low+high)/2)
