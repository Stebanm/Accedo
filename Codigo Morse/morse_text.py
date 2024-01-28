from dictionary import MORSE_MESSAGE

# Funcion para convertir código morse a texto.
def morse_to_txt(message):

    # Separamos las palabras en código morse.
    message = message.split(" ")
    text = []

    for morse_code in message:

        # Verificamos si el codigo morse se encuentra en el diccioario inverso.
        if morse_code in MORSE_MESSAGE:
            text.append(MORSE_MESSAGE[morse_code])

    # Retornamos las letras unidas en una única cadena de texto.
    return " ".join(text)