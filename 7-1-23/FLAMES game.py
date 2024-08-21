import time
relationship = ["Friends", "Lovers", "Affection", "Marriage", "Enemies", "Siblings"]
def remove(lp1, lp2):
    for x in range(len(lp1)):
        for y in range(len(lp2)):
            if lp1[x] == lp2[y]:
                z = lp1[x]
                lp1.remove(z)
                lp2.remove(z)
                lp3 = lp1 + ["|"] + lp2
                return [lp3, True]
    lp3 = lp1 + ["|"] + lp2
    return [lp3, False]
play_again = 'y'
while play_again == 'y':
    person1 = input('Type your name: ').lower()
    per1_list = list(person1)

    person2 = input("Type a person's name: ").lower()
    per2_list = list(person2)

    start = True
    while start:
        return_list = remove(per1_list, per2_list)
        concat_list = return_list[0]
        start = return_list[1]
        line = concat_list.index("|")
        per1_list = concat_list[: line]
        per2_list = concat_list[line + 1:]

    count = len(per1_list) + len(per2_list)

    while len(relationship) > 1:
        split_index = (count % len(relationship) - 1)
        if split_index >= 0:
            right_side = relationship[split_index + 1:]
            left_side = relationship[: split_index]
            relationship = right_side + left_side
        else:
            relationship = relationship[: len(relationship) - 1]
    print("Your relationship with that person is...")
    time.sleep(1)
    print('Calculating...')
    time.sleep(1)
    print('...')
    time.sleep(1)
    print(relationship[0])
    time.sleep(1)
    play_again = input('Would you like to play again? (y/n): ')