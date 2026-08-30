from tkinter import *

#Steps to success
# - Make copies of this file
# - Add and remove pages as necessary, name appropriately
# - Layout widgets (Buttons, Labels, etc)
# - Link pages
# - Write in algorithms

##---------------------------------------------------------------------------##
#                            Window Generator                                 #
##---------------------------------------------------------------------------##

class solution(Tk):
    def __init__(self, *args, **kwargs): #args etc are overrides to allow us to run multiple arguments/operations

        Tk.__init__(self, *args, **kwargs)
        gui = Frame(self)

        #Window Settings
        gui.pack(side="top", fill="both", expand = True)
        gui.grid_rowconfigure(0, weight=1)
        gui.grid_columnconfigure(0, weight=1)
        self.title("MultiFrame") #Window Title


        ##---------------------------------------------------------------------------##
        #                                    MENU BAR                                 #
        ##---------------------------------------------------------------------------##
        menuBar = Menu(self)

        # Create a pulldown menu, and add it to the menu bar
        fileMenu = Menu(menuBar, tearoff=0)
        fileMenu.add_command(label="Open", command=lambda: doNothing)
        fileMenu.add_command(label="Save", command=lambda: doNothing)
        fileMenu.add_separator()
        fileMenu.add_command(label="Exit", command=lambda: doNothing)
        menuBar.add_cascade(label="File", menu=fileMenu)

        # create more pulldown menus
        editMenu = Menu(menuBar, tearoff=0)
        editMenu.add_command(label="Cut", command=lambda: doNothing)
        editMenu.add_command(label="Copy", command=lambda: doNothing)
        editMenu.add_command(label="Paste", command=lambda: doNothing)
        menuBar.add_cascade(label="Edit", menu = editMenu)

        # display the menu
        self.config(menu=menuBar)
        ##---------------------------------------------------------------------------##
        #                                   MENU BAR                                  #
        ##---------------------------------------------------------------------------##

        #Dictionary of Frames
        self.frames = {}

        for F in (StartPage, PageOne, PageTwo): #Add new class frames here.

            frame = F(gui, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew") #Setting Window/Frame Size

        self.show_frame(StartPage) #Starting frame (Class Name)

    def show_frame(self, cont): #Command for frame change

        frame = self.frames[cont]
        frame.tkraise()

##---------------------------------------------------------------------------##
#                    Frames - Each frame is a new class.                      #
#                                                                             #
#         To change frame using a command use the following command.          #
#               command=lambda: controller.show_frame(pagename)               #
##---------------------------------------------------------------------------##

class StartPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self,parent)

        #Label
        label = Label(self, text="Home Screen", borderwidth=2, relief="solid")
        label.grid(row = 1, column = 2, columnspan = 2)

        #Blank Space
        label = Label(self, text="")
        label.grid(row = 2, column = 1)

        #Button (Change Frame)
        button1 = Button(self, text="Home", command=lambda: controller.show_frame(StartPage))
        button1.grid(row = 3, column = 1)

        #Button (Change Frame)
        button1 = Button(self, text="Page 1", command=lambda: controller.show_frame(PageOne))
        button1.grid(row = 3, column = 2)

        #Button (Change Frame)
        button2 = Button(self, text="Page 2", command=lambda: controller.show_frame(PageTwo))
        button2.grid(row = 3, column = 3)

        #Button (Exit Button)
        button2 = Button(self, text="Exit", command=lambda: app.destroy())
        button2.grid(row = 3, column = 4)


##---------------------------------------------------------------------------##
#                            Widgets Listed Below                             #
##---------------------------------------------------------------------------##

        #Blank Space
        label = Label(self, text="")
        label.grid(row = 4, column = 1)

        #Entry Widget
        entryW = Entry(self, width = 4, background = "red")
        entryW.grid(row = 5, column = 1)

        #Option Menu/Drop Down List
        optionMenuV = StringVar(self) #Option Menu Variable type to store input
        optionMenuV.set("") #Option Menu variable set
        optionMenuW = OptionMenu(self, optionMenuV, "One", "Two", "Three")
        optionMenuW.grid(row = 6, column = 1)

        #Label
        labelW = Label(self, text="Label")
        labelW.grid(row = 7, column = 1)

        #Button
        buttonW = Button(self, text="Button", command=lambda: doNothing())
        buttonW.grid(row = 9, column = 1)

        #Check Button
        checkButtonV = IntVar(self) #Check Button Variable type to store input
        checkButtonW = Checkbutton(self, text = "checkButton", variable = checkButtonV)
        checkButtonW.grid(row = 10, column = 1, columnspan = 2)

        ##---------------------------------------------------------------------------##
        #                            Widget Manipulation                              #
        ##---------------------------------------------------------------------------##

        #Entry Widget
        def entryWidget():
            entryVar = entryW.get() #Stores entry as a variable
            entryW.config(state = DISABLED) #Disables input
            entryW.config(state = NORMAL) #Enables input
            entryW.delete(0, END) #Clear Entry
            return

        #Button Widget
        def doNothing(): #This is the command the button will execute
            print("Nothing")
            return

        #Option Menu Widget
        def optionMenuWidget():
            optionMenuVar = optionMenuV.get() #Stores input as a variable
            optionMenuV.set("") #Option Menu variable set
            return

        #Label Change (Output)
        def labelConfigWidget():
            labelW.config(text = "New Text/Output")
            return

        #Checkbox
        def checkButtonWidget():
            checkButtonVar = checkButtonV.get() #Stores input as a variable
            checkButtonV.set(0) #De-check Box
            checkButtonV.set(1) #Pre-check Box
            return

class PageOne(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        #Label
        label = Label(self, text="Page One")
        label.grid(row = 1, column = 2, columnspan = 2)

        #Button (Change Frame)
        button1 = Button(self, text="Home", command=lambda: controller.show_frame(StartPage))
        button1.grid(row = 2, column = 1)

        #Button (Change Frame)
        button1 = Button(self, text="Page 1", command=lambda: controller.show_frame(PageOne))
        button1.grid(row = 2, column = 2)

        #Button (Change Frame)
        button2 = Button(self, text="Page 2", command=lambda: controller.show_frame(PageTwo))
        button2.grid(row = 2, column = 3)

        #Button (Exit Button)
        button2 = Button(self, text="Exit", command=lambda: app.destroy())
        button2.grid(row = 2, column = 4)

class PageTwo(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        #Label
        label = Label(self, text="Page Two")
        label.grid(row = 1, column = 2, columnspan = 2)

        #Button (Change Frame)
        button1 = Button(self, text="Home", command=lambda: controller.show_frame(StartPage))
        button1.grid(row = 2, column = 1)

        #Button (Change Frame)
        button1 = Button(self, text="Page 1", command=lambda: controller.show_frame(PageOne))
        button1.grid(row = 2, column = 2)

        #Button (Change Frame)
        button2 = Button(self, text="Page 2", command=lambda: controller.show_frame(PageTwo))
        button2.grid(row = 2, column = 3)

        #Button (Exit Button)
        button2 = Button(self, text="Exit", command=lambda: app.destroy())
        button2.grid(row = 2, column = 4)

app = solution()
app.mainloop()
