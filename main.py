import argparse
import options
import sys

FUNCTIONS = {'AS' : options.album_search,
             'TA' : options.top_albums_all_time}

def main():
    # define the arguments for the parser
    parser = argparse.ArgumentParser(description='Search for information on albumoftheyear.com')
    parser.add_argument('-AS', action='store_true', help='Search for an album')
    parser.add_argument('-TS', action='store_true', help='Search for the top albums all time in a genre')
    parser.add_argument('-ar', '--artist', type=str, required=any(func in sys.argv for func in FUNCTIONS), help='Name of a musical artist', metavar='')
    parser.add_argument('-al', '--album', type=str, required=any(func in sys.argv for func in FUNCTIONS), help='Name of an album', metavar='')
    parser.add_argument('-v', '--verbose', help='increase output verbosity', action='store_true')
    args = parser.parse_args()

    # find which search function to run
    arg_dict = vars(args)
    for key in arg_dict:
        if arg_dict[key]:
            run_func = FUNCTIONS[key]
            break

    run_func(args)

if __name__ == "__main__":
    main()








