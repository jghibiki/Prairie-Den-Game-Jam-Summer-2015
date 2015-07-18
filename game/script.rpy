# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"
image black = "#000"
image white = "#fff"
image room = "#555000"
image img_ben = "game/images/characters/white/ben_carlson.png"
image img_chris = "game/images/characters/white/chris_harrison.png"
image img_ceo = "game/images/characters/white/ceo.png"
image img_traitor = "game/images/characters/white/traitor.png"
image img_scientist = "game/images/characters/white/scientist.png"
image img_inventor = "game/images/characters/white/inventor.png"
image img_investor = "game/images/characters/white/investor.png"

# Declare characters used by this game.
define ben = Character('Ben', color="#FF7700")
define _ben = Character('Ben', type=nvl, color="#FF7700")

define ceo = Character('Chad Hewett', color="#0088FF")
define scientist = Character('Dr. Dorian', type=nvl, color="#0088FF")
define inventor = Character("Kimberly McLaren", type=nvl, color="#0088FF")

define environmentalist = Character('Lenard Malcom', color="#09FF00")
define traitor = Character("Ellen Wyse", color="#09FF00")

define chris = Character("Chris Harrison", color="#c8ffc8")


#########
#NOTES:
# NeoGenesis: + integer values
# Celestial Preservation Coalition: - integer values
#
# Character Aliases - SED project to fix
# - X22 : PhD


# The game starts here.
label start:

    call intro

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

        implementer_interview_available = False
        implementer_interview_seen = False
        implementer_interview_synopsis = None

        investor_interview_available = False
        investor_interview_seen = False
        investor_interview_synopsis = None

        ceo_interview_available = False
        ceo_interview_seen = False
        ceo_interview_synopsis = None

        implementer_interview_2_available = False
        implementer_interview_2_seen = False
        implementer_interview_2_synopsis = None

        enviro_interview_available = False
        enviro_interview_seen = False
        enviro_interview_synopsis = None

        vp_interview_available = False
        vp_interview_seen = False
        vp_interview_synopsis = None


        # alignment values
        stance = 0
        neog_influence = 0
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
                $seen_ben_intro = True

            "Origami Effect Conceptualized by X22 PhD" if seen_ben_intro:
                call origami_intro_video
                $phd_interview_available = True
                $seen_origami_intro = True

            "Company Neo Genesis announces Universal Highway Project" if seen_origami_intro:
                call neo_genesis_highway_video
                $implementer_interview_available = True
                $seen_highway_video = True
            
            "Neo Genesis Secures Generous Funding From Undisclosed Source" if seen_highway_video:
                call generous_funding_video
                $investor_interview_available = True
                $seen_generous_funding_video = True

            "Public Outcry After Neo Genesis Whistle-Blower Leaks Massive Budget Prompts Government Investigation" if seen_generous_funding_video:
                call public_outcry_video
                $ceo_interview_available = True
                $seen_public_outcry_video = True

            "Government Investigation Reveals That Neo Genesis Money Is Being Spent As Intended" if seen_public_outcry_video:
                call government_investigation_video
                $seen_government_investigation_video = True

            "Ion Storm Causes Malfunction in Genesis Gate Causing The Destruction Of A Nearby Star System" if (seen_highway_video and implementer_interview_seen):
                call ion_storm_video
                $seen_ion_storm_video = True
                $inventor_interview_2_available = True

            "Celestial Preservation Coalition Forms, Demanding Regulations For Origami Effect Utilization" if seen_ion_storm_video:
                call cpc_video
                $seen_cpc_video = False
                $enviro_interview_available = True

            "Back":
                jump start_computer

    if computer_mode == "email":
        menu:
            "Implementer" if implementer_interview_available and not implementer_interview_seen:
                call implementer_email
                $implementer_interview_seen = True

            "Investor" if (investor_interview_available and not investor_interview_seen):
                call investor_email
                $investor_interview_seen = True

            "CEO" if (ceo_interview_available and not ceo_interview_seen):
                call ceo_email
                $ceo_interview_seen = True

            "Impmementer" if implementer_interview_2_available and not implementer_interview_2_seen:
                call implementer_email_2
                $implementer_interview_2_seen = True

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

        "phd" if phd_interview_available and not phd_interview_seen:
            call phd_interview
            $phd_interview_seen = True

        "implementer" if implementer_interview_available and not implementer_interview_seen:
            call implementer_email
            $implementer_interview_seen = True

        "invester" if investor_interview_available and not investor_interview_seen:
            $computer_mode = "email"
            jump computer

        "CEO" if ceo_interview_available and not ceo_interview_seen:
            $computer_mode = "email"
            jump computer

        "implementer" if implementer_interview_2_available and not implementer_interview_2_seen:
            $computer_mode = "email"
            jump computer

        "enviro" if enviro_interview_available and not enviro_interview_seen:
            call enviro_interview
            $enviro_interview_seen = True
            $vp_interview_available = True
        "vp" if vp_interview_available and not vp_interview_seen:
            call vp_interview
            $vp_interview_seen = True

        "Back": 
            jump overview

    jump investigate


label notepad:
    menu: 
        "phd" if phd_interview_seen:
            centered "[phd_interview_synopsis]"

        "implementer" if implementer_interview_seen:
            centered "[implementer_interview_synopsis]"

        "investor" if investor_interview_seen:
            centered "[investor_interview_synopsis]"

        "ceo" if ceo_interview_seen:
            centered "[ceo_interview_synopsis]"

        "Back":
            jump overview


    jump notepad

label intro:
    scene black

    return
