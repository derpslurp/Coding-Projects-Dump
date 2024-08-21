user_input = input('Type in a number to spell out in letters: ')

tens = {2:'twenty',3:'thirty',4:'forty',5:'fifty',6:'sixty',7:'seventy',8:'eighty',9:'ninety',10:'hundred'}

tensi = (2,3,4,5,6,7,8,9)

double_low = {10:'ten', 11:'eleven', 12:'twelve', 13:'thirteen', 14:'fourteen', 15:'fifteen',16:'sixteen',17:'seventeen',18:'eighteen',19:'nineteen'}

single = {0:'zero',1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine'}
if len(user_input) == 1:
    for i in range(0,10):
        if int(user_input) == i:
            print(single[i])
elif len(user_input) == 2:
    if int(user_input) <= 19:
        for i in range(10,20):
            if int(user_input) == i:
                print(double_low[i])
    elif int(user_input) >= 20:
        for i in range(2,10):
            if int(str(user_input)[:1]) == i:
                print(tens[i])
        for i in range(0,10):
            if int(str(user_input)[-1]) == i:
                print(single[i])