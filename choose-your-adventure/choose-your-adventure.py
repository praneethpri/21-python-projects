def main():
    while True:
        pressed_key = input('''
    Welcome to,
    
          ___                 _     ___          _     _        
         / __| ___ __ _ _ ___| |_  / __| ___  __(_)___| |_ _  _ 
         \__ \/ -_) _| '_/ -_)  _| \__ \/ _ \/ _| / -_)  _| || |
         |___/\___\__|_| \___|\__| |___/\___/\__|_\___|\__|\_, |
                                                           |__/
    
    Choose Your own Adventure Game.
    
          to start press 'A' and enter.
          to quit press any other button and enter.
    
    
    
    This is a story from https://choose-your-adventure.com/mystery/the-secret-society website.
        
          ''')
    
        if pressed_key.lower() == "a":
            enter_to_story()
        else:
            break
    
def enter_to_story():
    start_story = input('''
A story in which the protagonist stumbles upon a secret society and must choose between joining their ranks or exposing their nefarious deeds to the world.

        1) Press 'A' and enter to start the stroy.
        2) Press any other key to exit.
    ''')

    if start_story.upper() == 'A':
        print('A')
    else:
        quit()

def story_started():
    message = input('''
You receive a mysterious invitation to a secret gathering of powerful individuals. The invitation tells you to come alone and to bring nothing with you. Do you attend the gathering or ignore the invitation?

        1) Press 'A' to attend the gathering.
        2) Press 'B' to ignore the invitation.
        3) Press any other key to exit.
    ''')

    if message.lower() == 'A':
        attend_the_gathering()
    elif message.lower() == 'B':
        ignore_the_invitation()
    else:
        quit()


def attend_the_gathering():
    message = input('''
You arrive at the gathering and are greeted by a group of wealthy and powerful individuals. They explain that they are part of a secret society that has been operating in the shadows for centuries. They claim to have the power to shape the world and control the destiny of nations. They offer you a chance to join their ranks. Do you accept their offer or decline?

        1) Press 'A' to accept their offer.
        2) Press 'B' to decline their offer.
        3) Press any other key to quit.
    ''')

    if message.upper() == 'A':
        accept_their_offer()
    elif message.upper() == 'B':
        decline_their_offer()
    else:
        quit()


def accept_their_offer():
    message = input('''
You accept their offer and become a member of the secret society. They tell you that their goal is to bring about a new world order where they are in control. They promise to give you power and influence beyond your wildest dreams. Do you work with the society to achieve their goals or try to stop them? 
 
    1) Press 'A' to work with the society.
    2) Press 'B' to try to stop them.
    3) Press 'C' to go back.
    4) Press any other key to quit.
    ''')

    if message.upper() == 'A':
        pass
    elif message.upper() == 'B':
        pass
    elif message.upper() == 'C':
        attend_the_gathering()
    else:
        quit()

def ignore_the_invitation():
    message = input('''
You decide to ignore the invitation and continue with your life. However, you can't shake the feeling that something is off. Do you investigate the invitation or try to forget about it?

    1) Press 'A' to investigate the situation.
    2) Press 'B' to try to forget about it.
    3) Press 'C' to go back.
    4) Press any other key to quit.
                    ''')

    if message.upper() == 'A':
        pass
    elif message.upper() == 'B':
        pass
    elif message.upper() == 'C':
        story_started()
    else:
        quit()

def decline_their_offer():
    message = input('''
You decline their offer and leave the gathering. As you walk away, you can't help but wonder what kind of power and influence the secret society has. Do you investigate the society or leave it alone?

    1) Press 'A' to investigate the society.
    2) Press 'B' to leave it alone.
    3) Press 'C' to go back.
    4) Press any other key to quit.
    ''')

    if message.upper() == 'A':
        investigate_the_society()
    elif message.upper() == 'B':
        pass
    elif message.upper() == 'C':
        attend_the_gathering()
    else:
        quit()

def investigate_the_society():
    message = input('''
You decide to investigate the invitation further. You discover that the secret society has been involved in many illegal activities, including bribing politicians and business leaders. Do you expose the society to the public or keep the information to yourself?

    1) Press 'A' to expose the society to the public.
    2) Press 'B' to keep the information to yourself.
    3) Press 'C' to go back.
    4) Press any other key to quit.
    ''')

    if message.upper() == 'A':
        pass
    elif message.upper() == 'B':
        pass
    elif message.upper() == 'C':
        decline_their_offer()
    else:
        quit()

def leave_it_alone():
    message = input('''
You decide to leave the secret society alone and continue with your life. However, you can't shake the feeling that you made the wrong choice. Do you investigate the society further or live with your decision?

    1) Press 'A' to investigate the society further.
    2) Press 'B' to live with your decision.
    3) Press 'C' to go back.
    4) Press any other key to quit.
                    ''')

    if message.upper() == 'A':
        investigate_the_society_further()
    elif message.upper() == 'B':
        decline_their_offer()
    elif message.upper() == 'C':
        pass
    else:
        quit()

def investigate_the_society_further():
    message = input('''
You continue to investigate the secret society and discover that they have even deeper roots than you thought. Their influence extends to the highest levels of government and the economy. Do you continue to pursue the story or give up?

    1) Press 'A' to continue to pursue the story.
    2) Press 'B' to give up.
    3) Press 'C' to go back.
    4) Press any other key to quit.
                    ''')

    if message.upper() == 'A':
        pass
    elif message.upper() == 'B':
        pass
    elif message.upper() == 'C':
        decline_their_offer()
    else:
        quit()

def give_up():
    message = input('''
You move on from the secret society and start to investigate other stories. However, you can't help but wonder if you made the right choice. Do you revisit the story or let it go?

    1) Press 'A' to revisit the story.
    2) Press 'B' to let it go.
    3) Press 'C' to go back.
    4) Press any other key to quit.
    ''')

    if message.upper() == 'A':
        pass
    elif message.upper() == 'B':
        pass
    elif message.upper() == 'C':
        investigate_the_society_further()
    else:
        quit()

def let_it_go():
    message = input('''
Years pass, and you continue to pursue new stories. However, the memory of the secret society stays with you. You wonder if there are other secret organizations out there, working in the shadows to shape the world. Do you investigate further or let it go?

    1) Press 'A' to investigate further.
    2) Press 'B' to let it go.
    3) Press 'C' to go back.
    4) Press any other key to quit.
    ''')

    if message.upper() == 'A':
        pass
    elif message.upper() == 'B':
        pass
    elif message.upper() == 'C':
        give_up()
    else:
        quit()

main()
