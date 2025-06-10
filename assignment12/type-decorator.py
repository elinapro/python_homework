def type_decorator(type_of_output):
    def decorator(func):
        def wrapper(*args, **kwargs):
            x = func(*args, **kwargs)
            return type_of_output(x)
        return wrapper
    return decorator

# 3


@type_decorator(str)
def return_int():
    return 5

# 4


@type_decorator(int)
def return_string():
    return "not a number"

# 5 mainline


if __name__ == "__main__":
    y = return_int()
    print(type(y).__name__)  # This should print "str"
    try:
        y = return_string()
        print("shouldn't get here!")
    except ValueError:
        # This is what should happen
        print("can't convert that string to an integer!")
