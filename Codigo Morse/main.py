from text_morse import text_to_morse
from morse_text import morse_to_txt
from display import display_menu


# Función principal.
def main():
    while True:
        display_menu()
        option = input("Ingrese una opción (1/2): ")
        if option == "1" or option == "2":
            break
    
    if option == "1":
        morse_input = input("Ingrese el código Morse (caracteres separados con espacios): ")
        text_output = morse_to_txt(morse_input)
        print("Código morse a texto: ")
        print(text_output)

    elif option == "2":
        text_input = input("Ingrese un mensaje: ").upper()
        morse_output = text_to_morse(text_input)
        print("Texto a código morse: ")
        print(morse_output)
        

    else:
        print("Opción invalida. Por favor ingrese una opción entre 1 y 2.")


if __name__ == "__main__":
    main()