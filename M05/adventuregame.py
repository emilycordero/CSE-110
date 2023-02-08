""" 
File: Adventuregame.py
Author: Emily Cordero 

Purpose: Write a text based adventure game. 

"""

# Introduce the user and the 1st choise

item = input('You are walking through a dark forest and find two items: a MATCH and a FLASHLIGHT. Which one do you want to pick up? \n')

# First choice: Match -- Nest an if statement for a second level
if item.lower() == 'match':
    item_match = input('You pick up the match and strike it, and for an instant, the forest around you is illuminated. You see a large grizzly bear, and then the match burns out. Do you want to RUN, or HIDE behind a tree? \n')

    # Second choice: RUN -- Nest an if statement for third level
    if item_match.lower() == 'run':
        action_run = input('You choose to run. The branches of the trees slap your face as you run. You can hear your heart pounding and the roars of the bear behind you. "I am going to die!" You yelled out as you swarmed past the trees. All of sudden you trip and fall in a ditch. Do you want to SCREAM for help or HIDE? \n')
        # Third choice: SCREAM -- Nest another if statement for a fourth level
        if action_run.lower() == 'scream':
            action_scream = input('You let out a loud scream, and there was only silence in response. All of a sudden a voice is heard. "Is someone there?" Although you are getting a sense of relief, the hairs behind your neck rise. Do you want to GO towards the voice or STAY where you are? \n')
            # Fourth choice: GO -- END of program
            if action_scream.lower() == 'go':
                print('You decide to head towards the voice. You go deeper and deeper in the darkness of the forest. The voice never gets closer, but you can clearly hear it. You continue to head towards it. You feel like you are walking for hours. All of a sudden you stumble on road pavement and you see a car traveling towards you. You wave your hands and the car stops. You are successfully rescued and taken home! Great Job! \n')
            # Fourth choice: STAY -- End of program
            elif action_scream.lower() == 'stay':
                print('You stay hidden, waiting for the voice to go away. You head towards a light off from a distance. You continue walking until the light gets brighter and brighter. You see a home not far off. You head towards it and knock. You ask for help and help arrives and you are rescued from the forest! Great job! \n')
            # Fourth choice: INVALID -- END of program
            else:
                print('This is not a valid choice. \n')
        
        # Third choice: HIDE -- Nest another if statement for a fourth level
        elif action_run.lower() == 'hide':
            action_run_2 = input('You decide to hide in the ditch. An hour passed and you did not hear the bear. The sun started to set and you start feeling hungry. Do you want to LOOK for food or WALK through the forest? \n')
            # Fourth choice: LOOK -- END of program.
            if action_run_2.lower() == 'look':
                print('You are looking for food and stumble upon a camping ground with few occupants. Filled with relief you ask for help from one of them and help is sent over. Great job! \n')
        
            # Fourth choice: WALK -- END of program.
            elif action_run_2.lower() == 'walk':
                print('You decide to ignore your tummy and walk aimlessly through the forest. You find a cabin hidden deep in the woods. You head inside and it is empty but has been used recently. It most likely is a vacation cabin. In the cabin is a phone and you use it to call for help. Great job! \n')
            # Fourth choice: INVALID -- END of program.
            else:
                print('This is not a valid choice. \n')
        # Third choice: INVALID -- Nest another if statement for a fourth level
        else:
            print('This is not a valid choice. \n')
        
    # Second choice: HIDE -- Nest another if statement for a third level
    elif item_match.lower() == 'hide':
        item_hide = input('You choose to hide behind some trees. You can hear your heart thumping loudly as the bear nears to your location. You start breathing more heavily as the sounds come nearer and nearer. Then out of nowhere you hear a loud gunshot from somwhere nearby. The bear was startled and made a run for it. It sounded close by. Do you want to INVESTIGATE where the sound came from or do you want to WANDER further in the woods? \n')
        # Third choice: Investigate -- End of program
        if item_hide.lower() == 'investigate':
            print('You head towards the area that you believe the shot came from, yelling for help. Eventually you come across a hunting group who help you right away. You feel grateful to them. Great job for getting through! \n')
        
        # Third choice: Wander -- End of program
        elif item_hide.lower() == 'wander':
            print('Unfortunately, you head towards the part of the forest that is almost impossible to escape from. You end up wandering until you cannot anymore. Better luck next time! \n')
        # Third choice: -- End of program
        else:
            print('This is not a valid choice. \n')
    
    # Print if not a valid choice
    else:
        print('This is not a choice. \n')

# First choice: Flashlight -- Nest for a second level
elif item.lower() == 'flashlight':
    item_flashlight = input('You pick up the flashlight and turn it on. You see the pathway lit up in front of you, but you thought you also heard something off to the side. Do you want to FOLLOW the path or LOOK in the trees for the thing that made the noise? \n')
    # Second choicee: Follow -- Nest for a third level
    if item_flashlight.lower() == 'follow':
        action_follow = input('You follow the path and reach the hiking trail. You follow the hiking trail until you reach a forkway. A right path and a left path. Both are unmarked and seem to be dark. Do you choose the RIGHT path or the LEFT? \n')
        # Third choice: RIGHT -- end of program
        if action_follow.lower() == 'right':
            print('You choose the path to the right. Unfortunately the path to the right lead to a dirt trail and then it started to become unmarked. You suddenly do not remember the way you came from as everything looks like the same. You continue to wander aimlessly deeper and deeper in the forest. Better luck next time! \n')
        
        # Third choice: LEFT -- end of program
        elif action_follow.lower() == 'left':
            print('You choose the path to the left. Thankfully, the path leads to a resort with a customer desk. You ask for help as you were lost in the forest. Help is taken to you and you are saved. Great job! \n')
        # Third choice -- end of program
        else:
            print('This is not a valid choice. \n')
        
    # Second choice: LOOK -- Nest another if statement for a third level
    elif item_flashlight.lower() == 'look':
        item_hide_2 = input('You decide to look for the source of the noise. Behind the bushes was a large grizzly bear. It is smelling around the trees and heading towards you. Do you want to SCREAM or RUN from the bear? \n')

        # Third choice: Scream -- Nest another if statement for a Fourth level
        if item_hide_2.lower() == 'scream':
            item_scream = input('You scream at the bear and the bear suddenly jolts up. The bear roars and runs towards you. You start running the opposite direction. There is a suddenly a fork in the trail. With the bear behind you, do you choose the RIGHT or LEFT path? \n')
            # Fourth choice: Right -- End of program
            if item_scream.lower() == 'right':
                print('You choose the path to the right. Thankfully, the path leads to a resort with a customer desk. You ask for help as you were lost in the forest. Help is taken to you and you are saved. Great job! \n')
            # Fourth choice: Right -- End of program
            elif item_scream.lower() == 'left':
                print('You choose the path to the left. Unfortunately the path to the right lead to a dirt trail and then it started to become unmarked. You suddenly do not remember the way you came from as everything looks like the same. You continue to wander aimlessly deeper and deeper in the forest. Better luck next time! \n')
            else:
                print('This is not a valid choice. \n')
        
        # Third choice: RUN-- Nest another if statement for a fourth level
        elif item_hide_2.lower() == 'run':
            action_run = input('You choose to run. The branches of the trees slap your face as you run. You can hear your heart pounding and the roars of the bear behind you. "I am going to die!" You yelled out as you swarmed past the trees. All of sudden you trip and fall in a ditch. You hide out until you feel safe enough to travel again. Do you want to STAY or WALK for help? \n')
            # Fourth choice: STAY -- END 
            if action_run.lower() == 'stay':
                print('You stay for another hour and it starts to get darker outside. You do not hear anything out. You get up and start walking. You are found by some hikers and help is called. Great job! \n')
            # Fourth choice: WALK -- END
            elif action_run.lower() == 'walk':
                print('You walk with a broken ankle. The bear happens to still be around. With your ankle broken, you cannot escape again. Better luck next time! \n')
            else:
                print('This is not a valid choice. \n')

        # Third choice: -- End of program
        else:
            print('This is not a valid choice. \n')

    # Second choice: End of program
    else:
        print('This is not a valid choice. \n')
# First choice: end of program
else:
    ('That is not a choice. \n')