def main():
    items = {}

    while True:
        try:
            item = input().strip().upper()
            if item:  
                items[item] = items.get(item, 0) + 1
        except EOFError:
            break
    
    for item in sorted(items):
        print(f"{items[item]} {item}")

if __name__ == "__main__":
    main()