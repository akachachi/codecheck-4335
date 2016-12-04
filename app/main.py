#!/usr/bin/env python3
def main(argv):

    #入力が10進数ではなかった場合,先頭に0がある場合
    if argv[0][0] == "0" and len(argv[0][0]) != 1:
        print("rrrrr")
        return

    if argv[1][0] == "0" and len(argv[1][0]) != 1:
        print("rrrrr")
        return
    
    arg_hour = int(argv[0])
    arg_minute = int(argv[1])

    if arg_hour < 0 or arg_hour > 12:
        print("rrrrr")
        return

    #5分刻みではない場合
    if arg_minute%5 != 0 and arg_minute != 0:
        print("rrrrrr")
        return

    #0~55ではない場合
    if arg_minute/5 < 0 or arg_minute/5 > 12:
        print("rrrrr")
        return

    result = []
    colors = ["w", "b", "g", "r"] 
    for color_1_1 in colors:
        for color_1_2 in colors:
            for color_2 in colors:
                for color_3 in colors:
                    for color_5 in colors:
                        blue = 0
                        if color_1_1 == "b":
                            blue += 1
                        if color_1_2 == "b":
                            blue += 1
                        if color_2 == "b":
                            blue += 2
                        if color_3 == "b":
                            blue += 3
                        if color_5 == "b":
                            blue += 5

                        green = 0
                        if color_1_1 == "g":
                            green += 1
                        if color_1_2 == "g":
                            green += 1
                        if color_2 == "g":
                            green += 2
                        if color_3 == "g":
                            green += 3
                        if color_5 == "g":
                            green += 5

                        red = 0
                        if color_1_1 == "r":
                            red += 1
                        if color_1_2 == "r":
                            red += 1
                        if color_2 == "r":
                            red += 2
                        if color_3 == "r":
                            red += 3
                        if color_5 == "r":
                            red += 5

                        hour = blue + green
                        minute = (green + red) * 5

                        if int(argv[0]) == hour and int(argv[1]) == minute:
                            string = color_1_1 + color_1_2 + color_2 + color_3 + color_5
                            result.append(string)
                          
    result = sorted(result)
    print(result[0])
