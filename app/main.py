#!/usr/bin/env python3
def main(argv):
    for v in argv:
        print(v)

    result = []
    colors = ["w", "b", "g", "r"] 
    for 1_1_color in colors:
        for 1_2_color in colors:
            for 2_color in colors:
                for 3_color in colors:
                    for 5_color in colors:
                        blue = 0
                        if 1_1_color == "b":
                            blue += 1
                        if 1_2_color == "b":
                            blue += 1
                        if 2_color == "b":
                            blue += 2
                        if 3_color == "b":
                            blue += 3
                        if 5_color == "b":
                            blue += 5

                        green = 0
                        if 1_1_color == "g":
                            green += 1
                        if 1_2_color == "g":
                            green += 1
                        if 2_color == "g":
                            green += 2
                        if 3_color == "g":
                            green += 3
                        if 5_color == "g":
                            green += 5

                        red = 0
                        if 1_1_color == "r":
                            red += 1
                        if 1_2_color == "r":
                            red += 1
                        if 2_color == "r":
                            red += 2
                        if 3_color == "r":
                            red += 3
                        if 5_color == "r":
                            red += 5

                        hour = blue + green
                        minute = (green + red) * 5

                        if argv[0] == hour and argv[1] == minute:
                            string = 1_1_color + 1_2_color + 2_color + 3_color + 5_color
                            result.append(string)
                          

    print(result)
