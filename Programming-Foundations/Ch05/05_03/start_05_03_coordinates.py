""" Where's My Mouse? """
import tkinter

my_tuple = ('a', 'b', 'c', 1, 2, 3)
print(my_tuple)
print(my_tuple[2])

"""my_tuple[2] = 'brick'"""

def mouse_click(event):

    # retrieve XY coords as a tuple
    coords = root.winfo_pointerxy()
    print('coords: {}'.format(coords))
    print('X: {}'.format(coords[0]))
    print('Y: {}'.format(coords[1]))
    
root = tkinter.Tk()
root.bind('<Button>', mouse_click)
root.mainloop()
