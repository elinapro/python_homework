import logging
from functools import wraps

logger = logging.getLogger(__name__ + "_parameter_log")
logger.setLevel(logging.INFO)
logger.addHandler(logging.FileHandler("./decorator.log", "a"))

# decorator


def logger_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        pos = list(args) if args else "none"
        kw = kwargs if kwargs else "none"
        logger.info(
            f"function: {func.__name__} | "
            f"positional parameters: {pos} | "
            f"keyword parameters: {kw} | "
            f"return: {result}"
        )
        return result
    return wrapper


# no params, no return
@logger_decorator
def say_hello():
    print("Hello, World!")

# variable num of positional arguments


@logger_decorator
def always_true(*args):
    return True

# no positional args, variable keyword args, return nothing


@logger_decorator
def show_keywords(**kwargs):
    pass


# mainline code
if __name__ == "__main__":
    say_hello()
    always_true(1, 2, 3)
    show_keywords(a=10, b=20)
