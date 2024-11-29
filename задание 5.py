Dict = {}
Input = input()
while Input != '':
    InputF = Input.split()
    if Dict.get(InputF[0]) is None:
        Dict[InputF[0]] = {}
    if Dict[InputF[0]].get(InputF[1]) is None:
        Dict[InputF[0]][InputF[1]] = []
    (Dict[InputF[0]][InputF[1]]).append(InputF[2])
    Input = input()

for category, students in Dict.items():
    print(category)
    for student, marks in students.items():
        print(f"{student} {' '.join(marks)}")
    print()

