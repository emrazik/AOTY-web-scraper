import argparse
import config

def main():
    # define the arguments for the parser
    parser = argparse.ArgumentParser(description='Search for information on albumoftheyear.com')
    parser.add_argument('-AS', action='store_true', help='Search for an album')
    parser.add_argument('-YS', action='store_true', help='Search for the top albums all time in a genre')
    parser.add_argument('-ar', '--artist', type=str, help='Name of a musical artist', metavar='')
    parser.add_argument('-al', '--album', type=str, help='Name of an album', metavar='')
    parser.add_argument('-y', '--year', type=str, help='Year or decade of albums (e.g. 2012 or 2010s)', metavar='')
    parser.add_argument('-c', '--critic', action='store_true', help='Use critic rating')
    parser.add_argument('-u', '--user', action='store_true', help='Use user rating')
    parser.add_argument('-v', '--verbose', action='store_true', help='increase output verbosity')
    args = parser.parse_args()

    arg_dict = vars(args)
    config.handle_search_function(args, arg_dict)

if __name__ == "__main__":
    main()








