# user_num = int(input('введите число'))
# if user_num <= 9:
#     print(user_num)
# while user_num > 9:
#     sum = 0
#     for char in str(user_num):
#         sum += int(char)
#     user_num = sum
# print('полученное число', user_num)


user_num = int(input('введите число'))
while   user_num >= 10:
    user_num = sum(int(digit) for digit in str(user_num))
print(user_num)