def reverse_string(o_string):
    r_string = ""

    for char in o_string[::-1]:
        r_string += char

    print("String original:", o_string)
    print("String invertida:", r_string)

o_string = input("Digite uma string para inverter: ")
reverse_string(o_string)