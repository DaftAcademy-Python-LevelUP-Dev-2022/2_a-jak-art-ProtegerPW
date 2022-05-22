from functools import wraps


def greeter(func):
    @wraps(func)
    def inside_wrapper(*args):
        get_name = func(*args)
        return "Aloha " + get_name.lower().title()
        
    return inside_wrapper
        


def sums_of_str_elements_are_equal(func):
    pass


def format_output(*required_keys):
    pass


def add_method_to_instance(klass):
    pass
