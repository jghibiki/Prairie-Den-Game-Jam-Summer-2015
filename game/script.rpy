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
    call screen computer

    # computer states
    if _return == "watch_video":
        $computer_mode = "video"
    elif _return == "check_email":
        $computer_mode = "email"
    elif _return == "leave_computer":
        jump investigate
    elif _return == "exit_videos":
        $computer_mode = None
    elif _return == "exit_email":
        $computer_mode = None
    
    # videos 
    elif _return == "ben_intro_video":
        $first_video = False
        call ben_intro_video
    elif _return == "origami_intro_video":
        call origami_intro_video

    jump computer
    

label investigate:
    call screen investigate

    if _return == "start_computer":
        jump start_computer
