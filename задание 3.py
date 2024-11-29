# text = input('введите текст:')
# encoded = ""
# count = 1
# prev_char = text[0]
#
# for i in range(1, len(text)):
#   if text[i] == prev_char:
#     count += 1
#   else:
#     encoded += str(count) + prev_char
#     prev_char = text[i]
#     count = 1
#
# encoded += str(count) + prev_char
# print(encoded)


Input = input('введите')
n = 0
output = ""
for i in Input:
    if n == 0:
        c = i
    if c == i:
        n += 1
    else:
        output += str(n) + c
        c = i
        n = 1

output += str(n) + c
print(output)