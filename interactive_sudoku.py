from tkinter import *
from sudoku import *
import random, copy, time

class Box():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.value = 0
        self.length = 55
        self.empty = True
        self.selected_box_value = 0
        self.selected_box_x = 0
        self.selected_box_y = 0

    def highlight_box(self):
        if self.x >= 0 and self.x < 168:
            XBORDER = 3
        elif self.x >= 168 and self.x < 336:
            XBORDER = 5
        elif self.x >= 336 and self.x <= 504:
            XBORDER = 7
        if self.y >= 0 and self.y < 168:
            YBORDER = 3
        elif self.y >= 168 and self.y < 336:
            YBORDER = 5
        elif self.y >= 336 and self.y <= 504:
            YBORDER = 7
        highlight = mycanvas.create_rectangle(self.x + XBORDER, self.y + YBORDER, self.x + 57, self.y + 57, fill='#e8f4f8', outline='#D3D3D3', tags='rect')

def highlight_wrong_box(x, y):
    if x >= 0 and x < 168:
        XBORDER = 3
    elif x >= 168 and x < 336:
        XBORDER = 5
    elif x >= 336 and x <= 504:
        XBORDER = 7
    if y >= 0 and y < 168:
        YBORDER = 3
    elif y >= 168 and y < 336:
        YBORDER = 5
    elif y >= 336 and y <= 504:
        YBORDER = 7
    highlight = mycanvas.create_rectangle(x + XBORDER, y + YBORDER, x + 57, y + 57, fill='#ffcccb', outline='#D3D3D3', tags='rect')


def display_num(value, x, y):
    num_label = Label(mycanvas, text=str(value), bg='white', fg='black', font='none 16 bold')
    num_label.place(x=x, y=y)
    check_if_done()

def display_coordinates(event):
    for i, box in enumerate(boxlist):
        if event.x > box.x and event.x < box.x + 56 and event.y > box.y and event.y < box.y + 56:
            mycanvas.delete('rect')
            for temp_box in boxlist:
                temp_box.selected_box_value = solution_boxlist[i].value
                temp_box.selected_box_x = solution_boxlist[i].x
                temp_box.selected_box_y = solution_boxlist[i].y
            if box.empty:
                box.highlight_box()

def click():
    guess = textentry.get()
    global full_boxes
    if guess not in ['1','2','3','4','5','6','7','8','9']:
        display_error_message()
        highlight_wrong_box(boxlist[0].selected_box_x, boxlist[0].selected_box_y)
        return
    elif int(guess) == boxlist[0].selected_box_value:
        display_num(boxlist[0].selected_box_value, boxlist[0].selected_box_x + 18, boxlist[0].selected_box_y + 16)
        mycanvas.delete('rect')
        textentry.delete(0, END)
        message_canvas.delete('rect')
        full_boxes += 1
    else:
        textentry.delete(0, END)
        display_error_message()
        highlight_wrong_box(boxlist[0].selected_box_x, boxlist[0].selected_box_y)

def display_error_message():
    message = message_canvas.create_text(0, 8, text='Incorrect, try again', fill='black', font='none 12 bold', tags='rect', anchor=NW)
    message_canvas.update()

def check_if_done():
    global full_boxes
    if full_boxes >= 81:
        Stop()


h=0; m=0; s=0; ms=0
stop_flag=False
reset_txt=f"00:00:00:00"
def clock_run():
    global h, m, s, ms
    if not stop_flag:
        clock_lbl['text']=f"{h:02}:{m:02}:{s:02}:{abs(ms):02}"
        ms+=10
        if ms == 100:
            s+=1; ms= 0
        elif s == 60:
            m+=1; s=0
        elif m == 60:
            h+=1; m=0
        window.after(100, clock_run)

def  Start():
    global stop_flag
    stop_flag=False
    clock_run()

def Stop():
    global stop_flag
    stop_flag=True
    clock_run()

window = Tk()
window.title('Sudoku!')
window.geometry('700x800')
window.configure(background='white')
photo1 = PhotoImage(file='blank-sudoku-grid.png')
mycanvas = Canvas(window, width=500, height=500)
mycanvas.pack()
mycanvas.create_image(0, 0, image=photo1, anchor=NW)
mycanvas.bind('<Button-1>', display_coordinates)
mycanvas.place(x=100, y=100)
message_canvas = Canvas(window, width=400, height=30, bg='white', highlightthickness=0)
message_canvas.place(x=105, y=720)

txt = Label(window, text='Select square above and enter number:', bg='white', fg='black', font='none 12 bold')
txt.place(x=100, y=620)
textentry = Entry(window, width=5, bg='white')
textentry.place(x=105, y=650)
button = Button(window, text='CHECK', width=14, command=click)
button.place(x=105, y=680)

clock_lbl = Label(master=window, height=2, width=10, text=reset_txt,bg= '#0059b3', fg="white",font=(None, 20))
clock_lbl.pack(side = TOP, fill=X , expand=False)
Start()

full_boxes = 0

puzzle1 = [[0,8,0,0,0,2,5,0,6], [4,0,5,0,0,0,9,0,0], [2,0,0,0,1,8,0,3,0], [0,6,9,0,5,0,8,0,0], [0,0,0,0,0,6,1,5,7], [3,0,0,0,2,1,6,0,9], [0,7,5,9,0,0,0,0,0], [0,3,0,6,0,2,0,0,0], [9,6,0,0,5,0,7,0,2]]
puzzle2 = [[6,4,0,5,0,1,0,0,0], [0,3,0,0,7,0,0,0,0], [0,0,7,9,0,0,0,1,0], [0,0,4,0,8,0,0,0,0], [9,0,8,0,0,3,4,0,0], [0,6,0,0,2,0,0,0,0], [4,0,0,2,0,8,7,5,0], [1,5,7,3,0,0,0,0,0], [0,3,0,0,4,0,0,9,6]]
puzzle3 = [[6,0,0,8,0,1,0,7,5], [1,0,0,0,9,0,0,8,4], [0,0,2,0,0,0,0,0,0], [4,3,0,5,1,8,0,9,6], [0,2,0,7,0,0,4,1,0], [5,6,1,4,0,9,3,0,0], [0,0,0,0,6,0,7,0,2], [0,7,0,0,3,1,5,4,0], [0,0,0,0,5,0,6,0,3]]
puzzle4 = [[5,1,9,7,2,4,0,0,0], [0,0,0,9,0,0,2,5,4], [4,3,0,0,0,0,9,0,0], [1,7,0,0,0,0,0,0,3], [0,4,0,0,9,0,0,0,6], [2,0,6,0,0,3,0,8,0], [0,0,1,0,0,0,0,9,0], [4,7,0,5,0,8,0,6,0], [0,6,0,1,2,0,3,0,4]]
puzzle5 = [[0,0,0,4,5,1,9,8,2], [0,0,5,0,0,2,0,0,0], [4,0,9,3,0,0,5,6,1], [6,0,7,0,0,3,5,0,0], [0,0,0,4,6,0,2,8,7], [9,8,0,0,0,0,0,1,0], [0,4,0,3,0,0,0,0,5], [0,7,0,0,0,0,9,4,6], [0,9,6,7,0,0,8,0,2]]
puzzle6 = [[5,0,0,0,4,9,8,0,0], [6,7,0,8,3,0,5,0,0], [9,0,0,0,0,0,6,1,3], [0,6,2,1,0,0,3,7,4], [4,0,0,0,0,3,9,2,8], [0,7,0,0,2,9,0,0,0], [0,9,6,2,1,8,0,5,0], [1,0,7,0,0,6,0,8,0], [8,0,2,0,4,5,0,9,0]]
puzzle_list = [puzzle1, puzzle2, puzzle3, puzzle4, puzzle5, puzzle6]
rand = random.randint(0, len(puzzle_list) - 1)
puzzle = puzzle_list[rand]
temp_puzzle = copy.deepcopy(puzzle)
lst = make(puzzle)
solved = solve(lst, puzzle)

print(temp_puzzle)
print(puzzle)
unsolved_list = []
for square in temp_puzzle:
    unsolved_list += square

boxlist = []
for y in range(0, 165, 55):
    for x in range(0, 165, 55):
        box = Box(x, y)
        boxlist.append(box)
for y in range(0, 165, 55):
    for x in range(165, 330, 55):
        box = Box(x, y)
        boxlist.append(box)
for y in range(0, 165, 55):
    for x in range(330, 495, 55):
        box = Box(x, y)
        boxlist.append(box)
for y in range(165, 330, 55):
    for x in range(0, 165, 55):
        box = Box(x, y)
        boxlist.append(box)
for y in range(165, 330, 55):
    for x in range(165, 330, 55):
        box = Box(x, y)
        boxlist.append(box)
for y in range(165, 330, 55):
    for x in range(330, 495, 55):
        box = Box(x, y)
        boxlist.append(box)
for y in range(330, 495, 55):
    for x in range(0, 165, 55):
        box = Box(x, y)
        boxlist.append(box)
for y in range(330, 495, 55):
    for x in range(165, 330, 55):
        box = Box(x, y)
        boxlist.append(box)
for y in range(330, 495, 55):
    for x in range(330, 495, 55):
        box = Box(x, y)
        boxlist.append(box)

for i, box in enumerate(boxlist):
    box.value = unsolved_list[i]
    if box.value != 0:
        display_num(box.value, box.x + 18, box.y + 16)
        box.empty = False
        full_boxes += 1

solved_list = []
for square in puzzle:
    solved_list += square

solution_boxlist = []
for y in range(0, 165, 55):
    for x in range(0, 165, 55):
        box = Box(x, y)
        solution_boxlist.append(box)
for y in range(0, 165, 55):
    for x in range(165, 330, 55):
        box = Box(x, y)
        solution_boxlist.append(box)
for y in range(0, 165, 55):
    for x in range(330, 495, 55):
        box = Box(x, y)
        solution_boxlist.append(box)
for y in range(165, 330, 55):
    for x in range(0, 165, 55):
        box = Box(x, y)
        solution_boxlist.append(box)
for y in range(165, 330, 55):
    for x in range(165, 330, 55):
        box = Box(x, y)
        solution_boxlist.append(box)
for y in range(165, 330, 55):
    for x in range(330, 495, 55):
        box = Box(x, y)
        solution_boxlist.append(box)
for y in range(330, 495, 55):
    for x in range(0, 165, 55):
        box = Box(x, y)
        solution_boxlist.append(box)
for y in range(330, 495, 55):
    for x in range(165, 330, 55):
        box = Box(x, y)
        solution_boxlist.append(box)
for y in range(330, 495, 55):
    for x in range(330, 495, 55):
        box = Box(x, y)
        solution_boxlist.append(box)

for i, box in enumerate(solution_boxlist):
    box.value = solved_list[i]






window.mainloop()
