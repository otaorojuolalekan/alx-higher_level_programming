#!/usr/bin/python3

if __name__ == "__main__":
    import hidden_4

args = dir(hidden_4)

for arg in args:
    if not(arg.startswith("__")):
        print(arg)
