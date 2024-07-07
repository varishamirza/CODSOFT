# Import packages
from tkinter import *
import math
#import numpy as np

'''
Functions
'''
# Function to add in the entry of text display
def button_click(char):
    global calc_operator
    calc_operator += str(char)
    text_input.set(calc_operator)

# Function to clear the whole entry of text display
def button_clear_all():
    global calc_operator
    calc_operator = ""
    text_input.set("")

# Function to delete one by one from the last in the entry of text display
def button_delete():
    global calc_operator
    text = calc_operator[:-1]
    calc_operator = text
    text_input.set(text)



# Function to change the sign of number
def sign_change():
    global calc_operator
    if calc_operator[0]=='-':
        temp = calc_operator[1:]
    else:
        temp = '-'+calc_operator
    calc_operator = temp
    text_input.set(temp)    

# Function to calculate the percentage of a number
def percent():
    global calc_operator
    temp = str(eval(calc_operator+'/100'))
    calc_operator = temp
    text_input.set(temp)

# Funtion to find the result of an operation
def button_equal():
    global calc_operator
    temp_op = str(eval(calc_operator))
    text_input.set(temp_op)
    calc_operator = temp_op

'''
Variables
'''


tk_calc = Tk()
tk_calc.configure(bg="#293C4A", bd=10)
tk_calc.title("CALCULATOR")

calc_operator = ""
text_input = StringVar()

text_display = Entry(tk_calc, font=('sans-serif', 20, 'bold'), textvariable=text_input,
                     bd=5, insertwidth = 5, bg='#BBB', justify='right').grid(columnspan=5, padx = 10, pady = 15)

button_params = {'bd':5, 'fg':'#BBB', 'bg':'#3C3636', 'font':('sans-serif', 20, 'bold')}
button_params_main = {'bd':5, 'fg':'#000', 'bg':'#BBB', 'font':('sans-serif', 20, 'bold')}

'''
Buttons
'''


#--5th row--
# Add a left parentheses
left_par = Button(tk_calc, button_params, text='(',
                  command=lambda:button_click('(')).grid(row=5, column=0, sticky="nsew")
# Add a right parentheses
right_par = Button(tk_calc, button_params, text=')',
                   command=lambda:button_click(')')).grid(row=5, column=1, sticky="nsew")   
# Change the sign of a number
signs = Button(tk_calc, button_params, text='\u00B1',
               command=sign_change).grid(row=5, column=2, sticky="nsew")
# Transform number to percentage
percentage = Button(tk_calc, button_params, text='%',
               command=percent).grid(row=5, column=3, sticky="nsew")


#--6th row--
button_7 = Button(tk_calc, button_params_main, text='7',
                  command=lambda:button_click('7')).grid(row=6, column=0, sticky="nsew")
button_8 = Button(tk_calc, button_params_main, text='8',
                  command=lambda:button_click('8')).grid(row=6, column=1, sticky="nsew")
button_9 = Button(tk_calc, button_params_main, text='9',
                  command=lambda:button_click('9')).grid(row=6, column=2, sticky="nsew")
delete_one = Button(tk_calc, bd=5, fg='#000', font=('sans-serif', 20, 'bold'),
              text='DEL', command=button_delete, bg='#db701f').grid(row=5, column=1, sticky="nsew")
delete_all = Button(tk_calc, bd=5, fg='#000', font=('sans-serif', 20, 'bold'),
              text='AC', command=button_clear_all, bg='#db701f').grid(row=5, column=0, sticky="nsew")

#--7th row--
button_4 = Button(tk_calc, button_params_main, text='4',
                  command=lambda:button_click('4')).grid(row=7, column=0, sticky="nsew")
button_5 = Button(tk_calc, button_params_main, text='5',
                  command=lambda:button_click('5')).grid(row=7, column=1, sticky="nsew")
button_6 = Button(tk_calc, button_params_main, text='6',
                  command=lambda:button_click('6')).grid(row=7, column=2, sticky="nsew")
mul = Button(tk_calc, button_params_main, text='*',
             command=lambda:button_click('*')).grid(row=6,columnspan=2, column=3, sticky="nsew")
div = Button(tk_calc, button_params_main, text='/',
             command=lambda:button_click('/')).grid(row=5,columnspan=2,column=3, sticky="nsew")

#--8th row--
button_1 = Button(tk_calc, button_params_main, text='1',
                  command=lambda:button_click('1')).grid(row=8, column=0, sticky="nsew")
button_2 = Button(tk_calc, button_params_main, text='2',
                  command=lambda:button_click('2')).grid(row=8, column=1, sticky="nsew")
button_3 = Button(tk_calc, button_params_main, text='3',
                  command=lambda:button_click('3')).grid(row=8, column=2, sticky="nsew")
add = Button(tk_calc, button_params_main, text='+',
             command=lambda:button_click('+')).grid(row=7,columnspan=2, column=3, sticky="nsew")
sub = Button(tk_calc, button_params_main, text='-',
             command=lambda:button_click('-')).grid(row=8,columnspan=3, column=3, sticky="nsew")

#--9th row--
button_00 = Button(tk_calc, button_params_main, text='00',
                  command=lambda:button_click('00')).grid(row=9, column=0, sticky="nsew")
point = Button(tk_calc, button_params_main, text='.',
               command=lambda:button_click('.')).grid(row=9, column=2, sticky="nsew")
button_0 = Button(tk_calc, button_params_main, text='0', font=('sans-serif', 16, 'bold'),
             command=lambda:button_click('0')).grid(row=9, column=1, sticky="nsew")
equal = Button(tk_calc, button_params_main, text='=',
               command=button_equal).grid(row=9, columnspan=2, column=3, sticky="nsew")


tk_calc.mainloop()