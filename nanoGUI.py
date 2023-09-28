# This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
# You should have received a copy of the GNU General Public License along with this program. If not, see <https://www.gnu.org/licenses/>. 


from tkinter import *
from tkinter.ttk import *


class Container:
    def __init__(self, widget, parent=None, side=TOP):
        self.widget = widget
        self.parent = parent if parent != None else self
        self.side = side


class Interactor:
    def __init__(self, widget, parent, wrapper=None):
        self.widget = widget
        self.parent = parent
        self.wrapper = wrapper if wrapper != None else widget


def init():
    global window, mainframe, current_container
    window = Tk()
    window.title("nanoGUI")
    window.minsize(300,100)

    mainframe = Frame(window, padding="6 6 6 6")
    mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

    current_container = Container(mainframe)


def start():
    window.mainloop()


### Interactors


def label(name):
    """Adds a label to the window."""
    interactor = Label(current_container.widget, text=name)
    interactor.pack(side=current_container.side)
    return Interactor(interactor, current_container)


def entry(name=""):
    """Adds an interactive input to the window."""
    frame = Labelframe(current_container.widget, text=name)
    interactor = Entry(frame)
    interactor.pack(side=LEFT)
    frame.pack(side=current_container.side)
    return Interactor(interactor, current_container, frame)


def button(name, command=lambda:0, *args):
    """Adds a button to the window."""
    interactor = Button(
        current_container.widget, 
        text=name, 
        command=lambda:command(*args),
    )
    interactor.pack(side=current_container.side)
    return Interactor(interactor, current_container)


def slider(from_, to, name=""):
    """Adds a slider to the window."""
    
    
    frame = Labelframe(current_container.widget, text=name)
    
    svar = StringVar(master=frame, value=str(from_), name="svar")
    
    def __update_svar(val):
        svar.set(f'{float(val):.1f}')
    
    interactor = Scale(
        frame, 
        from_=from_,
        to=to,
        value=from_,
        command = __update_svar,
        orient=HORIZONTAL,
        length=150,
    )
    interactor.pack(side=TOP, padx=3,pady=3)
    
    mini = Label(frame,text=from_)
    mini.pack(side=LEFT, padx=3)
    maxi = Label(frame,text=to)
    maxi.pack(side=RIGHT, padx=3)
    
    indicator = Label(frame, textvariable=svar)
    indicator.pack(side=BOTTOM)
    frame.pack(side=current_container.side)
    return Interactor(interactor, current_container, frame)


def delete(interactor):
    interactor.wrapper.destroy()

### Interactor access

#### Getters


def get(interactor, property_name):
    
    if property_name=="name":
        return get_name(interactor)
    if property_name=="text":
        return get_text(interactor)
    
    return interactor.widget.cget(name)


def get_name(interactor):
    return interactor.wrapper.cget("text")


def get_text(interactor):
    w = interactor.widget
    if type(w)==Entry:
        return w.get()
    if type(w)==Scale:
        return interactor.wrapper.cget("text")
    return w.cget("text")


def get_number(interactor):
    w = interactor.widget
    if type(w) in (Entry, Scale):
        return float(w.get())
    return float(w.cget("text"))


def get_command(interactor):
    return get(interactor, "command")


#### Setters


def set_name(interactor, name):
    interactor.wrapper.config(text=name)


def set_text(interactor, text):
    w = interactor.widget
    if type(w)==Entry:
        w.delete(0, END)
        w.insert(0, text)
    elif type(w)==Scale:
        set_name(interactor, text)
    else:
        w.config(text=text)


def set_number(interactor, x):
    w = interactor.widget
    if type(w)==Scale:
        w.config(value=x)
    else:
        set_text(interactor, str(x))


def set_command(interactor, command):
    w = interactor.widget
    if type(w)==Scale:
        def cmd(val):
            interactor.wrapper.setvar(name="svar", value = f'{float(val):.1f}')
            command(val)
    else:
        cmd = command
    w.config(command=cmd)


### Conteneurs


def begin_horizontal():
    global current_container
    frame = Frame(current_container.widget, padding="6 6 6 6")
    current_container = Container(frame, current_container, LEFT)
    return current_container


def begin_vertical():
    global current_container
    frame = Frame(current_container.widget, padding="6 6 6 6")
    current_container = Container(frame, current_container, TOP)
    return current_container


def end_horizontal():
    global current_container
    current_container.widget.pack(
        side=current_container.parent.side
    )
    current_container = current_container.parent


def end_vertical():
    global current_container
    current_container.widget.pack(
        side=current_container.parent.side
    )
    current_container = current_container.parent
