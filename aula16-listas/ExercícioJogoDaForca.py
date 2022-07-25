print("Adivinhe a palavra!")

palavra = "tryndamere"
string_vazia = ""
controle = 0

while True:


    digito = input("Digite uma letra: ")

    if digito.isdigit() or len(digito) > 1:
        print("Ofereça um dígito válido!")
        continue

    if digito in palavra:
        print(f"Parabéns, a letra {digito} está na palavra.")
        cont = 0
        for letra in palavra:
            if digito == palavra[cont]:
                string_vazia += palavra[cont]
                if controle == 1:
                    continue
            elif digito != palavra[cont]:
                string_vazia += "*"
            cont += 1
        print(string_vazia)
        controle = 1

    if string_vazia == palavra:
        print(f"Parabéns, você achou a palavra {string_vazia}!")
