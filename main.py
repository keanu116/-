import sys
import numpy as np
import pygame as pg
import csv

#button diff
#0=4x4, 1=6x6, 2=8x8, 3=10x10

def read_csv(name):
    with open(name, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            print(*row)

def write_csv(name, matrix):
    with open(name, 'w', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(matrix)

def overwrite_csv(name, matrix, coordinates, DATA):
    with open(name, 'w', encoding='utf-8') as file:
        writer = csv.writer(file)

def EXECUTE(INPUT):
    if INPUT == '':
        print()

def Layout(SCREEN):
    #rect1
    r1SIZE = (10,10,580,580)
    pg.draw.rect(SCREEN,(30,30,30),r1SIZE)
    pg.draw.rect(SCREEN, (255, 255, 255), r1SIZE, 2)

    #rect2
    r2SIZE = (600,10,390,580)
    pg.draw.rect(SCREEN,(30,30,30),r2SIZE)
    pg.draw.rect(SCREEN, (255, 255, 255), r2SIZE, 2)

def create_button(SCREEN, diff, BUTTON_DATA):
    #grid square size
    num_list = {0:4, 1:6, 2:8, 3:10}
    num = num_list[diff]
    sep = 5
    button = []
    color = []

    SQRSIZE = ((580 - sep)/num)-sep

    for i in range(num):
        button_rows = []
        color_rows = []
        for j in range(num):
            rectsize = pg.Rect( (10+sep) + j*(SQRSIZE + sep),
                                (10+sep) + i*(SQRSIZE + sep),
                                SQRSIZE,
                                SQRSIZE )

            button_rows.append(rectsize)
            color_rows.append((60, 60, 60))

        button.append(button_rows)
        color.append(color_rows)

    write_csv("BUTTON.csv", button)
    write_csv("COLOR.csv", color)

    if BUTTON_DATA == True:
        return button

    else: #ignore error
         for i in range(num):
            for j in range(num):
                pg.draw.rect(SCREEN, color[i][j], button[i][j])
                pg.draw.rect(SCREEN, "white", button[i][j], 2)

def main():
    pg.init()

    SCREEN_SIZE = (1000, 600)
    SCREEN = pg.display.set_mode(SCREEN_SIZE)
    BUTTON_DATA = create_button(SCREEN, 0, True)
    print(BUTTON_DATA)

    while True:
        pg.display.update()
        Layout(SCREEN)
        create_button(SCREEN, 0, False)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

            if event.type == pg.MOUSEBUTTONDOWN:
                for button_row in BUTTON_DATA:
                    for button in button_row:
                        if button.collidepoint(event.pos):
                            print(button)



if __name__ == "__main__":
    main()

