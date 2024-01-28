# Creamos un diccionario que contiene las letras del alfabeto con su correspondiente codigo morse.
MORSECODE = { 
    "A": ".-", 
    "B": "-...", 
    "C": "-.-.", 
    "D": "-..", 
    "E": ".", 
    "F": "..-.", 
    "G": "--.", 
    "H": "....", 
    "I": "..", 
    "J": ".---", 
    "K": "-.-", 
    "L": ".-..", 
    "M": "--", 
    "N": "-.", 
    "O": "---", 
    "P": ".--.", 
    "Q": "--.-", 
    "R": ".-.", 
    "S": "...", 
    "T": "-", 
    "U": "..-", 
    "V": "...-", 
    "W": ".--", 
    "X": "-..-",
    "Y": "-.--", 
    "Z": "--.."
    }


# Creamos un diccionario inverso que contiene código morse a letras.
MORSE_MESSAGE = {value: key for key, value in MORSECODE.items()}