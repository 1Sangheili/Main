from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import pyperclip
import random



def learn_more():
    top = Toplevel()
    top.title('Learn More')
    top.geometry('640x400+200+200')
    # top.resizable(False, False)

    label = Label(top, font=('Rockwell', 10),text='Learn more about our R.P GENERATOR  &  How to create better passwords',
                  bg='#a87532', fg='white', height=3, width=91).place(x=0, y=0)
    texts = Text(top, font=('arial', 10), width=91, bg='cyan')
    texts.place(x=0, y=40)
    scroll = ttk.Scrollbar(top, orient=VERTICAL,
                           command=texts.yview)
    scroll.place(x=620, y=40)
    

    # take notes from notepad and insert into texts Widget
    texts.config(yscrollcommand=scroll.set)
    texts.insert(INSERT,
                 'With our R.P GENERATOR, you can create super-complicated, extra-long passwords \nthat are infinitely more difficult to crack than any passwords a human might \ncome up with')
    texts.insert(
        END, '\n-----------------------------------------------------------------------------\n')
    texts.insert(
        END,
        '\n\nIs our R.P GENERATOR safe to create your password?\nCan it be brute force attacked?\nAnswer: NO\n\nCan it be dictionary attacked?\nAnswer: NO\n\n')
    texts.insert(END,
                 'The best password methods (and great password examples)\n-> The revised passphrase method This is the multiple word phrase method with a twist — \n')
    texts.insert(
        END,
        'choose bizarre and uncommon words. Use proper nouns, the names of local businesses, historical figures,\n')
    texts.insert(
        END,
        'any words you know in another language, etc. A hacker might guess Quagmire, but he or she would find it \n')
    texts.insert(
        END, 'ridiculously challenging to try to guess a good password example like this:')
    texts.insert(END, '\n\n\t\t\t\tQuagmireHancockMerciDeNada')

    top.mainloop()


def let_copy():
    string = e.get()
    pyperclip.copy(string)


def increase_slide():
    x = passLen.get()
    x = x + 1
    passLen.set(x)


def decrease_slide():
    x = passLen.get()
    x = x - 1
    passLen.set(x)


'''def triggeruseKeyword():
    obj = displayDecorImg()
    if butt5Val.get():
        obj.cold(0)
        check.config(state=DISABLED)

        pass_lvl.config(bg='#33ff9c', fg='black', font='kabel')
        pass_lvl.delete(0, END)
        pass_lvl.insert(0, 'GUARANTEED')

        passLen.get()
        passLen.config(from_=10, to=30)
    else:
        obj.cold(1)
        pass_lvl.config(bg='white')
        pass_lvl.delete(0, END)
        check.config(state=NORMAL)
        passLen.config(from_=1, to=30)
        passLen.set(1)'''


def generatePassword():
    e.delete(0, END)
    ABC = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
           'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
           'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    Symbols = ['#', '@', '!', '$', '&', '*' '}',
               '{', '%', '=', '-', '+', ';', '[', ']', '~', '>', '<']
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    lenSlider = int(passLen.get())

    rand1 = []
    if butt1Val.get():
        rand1 = rand1 + ABC
    if butt2Val.get():
        rand1 = rand1 + abc
    if butt3Val.get():
        rand1 = rand1 + numbers
    if butt4Val.get():
        rand1 = rand1 + Symbols
    # password= randint(0, take as much box tiks)
    # in for loop
    # times -= 1
    if rand1 == []:
        Warn = messagebox.showwarning(
            'Password Generator', 'Please select at least 1 Option !')
        lenSlider = 0
        pass_lvl.config(bg='white')
        pass_lvl.delete(0, END)
    else:
        checkSECLEVEL()
    for i in range(0, lenSlider):
        lenSlider -= 1
        random_pick = random.choice(rand1)
        e.insert(0, random_pick)


def checkSECLEVEL():
    x = int(passLen.get())
    if x < 8:
        pass_lvl.config(bg='#ff0000', fg='#aeff00')
        pass_lvl.delete(0, END)
        pass_lvl.insert(0, 'WEAK')
    elif x >= 8 and x <= 10:
        pass_lvl.config(bg='#15bad4', fg='black')
        pass_lvl.delete(0, END)
        pass_lvl.insert(0, 'GOOD')
    elif x > 10 and x <= 12:
        pass_lvl.config(bg='#4188fa', fg='black')  # 9900ff
        pass_lvl.delete(0, END)
        pass_lvl.insert(0, 'STRONG')
    elif x > 12 and x <= 15:
        pass_lvl.config(bg='#00ffc3', fg='black')
        pass_lvl.delete(0, END)
        pass_lvl.insert(0, 'VERY STRONG')
    elif x > 15:
        pass_lvl.config(bg='#FFD700', fg='black')
        pass_lvl.delete(0, END)
        pass_lvl.insert(0, 'GUARANTEED')


root = Tk()
root['bg'] = 'cyan'
root.title('Random Password Generator by HEILI')
root.geometry('578x284+200+200')
root.resizable(False, False)

SecurityImg = PhotoImage(file='shield(1).png')
placeSecImg = Label(root, image=SecurityImg, bg='cyan').place(x=222, y=150)
e = Entry(root, width=38, font='Arial', borderwidth=4)
e.place(x=0, y=0)

# generate password button
refreshImg = PhotoImage(file='refresh(1).png')
gen = Button(root, text='GENERATE', width=107, command=generatePassword,
             height=63, image=refreshImg, bg='black', activebackground='black')
gen.place(x=465, y=-2)

# password security level
safety_lvl = Label(root, text='Safety level: ', bg='cyan').place(x=50, y=34)
pass_lvl = Entry(root, width=17, font='kabel', borderwidth=0)
pass_lvl.place(x=200, y=30)


# password lengrh slider
pass_label = Label(root, text='Password length: ', bg='cyan')
pass_label.place(x=50, y=77)
passLen = Scale(root, from_=1, to=30, orient=HORIZONTAL, troughcolor='orange',
                sliderlength=15, length=200, bg='cyan', borderwidth=FALSE)
passLen.place(x=200, y=63)

# button for increasing slider value
lower_scale = Button(root, text='-', command=decrease_slide,
                     bg='#17ffc5', activebackground='#17ffc5')
higher_scale = Button(root, text='+', command=increase_slide,
                      bg='#17ffc5', activebackground='#17ffc5')
lower_scale.place(x=180, y=77)
higher_scale.place(x=410, y=77)

# tick boxes for user to choose what elements have to present in the password
char_used = Label(root, text='Characters used: ', bg='cyan').place(x=50, y=115)
butt1Val = IntVar()
butt2Val = IntVar()
butt3Val = IntVar()
butt4Val = IntVar()
butt5Val = IntVar()

info_img = PhotoImage(file='information-button.png')
info_button = Button(root, image=info_img, bg='cyan', borderwidth=0,
                     activebackground='cyan', command=learn_more).place(x=0, y=249)

copy = Button(root, text='COPY', command=let_copy, borderwidth=0, width=15,
              height=4, bg='#00c3ff', activebackground='#00c3ff').place(x=351, y=0)


checkbutt1 = Checkbutton(root, text='ABC', onvalue=1, offvalue=0, borderwidth=0,
                         variable=butt1Val, bg='cyan', activebackground='cyan').place(x=150, y=115)
checkbutt2 = Checkbutton(root, text='abc', onvalue=1, offvalue=0, borderwidth=0,
                         variable=butt2Val, bg='cyan', activebackground='cyan').place(x=230, y=115)
checkbutt3 = Checkbutton(root, text='123', onvalue=1, offvalue=0, borderwidth=0,
                         variable=butt3Val, bg='cyan', activebackground='cyan').place(x=310, y=115)
checkbutt4 = Checkbutton(root, text='#$&', onvalue=1, offvalue=0, borderwidth=0,
                         variable=butt4Val, bg='cyan', activebackground='cyan').place(x=390, y=115)
'''checkbutt5 = Checkbutton(root, text='No Keyword', onvalue=1, offvalue=0, variable=butt5Val, borderwidth=0,
                         bg='cyan', activebackground='cyan', command=triggeruseKeyword).place(x=470, y=115)
'''
root.mainloop()
