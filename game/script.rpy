# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"
image black = "#000"
image white = "#fff"
image room = im.FactorScale("images/backgrounds/captainsloft.jpg", 1.0)
image computer = im.FactorScale("images/backgrounds/captainsloft.jpg", 1.0)
image computer_video = im.FactorScale("images/backgrounds/captainsloft.jpg", 1.0)
image city = im.FactorScale("images/backgrounds/city.jpg", 0.75)
image lab = im.FactorScale("images/backgrounds/lab.jpg", 1.2)

# character images
image img_ben = im.FactorScale("images/characters/white/ben_carlson.png", 0.25)
image img_chris = im.FactorScale("images/characters/white/chris_harrison.png", 0.5)
image img_chris_mini = im.FactorScale("images/characters/white/chris_harrison.png", 0.25)
image img_ceo = im.FactorScale("images/characters/white/ceo.png", 0.5)
image img_ceo_mini = im.FactorScale("images/characters/white/ceo.png", 0.25)
image img_traitor = im.FactorScale("images/characters/white/traitor.png", 0.5)
image img_scientist = im.FactorScale("images/characters/white/scientist.png", 0.5)
image img_scientist_mini = im.FactorScale("images/characters/white/scientist.png", 0.25)
image img_inventor = im.FactorScale("images/characters/white/inventor.png", 0.5)
image img_inventor_mini = im.FactorScale("images/characters/white/inventor.png", 0.25)
image img_investor = im.FactorScale("images/characters/white/investor.png", 0.5)
image img_investor_mini = im.FactorScale("images/characters/white/investor.png", 0.25)
image img_enviro = im.FactorScale("images/characters/white/environmentalist.png", 0.5)

# Declare characters used by this game.
define ben = Character('Ben', color="#FF7700")
define _ben = Character('Ben', kind=nvl, color="#FF7700")

define ceo = Character('Chad Hewett', kind=nvl, color="#0088FF")
define scientist = Character('Dr. Matthew Dorian', color="#0088FF")
define inventor = Character("Kimberly McLaren", kind=nvl, color="#0088FF")

define environmentalist = Character('Lenard Malcom', color="#09FF00")
define traitor = Character("Ellen Wyse", color="#09FF00")

define chris = Character("Chris Harrison", color="#c8ffc8")

define video = Character("", kind=nvl, color="#fff")


#########
#NOTES:
# NeoGenesis: + integer values
# Celestial Preservation Coalition: - integer values
#
# Character Aliases - SED project to fix


# The game starts here.
label start:

    #initialize state values
    python:
        # video flags
        seen_ben_intro = False
        seen_origami_intro = False
        seen_highway_video = False
        seen_generous_funding_video = False
        seen_public_outcry_video = False
        seen_government_investigation_video = False
        seen_ion_storm_video = False
        seen_cpc_video = False

        # interview flags
        phd_interview_available = False
        phd_interview_seen = False
        phd_interview_synopsis = None

        inventor_interview_available = False
        inventor_interview_seen = False
        inventor_interview_synopsis = None

        investor_interview_available = False
        investor_interview_seen = False
        investor_interview_synopsis = None

        ceo_interview_available = False
        ceo_interview_seen = False
        ceo_interview_synopsis = None

        inventor_interview_2_available = False
        inventor_interview_2_seen = False
        inventor_interview_2_synopsis = None

        enviro_interview_available = False
        enviro_interview_seen = False
        enviro_interview_synopsis = None

        vp_interview_available = False
        vp_interview_seen = False
        vp_interview_synopsis = None


        # alignment values
        stance = 1
    

    jump overview

label start_computer:
    # Resets computer state values
    python:
        computer_mode = None

    jump computer

label computer:
    if computer_mode == None:
        scene computer with dissolve
        menu:
            "Watch News Clips":
                $computer_mode = "video"

            "Check Emails":
                $computer_mode = "email"

            "Leave Computer":
                jump overview

    if computer_mode == "video":
        scene computer_video with dissolve
        menu:
            "Ben Carlson Misreports Military Operation":
                call ben_intro_video
                $seen_ben_intro = True

            "Dr. Matthew Dorian's Origami Effect Bought by NeoGenesis Corporation" if seen_ben_intro:
                call origami_intro_video
                $phd_interview_available = True
                $seen_origami_intro = True

            "NeoGenesis Corporation Aannounces Universal Highway Project" if seen_origami_intro:
                call neo_genesis_highway_video
                $inventor_interview_available = True
                $seen_highway_video = True
            
            "NeoGenesis Corporation Secures Strong Funding" if seen_highway_video:
                call generous_funding_video
                $investor_interview_available = True
                $seen_generous_funding_video = True

            "NeoGenesis Whistle-Blower Leaks higher Than Disclosed Budget" if (seen_generous_funding_video and inventor_interview_seen):
                call public_outcry_video
                $ceo_interview_available = True
                $seen_public_outcry_video = True

            "Government Rules In Favor of NeoGenesis Corporation" if seen_public_outcry_video:
                call government_investigation_video
                $seen_government_investigation_video = True

            "Genesis Gate Malfunctions" if (seen_highway_video and inventor_interview_seen):
                call ion_storm_video
                $seen_ion_storm_video = True
                $inventor_interview_2_available = True

            "CPC Leads Demands for Regulations on Genesis Gates" if seen_ion_storm_video:
                call cpc_video
                $seen_cpc_video = True
                $enviro_interview_available = True

            "Back":
                jump start_computer

    if computer_mode == "email":
        scene computer with dissolve
        menu:
            "Kimberly McLaren" if inventor_interview_available and not inventor_interview_seen:
                call inventor_email
                $inventor_interview_seen = True

            "Investor" if (investor_interview_available and not investor_interview_seen):
                call investor_interview
                $investor_interview_seen = True

            "Chad Hewett" if (ceo_interview_available and not ceo_interview_seen):
                call ceo_email
                $ceo_interview_seen = True

            "Kimberly McLaren" if inventor_interview_2_available and not inventor_interview_2_seen:
                call inventor_email_2
                $inventor_interview_2_seen = True

            "Back":
                jump start_computer

    jump computer 

label overview:
    scene room with dissolve
    menu:
        "Check Computer":
            jump start_computer
        "Investigate":
            jump investigate
        "Check Notes":
            jump notepad

label investigate:
    menu:
        "Who should I try to schedule an interview with?"

        "Dr. Matthew Dorian" if phd_interview_available and not phd_interview_seen:
            call phd_interview
            $phd_interview_seen = True

        "Kimberly McLaren" if inventor_interview_available and not inventor_interview_seen:
            call inventor_email
            $inventor_interview_seen = True

        "Mysterious Investor" if investor_interview_available and not investor_interview_seen:
            $computer_mode = "email"
            jump computer

        "Chad Hewett" if ceo_interview_available and not ceo_interview_seen:
            $computer_mode = "email"
            jump computer

        "Kimberly McLaren" if inventor_interview_2_available and not inventor_interview_2_seen:
            $computer_mode = "email"
            jump computer

        "Lenard Malcom" if enviro_interview_available and not enviro_interview_seen:
            call enviro_interview
            $enviro_interview_seen = True
            $vp_interview_available = True
        "Ellen Wyse" if vp_interview_available and not vp_interview_seen:
            call vp_interview
            $vp_interview_seen = True

        "Back": 
            jump overview

    jump investigate


label notepad:
    show black with dissolve
    menu: 
        "Dr. Matthew Dorian" if phd_interview_seen:
            centered "[phd_interview_synopsis]"

        "Kimberly McLaren Interview #1" if inventor_interview_seen:
            centered "[inventor_interview_synopsis]"

        "Mysterious Investor" if investor_interview_seen:
            centered "[investor_interview_synopsis]"

        "Chad Hewett" if ceo_interview_seen:
            centered "[ceo_interview_synopsis]"

        "Kimberly McLaren Interview #2" if inventor_interview_2_seen:
            centered "[inventor_interview_2_synopsis]"

        "Lenard Malcom" if enviro_interview_seen:
            centered "[enviro_interview_synopsis]"

        "Ellen Wyse" if vp_interview_seen:
            centered "[vp_interview_synopsis]"

        "Back":
            hide black with dissolve
            jump overview


    jump notepad

label intro:
    scene black
    pause 0.2
    show space2 with dissolve

    centered "This is the intro"

    show black with dissolve
    pause 0.2
    return

label end_game:
    if stance == 1:
        jump ending1
    elif stance == 2:
        jump ending2
    elif stance == 3:
        jump ending3
    elif stance == 4:
        jump ending4
    elif stance == 5:
        jump ending5

label ending1:
    scene black
    pause 0.2
    show space2 with dissolve

    centered "Chris Harrison leads operation to eliminate NeoGenesis key figures and critical machinery."
    return    
label ending2:
    scene black
    pause 0.2
    show space2 with dissolve

    centered "Under public pressure, NeoGenesis is forced to break up its company and Chad's goal is thwarted."
    return
label ending3:
    scene black
    pause 0.2
    show space2 with dissolve

    centered "Ellen Wyse is the sole leader of NeoGenesis and she uses the gates to secure even more power to guide humanity beyond."
    return
label ending4:
    scene black
    pause 0.2
    show space2 with dissolve

    centered "A semi crunch was performed due to a drastic under estimation of the energy required. Though it is found it might be usable to counter the big freeze without ending The Universe."
    return
label ending5:
    scene black
    pause 0.2
    show space2 with dissolve

    centered "Over the years Chad Hewett's plan is finally realized and a big crunch commences. A big bounce was successful for those who have faith."
    return
