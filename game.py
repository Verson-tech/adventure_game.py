import time
import random


creature = random.choice(['pirate','monster','dragon','thief' ])
tool = random.choice(['fork','stick','baseball bat','dagger'])



def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(1)


def intro():
    print_pause('You find yourself standing in an open field,'
    'filled with grass and yellow wildflowers.')
    print_pause(f'Rumor has it that a {creature} is somewhere around here,'
    'and has been terrifying the nearby village.')
    print_pause('In front of you is a house. ')
    print_pause('To your right is a dark cave. ')
    print_pause('In your hand you hold your trusty'
    f'(but not very effective) {tool}. ')
    print_pause('Enter 1 to knock on the door of the house. ')
    print_pause('Enter 2 to peer into the cave. ') 
intro()

choice = input('What would you like to do? (Please enter 1 or 2.) \n')
def knock_or_peer():   
    while True:
        choice     
        if  '1' in choice:
            print_pause('You approach the door of the house. ')       
            print_pause(f'You are about to knock when the door opens and out steps a {creature}. ')       
            print_pause(f'''Eep! This is the {creature}'s house!''')       
            print_pause(f'The {creature} attacks you!') 
            print_pause(f'You feel a bit under-prepared for this, what with only having a tiny {tool}.')
            fight_or_run()
            break
        elif '2' in choice:
            print_pause('You peer cautiously into the cave. ')
            print_pause('It turns out to be only a very small cave. ')
            print_pause('Your eye catches a glint of metal behind a rock. ')
            print_pause('You have found the big sword! ')
            print_pause(f'You discard your silly old {tool} and take the sword with you. ')
            print_pause('You walk back out to the field. ')
            break
        else:
            print('Wrong input. Please, enter 1 or 2')
            break 
            
knock_or_peer()

# def field_or_house():
#     print_pause('Would you like to (1) go back to the house'
#     ' or (2) stay at the field?')
#     while True:
#          choice 
#          if  '1' in choice:
#               print_pause('You approach the door of the house. ')
#               print_pause('In your hand you hold a big sword. ')            
#               break
#          elif '2' in choice:
#               print_pause ('It is too scary to go back to the house...👻'
#               ' You stay at the field and finish the game🏳. ') 
#               break
#          else:
#               print('Wrong input. Please, enter 1 or 2')

# field_or_house()
        
# def knock_or_peer_two():
#     while True:

#         choice 
        
#         if  '1' in choice:
#             print_pause('You approach the door of the house. ')   
#             print_pause(f'You are about to knock when the door opens and out steps a {creature}. ')
#             print_pause(f'''Eep! This is the {creature}'s house! ''')    
#             print_pause(f'The {creature} attacks you! ')              
#             break
#         elif '2' in choice:
#             print_pause('You peer cautiously into the cave. ')
#             print_pause('''You've been here before, and gotten all the good stuff. It's just an empty cave now.  ''')       
#             print_pause('You walk back out to the field.  ') 
#             field_or_house()
#             break
#         else:
#             print('Wrong input. Please, enter 1 or 2')  
        
# knock_or_peer_two()



def fight_or_run():
    print_pause('Would you like to (1) fight'
    'or (2) run away?')
    while True:

        choice 
        
        if  '1' in choice:
            print_pause('You do your best... '
            f'but your {tool} is no match for the {creature}.' )   
            print_pause('You have been defeated!')
            # start another game   ?():         
            break
        elif '2' in choice:
            print_pause('''You run back into the field. Luckily, you don't seem to have been followed.  ''')
            # field_or_house()
            break
        else:
            print('Wrong input. Please, enter 1 or 2')     
            






# def fight_or_run_with_sword():
#     print_pause('Would you like to (1) fight'
#     'or (2) run away?')
#     while True:

#         choice 
        
#         if  '1' in choice:
#             print_pause(f'As the {creature} moves to attack, you unsheath your new sword.  ')   
#             print_pause(f'The big sword shines brightly in your hand as you brace yourself for the attack.  ')
#             print_pause(f'But the {creature} takes one look at your shiny new toy and runs away! ')    
#             print_pause(f'You have rid the town of the {creature}. You are victorious!  ')              
#             break
#         elif '2' in choice:
#             print_pause('You peer cautiously into the cave. ')
#             print_pause('''You've been here before, and gotten all the good stuff. It's just an empty cave now.  ''')       
#             print_pause('You walk back out to the field.  ') 
#             break
#         else:
#             print('Wrong input. Please, enter 1 or 2')     
            
# fight_or_run_with_sword()



# def play_game(choice):
#     while intro():
#         while knock_or_peer():
#             if choice == '2':
#                 field_or_house()
            



  
    
    # knock_or_peer()
    # if choice == '1':
    #     fight_or_run()

# play_game()        


   









