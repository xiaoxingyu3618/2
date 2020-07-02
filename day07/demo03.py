"""

    for r in range(4):
        for c in range(r + 1):
            print("*", end="")
    print()
"""

def print_rectangle():
    """
    尽量让适用范围越广
    :return:
    """
    for r in range(4):
        for c in range(r + 1):
            print("*", end="")
        print()


print_rectangle()