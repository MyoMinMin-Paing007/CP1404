
HEX_COLORS = {"blueviolet": "#8a2be2", "cadetblue": "#5f9ea0", "carnelian": "#b31b1b", "darksalmon": "#e9967a", "floralwhite": "#fffaf0",
              "goldenrod": "#daa520", "iceberg": "#71a6d2", "keppel": "#3ab09e", "limegreen": "#32cd32", "midnightBlue": "#191970"}
print(HEX_COLORS)
hex_color = input("Enter color name: ").lower()
while hex_color != "":
    try:
        print(hex_color, "is", HEX_COLORS[hex_color])
    except KeyError:
        print("Invalid short state")
    hex_color = input("Enter color name:  ").lower()