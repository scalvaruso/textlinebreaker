import os

def main():

    text = [("hello",36,47),
            "",
            "this is an example of textlinebreaker",
            "",
            "next line is 6 characters:", "123456",
            "next line is 12 characters:", "123456789012",
            "next line is 25 characters:", "1234567890123456789012345",
            "next line is 50 characters:", "12345678901234567890123456789012345678901234567890",
            "next line is 100 characters:", "1234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890",
            "next word is 100 characters: 1234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890",
            "next line is 150 characters:",
            "123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890",
            "next line is 200 characters:",
            "12345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890",
            "",
            "one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen twenty",
            ""
            ]

    terminal_width = os.get_terminal_size().columns
    #max_width = int(2* terminal_width / 3)
    #max_width = terminal_width - 20
    max_width = terminal_width
    max_width = 100

    menu_list = []
    
    for item in text:
        
        t_colour = 0
        t_background = 0

        # Check if item is a tuple.
        if isinstance(item, tuple):
            """
            If True:
            item[0] is the string
            item[1] is the colour of the text
            item[2] is the backgroud colour of the text.
            """
            words = item[0].split(" ")
            
            if item[1] != "":
                #text_colour = _valid_colour(item[1])
                text_colour = item[1]
            else:
                text_colour = t_colour    
            try:
                #text_background = _valid_colour(item[2], "back")
                text_background = item[2]
            except:
                text_background = t_background
                pass

        else:
            words = item.split(" ")
            text_colour = t_colour
            text_background = t_background

        for line in split_line(words, max_width, alignment="centre"):
            menu_list.append((line,text_colour,text_background))
            
    #to_print = split_line(text, max_length)

    for item in menu_list:
        print(f"\033[{item[2]}m\033[{item[1]}m{item[0]}\033[0m")

    print(f"Terminal width={terminal_width}\nLine max lenght={max_width}")


def split_line(line, max_width, alignment="left"):

    new_list = []
    new_line = ""
    space = " "
    #adjustment = "{:^50}"
    if alignment.lower() == "right":
        positioning = "{:>"
    elif alignment.lower()=="centre" or alignment.lower()=="center":
        positioning = "{:^"
    else:
        positioning = "{:<"
    adjustment = positioning + f"{max_width}" + "}"
    
    # Split the lines if they are longer than the max length characters.
    
    if line == [""]:
        new_list.append(" "*max_width)

    for word in line:
        word = word.replace("\t", "    ")
        
        if len(new_line+word) < (max_width+1):
            new_line += word + space

        else:
            if len(word) >= max_width:

                remaining_width = max_width - len(new_line)
                new_line += word[:remaining_width] + space
                word = word[remaining_width:]
                #new_line = adjustment.format(new_line.rstrip(" "))    #Test alignement
                new_list.append(adjustment.format(new_line.rstrip(" ")))

                while len(word) >= max_width:
                    new_line = word[:max_width] + space
                    word = word[max_width:]
                    #new_line = adjustment.format(new_line.rstrip(" "))    #Test alignement
                    new_list.append(adjustment.format(new_line.rstrip(" ")))
                new_line = word + space

            else:
                #new_line = adjustment.format(new_line.rstrip(" "))    #Test alignement
                new_list.append(adjustment.format(new_line.rstrip(" ")))
                new_line = word + space
    
    if new_line != " ":
        #new_line = adjustment.format(new_line.rstrip(" "))    #Test alignement
        new_list.append(adjustment.format(new_line.rstrip(" ")))
        
    return new_list


if __name__ == "__main__":
    main()