# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

init python:
    def text_sound(event, **kwargs):
        if event == "show":
            renpy.music.play("audio/type_blip.ogg", channel="sound", loop=True)
        elif event == "slow_done" or event == "interact":
            renpy.music.stop(channel="sound")

define narrator = Character(None, callback=text_sound)
define avalice = Character("Avalice", callback=text_sound)

label start:
    scene bg city

    "Somewhere in a sprawling city where humans and other species live side-by-side, there is a girl named Avalice."

    "To the world, she is just an ordinary citizen. But in reality, she is an anomaly." 

    "She carries a forbidden, cursed bloodline—a bloodline that society believes was completely wiped out centuries ago."

    "Because of this, she lives under a false name, blending into the crowd to keep her existence a secret."

    # 2. Introducing the Rival Family's Motive (Political Erasure)
    "What Avalice doesn't know is that the ruling Family is already hunting her down."

    "For generations, this elite bloodline has ruled the city, claiming their power comes from a pure, divine blessing." 

    "But their empire is built on a lie."

    "Avalice's cursed blood is the living proof of their dark history—a secret that, if revealed, would destroy the ruling family's reputation and strip them of their power overnight."

    # 3. The Threat & The Ticking Clock
    "To protect their perfect image, they cannot let her live free." 

    "They don't just want her captured; they need her erased from history entirely."

    # 4. Smooth Transition to the Main Character
    scene bg mc_room
    with fade

    "Avalice's cover is about to break..."
    "And the only person who can step into the shadows to save her... is you."
    return
