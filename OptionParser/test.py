import OptionParser
# if option doesn't exist in parsed arguments raise option error
OptionParser.options.set_option('keywords', str, required=False)
OptionParser.options.set_option('index', int, required=False)
OptionParser.options.set_option('flag', bool, required=False)

def main(): 
    print(OptionParser.options.get())

if __name__ == '__main__':
    main()