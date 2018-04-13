"""option module documentation

Example:
    This example demonstrates how to use OptionParser. By importing OptionParser 
    you are given the ability to set multiple options for the .py file and apply
    required data types to the option values - parameters::

        import OptionParser
        OptionParser.options.set_option('arg', str, required=False)
        print(OptionParser.options.get_options())


Attributes:
    required_options (list): Module level list type variable that hold developers
        required option(s), and option param data type. The list elements are wrapped in
        a tuple object for example: [(option, param(s))]
        
    option_temp (list): Module level variable

Todo:
    * set_option(option: str, o_type: type, [required: bool]) add required argument
    that flags the option as a required option the must be defined or not required.
    
    * Create InvalidOption class to handle unknown parsed options from user and provide 
    appropriate prompts.
    
    * add option message suggesting help message --help if help option is enabled.
    
    * find better solutions for processing the raw system arguments 


"""

import sys

required_options = []
option_temp = []
    
    
def set_option(option: str, o_type: type, required: bool) -> bool:
    """This will append all the function arguments parameters 
    to the required_options list. Types, Arguments and function return type are
    Documented in this docstring.
    
    Args:
        option (str): An option set by developer 
        represented by character or word with '--' notation - prefix. 
        For example [OPTION: --arg] [VALUE: param] i.e --arg param.
        
        o_type (type): The data type needed for the required option. 
        for example --arg 'param' where param is string type object, and --args 1 2 3 
        values are int type objects.
        
        required (bool): third parameter. TODO
    Returns:
        Void

    """
    option_temp.append(option)
    required_options.append((option, o_type))
    
def get_options():
    """Example function with args, types, attributes, return types 
    and raise exceptions documented in the docstring.

    Args:
        None
        
    Attributes:
        sorted_sys_args (list):  The proposed options and values populated by user.
        options_list (list): The required options and values list after 
        discarding unknown options if any.
        
        args (list): the system arguments passed through with 
        file parameter striped away and split with option identifier '--' prefix.
        
    Returns:
        options_list (list): returns all successful required options in a list each item
        is wrapped in a tuple and each value is wrapped in a list type object
        i.e list(tuple(str(option), [value])) [(o, [v]), (o, [v])]
    
    Raises:
        ValueError: If `param2` is equal to `param1`.

    """
    sorted_sys_args = []
    options_list = []
    
    args = ' '.join(sys.argv[1:]).split('--')
    
    # x = list((map(lambda x: sorted_sys_args.append((x.split(' ')[0], x.split(' ')[1:] )), args)))
    for arg in args:
        option_type = arg.split(' ')[0]
        option_arg = arg[1:].split(' ')[1:]
        sorted_sys_args.append((option_type, option_arg))
        
    # Remove empty item at beginning of list [1:]
    sorted_sys_args = sorted_sys_args[1:]
    
    for k, v in sorted_sys_args:
        if k not in option_temp:
            print('Unknown Option Found --{0}. Exiting.'.format(k))
            sys.exit()
    # Loop
    for raw_option_type, raw_option_values in sorted_sys_args:
        # Remove spaces from raw values if any exist    
        for value in raw_option_values:
            if value == '':
                del raw_option_values[raw_option_values.index(value)] # Remove empty array white spaced items : del ''
        
    # Loop - Check if Required Options are in proposed options list
    for raw_option_type, raw_option_values in sorted_sys_args:
        for req_option, req_type in required_options:
            if req_option == raw_option_type:
                # print("Found Required Option: ", req_option)
        
                # Cast Values to appropriate data type
                def cast_type(x):
                    if req_type == str:
                        return str(x)
                    elif req_type == int:
                        return int(x)
                    elif req_type == bool:
                        return bool(x)
                
                params = list(map(cast_type, raw_option_values))
        
                # Append approved options and values to option list
                options_list.append((req_option, params))
                break
    
    return options_list

    
        
    
