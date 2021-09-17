# pseudo code:
# intro()
# field    --> knock or peer
# cave     --> sword  
# house    --> fight or run
# move_around()
# play_game()

import time
import random

creature = random.choice(['pirate','monster','dragon','thief' ])
tool = random.choice(['fork','stick','baseball bat','tool'])

def print_pause(message_to_print):
    print(message_to_print)
    # time.sleep(1)

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
    print_pause('Enter 1 to knock on the door of the house. ')
    print_pause('Enter 2 to peer into the cave. ') 


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
    print_pause(f'You feel a bit under-prepared for this, what with only having a tiny {tool}. ')  


def move(creature,tool,weapon):
    print_pause('What would you like to do?  ')
    house_or_cave = input('Enter 1 to knock on the door of the house. \n'
                          'Enter 2 to peer into the cave. \n'  )
    if house_or_cave == '1':
        house(creature,tool,weapon)
    elif house_or_cave == '2':
        cave(creature,tool,weapon)    



def play_game():
    weapon = []
    intro()  
    move(creature,tool,weapon)
play_game()    


                   
   









# def knock_or_peer_with_sword():
#       while True:
#         choice = input('What would you like to do? (Please enter 1 or 2.) \n')        
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

# def field_or_house():
#       print_pause('You find yourself standing in '
#        'an open field, filled with grass and yellow wildflowers.')
#       print_pause('Go back to the house and knock (1) or peer into the cave (2)') 
#       knock_or_peer()
#     #   print_pause('Stay at the field(2) knock on the door(1).')
#       while True:
#          choice = input('What would you like to do? (Please enter 1 or 2.) \n') 
#          if  '1' in choice:
#             #   print_pause('You approach the door of the house. ')
#             #   if weapon ->
#               if 'sword' in weapon:
#                   print_pause(f'In your hand you hold a big sword.')  
#                   print_pause('Fight (1) or run (2)')
#                   knock_or_peer_with_sword()
#                   break
#               else:
#                   knock_or_peer()             
#               break
#          elif '2' in choice:
#               print_pause ('It is too scary to go back to the house...👻'
#               ' Confirm that you stay at the field and finish the game🏳. ') 
#               print_pause('Game over!')
#               break
#          else:
#               print('Wrong input. Please, enter 1 or 2')
#               break

# def knock_or_peer():   
#     while True:
#         choice = input('What would you like to do? (Please enter 1 or 2.) \n')    
#         if  '1' in choice:
#             print_pause('You approach the door of the house. ')       
#             print_pause(f'You are about to knock when the door opens and out steps a {creature}. ')       
#             print_pause(f'''Eep! This is the {creature}'s house!''')       
#             print_pause(f'The {creature} attacks you!') 
#             print_pause(f'You feel a bit under-prepared for this, what with only having a tiny {tool}.') 
#             print_pause('You can fight (1) or run (2)')       
#             fight_or_run()        
#             break
#         elif '2' in choice:
#             print_pause('You peer cautiously into the cave. ')
#             print_pause('It turns out to be only a very small cave. ')
#             print_pause('Your eye catches a glint of metal behind a rock. ')
#             print_pause('You have found the big sword! ')
#             print_pause(f'You discard your silly old {tool} and take the sword with you. ')
#             print_pause('You walk back out to the field. ')
#             weapon.append('sword')
#             knock_or_peer_with_sword()
#             break
#         else:
#             print('Wrong input. Please, enter 1 or 2')
#             break 
            
# knock_or_peer()




        




            






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







   









