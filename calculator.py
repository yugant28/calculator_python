from tkinter import *
 
# globally declare the expression variable
expression = ""
 
 
# Function to update expression
# in the text entry box
def press(num):
    # point out the global expression variable
    global expression
 
    # concatenation of string
    expression = expression + str(num)
 
    # update the expression by using set method
    equation.set(expression)
 
 
# Function to evaluate the final expression
def equalpress():
    # Try and except statement is used
    # for handling the errors like zero
    # division error etc.
 
    # Put that code inside the try block
    # which may generate the error
    try:
 
        global expression
 
        # eval function evaluate the expression
        # and str function convert the result
        # into string
        total = str(eval(expression))
 
        equation.set(total)
 
        # initialize the expression variable
        # by empty string
        expression = ""
 
    # if error is generate then handle
    # by the except block
    except:
 
        equation.set(" error ")
        expression = ""
 
 
# Function to clear the contents
# of text entry box
def clear():
    global expression
    expression = ""
    equation.set("")
 
 
# Driver code
if __name__ == "__main__":
    # create a GUI window
    gui = Tk()
 
    # set the background colour of GUI window
    gui.configure(background="light yellow")
 
    # set the title of GUI window
    gui.title("Simple Calculator")
 
    # set the configuration of GUI window
    gui.geometry("600x600")
 
    # StringVar() is the variable class
    # we create an instance of this class
    equation = StringVar()
 
    # create the text entry box for
    # showing the expression .
    expression_field = Entry(gui, textvariable=equation)
 
    # grid method is used for placing
    # the widgets at respective positions
    # in table like structure .
    expression_field.grid(columnspan=10, ipadx=100,padx=22,pady=22)
 
    # create a Buttons and place at a particular
    # location inside the root window .
    # when user press the button, the command or
    # function affiliated to that button is executed .
    button1 = Button(gui, text=' 1 ', fg='black', bg='grey',
                    command=lambda: press(1), height=3, width=10)
    button1.grid(row=2, column=0,padx=22,pady=22)
 
    button2 = Button(gui, text=' 2 ', fg='black', bg='grey',
                    command=lambda: press(2),  height=3, width=10)
    button2.grid(row=2, column=1,padx=22,pady=22)
 
    button3 = Button(gui, text=' 3 ', fg='black', bg='grey',
                    command=lambda: press(3),  height=3, width=10)
    button3.grid(row=2, column=2,padx=22,pady=22)
 
    button4 = Button(gui, text=' 4 ', fg='black', bg='grey',
                    command=lambda: press(4),  height=3, width=10)
    button4.grid(row=3, column=0,padx=22,pady=22)
 
    button5 = Button(gui, text=' 5 ', fg='black', bg='grey',
                    command=lambda: press(5),  height=3, width=10)
    button5.grid(row=3, column=1,padx=22,pady=22)
 
    button6 = Button(gui, text=' 6 ', fg='black', bg='grey',
                    command=lambda: press(6),  height=3, width=10)
    button6.grid(row=3, column=2,padx=22,pady=22)
 
    button7 = Button(gui, text=' 7 ', fg='black', bg='grey',
                    command=lambda: press(7),  height=3, width=10)
    button7.grid(row=4, column=0,padx=22,pady=22)
 
    button8 = Button(gui, text=' 8 ', fg='black', bg='grey',
                    command=lambda: press(8),  height=3, width=10)
    button8.grid(row=4, column=1,padx=22,pady=22)
 
    button9 = Button(gui, text=' 9 ', fg='black', bg='grey',
                    command=lambda: press(9), height=3, width=10)
    button9.grid(row=4, column=2,padx=22,pady=22)
 
    button0 = Button(gui, text=' 0 ', fg='black', bg='grey',
                    command=lambda: press(0),  height=3, width=10)
    button0.grid(row=5, column=0,padx=22,pady=22)
 
    plus = Button(gui, text=' + ', fg='black', bg='grey',
                command=lambda: press("+"),  height=3, width=10)
    plus.grid(row=2, column=3,padx=22,pady=22)
 
    minus = Button(gui, text=' - ', fg='black', bg='grey',
                command=lambda: press("-"),  height=3, width=10)
    minus.grid(row=3, column=3,padx=22,pady=22)
 
    multiply = Button(gui, text=' * ', fg='black', bg='grey',
                    command=lambda: press("*"),  height=3, width=10)
    multiply.grid(row=4, column=3,padx=22,pady=22)
 
    divide = Button(gui, text=' / ', fg='black', bg='grey',
                    command=lambda: press("/"),  height=3, width=10)
    divide.grid(row=5, column=3,padx=22,pady=22)
 
    equal = Button(gui, text=' = ', fg='black', bg='grey',
                command=equalpress,  height=3, width=10)
    equal.grid(row=6, column=3,padx=22,pady=22)
 
    clear = Button(gui, text='Clear', fg='black', bg='grey',
                command=clear,  height=3, width=10)
    clear.grid(row=5, column='1',padx=22,pady=22)
    exit = Button(gui, text='Exit', fg='black', bg='grey',
                command=quit,  height=3, width=10)
    exit.grid(row=5, column='2',padx=22,pady=22)
 
    Decimal= Button(gui, text='.', fg='black', bg='grey',
                    command=lambda: press('.'),  height=3, width=10)
    Decimal.grid(row=6, column=0,padx=22,pady=22)
    # start the GUI
    gui.mainloop()

