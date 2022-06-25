from tkinter import *
import random
import tkinter.messagebox
inpu= 'hi'
#function
def inp1() :
    global inpu
    inpu = 'O'
    #print(inpu)
def inp2() :
    global inpu
    inpu = 'Y'
    #print(inpu)
def inp3() :
    global inpu
    inpu = 'B'
    #print(inpu)
def But1() : 
    global inpu
    inpu2 = random.randrange(1,6)
    #เสมอ
    if inpu == 'O' and inpu2 == 1 or inpu == 'O' and inpu2 == 4 :
        tkinter.messagebox.showinfo('แจ้งเตือน','ฉันตอบ "O"\tเสมอ')
        inpu= 'hi'
    elif inpu == 'Y' and inpu2 == 2 or inpu == 'Y' and inpu2 == 5 :
        tkinter.messagebox.showinfo('แจ้งเตือน','ฉันตอบ "Y"\tเสมอ')
        inpu= 'hi'
    elif inpu == 'B' and inpu2 == 3 or inpu == 'B' and inpu2 == 6 :
        tkinter.messagebox.showinfo('แจ้งเตือน','ฉันตอบ "B"\tเสมอ')
        inpu= 'hi'
    #ชนะ
    elif inpu == 'O' and inpu2 == 2 or inpu == 'O' and inpu2 == 5 :
        tkinter.messagebox.showinfo('แจ้งเตือน','ฉันตอบ "Y"\tคุณชนะ')
        inpu= 'hi'
    elif inpu == 'Y' and inpu2 == 3 or inpu == 'Y' and inpu2 == 6 :
        tkinter.messagebox.showinfo('แจ้งเตือน','ฉันตอบ "B"\tคุณชนะ')
        inpu= 'hi'
    elif inpu == 'B' and inpu2 == 1 or inpu == 'B' and inpu2 == 4 :
        tkinter.messagebox.showinfo('แจ้งเตือน','ฉันตอบ "O"\tคุณชนะ')
        inpu= 'hi'
    #แพ้
    elif inpu == 'O' and inpu2 == 3 or inpu == 'O' and inpu2 == 6 :
        tkinter.messagebox.showinfo('แจ้งเตือน','ฉันตอบ "B"\tคุณแพ้')
        inpu= 'hi'
    elif inpu == 'Y' and inpu2 == 1 or inpu == 'Y' and inpu2 == 4 :
        tkinter.messagebox.showinfo('แจ้งเตือน','ฉันตอบ "O"\tคุณแพ้')
        inpu= 'hi'
    elif inpu == 'B' and inpu2 == 2 or inpu == 'B' and inpu2 == 5 :
        tkinter.messagebox.showinfo('แจ้งเตือน','ฉันตอบ "Y"\tคุณแพ้')
        inpu= 'hi'

    else :
       tkinter.messagebox.showerror('ERROR','โปรดเลือก กระดาษ กรรไกร ค้อน') 

win = Tk()
win.geometry('185x150+643+280')
label = Label(text = 'O = ค้อน , Y = กรรไกร , B = กระดาษ' , bg='#b5ffad').place(x=0 , y=0)
Butt = Button(text=' O ',bg='red',command=inp1).place(x=100-40 , y= 21)
Butt2 = Button(text=' Y ',bg='blue',command=inp2).place(x=70+50-35 , y= 21)
Butt2 = Button(text=' B ',bg='yellow',command=inp3).place(x=70+50-30+19 , y= 21)
Butt3 = Button(text='        ok        ',bg='#fffdad',command=But1).place(x=60 , y= 21+26)
win.mainloop()
