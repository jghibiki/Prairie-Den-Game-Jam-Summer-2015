label phd_interview:
    show black with dissolve
    pause 0.5
    scene lab with dissolve
    show img_scientist
    ben "Dr. Dorian, it sounds like your work could start a new chapter for space travel. Could you summarize your theory for me?"

    scientist "It's a hypothesis, Ben."

    ben "Well, yeah. Tell me about your hypothesis then..."

    scientist "Sure. Don't fall for the hype, the concept of folding space time is not new.{w} However, the bulk of my work puts forth a hypothesis that is testable far sooner than previous scientific models.{w} We might even be able to do small scale tests right now, which is why NeoGenesis has already secured the rights to my work, for a royalty of course."
    scientist "Folding space time requires exponential energy meaning the bigger the fold the more energy per meter needed to make the fold.{w} My hypothesis calls for many little folds that cover the same distance as a big fold, which is much more manageable.{w} You can read my thesis for the details, but basically it is similar to origami with space time instead of paper.{w} Thus making it possible to travel many lightyears in the blink of an eye with much less energy than previously thought."

    ben "I think the implications on transportation are obvious and it may be some time before we see it practically affecting our transportation systems.{w} However, many technologies have been implemented swiftly due to their value as a weapon.{w} What do you think about the warnings in the scientific community that a device using this origami effect could be used as a weapon of unprecedented destruction?"

    scientist "Ha! Even if someone did manage to weaponize the origami effect it wouldn't be very precise. We're talking about taking out a star system as one of its smallest targets. Then take into consideration the amount of energy required...{w} more convnentional weapons are probably better suited to the task, though yes it could be \"weaponized\" to coagulate celestial bodies to a single point."

    ben "Interesting.{w} Well I've got what I was interested in writing my article about.{w} Thank you for your time Dr. Dorian."

    scientist "Glad I could help. Let me know if you need further clarification."

    ben "Thanks, will do."

    scene black with dissolve
    pause 0.2
    scene room with dissolve

    menu:
        "Following my interview with Dr. Dorian, I'll report..."

        "The origami effect will be the doom for mankind.":
            $stance = 2
            $phd_interview_synopsis = "Dr. Dorian introduced me the basic concept of his hypothesis the origami effect. He was insistent that it wasn't a practical weapon."

        "The origami effect is impractical as a weapon and could be the boon to industry outside of our solar system.":
            $phd_interview_synopsis = "Dr. Dorian introduced me the basic concept of his hypothesis the origami effect. He was insistent that it wasn't a practical weapon."

        "Origami effect is a wondrous advancement for the economy.":
            $stance = 5
            $phd_interview_synopsis = "Dr. Dorian introduced me the basic concept of his hypothesis the origami effect. He was insistent that it wasn't a practical weapon."
    
    ben "Time to write that article."
    
    scene black with dissolve
    pause 0.4
    scene room with dissolve
    return


label investor_interview:
    show black with dissolve
    pause 0.5
    scene room with dissolve
    show img_investor

    ben "I just can't find anything on him.{w} It's like he's watching my every move.{w} I'm being followed when I'm out though, I better be careful."

    menu:
        "This development is concerning, I'll report..."

        "About my stalker.":
            $stance = 2
            $investor_interview_synopsis = "The investor has taken many precautions to hide his identity."

        "Skip the report. Just update my neglected personal blog.":
            $investor_interview_synopsis = "The investor has taken many precautions to hide his identity."

    ben "Time to write that article."

    show black with dissolve
    pause 0.5
    show room with dissolve
    return


label enviro_interview:
    scene city
    show img_enviro

    ben "Mr. Malcom, your organization, the Celestial Preservation Coalition, recently called for origami effect regulations.{w} You also publicly encourage challenging NeoGenesis while they deploy their genesis gates that use the origami effect.{w} What sparked these protests?"

    environmentalist "I’m glad that somebody will listen to our side, Ben.{w} Due to the recent genesis gate malfunction caused by energy anomalies said to be caused by a solar flare.{w} It is very clear that these genesis gates can be dangerous.{w} We need new regulations and more competition in the industry to help ensure things are done right.{w} There is no reason that an entire star system should be wiped from existence for any reason."

    ben "NeoGenesis Corporation alleges that their genesis gate was sabotaged.{w} It might have not been an accident."

    environmentalist "I can assure you Mr. Carlson we are a peaceful organization acting within the bounds of the law.{w} I do have to admit that sabotage might help in our end goal, but blowing up a whole star system does not.{w} Here, let me help you get in contact with our Vice President, Ellen Wyse, who oversees our internal day to day operations."

    scene black with dissolve
    pause 0.2
    scene room with dissolve

    menu:
        "Following my interview with Lenard Malcom of CPC, I think..."

        "NeoGenesis should be held responsible for their negligence.":
            $stance = 2
            $enviro_interview_synopsis = "Lenard is a passionate guy who wants what is best for everyone, but especially their safety."

        "How could a genesis gate implode an entire star system with just a solar flare?": 
            $enviro_interview_synopsis = "Lenard is a passionate guy who wants what is best for everyone, but especially their safety."

        "The genesis gate must have been sabotaged, but maybe not by the CPC.":
            $stance = 5
            $enviro_interview_synopsis = "Lenard is a passionate guy who wants what is best for everyone, but especially their safety."

    ben "Time to write that article."

    show black with dissolve
    pause 0.5
    show room with dissolve
    return

label vp_interview:
    show black with dissolve
    pause 0.5
    scene city with dissolve
    show img_traitor

    ben "Ellen Wyse, I was informed that you lead the day to day operations for CPC.{w} Could you shed some light on how your organization operates for me and the public?"

    traitor "Of course, Ben, we merely perform legal inspections on genesis gates.{w} What we've found might be surprising though.{w} It seems that their engineering efforts lowered the energy required to cause the origami effect for transportation, yet they're still using near the theoretical energy levels, while also not increasing the distance between their 'gates'."

    ben "What do you mean by 'gates'?"

    traitor "Don't let Chad Hewett's charm fool you.{w} The genesis gate incident was a cover up for testing the genesis gate's potential as a weapon.{w} We just can't definitively prove it because...{w} well the evidence is gone and with the rumors of it being a sabotage with CPC being a suspect it's difficult to get close to any genesis gates to see if they too have the same or better potential for that matter as a weapon."

    ben "You seem to know a lot about NeoGenesis's internal operations."

    traitor "I've invested into NeoGenesis to be on the board to guide humans beyond our solar system and even beyond humanity.{w} I know all of this because I've heard the rest of the board of directors talk about their plans.{w} They are planning to cause a big crunch for The Universe to do a big bounce so that The Universe continues eternally, ending everything that it is now.{w} They actually believe it is up to sentient beings to prevent the big freeze and hope sentient life re-evolves in the next universe to do the same.{w} These genesis gates are a gift for mankind, I'm just afraid of how they'll be used.{w} I know it might sound far fetched to you but we must stop Chad, please Ben."

    ben "I'll have to think about it. That's a lot to take in."

    traitor "I understand, Ben.{w} Remember you can't take your time with this issue."

    scene black with dissolve
    pause 0.2
    scene room with dissolve

    menu:
        "Following my interview with Ellen Wyse, VP of CPC, I think..."

        "The genesis gates need to be destroyed before they can be used for mass destruction.":
            $stance = 2
            $vp_interview_synopsis = "Ellen seems to be against NeoGenesis based on her concerns for Chad Hewett's intent more than concern for safety or celestial preservation."

        "The mysterious investor comes forth and reveals Chad Hewett's corrupt plans.":
            $stance = 3
            $vp_interview_synopsis = "Ellen seems to be against NeoGenesis based on her concerns for Chad Hewett's intent more than concern for safety or celestial preservation."

        "Expose Ellen for the crazed lunatic she is.":
            $stance = 5
            $vp_interview_synopsis = "Ellen seems to be against NeoGenesis based on her concerns for Chad Hewett's intent more than concern for safety or celestial preservation."

    ben "Time to write that article."

    show black with dissolve
    pause 0.5
    show room with dissolve

    jump end_game
