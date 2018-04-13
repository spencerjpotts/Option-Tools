"""Example of Python-Tools/OptionParser.

This module demonstrates the usage of OptionParser

Example:
    Example here demonstrates how to define options using '--' prefix.
    
        $ python test.py --arg param --args foo bar

Todo:
    * Create OptionError Exception class for unknown option being passed.

"""
import OptionParser


OptionParser.options.set_option('arg', str, required=False)
OptionParser.options.set_option('args', str, required=False)


def main(): 
    for k, v in OptionParser.options.get_options():
        option, values = k, v
        print(option, ' : ', values)
        
    
if __name__ == '__main__':
    main()