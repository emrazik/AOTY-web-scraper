import options
import sys

FUNCTIONS = {'AS' : options.album_search,
             'YS' : options.top_albums_all_time}

MAP_REQUIRE = {'AS' : ['artist', 'album'],
               'YS' : ['year']}

class TextColors:
    GREEN = '\u001b[32m'
    YELLOW = '\u001b[33m'
    RED = '\u001b[31m'
    END = '\u001b[0m'

def handle_text_color(score):
    if score == 'NR':
        return TextColors.END
    else:
        score = int(score)

    if score > 70:
        return TextColors.GREEN
    elif score > 50:
        return TextColors.YELLOW
    else:
        return TextColors.RED

def handle_search_function(args, arg_dict):
    # find which search function to run
    for key in arg_dict:
        if arg_dict[key]:
            run_func = FUNCTIONS[key]
            # check if the required arguments have been provided
            if not check_required_args(arg_dict, key):
                sys.exit()
            break

    run_func(args)

def check_required_args(arg_dict, key):
    check_list = MAP_REQUIRE[key]
    for arg in check_list:
        if arg_dict[arg] == None:
            print("Error: you are missing at least one of the following arguments: " + ", ".join(check_list))
            print("Specify these arguments with: ", end="")
            for word in check_list:
                print("--" + word, end=" ")
            print() 

            return False

    return True
