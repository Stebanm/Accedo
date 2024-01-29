# Diccionario que contiene las letras del alfabeto con su correspondiente código morse.
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


# Diccionario invertido de código morse a letras.
MORSE_MESSAGE = {value: key for key, value in MORSECODE.items()}