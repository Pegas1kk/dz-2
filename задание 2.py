# пронумеровать и разделить ряды, а в рядах пронумеровать и разделить места
# поставить счетчик пустых мест во вложенном цике
# КАК ПРОВЕРИТЬ ЧТО ПУСТЫЕ МЕСТА РЯДОМ REEEEEEEEEEEEEEEEE
seats = [[0, 1, 1, 0], [1, 0, 0, 0], [0, 1, 0, 0]]
tickets = int(input('Введите кол-во билетов:'))

available_row = -1

for i_row, row in enumerate(seats):
    empty_seats = 0
    # print(i_row, row)
    for i_seats, seat in enumerate(row):
        # print(i_seats, seat)
        if seat == 0:
            empty_seats += 1
            if empty_seats == tickets:
                available_row = i_row
                break
        else:
            empty_seats = 0
    if available_row >= 0:
        break
if available_row >= 0:
    print(available_row + 1)
else:
    print(False)
#
