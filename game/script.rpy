# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

# Declare characters used by this game.
define ben = Character('Ben', color="#c8ffc8")

#########
#NOTES:
# NeoGenisis: + integer values
# Celestial Preservation Coalition - integer values
#
# Character Aliases - SED project to fix
# - X22 : PhD


# The game starts here.
label start:

    #initialize state values
    python:
        first_video = True
        stance = 0
        neogeo_influence = 0
        cpc_influence = 0
    

    jump investigate
    return

label start_computer:
    # Resets computer state values
    python:
        computer_mode = None

    jump computer

label computer:
    if computer_mode == None:
        menu:
            "Watch News Clips":
                $computer_mode = "video"

            "Check Emails":
                $computer_mode = "email"

            "Leave Computer":
                jump investigate

    if computer_mode == "video":
        menu:
            "Ben Carlson Misreports Mass Execution":
                call ben_intro_video

            "Origami Effect Conceptualized by X22  PhD" if (not first_video):
                call origami_intro_video

            "Back":
                jump start_computer

    if computer_mode == "email":
        menu:
            "Back":
                jump start_computer

    jump computer 

label investigate:
    menu:
        

        "Check Computer":
            jump start_computer
