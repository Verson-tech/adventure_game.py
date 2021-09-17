import time
import random

creature = random.choice(['pirate','monster','dragon','thief' ])
tool = random.choice(['fork','stick','baseball bat'])

def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(1)

def intro():
    print_pause('You find yourself standing in an open field,'
    ' filled with grass and yellow wildflowers.')
    print_pause(f'Rumor has it that a {creature} is somewhere around here,'
    'and has been terrifying the nearby village.')
 
def field(creature,tool,weapon):
    print_pause('In front of you is a house. ')
    print_pause('To your right is a dark cave. ')
    print_pause('In your hand you hold your trusty'
    f'(but not very effective) {tool}. ')
    # print_pause('Enter 1 to knock on the door of the house. ')
    # print_pause('Enter 2 to peer into the cave. ') 
 

def cave(creature,tool,weapon):
    print_pause('You peer cautiously into the cave.  ')
 
    if 'sword' in weapon:
        print_pause('''You've been here before, and gotten all the good stuff. It's just an empty cave now. ''')
    else:
        print_pause('It turns out to be only a very small cave. ')
        print_pause('Your eye catches a glint of metal behind a rock. ')
        print_pause('You have found the big sword! ')
        print_pause(f'You discard your silly old {tool} and take the sword with you. ')
        print_pause('You walk back out to the field. ')
        weapon.append('sword')
    move(creature,tool,weapon)  

def house(creature,tool,weapon):
    print_pause('You approach the door of the house.')
    print_pause(f'You are about to knock when the door opens and out steps a {creature}. ')
    print_pause(f'''Eep! This is the {creature}'s house! ''')    
    print_pause(f'The {creature} attacks you! ')  
 

    if 'sword' in weapon:
        print_pause(f'As the {creature} moves to attack, you unsheath your new sword.  ')   
        print_pause(f'The big sword shines brightly in your hand as you brace yourself for the attack.  ')
        print_pause(f'But the {creature} takes one look at your shiny new toy and runs away! ')    
        print_pause(f'You have rid the town of the {creature}. You are victorious!  ')   
        # play again?
        print_pause('Would you like to play again? (y/n)')
        new_game = input('Type    y    for a new game.\n'
                   'Type    n     to finish the game.\n')
        if new_game == 'y':
            print_pause('Excellent!!! Starting a new game!!!')
            play_game()
        else:
            print_pause('Ok! See you later! Bye for now!')  
    else:
        print_pause(f'You feel a bit under-prepared for this, what with only having a tiny {tool}. ')
        attack(creature,tool,weapon)
    
    
def move(creature,tool,weapon):
    print_pause('What would you like to do?  ')
    house_or_cave = input('Enter 1 to knock on the door of the house. \n'
                          'Enter 2 to peer into the cave. \n'  )
    if house_or_cave == '1':
        house(creature,tool,weapon)
    elif house_or_cave == '2':
        cave(creature,tool,weapon)    

def attack(creature,tool,weapon):
    print_pause('What would you like to do?  ')
    run_or_fight = input('Enter 1 to run away. \n'
                          'Enter 2 to fight. \n'  )
    if run_or_fight == '1':
        print_pause('''You run back into the field. Luckily, you don't seem to have been followed. ''')
        field(creature,tool,weapon)
        move(creature,tool,weapon)
    
    elif run_or_fight == '2':
        print_pause('You do your best... ')
        print_pause(f'but your dagger is no match for the {creature}. ')
        print_pause('You have been defeated! ')
        # play again?
        print_pause('Would you like to play again? (y/n)')
        new_game = input('Type    y    for a new game.\n'
                   'Type    n     to finish the game.\n')
        if new_game == 'y':
            print_pause('Excellent!!! Starting a new game!!!')
            play_game()
        else:
            print_pause('Ok! See you later! Bye for now!')    

def play_game():
    weapon = []
    intro()  
    move(creature,tool,weapon)
play_game()    


     









   









