""" A Brief Study in Handling Life Events """

from tkinter import Tk, Button
from time import sleep

# handler for timer event
def alarm():
    print('Calling the Pizza Company.')
    
# handler for ringing doorbell
def doorbell():
    print('Ding Dong!')
    sleep(4)
    print('Opening the Door')

# handler for when the phone rings
def phonecall():
    print('Answering the phone.')
    
# create buttons and assign callbacks    
root = Tk()
Button(root, text='Ring Doorbell', command=doorbell).pack()
Button(root, text='Call Phone', command=phonecall).pack()

# set a timer for 1 second
root.after(4000, alarm)

# start the event loop
root.mainloop()
 
