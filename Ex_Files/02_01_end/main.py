RUN_INDENTED = True

message = "running unindented1"

if RUN_INDENTED:
    message = "running indented"

print(message)


def my_function():
    greet = "Hello"
    return greet


print(my_function())
