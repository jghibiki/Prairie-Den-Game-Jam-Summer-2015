label ceo_email:
    _ben "Mr. Hewett"
    _ben "I wanted to meet with you on the recently leaked NeoGenesis budget and your goals for the genesis gates."
    ceo "As far as the budget is concerned I'll have an official statement addressing that in a press conference coming up soon."

    if stance == 5:
        ceo "You've got some good sources. My goals are pretty straight forward, I've always wanted to explore The Universe and being stuck in our solar system had just been a teaser for far too long. Finally now we have virtually infinite places to explore, collect resources from, and can finally expand our search for other beings in The Universe. I want it all in my life time so there just isn't any time to lose especially since being the first one on the market makes you a rich man."
    elif stance == 2:
        ceo "I don't know where you find your material but you'll just have to wait for the press conference like everyone else. I can see lying for your best friend but doing it to destroy my company's reputation isn't appreciated. Connecting The Universe isn't easy as it is. I don't need you running around spreading conspiracy theories about genesis gates being used as a weapon since their potential is far greater in service to The Universe's eternalness."
    else:
        ceo "Seems like you're trying to be fair and objective by fact checking your sources these days. I understand wanting something bad enough that you'll do it even if it might be the wrong decision, and I believe in second chances. Heck I wouldn't be doing what I do if it didn't."

    menu:
        "Following my interview with Chad Hewett, I'll report..."

        "The genesis gate highway project must have some other function with a budget and scale like this.":
            $stance = 2
            if stance == 5:
                $ceo_interview_synopsis = "Chad was happy to talk about his goals for the genesis gate highway system."
            elif stance == 2:
                $ceo_interview_synopsis = "Chad was not pleased with my past reporting."
            else:
                $ceo_interview_synopsis = "Chad was glad I'm trying to earn my credibility."

        "The genesis gates will connect The Universe on a level only dreamed of before.":
            $stance = 5
            if stance == 5:
                $ceo_interview_synopsis = "Chad was happy to talk about his goals for the genesis gate highway system."
            elif stance == 2:
                $ceo_interview_synopsis = "Chad was not pleased with my past reporting."
            else:
                $ceo_interview_synopsis = "Chad was glad I'm trying to earn my credibility."

    nvl clear
    return

label inventor_email:
    _ben "Ms. Mclaren"
    _ben "I was wondering if you were available for an interview?"

    inventor "Sorry. I can't meet in person, but I could maybe answer a few questions via email here."

    _ben "Great! What sort of travel options can we expect from genesis gates? What would you say you owe your success in engineering the genesis gates so quickly?"

    inventor "I was able to engineer the genesis gates so quickly because it was easy, though I have to admit our CEO, Chad, had some specifications that were pretty extreme for our prototype, but I managed. The travel options are pushed to the limit thanks to Chad's vision. I guess that means you can expect 1 genesis gate for each star system and even a few in between."

    _ben "That sounds great. What kind of crazy specifications did Chad have? I'm really curious to know why would we have genesis gates in between star systems too?"

    inventor "Well even though I was able to reduce the energy requirements even lower than Dr. Dorian's model predicted we're still using about the same amount of energy needed in the hypothetical models.{w} I keep telling him its a waste of money but he insists \"it is just in case.\"{w} As for genesis gates in the middle of no where, I have no clue because with the energy these things can pull in they could be almost twice as far... Then again, I guess maybe to allow more customizable routes between star systems, but that's pretty much the only reason I could think of."
    inventor "Honestly, I just like the challenges to meet his vision, speaking of which we've got some real tight deadlines and I might have violated my NDA, but it sucks not being able to show everyone how cool this stuff really is, just don't disclose me as a source and we'll call it even, okay?"

    _ben "Sounds like quite the challenge. I'll definitely keep you anonymous it was great material."

    menu:
        "Following my interview with Kim McLaren, I'll report..."

        "The genesis gates are using an alarming amount of energy and are way to close to each other.":
            $stance = 2
            $inventor_interview_synopsis = "Kim reveals her brilliance meeting all of NeoGenesis's specifications. Even though she has improved the genesis gates significantly those improvements aren't being utilized much."

        "The genesis gates are pushing technology to the limits.":
            $stance = 4
            $inventor_interview_synopsis = "Kim reveals her brilliance meeting all of NeoGenesis's specifications. Even though she has improved the genesis gates significantly those improvements aren't being utilized much."

        "The genesis gates will provide very customizable routes for their highways between star systems using many genesis gates and variable power to fold greater distances when needed.":
            $stance = 5
            $inventor_interview_synopsis = "Kim reveals her brilliance meeting all of NeoGenesis's specifications. Even though she has improved the genesis gates significantly those improvements aren't being utilized much."

    nvl clear
    return

label inventor_email_2:
    _ben "Hello, Kimberly McLaren"
    _ben "It has been a while, but I just wanted to know about your thoughts on the genesis gate malfunction."

    inventor "Ugh! It just makes me so angry! I know I didn't mess up on that one. I even gave a quality check after that one was produced and everything seemed to be in order."

    _ben "Why does it make you so angry? I thought NeoGenesis claimed a massive solar flare struck the genesis gate, that couldn't be your fault?"

    inventor "The amount of energy these gates can take wouldn't cause a whole star system to implode because it was struck by a solar flare. It had to be sabotaged while being inspected by CPC or something. They're always getting in the way and spreading rumors that NeoGenesis plans to use them as a weapon. I mean come on at the rate we're building these gates, we'd be imploding the whole known universe and then some. We want to connect The Universe not destroy it... I just cannot believe Chad would want to, he's just too passionate and kind."

    _ben "So, why would NeoGenesis claim it was a solar flare that caused it?"

    inventor "I thought that myself. I guess I just threw it up to the fact that those representatives don't know anything when it comes to technology. It is weird they didn't even ask me to check it out, even if they did... I couldn't though, the gate and star system is just one giant mass now. Probably saved me a headache trying to explain it to them anyway."

    _ben "That is strange though. I'll have to speak with CPC soon."

    menu:
        "Following my interview with Kim McLaren, I'll report..."

        "NeoGenesis corporation covers up genesis gate weapons testing.":
            $stance = 2
            $inventor_interview_synopsis = "Kim reveals her frustration with the genesis gate malfunction."

        "NeoGenesis corporation still doesn't know the genesis gate malfunction's cause.":
            $stance = 4
            $inventor_interview_synopsis = "Kim reveals her frustration with the genesis gate malfunction."

        "The genesis gate malfunction was probably due to sabotage.":
            $stance = 5
            $inventor_interview_synopsis = "Kim reveals her frustration with the genesis gate malfunction."


    nvl clear
    return
