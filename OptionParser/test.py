import OptionParser
# if option doesn't exist in parsed arguments raise option error
OptionParser.options.set_option('keywords', str, required=False)
OptionParser.options.set_option('index', int, required=False)
OptionParser.options.set_option('flag', bool, required=False)
OptionParser.options.set_option('test', str, required=False)

def main(): 
    for k, v in OptionParser.options.get_options():
        key, value = k, v
        print(key, ' : ', value)
        
    
if __name__ == '__main__':
    main()