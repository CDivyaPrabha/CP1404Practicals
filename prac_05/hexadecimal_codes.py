COLOR_CODES = {"WHITE": "#FFFFFF", "SILVER": "#C0C0C0", "AQUA": "#00FFFF", "BLACK": "#000000", "RED": "#FF0000",
               "MAROON": "#800000", "YELLOW": "#FFFF00", "OLIVE": "#808000", "LIME": "#00FF00", "PURPLE": "#800080"}
color_name = input("Enter a color name: ").upper()
while color_name != "":
    if color_name in COLOR_CODES:
        print(color_name, " is ", COLOR_CODES[color_name])
    else:
        print("Invalid color name")
    color_name = input("Enter a color name: ").upper()