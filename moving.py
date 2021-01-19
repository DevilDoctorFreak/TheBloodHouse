def move_char(x, y, click, border):
    side = ''
    if x != click[0]:
        if x > click[0]:
            for i in border:
                if (x - 5 >= i[0]) and x - 5 <= i[2]:
                    if (y + 5 >= i[1]) and y + 5 <= i[3]:
                        break
                    elif (y + 5 >= i[1]) and y + 5 <= i[3]:
                        break
            else:
                x = x - 5
                side = 'влево'

        elif x < click[0]:
            for i in border:
                if (x + 5 >= i[0]) and x + 5 <= i[2]:
                    if (y + 5 >= i[1]) and y + 5 <= i[3]:
                        break
                    elif (y + 5 >= i[1]) and y + 5 <= i[3]:
                        break
            else:
                x = x + 5
                side = 'вправо'

    elif y != click[1]:
        if y > click[1]:
            for i in border:
                if (y - 5 >= i[1]) and y - 5 <= i[3]:
                    if (x + 5 >= i[0]) and x + 5 <= i[2]:
                        break
                    elif (x - 5 >= i[0]) and x - 5 <= i[2]:
                        break
            else:
                y = y - 5
                side = 'вверх'

        elif y < click[1]:
            for i in border:
                if (y + 5 >= i[1]) and y + 5 <= i[3]:
                    if (x + 5 >= i[0]) and x + 5 <= i[2]:
                        break
                    elif (x - 5 >= i[0]) and x - 5 <= i[2]:
                        break
            else:
                y = y + 5
                side = 'вниз'
        elif x == click[0] and y == click[1]:
            x, y = x, y

    return x, y, side
