import tkinter as t
window = None
display_label = None
expression = ''
def press(num):
    global expression 
    expression += str(num)
    display_label['text'] = expression
def press_clear():
        global expression
        expression =''
        display_label['text'] = '0'
        
def press_result():
        global expression
        expression = ''
        display_label['text'] = str(eval(expression))
        expression =''
def setup_GUI():
            global window
            global display_label
            window = t.Tk()
            window.title('my calc')
            display_label = t.Label(window, text='', anchor='e', relief=t.SUNKEN, width=15, font='Arial 20')
            display_label.grid(row=0, columnspan=4)
            
            btn1 = t.Button(window, text='1' , width=5, height=2, font='Aral 15', command=lambda:press (1))
            btn2 = t.Button(window, text='2' , width=5, height=2, font='Aral 15', command=lambda:press (2))
            btn3 = t.Button(window, text='3' , width=5 , height=2, font='Aral 15',command=lambda:press (3))
            btn4 = t.Button(window, text='4' ,width=5 ,height=2, font='Aral 15',command=lambda:press (4))
            btn5 = t.Button(window, text='5' ,width=5, height=2, font='Aral 15',command=lambda:press (5))
            btn6 = t.Button(window, text='6' ,width=5, height=2, font='Aral 15',command=lambda:press (6))
            btn7 = t.Button(window, text='7' ,width=5, height=2, font='Aral 15',command=lambda:press (7)) 
            btn8 = t.Button(window, text='8' ,width=5, height=2, font='Aral 15',command=lambda:press (8))
            btn9 = t.Button(window, text='9' ,width=5, height=2, font='Aral 15',command=lambda:press (9))                             
            clear_btn = t.Button(window, text='c', width=5, height=2, font='Arial 15', command=press_clear)
            result_btn = t.Button(window, bg='green', text='=', width=5, height=2, font='Arial 15', command=press_clear)
            add_btn = t.Button(window, text='+' , width=5, height=2 , font='Arial 15' ,command=press_result)
            btn1.grid(row=1, column=0)
            btn2.grid(row=1, column=1)
            btn3.grid(row=1, column=2)
            btn4.grid(row=2, column=0)
            btn5.grid(row=2, column=1)
            btn6.grid(row=2, column=2)
            btn7.grid(row=3, column=0)
            btn8.grid(row=3, column=1)
            btn9.grid(row=3, column=2)
            clear_btn.grid(row=4, column=0)
            result_btn.grid(row=4, column=2) 
            add_btn.grid(row=1, column=3)                                              
            
setup_GUI()

window.mainloop()
