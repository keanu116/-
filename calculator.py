import sys
import pygame as pg

#display data
SCREEN_SIZE = (600, 820)
SCREEN = pg.display.set_mode(SCREEN_SIZE)

#button data
button_DATA = [] #pg.rect
button_prog_DATA = []
button_color_DATA = []
button_coordinates_DATA = []
selected_button_DATA = [True, True, None] #[button_pressed, display_answer, coordinates]

#text data
text_SIZE = 80
text_coordinates_DATA = []
text_DATA = [["7", "8", "9", "+"],
             ["4", "5", "6", "-"],
             ["1", "2", "3", "*"],
             ["A", "0", "=", "/"],]

text_display = []
text_display_answer = []

dpl_text_size = [80]

#joke
JOKE = True

def DISPLAY():
    rect1 = pg.Rect(10, 10, 580, 200)
    rect2 = pg.Rect(10, 220, 580, 580)

    # layout
    pg.draw.rect(surface= SCREEN, color= (30, 30, 30), rect= rect1)
    pg.draw.rect(surface= SCREEN, color= "white", rect= rect1, width= 2)

    pg.draw.rect(surface=SCREEN, color=(30, 30, 30), rect=rect2)
    pg.draw.rect(surface=SCREEN, color="white", rect=rect2, width=2)

    text = ""
    if selected_button_DATA[1] == True:
        text = "".join(text_display)

    elif selected_button_DATA[1] == False:
        text = text_display_answer[0]

    font = pg.font.SysFont("hg正楷書体pro", dpl_text_size[0])
    text1 = font.render(text,True, "white")
    SCREEN.blit(text1, (20, 60))

def draw_text():
    font1 = pg.font.SysFont("hg正楷書体pro", text_SIZE)

    for i in range(4):
        for j in range(4):
            text1 = font1.render(text_DATA[i][j], True, "white")
            SCREEN.blit(text1, text_coordinates_DATA[i][j])

def program():
    operator = [[0, 3], [1, 3], [2, 3], [3, 3]]
    equal = [3, 2]
    Ac = [3, 0]

    dpl_text_size[0] = 80

    if selected_button_DATA[0] == True:
        row = selected_button_DATA[2][0]
        col = selected_button_DATA[2][1]

        if selected_button_DATA[2] == equal:

            if len(text_display) == 3 and JOKE == True:
                dpl_text_size[0] = 30
                text_display.clear()
                text_display_answer.clear()
                text_display_answer.append("そんくらい自分で計算しろ、バーカ！！！")
                selected_button_DATA[1] = False

            else:
                try:
                    calc = "".join(text_display)

                except:
                    pass

                try:
                    answer = eval(calc)

                except:
                    text_display.clear()
                    text_display.append(["ERROR"])
                    selected_button_DATA[1] = False

                else:
                    text_display.clear()
                    text_display_answer.clear()
                    text_display_answer.append(f"{answer:<.6f}")
                    selected_button_DATA[1] = False


        elif selected_button_DATA[2] in operator:
            if text_display == []:
                pass

            elif text_display[len(text_display) - 1] in ["+", "-", "*", "/"]:
                pass

            else:
                text_display.append(text_DATA[row][col])

        elif selected_button_DATA[2] == Ac:
            text_display.clear()

        else:
            text_display.append(text_DATA[row][col])

        print(text_display)

def create_button(BUTTON_DATA):
    #grid square size
    sep = 5
    button = []
    color = []

    preset = [0, 210]

    SQRSIZE = ((580 - sep)/4)-sep

    # print("BUTTON DATA", "", button)
    # print("COLOR DATA", "" ,color)

    if BUTTON_DATA == True:
        for i in range(4):
            button_rows = []
            button_rows1 = []
            for j in range(4):
                rect_button = pg.Rect(button_coordinates_DATA[i][j][0], button_coordinates_DATA[i][j][1], SQRSIZE, SQRSIZE)
                rect_size_nocode = (button_coordinates_DATA[i][j][0], button_coordinates_DATA[i][j][1], SQRSIZE, SQRSIZE)

                button_rows.append(rect_size_nocode)
                button_rows1.append(rect_button)

            button_DATA.append(button_rows)
            button.append(button_rows1)

        return button

    else:  # ignore error
        for row in range(4):
            for col in range(4):
                pg.draw.rect(SCREEN, button_color_DATA[row][col], button_DATA[row][col])
                pg.draw.rect(SCREEN, "white", button_DATA[row][col], 2)
                return None
            return None
        return None

def draw_button(BUTTON_DATA, BUTTON_COLOR_DATA):
    for i, j in zip(BUTTON_DATA, BUTTON_COLOR_DATA):
        for k, l in zip(i, j):
            pg.draw.rect(SCREEN, l, k)
            pg.draw.rect(SCREEN, "white", k, 2)

def button_event(event, button_data):

    for button_row, coordinates_row in zip(button_data, button_prog_DATA):

        for button, coord in zip(button_row, coordinates_row):

            if button.collidepoint(pg.mouse.get_pos()):
                button_color_DATA[coord[0]][coord[1]] = (100, 100, 100)

                if event.type == pg.MOUSEBUTTONDOWN:
                    if selected_button_DATA[1] == False:
                        text_display.clear()

                    selected_button_DATA[1] = True
                    selected_button_DATA[2] = coord

                    print(selected_button_DATA)
                    button_color_DATA[coord[0]][coord[1]] = (255, 255, 255)

                    program()
                    selected_button_DATA[0] = False

                elif event.type == pg.MOUSEBUTTONUP:
                    selected_button_DATA[0] = True

                    print(selected_button_DATA)

                    button_color_DATA[coord[0]][coord[1]] = (60, 60, 60)

            else:
                button_color_DATA[coord[0]][coord[1]] = (60, 60, 60)

def coordinates_color():
    sep = 5
    preset = [0, 210]

    SQRSIZE = ((580 - sep)/4)-sep
    text_allign = (SQRSIZE - text_SIZE)/2

    if text_allign < 0:
        print("text_size too big")
        sys.exit()

    for i in range(4):
        button_rows = []
        button_prog_rows = []
        text_rows = []
        color_rows = []
        for j in range(4):
            rect_coordinates = ((10 + sep) + j * (SQRSIZE + sep) + preset[0],
                                (10 + sep) + i * (SQRSIZE + sep) + preset[1])

            button_prog_coordinates = [i, j]

            text_coordinates = ((10 + sep) + j * (SQRSIZE + sep) + preset[0] + text_allign,
                                (10 + sep) + i * (SQRSIZE + sep) + preset[1] + text_allign)

            button_rows.append(rect_coordinates)
            button_prog_rows.append(button_prog_coordinates)
            text_rows.append(text_coordinates)
            color_rows.append((60, 60, 60))

        button_color_DATA.append(color_rows)
        button_coordinates_DATA.append(button_rows)
        button_prog_DATA.append(button_prog_rows)
        text_coordinates_DATA.append(text_rows)

def main():
    pg.init()
    coordinates_color()
    Buttons1 = create_button(True)
    print(Buttons1, "\n")
    print(button_coordinates_DATA, "\n")
    # print(button_color_DATA, "\n")


    while True:
        SCREEN.fill((60, 60, 60))
        DISPLAY()
        draw_button(button_DATA, button_color_DATA)
        draw_text()

        #events
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()

            button_event(event, Buttons1)

        pg.display.update()

if __name__ == '__main__':
    main()