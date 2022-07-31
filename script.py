# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Andrea")
define r = Character("Juan")
define t = Character("Tama")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    image bg room = "background.jpg"

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    image Andrea happy = "Andrea_happy.png"

    image Juan sad = "Juan_sad.png"

    image Tama joyful = "tamagod.png"

    show Andrea happy

    # These display lines of dialogue.

    e "Bienvenido a gei 1."

    e "Vuelve cuando programes algo más que solo ejemplos."

    hide Andrea happy

    show Juan sad

    r "el juego sigue vacío."

    r "Más vacío que mis ganas de vivir."

    hide Juan sad

    show Tama joyful

    

    t "MEOW"

    
    t "(Waiting for something to happen?)"



    # This ends the game.

    return
