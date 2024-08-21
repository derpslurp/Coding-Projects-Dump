loan = int(input('Choose amount of money you were loaned: '))
term = input('Choose loan term (Yearly/Monthly/Daily): ')
term2 = int(input('Choose loan time (Years): '))


interest1 = int(input('Choose interest rate: '))
interest2 = interest1 / 100
interest = interest2 + 1


if term == 'Yearly':
    payment = loan / term2
    payment1 = payment * interest
    print('The amount you need to pay per year is: $', payment1)
elif term == 'Monthly':
    term1 = term2 * 12
    payment = loan / term1
    payment1 = payment * interest
    print('The amount you need to pay per month is: $', payment1)
elif term == 'Daily':
    term1 = term2 * 12
    term3 = term1 * 365
    payment = loan / term3
    payment1 = payment * interest
    print('The amount you need to pay per day is: $', payment1)
