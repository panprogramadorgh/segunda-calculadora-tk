from tkinter import *
from typing import Tuple
from styles import regular_font

def build_numeric_buttons(root, display, offset: Tuple[int, int] = (0, 0)) -> None:
  row_offset = offset[0]
  column_offset = offset[1]

 # handles the click of numeric buttons
  def handle_click(number: int):
    handle_error(display)
    current_text = display.cget('text')
    if current_text == '0':
      new_text = f"{number}"
      display.config(text=new_text)
      return
    new_text = f"{current_text}{number}"
    display.config(text=new_text)

  # generates all the buttons inside a list
  numeric_buttons = [Button(root, text=i, font=regular_font, width=5, height=2, command=lambda number=i: handle_click(number)) for i in range(10)]

  # grids all the buttons
  for row in range(4):
    for column in range(3):
      index = row * 3 + column
      if index < 9:
        numeric_buttons[index].grid(row=row+row_offset, column=column+column_offset)
      else: numeric_buttons[-1].grid(row=3+row_offset, column=0+column_offset)

def build_op_buttons(root, display) -> None:
  # generats the operation buttons
  op_buttons = ['+', '-', "*", "/"]
  for op_index in range(len(op_buttons)):
    op_buttons[op_index] = Button(root, text=op_buttons[op_index], width=5, height=2, font=regular_font, command=lambda op=op_buttons[op_index]: handle_op(display, op))

  # grids the operation buttons
  op_buttons[0].config(height=4, pady=12)
  op_buttons[0].grid(row=4, column=2, rowspan=2)
  op_buttons[1].config(height=4, pady=12)
  op_buttons[1].grid(row=4, column=3, rowspan=2)
  op_buttons[2].grid(row=5, column=0)
  op_buttons[3].grid(row=5, column=1)

def handle_op(display, op: str):
  handle_error(display)
  current_text = display.cget('text')
  if current_text == '': current_text = '0'

  # spliting without blank strings
  splited_current_text = current_text.split(' ')
  splited_current_text_noblank = list()
  for split in splited_current_text:
    if split != '': splited_current_text_noblank.append(split)
  # controls when can the user can put operation symbol
  if splited_current_text_noblank[-1] in ('*', '/'): return
  if splited_current_text_noblank[-1] in ('+', '-') and op in ('*', '/'): return
  new_text = f"{current_text} {op} "
  # updates the display
  display.config(text=new_text)

def handle_remove(display):
  handle_error(display)
  current_text = display.cget('text')
  if len(current_text) > 1:
    # in case the user is removing a number
    if current_text[-1] != ' ':
      new_text = current_text[:-1]
      display.config(text=new_text)
    # and in case the user is removing a operation symbol
    else:
      new_text = current_text[:-3]
      display.config(text=new_text)
  else: display.config(text='')

def handle_dot(display):
  handle_error(display)
  current_text = display.cget('text')
  if current_text == '': return
  # checks if putting a dot at the end of the number makes a new number with sense
  splited_current_text = current_text.split(' ')
  splited_current_text_noblank = list()
  for slice in splited_current_text:
    if slice != '': splited_current_text_noblank.append(slice)
  try:
    float(f"{splited_current_text_noblank[-1]}.0")
  except ValueError:
    return
  else:
    new_text = f"{current_text}."
    display.config(text=new_text)

def handle_equal(display):
  handle_error(display)
  current_text = display.cget('text')
  # checks if the last word is a number instead of a operation symbol
  try:
    splited_current_text = current_text.split(' ')
    splited_current_text_noblank = list()
    for slice in splited_current_text:
      if slice != '': splited_current_text_noblank.append(slice)
    last_word = splited_current_text_noblank[-1]
    if last_word in ('+', '-', '*', '/'): raise Exception("Can not evaluate. Expected number at the end")
  except Exception:
    return

  # sets a maximum length of the resulting number and in case of overflow, throws an error at display
  max: int = 15
  result = f"{eval(current_text)}"
  if len(result) >= max:
    display.config(text='Error')
    return
  display.config(text=result)

# responsible for handling an error at the display
def handle_error(display):
  current_text = display.cget('text')
  if current_text == 'Error':
    new_text = ''
    display.config(text=new_text)
  else: return