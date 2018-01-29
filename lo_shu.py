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

# check rows
for row in square:
    if sum(row) != 15:
        is_square = False
        print(str(row) + " fails the test! lul faillllllll")

# check cols
for i in range(3):
    if square[0][i] + square[1][i] + square[2][i] != 15:
        is_square = False
        print("Column " + str(i) + " fails the test! why did you think that would work ?!?!?!?")

# check diagonals
if square[0][0] + square[1][1] + square[2][2] != 15:
    is_square = False
    print("Left->Right diagonal fails the test! jeBaited jeBaited jeBaited")

if square[0][2] + square[1][1] + square[2][0] != 15:
    is_square = False
    print("Right->Left diagonal fails the test! Kappa Kappa Kappa")

if not is_square:
    print("This is not a Lo Shu Magic Square! what were you thinking lol?")
else:
    print("This is a valid Lo Shu Magic Square! congrats, genius")



