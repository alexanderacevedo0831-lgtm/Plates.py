import inflect # pyright: ignore[reportMissingImports] # ignore Pylance warning about missing module

def names():
    names = []

    # Keep taking names until the user inputs a blank line
    while True:
        try:
            name = input()
            names.append(name)
        except EOFError:
            break

    # Format the output of names
    if len(names) == 0:
        return
    
    
    if len(names) == 1:
        print(f"Adieu, adieu, to {names[0]}")
    elif len(names) == 2:
        print(f"Adieu, adieu, to {names[0]} and {names[1]}")
    else:
        # Oxford comma: name1, name2 ..., and last
        print(f"Adieu, adieu, to {', '.join(names[:-1])}, and {names[-1]}")

if __name__ == "__main__":
    names()