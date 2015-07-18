label phd_interview:
    show black with dissolve
    pause 0.5
    scene lab with dissolve
    show img_scientist
    ben "Dr. Dorian, your theory of the Origami Effect is supposed to eventually bring  about a new chapter in the efficiency of space travel. How did you develop this theory?"    

    scientist "The theory of folding space time upon itself is not a new concept.{w} However, I have conceptualized a testable hypothesis that would allow us to - theoretically - fold space over on itself and then punch through the \"surface\" of the universe creating a hole that leads to another location in space, often called a wormhole."
    scientist "Similar to origami, this can be used multiple times making several distant places in space seem much closer by folding space as you would fold a piece of paper.{w} Thus making it possible to travel to distant locations rapidly."

    ben "That sounds like a rather bold concept. Are there any plans in the works to actually test and implement this concept or is this simply a grand theory?"

    scientist "It's a hypothesis Ben.{w} Though feasibly testable it isn't testable with the current state of technology today.{w} I do not forsee any breakthroughs in the implementation of my hypothesis, but hope to see it proved a theory in my life time.{w} As a project like this would require large venture capital to take interest in the concept of lowering the cost of transportation.{w} Unfortunately, at this point I don't think any one would be willing to put forth the capital needed to see this in practice."

    ben "So then you are telling me that at this point, it has no practicale uses?"

    scientist "No. That is not what I am saying at all. I am just saying it would be very expensive to attempt now, but say 10 years in the future, following current technology trends, it should be much more affordable."

    ben "So, Doctor assuming your hypothesis is eventually proven, there are warnings in the scientific community that a device implemented using your theory could be used to coagulate celestial bodies into one giant mass,{w} creating the theoretical conditions for an synthetic black hole.{w} What then, if instead of funding a new transportation method, funding was provided to utilize the origami effect hypothesis in a weapon?"

    scientist "Ha! Even if someone did manage to implement my hypothesis any time soon - much less weaponize it - the ammount of energy it would take to, fold space over and over until enough celestial bodies are positioned to significantly attract each other gravitaionally to produce a black hole, is tremendous.{w} So, at present, the answer to your question is: it is impossible!"

    scene black with dissolve
    pause 0.2
    scene room with dissolve

    menu:
        "Following my interview with Dr. Dorian, I think..."

        "The oragami effect hypothesis could be weaponized.":
            $stance = 2
            $phd_interview_synopsis = "Dr. Dorian introduced me the basic concept of his hypothesis the origami effect. By folding space over on itself, it should become possible to create a hole that bridges the two locations, similar to folding a piece of paper in half and poking a hole through it.{w} When I questioned him about the possibility of this potential technology being used to create weapons, he was insistent there wasn't much practical danager.{w} His main defense was to say that we cannot yet produce enough power to weaponize the origami effect."

        "The oragami effect hypothesis is impractical as a weapon":
            $stance = 1
            $phd_interview_synopsis = "Dr. Dorian introduced me the basic concept of his hypothesis the origami effect. By folding space over on itself, it should become possible to create a hole that bridges the two locations, similar to folding a piece of paper in half and poking a hole through it.{w} When I questioned him about the possibility of this potential technology being used to create weapons, he was insistent there wasn't much practical danager.{w} His main defense was to say that we cannot yet produce enough power to weaponize the origami effect."

        "Origami Effect cannot be used in the creation of a weapon":
            $stance = 5
            $phd_interview_synopsis = "Dr. Dorian introduced me the basic concept of his hypothesis the origami effect. By folding space over on itself, it should become possible to create a hole that bridges the two locations, similar to folding a piece of paper in half and poking a hole through it.{w} When I questioned him about the possibility of this potential technology being used to create weapons, he was insistent there wasn't much practical danager.{w} His main defense was to say that we cannot yet produce enough power to weaponize the origami effect."
    
    ben "Time to write that article."
    
    scene black with dissolve
    pause 0.4
    scene room with dissolve
    return


label investor_interview:
    show black with dissolve
    pause 0.5
    show room with dissolve
    show img_investor

    ben "I just can't find anything on him.{w} It's like he's watching my every move.{w} I'm being followed when I'm out though, I better be careful."

    menu:
        "This development is concerning, I think..."

        "To be safe I'll expose my watchdog.":
            $stance = 2
            $investor_interview_synopsis = "The investor has taken many precautions to hide his identity."

        "I'll act like nothing is happening and write a personal blog entry.":
            $investor_interview_synopsis = "The investor has taken many precautions to hide his identity."

    ben "Time to write that article."

    show black with dissolve
    pause 0.5
    show room with dissolve
    return


label enviro_interview:
    ben "Mr. Malcom, your organization, the Celestial Preservation Coalition, recently called for origami effect regulations.{w} You also publicly encourage challenging NeoGenesis while they deploy their genesis gates utilizing the origami effect.{w} What sparked these protests?"

    environmentalist "I’m glad that somebody will listen to our side, Ben.{w} Due to the recent accident at the Farest System's genesis gate caused by energy anomalies said to be caused by a solar flare.{w} It is very clear that these genesis gates can be dangerous.{w} We need new regulations and more competition in the industry to help ensure things are done right.{w} There is no reason that an entire star system should be wiped from existence due to an accident."

    ben "Genesis gates alleges that their genesis gate was sabotaged.{w} It might have not been an accident."

    environmentalist "I can assure you Mr. Carlson we are a peaceful organization acting within the bounds of the law.{w} I do have to admit that sabotage might help in our end goal, but blowing up a whole star system does not.{w} Here, let me help you get in contact with our Vice President, Ellen Wyse, who oversees our internal day to day operations."

    scene black with dissolve
    pause 0.2
    scene room with dissolve

    menu:
        "Following my interview with Lenard Malcom of CPC, I think..."

        "NeoGenesis should be held responsible for their negligence.":
            $stance = 2
            $enviro_interview_synopsis = "Lenard is a passionate guy who wants what is best for everyone, but especially their safety if a genesis gate can wipe out a star system or potentially a galaxy with a malfunction caused by natural occurances or malicious tinkering."

        "How could a genesis gate implode an entire star system with just a solar flare?": 
            $enviro_interview_synopsis = "Lenard is a passionate guy who wants what is best for everyone, but especially their safety if a genesis gate can wipe out a star system or potentially a galaxy with a malfunction caused by natural occurances or malicious tinkering."

        "The genesis gate in the Farest System must have been sabotaged.":
            $stance = 5
            $enviro_interview_synopsis = "Lenard is a passionate guy who wants what is best for everyone, but especially their safety if a genesis gate can wipe out a star system or potentially a galaxy with a malfunction caused by natural occurances or malicious tinkering."
    ben "Time to write that article."

    show black with dissolve
    pause 0.5
    show room with dissolve
    return

label vp_interview:
    show black with dissolve
    pause 0.5
    show city with dissolve
    show img_traitor

   
ben "Ellen Wyse, I was informed that you lead the day to day operations for CPC.{w} Could you shed some light on how your organization operates for me and the public?"

traitor "Of course, Ben, we merely perform legal inspections on genesis gates.{w} What we've found might be surprising though.{w} It seems despite that despite their engineering efforts to lower the energy required to cause the origami effect for transportation they're still using near the theoretical power levels, while also not increasing the distance between their 'gates'."

   ben "What do you mean by 'gates'?"

   traitor "Don't let Chad Hewett's charm fool you.{w} The Farest System accident/sabotage was a cover up for testing the genesis gate's potential as a weapon.{w} We just can't definitively prove it because...{w} well the evidence is gone and with the rumors of it being a sabotage with CPC being a suspect it's difficult to get close to any genesis gates to see if they too have the same or better potential for that matter as a weapon.{w} I know it might sound far fetched to you but we must stop Chad, please Ben.{w} What do you have left to lose since your reputation was washed away from not fact checking a military operative, even if he was a childhood friend?"

   ben "I'll think about it. This is a lot to take in."

   traitor "I understand, Ben.{w} Remember you can't take your time with this issue. Obviously you shouldn't disclose me as a source on this matter."

   scene black with dissolve
   pause 0.2
   scene room with dissolve

   menu:
        "Following my interview with Ellen Wyse, VP of CPC, I think..."

        "A full investigation should be conducted on the genesis gates by a reputable third party.":
            $stance = 3
            $vp_interview_synopsis = "Ellen seems to be against NeoGenesis based on her concerns for Chad Hewett's intent with them more than concern for safety or celestial preservation."

        "Chad Hewett needs to be investigated for plans to use the genesis gates as weapons.": 
            $vp_interview_synopsis = "Ellen seems to be against NeoGenesis based on her concerns for Chad Hewett's intent with them more than concern for safety or celestial preservation."

        "Expose Ellen for the crazed lunatic she is.":
            $stance = 5
            $vp_interview_synopsis = "Ellen seems to be against NeoGenesis based on her concerns for Chad Hewett's intent with them more than concern for safety or celestial preservation."

    ben "Time to write that article."

    show black with dissolve
    pause 0.5
    show room with dissolve

   return
