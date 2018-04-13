import sys

required_options = []
option_temp = []
    
    
def set_option(option: str, o_type: type, required: bool) -> bool:
    option_temp.append(option)
    required_options.append((option, o_type))
    
def get_options():
    
    # 
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

    
        
    
