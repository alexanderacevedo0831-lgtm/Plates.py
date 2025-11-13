import emoji # pyright: ignore[reportMissingImports] # ignore Pylance warning about missing module

def main():
    user_input = input().strip()
    output = emoji.emojize(user_input, language='alias')
    print(f'{output}')

if __name__ == "__main__":
    main()