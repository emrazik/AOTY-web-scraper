import argparse
import options
import sys


FUNCTIONS = {'-AS'}

def console_output():
    pass

def console_output_verbose():
    pass

def main():
    parser = argparse.ArgumentParser(description='Search for information on albumoftheyear.com')
    parser.add_argument('-AS', action='store_true', help='Search for an album')
    parser.add_argument('-ar', '--artist', type=str, required=any(func in sys.argv for func in FUNCTIONS), help='Name of a musical artist', metavar='')
    parser.add_argument('-al', '--album', type=str, required=any(func in sys.argv for func in FUNCTIONS), help='Name of an album', metavar='')
    args = parser.parse_args()

    if args.AS:
        options.album_search(args)
 
if __name__ == "__main__":
    main()








