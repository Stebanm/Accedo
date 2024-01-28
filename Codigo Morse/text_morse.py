from dictionary import MORSECODE

# Funcion para convertir texto a codigo morse.
def text_to_morse(message):

    morse_code = []

    for letter in message:

        # Verificamos si la letra está en el diccionario de código Morse.
        if letter in MORSECODE:
            morse_code.append(MORSECODE[letter])

    # Retornamos la secuencia de código morse con un espacio entre ellas.
    return " ".join(morse_code)