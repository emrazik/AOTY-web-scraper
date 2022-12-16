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