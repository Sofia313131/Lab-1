# ========== Constants =========
RED = '\u001b[41m'
BLUE = '\u001b[44m'
WHITE = '\u001b[47m'
END = '\u001b[0m'

SEP_COUNT = 3

# ========== Task 1 ============


def draw_flag(n, m):
    assert n % 2 == m % 2, "Числа должны быть одинаковой чётности"
    if n % 2 == 0:
        assert n >= 8 and m >= 20, "Минимальные размеры чётного флага 8x20."
    else:
        assert n >= 5 and m >= 11, "Минимальные размеры нечётного флага 5x11."
    h = min((n - 2) // 3, (m - 2) // 9)
    bn = (n - h * 3) // 2
    bm = (m - h * 9) // 2
    for _ in range(bn):
        print(RED, " " * m, END, sep="")
    for _ in range(h):
        print(RED, " " * (bm + h * 3), WHITE, " " * (h * 3), RED, " " * (m - bm - h * 6), END, sep="")
    for _ in range(h):
        print(RED, " " * bm, WHITE, " " * (h * 9), RED, " " * (m - bm - h * 9), END, sep="")
    for _ in range(h):
        print(RED, " " * (bm + h * 3), WHITE, " " * (h * 3), RED, " " * (m - bm - h * 6), END, sep="")
    for _ in range(n - bn - h * 3):
        print(RED, " " * m, END, sep="")


draw_flag(5, 21)

# ========== Separate ==========
for _ in range(SEP_COUNT):
    print()

# ========== Task 2 ============
COUNT = 6
print(f"   {WHITE}         {END}   " * COUNT)
print(f" {WHITE}   {END}       {WHITE}   {END} " * COUNT)
print(f"{WHITE}  {END}           {WHITE}  {END}" * COUNT)
print(f"{WHITE} {END}             {WHITE} {END}" * COUNT)
print(f"{WHITE}  {END}           {WHITE}  {END}" * COUNT)
print(f" {WHITE}   {END}       {WHITE}   {END} " * COUNT)
print(f"   {WHITE}         {END}   " * COUNT)

# ========== Separate ==========
for _ in range(SEP_COUNT):
    print()

# ========== Task 3 ============
X_LIMIT = 90
Y_LIMIT = 15

X_SIZE = 1
Y_SIZE = 0.4

X_STEP = 5

NUM_PAD = 4

field = [["-" for _ in range(X_LIMIT)] for _ in range(Y_LIMIT)]


def function(arg):
    return arg / 3


for x in range(1000):
    x *= X_LIMIT / 1000

    y = function(x)

    x = round(x * X_SIZE)
    y = round(y * Y_SIZE)

    if 0 <= x < X_LIMIT and 0 <= y < Y_LIMIT:
        field[Y_LIMIT - round(y) - 1][round(x)] = f"{RED} {END}"


for y in range(Y_LIMIT):
    print(
        str(
            round((Y_LIMIT - y - 1) / Y_SIZE)
        ).rjust(NUM_PAD),
        "|",
        "".join(field[y])
    )

print(" " * NUM_PAD, "|=", end="")

for x in range(X_LIMIT):
    if x % X_STEP == 0:
        print("|", end="")
    else:
        print("=", end="")

print()
print(" " * (NUM_PAD + 3), end="")

for x in range(X_LIMIT):
    if x % X_STEP == 0:
        print(
            str(
                round(x / X_SIZE)
            ).ljust(X_STEP),
            end=""
        )

print()

# ========== Separate ==========
for _ in range(SEP_COUNT):
    print()

# ========== Task 4 ============
NAME_IN_RANGE = "BEHIND -3 AND 3"
NAME_OTHER = "OTHER"
NAME_PAD = 16

X_RANGE = 90
X_STEP = 5

nums_in_range = 0
other_nums = 0


def number_filter(number):
    return -3 <= number <= 3


with open("sequence.txt", encoding="UTF-8") as sequence:
    for line in sequence.readlines():
        x = float(line.strip())
        if number_filter(x):
            nums_in_range += 1
        else:
            other_nums += 1


cf = X_LIMIT / max(nums_in_range, other_nums)

print(" " * NAME_PAD, "|")
print(NAME_IN_RANGE.rjust(NAME_PAD), "|", f"{RED}{' ' * round(cf * nums_in_range)}{END}")
print(" " * NAME_PAD, "|")
print(NAME_OTHER.rjust(NAME_PAD), "|", f"{RED}{' ' * round(cf * other_nums)}{END}")
print(" " * NAME_PAD, "|")
print(" " * NAME_PAD, "|=", end="")

for x in range(X_LIMIT + NUM_PAD):
    if x % X_STEP == 0:
        print("|", end="")
    else:
        print("=", end="")

print()
print(" " * (NAME_PAD + 3), end="")

for x in range(X_LIMIT + NUM_PAD):
    if x % X_STEP == 0:
        print(
            str(
                round(x / cf)
            ).ljust(X_STEP),
            end=""
        )

print()
