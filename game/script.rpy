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

        # character names
        phd = "phd"
        implementer = "implementer"

        # video flags
        seen_ben_intro = False
        seen_origami_intro = False

        # interview flags
        phd_interview_available = False
        phd_interview_seen = False
        phd_interview_synopsis = None

        implementer_interview_available = False
        implementer_interview_seen = False
        implementer_interview_synopsis = None


        stance = 0
        neogeo_influence = 0
        cpc_influence = 0
    

    jump overview

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
                jump overview

    if computer_mode == "video":
        menu:
            "Ben Carlson Misreports Mass Execution":
                call ben_intro_video

            "Origami Effect Conceptualized by %(phd) PhD" if seen_ben_intro:
                call origami_intro_video
                $phd_interview_available = True

            "Company Neo Genesis announces Universal Highway Project" if seen_origami_intro:
                call geo_genesis_highway_video
                $implementer_interview_available = True

            "Back":
                jump start_computer

    if computer_mode == "email":
        menu:
            "Back":
                jump start_computer

    jump computer 

label overview:
        "Check Notepad":
            jump notepad
        "Check Computer":
            jump start_computer
        "Investigate":
            jump investigate

label investigate:
    menu:
        "Who should I try to investigate?"

        "Back": 
            jump overview


label notepad:
    menu: 
        "%(phd)" if phd_interview_seen:
            "%(phd_interview_synopsis)"

        "%(implementer)"" if implementer_interview_available:
            "%(seen_origami_intr
