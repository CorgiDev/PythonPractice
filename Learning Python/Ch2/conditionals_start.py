#
# Example file for working with conditional statements
#


def main():
    x, y = 1000, 1000

    # conditional flow uses if, elif, else
    if(x<y):
        st = "x is less than y"
    elif(x>y):
        st = "x is greater than y"
    elif(x==y):
        st = "x and y are the same value"

    print(st)

    # conditional statements let you use "a if C else b"
    st = "x is less than y" if (x<y) else "x is greater than or the same as y"
    print (st)

    # Use dictionary mapping to implement a switch case in Python (Source: https://www.guru99.com/if-loop-python-conditional-structures.html#8)
    def SwitchExample(arg):
        switcher = {
            0: "This is Case Zero ",
            1: "This is Case One ",
            2: "This is Case Two ",
        }
        return switcher.get(arg, "nothing")

    print (SwitchExample(1))

if __name__ == "__main__":
    main()
