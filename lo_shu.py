# Mark Sherriff (mss2x)

numbers = (input("Numbers: ")).split()

square = [[0,0,0],[0,0,0],[0,0,0]]

count = 0

is_square = True

for i in range(3):
    for j in range(3):
        square[i][j] = int(numbers[count])
        count += 1
# print(square)
print("You entered:")
for row in square:
    print(str(row[0]) + '\t' + str(row[1]) + '\t' + str(row[2]))

# check square
is_square = _check('row', square) or _check('cols', square) or _check('diagonals', square)

if not is_square:
    print("This is not a Lo Shu Magic Square!")
else:
    print("This is a valid Lo Shu Magic Square!")


def _check(direction, square):
    is_square = True

    if direction == "row":
        for row in square:
            if sum(row) != 15:
                is_square = False
                print(str(row) + " fails the test!")

    elif direction == "cols":
        for i in range(3):
            if square[0][i] + square[1][i] + square[2][i] != 15:
                is_square = False
                print("Column " + str(i) + " fails the test!")

    elif direction == "diagonals":
        if square[0][0] + square[1][1] + square[2][2] != 15:
            is_square = False
            print("Left->Right diagonal fails the test!")

        if square[0][2] + square[1][1] + square[2][0] != 15:
            is_square = False
            print("Right->Left diagonal fails the test!")

    return is_square
