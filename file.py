from functools import wraps


def greeter(func):
    @wraps(func)
    def inside_wrapper(*args):
        get_name = func(*args)
        return "Aloha " + get_name.lower().title()
        
    return inside_wrapper
        


def sums_of_str_elements_are_equal(func):
    @wraps(func)
    def inside_wrapper(*args):
        num_one, num_two = func(*args).split()
        sum_one, sum_two = 0, 0

        if(num_one[0] == '-'):
            sum_one = sum([int(c) for c in num_one[1:]])
        else:
            sum_one = sum([int(c) for c in num_one])
        
        if(num_two[0] == '-'):
            sum_two = sum([int(c) for c in num_two[1:]])
        else:
            sum_two = sum([int(c) for c in num_two])

        if(sum_one == sum_two):
            if(num_one[0] == '-' and num_two[0] == '-'):
                    return "-" + str(sum_one) + " == -" + str(sum_two)
            if(num_one[0] != '-' and num_two[0] != '-'):
                    return str(sum_one) + " == " + str(sum_two)
            if(num_one[0] != '-' and num_two[0] == '-'):
                    return str(sum_one) + " != -" + str(sum_two)
            if(num_one[0] == '-' and num_two[0] != '-'):
                    return "-" + str(sum_one) + " != " + str(sum_two)
        else:
            if(num_one[0] == '-'):
                if(num_two[0] == '-'):
                    return "-" + str(sum_one) + " != -" + str(sum_two)
                else:
                    return "-" + str(sum_one) + " != " + str(sum_two)
            else:
                if(num_two[0] == '-'):
                    return str(sum_one) + " != -" + str(sum_two)
                else:
                    return str(sum_one) + " != " + str(sum_two)
                    
    return inside_wrapper


                    

                
            
        


def format_output(*required_keys):
    pass


def add_method_to_instance(klass):
    pass
