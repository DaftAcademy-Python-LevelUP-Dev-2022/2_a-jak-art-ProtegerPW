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
    def real_wrapper(func):
        def insider_wrapper(*args):
            got_dict = func(*args)
            
            list_of_keys = []
            for record in required_keys:
                for result in record.split('__'):
                    list_of_keys.append(result)
                    
            list_of_values = []
            help_dict = {}
            for key in list_of_keys:
                if(key in got_dict):
                    dict_value = got_dict.get(key)
                    if dict_value == '':
                        help_dict[key] = "Empty value"
                    else:
                       help_dict[key] = dict_value
                else:
                    raise ValueError
            
            help_list = [record.split('__') for record in required_keys]
            response_dict = {}
            
            for record in help_list:
                if len(record) > 1:
                    value_list = [help_dict.get(key) for key in record]
                    response_dict['__'.join(record)] = ' '.join(value_list)
                else:
                    response_dict[record[0]] = help_dict.get(record[0])
                    
            return response_dict                  
        return insider_wrapper
    return real_wrapper
        


def add_method_to_instance(klass):
    pass
