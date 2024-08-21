import random
import time
caught_pokemon = {}
invalid = ('lake','forest','city')
lake_pokemon = ('Squirtle','Magicarp','Poliwag','Dewgong','Seadra','Gyarados')
forest_pokemon = ('Bellsprout','Oddish','Gloom','Exeggutor','Meganium','Nuzleaf')
city_pokemon = ('Charizard','Pidgey','Zubat','Dodrio','Aerodactyl','Articuno')
#Diolog
print('Hello trainer, the pokemon of the city have gone loose!')
time.sleep(2)
print('We need your help to catch all of them, in return you can keep all the pokemon you catch')
time.sleep(2)
print('There are many... be careful.')
time.sleep(2)
print('Farewell!...')
#Start game
def game_start(biome):
    if biome == 'L':
        return 'lake'
    elif biome == 'F':
        return 'forest'
    elif biome == 'C':
        return 'city'
    else:
        print('Invalid biome...')
        time.sleep(1)
        print('Picking random biome...')
        choice = random.choice(invalid)
        return choice
#Start game
play = game_start(input('Choose which biome to embark on first... Lake, Forest or City (L/F/C): ').upper())
while True:
    #Lake biome
    if play == 'lake':
        time.sleep(1)
        print('While swimming in the lake, you feel something brush your leg...')
        for i in range(2):
            time.sleep(1)
            while True:
                lake_decision = input('Do you wish to run or look (R/L): ').upper()
                if lake_decision == 'R':
                    break
                elif lake_decision == 'L':
                    break
                else:
                    print('Please select an available option')
                    time.sleep(1)
            if lake_decision == 'R':
                print('You swam away...')
                time.sleep(1)
                print('What a loser, you drowned')
                exit()
            elif lake_decision == 'L':
                print('You choose to look...')
                time.sleep(1)
                pokemon = random.choice(lake_pokemon)
                print('You found a '+pokemon+'!')
                time.sleep(0.5)
                print('You caught it!')
                caught_pokemon.update({pokemon:random.randint(1,10)})
                print('Caught pokemon: '+str(caught_pokemon))
                time.sleep(1)
                print('You hear a small rumble...')
                time.sleep(1)
        print("It's coming from the forest!")
        time.sleep(1)
        print('You go in the forest...')
        play = 'forest'
    #Forest biome
    elif play == 'forest':
        time.sleep(1)
        print('While treading through the forest you hear a rustle...')
        for i in range(2):
            time.sleep(1)
            while True:
                forest_decision = input('Do you wish to run or look (R/L): ').upper()
                if forest_decision == 'R':
                    break
                elif forest_decision == 'L':
                    break
                else:
                    print('Please select an available option')
                    time.sleep(1)
            if forest_decision == 'R':
                print('You run out of the forest...')
                time.sleep(1)
                print('What a loser, you fell of a cliff')
                exit()
            elif forest_decision == 'L':
                print('You choose to look...')
                time.sleep(1)
                pokemon = random.choice(forest_pokemon)
                print('You found a ' + pokemon + '!')
                time.sleep(0.5)
                print('You caught it!')
                caught_pokemon.update({pokemon: random.randint(1, 10)})
                print('Caught pokemon: ' + str(caught_pokemon))
                time.sleep(1)
                print('You hear a loud crash!')
                time.sleep(1)
        print("It's coming from the city!")
        time.sleep(1)
        print('You run to the city')
        play = 'city'
    #City biome
    elif play == 'city':
        time.sleep(1)
        print('While running through the city you hear a loud bang!')
        for i in range(2):
            time.sleep(1)
            while True:
                city_decision = input('Do you wish to run or look (R/L): ').upper()
                if city_decision == 'R':
                    break
                elif city_decision == 'L':
                    break
                else:
                    print('Please select an available option')
                    time.sleep(1)
            if city_decision == 'R':
                print('You hide in a building...')
                time.sleep(1)
                print('What a loser, it came crashing down on you')
                exit()
            elif city_decision == 'L':
                print('You choose to look...')
                time.sleep(1)
                pokemon = random.choice(city_pokemon)
                print('You found a ' + pokemon + '!')
                time.sleep(0.5)
                print('You caught it!')
                caught_pokemon.update({pokemon: random.randint(1, 10)})
                print('Caught pokemon: ' + str(caught_pokemon))
                time.sleep(1)
                print('You hear an ominous sound')
                time.sleep(1)
        print("It's coming from the lake!")
        time.sleep(1)
        print('You head towards the lake')
        play = 'lake'
