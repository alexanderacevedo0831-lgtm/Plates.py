camel_case = input("camelCase: ")
snake_case = []
for i in range(len(camel_case)):
    if camel_case[i].isupper():
        snake_case.append("_" + camel_case[i].lower())
    else:
        snake_case.append(camel_case[i])
print("snake_case:" + "".join(snake_case))