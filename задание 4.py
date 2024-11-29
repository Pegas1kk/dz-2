text = input("Введите строку")
key = int(input("Введите ключ"))
alphabet = "abcdefghijklmnopqrstuvwxyz"
retext = ""
for char in text:
    if char.lower() in alphabet:
        i = alphabet.find(char.lower())
        new_index = (i + key) % 26
        if char.isupper():
            retext += alphabet[new_index].upper()
        else:
            retext += alphabet[new_index]
    else:
        retext += char
print(retext)


# word = input("Введите строку")
# shift = int(input("Введите ключ"))
# a = ord('a')
# z = ord('z')
# A = ord('A')
# Z = ord('Z')
# AlphabetSize = z - a + 1
# Output = ""
# for c in word:
#     C = ord(c)
#     # print(C, c)
#     if c != ' ':
#         if c.isupper():
#             C += shift
#             if (C > Z):
#                 C -= AlphabetSize
#         else :
#             C += shift
#             if (C > z):
#                 C -= AlphabetSize
#     # print("->", C, chr(C))
#     Output += chr(C)
# print(Output)