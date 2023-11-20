from tkinter import *
from styles import regular_font, display_font, regular_slot_dimensions, display_dimensions
from functions import build_numeric_buttons, handle_remove, handle_dot, handle_equal, build_op_buttons

# root
root = Tk()
root.title('Calculator')
root.resizable(width=False, height=False)

# display label
display = Label(root, text='0', font=display_font, width=display_dimensions[0], height=display_dimensions[1], bd=5)
display.grid(row=0, column=0, columnspan=4)

# numeric button grid
build_numeric_buttons(root, display, offset=(1, 0))

# remove button
remove = Button(root, text='rm', font=regular_font, command=lambda: handle_remove(display), width=regular_slot_dimensions[0], height=regular_slot_dimensions[1], bg='#cc2222', overrelief='flat')
remove.grid(row=1, column=3)

# dot button
dotButton = Button(root, text='.', font=regular_font, width=regular_slot_dimensions[0], height=regular_slot_dimensions[1], command=lambda: handle_dot(display))
dotButton.grid(row=4, column=1)

# equal button
equalButton = Button(root, text="eq", font=regular_font, width=regular_slot_dimensions[0], height=4, pady=12, bg="#4a2", fg='#fff', command=lambda: handle_equal(display))
equalButton.grid(row=2, column=3, rowspan=2)

# op buttons
build_op_buttons(root, display)


root.mainloop()