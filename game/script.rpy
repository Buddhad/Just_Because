#Starting Dialog
define n = Character("Naho Takamiya",color = "#381bd1")
define k = Character("Kyo Soma",color = "#d11b59")
define l = Character("lio sanchi",color = "#d11b59")
#kyo Character
image kyo cool = im.Scale("kyo cool.png", 607, 687)
image kyo sad = im.Scale("kyo sad.png", 607, 687)

#lio Character
image lio surprise = im.Scale("lio surprise.png", 607, 687)
image lio s = im.Scale("lio smile2.png", 607, 687)

#background
image classroom="Classroom_Day.png"
image hallway="School_Hallway_Day.png"


# The game starts here.
label start:
    show classroom
    show naho smile
    pause (2.0)
    show naho smile at left
    with move
    pause (3.0)

    play music "audio/guiter.mp3 "  fadein 2.0 volume 0.3
    # These display lines of dialogue.
    n "Hi there! How was class?"
    show kyo cool at right
    with moveinright
    pause(3.0)
    k "Good..."

    k "I can't bring myself to admit that it all went in one ear and out the other."

    n "Are you going home now? Wanna walk back with me?"
    stop music fadeout 2.0

    # show aiko shoutblush at right
    menu:
        "Yes !":
            call Yeah
        "...":
            call Naah
    # This ends the game.
    return

    label Yeah:

        k "Sure!"
        show naho delighted at left
        n "Okey! meet you in the hallway then after the end of this class ."

        scene hallway
        with fade
        play music "audio/gentalfootstep.mp3 "  fadein 6.0 volume 0.3
        show naho smile at left
        with moveinleft
        n "Hey Kyo wait for me !!"

        show lio surprise at right
        with moveinright
        l "What me ??!! "
        n "oh ! sorry I thought that your are naho !!"
        show lio s at right
        l "oh "
        stop music fadeout 2.0

        return

    label Naah:
    show naho sad at left
    show kyo sad at right
    k "Sorry! I have a tution So i didn't make it "
    n "oh!!"
    hide naho sad at right
    with moveoutleft
    pause(3.0)


   #  scene hallway
   #  with fade
   #
   # play music "audio/gentalfootstep.mp3 "  fadein 6.0 volume 0.3

label bgm:
    play music "audio/fogottenmemory.mp3"  fadein 4.0 volume 0.5
    scene hallway
    with fade



    return







label sprite:
    e  "Hi! I am a Rocky love to see you here "
    e  "Oh!"
label character:
    show eileen happy
label background:
    show picture_1
label sfx:
    show picture_1
label choices:
    menu:
        "Really Amazing...Thank You Eileen and How was your day ? ":
            call GoodDay
        "Naah it was a boring day.":
            call BadDay
    # This ends the game.
    return
