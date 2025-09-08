from pyfiglet import Figlet
import random
import sys

#create a figlet object, everything needed to perform figlet operations is stored inside the figlet object.
figlet = Figlet( )

#get a list of all the fonts inside figlet
fonts = figlet.getFonts()

#check if there are no extra words in the command line and pic a random font from the list
if len(sys.argv) == 1:
    font_name = random.choice(fonts)

#ensure that the font in the command line is given with -f or --font in the beginning of the font name
elif len(sys.argv) == 3 and sys.argv[1] in ['-f','--font']:
    font_name = sys.argv[2]
    if font_name not in fonts:
        sys.exit("Invalid font")
else:
        sys.exit("Font not found")

figlet.setFont(font=font_name)

phrase = input("Input: ")

print("Output: ")
print(figlet.renderText(phrase))