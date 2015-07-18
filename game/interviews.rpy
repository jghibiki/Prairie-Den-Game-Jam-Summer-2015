label phd_interview:
    show black with dissolve
    pause 0.5
    scene lab with dissolve
    show img_scientist
    ben "Dr. Dorian, your theory of the Origami Effect is supposed to eventually bring  about a new chapter in the efficiency of space travel. How did you develop this theory?"    

    scientist "The theory of folding space time upon itself is not a new concept.{w} However, I have conceptualized a theory that would allow us to - theoretically - fold space over on itself and then punch through the \"surface\" of the universe creating a hole that leads to another location in space, often called a wormhole."
    scientist "Similar to origami, this can be used multiple times making several distant places in space seem much closer by folding space as you would fold a piece of paper.{w} Thus making it possible to travel to distant locations quite rapidly."

    ben "That sounds like a rather bold concept. Are there any plans in the works to actually test and implement this concept or is this simply a grand theory?"

    scientist "With the current state of technology, I do not forsee any breakthroughs in the implementation of my theory.{w} As it is a project like this would require a large venture capital to take interest in the concept of lowering the cost of transportation.{w} And at this point I don't think any one would be willing to give up the extra cash needed to see this to realization."

    ben "So then you are telling me that at this point, it has no practicale uses?"

    scientist "No. That is not what I am saying at all. It would be very expensive to attempt now, but say 10 years in the future, following current technology trends, it should be much more affordable."

    ben "So, Doctor assuming your theory is eventually implemented, there are misgivings in the scientific community that a device implemented using your theory could be used to coagulate astral bodies into one giant mass,{w} creating the theoretical conditions for an synthetic black hole.{w} What then, if instead of funding a new transportation method, funding was provided to utilize the theory in a weapon?"

    scientist "Ha! Even if someone did manage to implement my theory any time soon - much less weaponize it - the ammount of energy it would take to, fold space over and over until enough astral bodies are positioned in the same gravitaional sphere to produce a black hole, is tremendous. By our current standards and forseeable future standards, impossible!"

    scene black with dissolve
    pause 0.2
    scene room with dissolve

    menu:
        "Following my interview with Dr. Dorian, I think..."

        "Oragami Effect could be weaponized":
            $stance -= 1
            $cpc_influence += 2
            $phd_interview_synopsis = "Dr. Dorian reintroduced me the basic concept of the Origami Effect. By folding space over on itself, it should become possible to create a hole that bridges the two locations, similar to folding a piece of paper in half and poking a hole through it.{w} When I questioned him about the possibility of this potential technology being used to create weapons, he failed to convince me that there was no danger.{w} His main defence was to say that we cannot yet produce enough power to weaponize the Origami Effect."

        "Oragami Effect is impractical as a weapon":
            $cpc_influence += 1 
            $phd_interview_synopsis = "Dr. Dorian reintroduced me the basic concept of the Origami Effect. By folding space over on itself, it should become possible to create a hole that bridges the two locations, similar to folding a piece of paper in half and poking a hole through it.{w} When I questioned him about the possibility of this potential technology being used to create weapons, he assured me that using the Origami Effect in a weapon would be impractical.{w} We cannot yet produce enough power to weaponize the Origami Effect."

        "Origami Effect cannot be used in the creation of a weapon":
            $neog_influence += 1
            $stance += 1
            $phd_interview_synopsis = "Dr. Dorian reintroduced me the basic concept of the Origami Effect. By folding space over on itself, it should become possible to create a hole that bridges the two locations, similar to folding a piece of paper in half and poking a hole through it.{w} When I questioned him about the possibility of this potential technology being used to create weapons, he assured me that using the Origami Effect in a weapon would be impossible.{w} Reguardless of technological advances, there are no means with which to weaponize the Origami Effect."
    
    ben "Time to write that article"
    
    scene black with dissolve
    pause 0.4
    scene room with dissolve
    return


label investor_interview:

    return


label enviro_interview:

    return

label vp_interview:

    return
