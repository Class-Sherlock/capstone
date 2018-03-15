from tkinter import *
from TestCaseFunctions import URLFilter
from TestCaseFunctions import FileBlocking

def Window_One():
    root = Tk()  # Creates the window; root is main window
    # Window size & Window priority
    root.geometry('800x500')
    root.attributes("-topmost", True)

    # TITLE OF FRAME & ICON
    root.title("SHIELD: A Next Generation Network Configuration Tool")
    root.iconbitmap("icon.ico")

    # CENTERING WINDOW
    # Gets the requested values of the height and width.
    windowWidth = root.winfo_reqwidth()
    windowHeight = root.winfo_reqheight()
    # Gets both half the screen width/height and window width/height
    positionRight = int(root.winfo_screenwidth() / 3.7 - windowWidth / 2)
    positionDown = int(root.winfo_screenheight() / 4 - windowHeight / 2)
    # Positions the window in the center of the page.
    root.geometry("+{}+{}".format(positionRight, positionDown))

    # Text in window ; Welcome message
    Label1 = Label(root, text="\n\n\n\n\n\n\n WELCOME TO SHIELD", font="Helvetica 16 bold").pack()
    Label2 = Label(root, text=" \n A Network Configuration Testing Tool ", font="Helvetica 14 bold italic").pack()
    Label3 = Label(root, text="\n To start testing your firewall, click start to proceed. \n \n ", font="Helvetica 13 italic").pack()

    # Invisible "containers" that goes into root
    topFrame = Frame(root)
    topFrame.pack()  #pack makes it display into the window
    bottomFrame = Frame(root)
    bottomFrame.pack(side=BOTTOM)

    # Buttons
    button1 = Button(bottomFrame, text="Exit", command = root.destroy)
    button2 = Button(bottomFrame, text="Start", command = Window_Two)
    button1.pack(side=RIGHT)
    button2.pack(side=RIGHT)

    root.mainloop()



#########################
# CHOOSE TEST CASE WINDOW
#########################
def click_run():
    if URLenable == 1:
        URLFilter()
    if FileBlocking_enable == 1:
        FileBlocking()
    Window_Show_Results()

def Window_Two():
    root = Tk()  # Creates the window; root is main window
    # Window size & Window priority
    root.geometry('800x500')
    root.attributes("-topmost", True)

    # TITLE OF FRAME & ICON
    root.title("SHIELD: A Next Generation Network Configuration Tool")
    root.iconbitmap("icon.ico")

    # CENTERING WINDOW
    # Gets the requested values of the height and width.
    windowWidth = root.winfo_reqwidth()
    windowHeight = root.winfo_reqheight()
    # Gets both half the screen width/height and window width/height
    positionRight = int(root.winfo_screenwidth() / 3.7 - windowWidth / 2)
    positionDown = int(root.winfo_screenheight() / 4 - windowHeight / 2)
    # Positions the window in the center of the page.
    root.geometry("+{}+{}".format(positionRight, positionDown))

    # Text in window
    Label1 = Label(root,text="\n\n\n\n\n LIST OF TEST CASES", font="Helvetica 16 bold").pack()
    Label2 = Label(root,text="\n \n Select one or more of the following options and click on run to view the results.\n",
                   font="Helvetica 13 italic").pack()

    # Invisible "containers" that goes into root
    topFrame = Frame(root)
    topFrame.pack() #pack makes it display into the window
    bottomFrame = Frame(root)
    bottomFrame.pack(side=BOTTOM)

    # CHECKBOXES
    checkedA = Checkbutton(root, text="File Blocking",command = Window_GetFileBlockingInput).pack()
    checkedB = Checkbutton(root, text="Antivirus Monitoring").pack()
    checkedC = Checkbutton(root, text="URL Filtering", command = Window_GetUrlInput).pack()

    # Buttons
    button1 = Button(bottomFrame, text="Cancel", command=root.destroy).pack(side=RIGHT, anchor='se')
    button2 = Button(bottomFrame, text="Run", command=click_run).pack(side=RIGHT, anchor='se')

    root.mainloop()



#########################
# URL FILTERING WINDOW
#########################
def click_UpdateURLs():
    file = open('website_list.txt', 'w')
    file.write(e1.get("1.0", "end"))

def Window_GetUrlInput():
    root = Tk() #Creates the window; root is main window
    #Window size & Window priority
    root.geometry('800x500')
    root.attributes("-topmost",True)

    #TITLE OF FRAME & ICON
    root.title("SHIELD: A Next Generation Network Configuration Tool")
    root.iconbitmap("icon.ico")

    # CENTERING WINDOW
    # Gets the requested values of the height and width.
    windowWidth = root.winfo_reqwidth()
    windowHeight = root.winfo_reqheight()
    # Gets both half the screen width/height and window width/height
    positionRight = int(root.winfo_screenwidth() / 3.7 - windowWidth / 2)
    positionDown = int(root.winfo_screenheight() / 4 - windowHeight / 2)
    # Positions the window in the center of the page.
    root.geometry("+{}+{}".format(positionRight, positionDown))

    #Text in window
    Label1 = Label(root, text="\n\n\n You have selected: URL Filtering\n", font="Helvetica 16 bold").pack()
    Label2 = Label(root, text="Step 1: Provide a list of your URLs.",font="Helvetica 13").pack()
    Label3 = Label(root, text="Step 2: Click on update URLs.", font="Helvetica 13 ").pack()
    Label4 = Label(root, text="Step 3: Click on continue. \n", font="Helvetica 13 ").pack()
    Label5 = Label(root, text="Files :", font="Helvetica 16 bold").pack()
    Label6 = Label(root, text="(Example -> https://www.telus.com)\n", font="Helvetica 13 italic").pack()

    #Invisible "containers" that goes into root
    topFrame=Frame(root)
    topFrame.pack() #pack makes it display into the window
    bottomFrame=Frame(root)
    bottomFrame.pack(side=BOTTOM)

    #TEXTBOX
    global e1
    e1 = Text(root)
    e1.pack()

    global URLenable
    URLenable = 1

    #Buttons
    button2 = Button(bottomFrame, text="Continue", command = root.destroy).pack(side=RIGHT, anchor='se')
    button3 = Button(bottomFrame, text="Cancel", command = root.destroy).pack(side=RIGHT, anchor='se')
    button1 = Button(bottomFrame, text="Update URLs", command=click_UpdateURLs).pack(side=RIGHT, anchor='se')

    root.mainloop()



#########################
# FILE BLOCKING WINDOW
##########################
def click_UpdateBlocking():
    file = open('download_list.txt', 'w')
    file.write(e2.get("1.0", "end"))

def Window_GetFileBlockingInput():
    root = Tk()  # Creates the window; root is main window
    # Window size & Window priority
    root.geometry('800x500')
    root.attributes("-topmost", True)

    # TITLE OF FRAME & ICON
    root.title("SHIELD: A Next Generation Network Configuration Tool")
    root.iconbitmap("icon.ico")

    # CENTERING WINDOW
    # Gets the requested values of the height and width.
    windowWidth = root.winfo_reqwidth()
    windowHeight = root.winfo_reqheight()
    # Gets both half the screen width/height and window width/height
    positionRight = int(root.winfo_screenwidth() / 3.7 - windowWidth / 2)
    positionDown = int(root.winfo_screenheight() / 4 - windowHeight / 2)
    # Positions the window in the center of the page.
    root.geometry("+{}+{}".format(positionRight, positionDown))

    # Text in window
    Label1 = Label(root, text="You have selected: File Blocking", font="Helvetica 16 bold").pack()
    Label2 = Label(root, text="Step 1: Provide a list of your files.", font="Helvetica 13").pack()
    Label3 = Label(root, text="Step 2: Click on update files.", font="Helvetica 13 ").pack()
    Label4 = Label(root, text="Step 3: Click on continue. \n", font="Helvetica 13 ").pack()
    Label5 = Label(root, text="Files :", font="Helvetica 16 bold").pack()
    Label6 = Label(root, text="(Example -> )\n", font="Helvetica 13 italic").pack()

    # Invisible "containers" that goes into root
    topFrame = Frame(root)
    topFrame.pack()  # pack makes it display into the window
    bottomFrame = Frame(root)
    bottomFrame.pack(side=BOTTOM)

    # TEXTBOX
    global e2
    e2 = Text(root)
    e2.pack()

    global FileBlocking_enable
    FileBlocking_enable = 1

    # Buttons
    button2 = Button(bottomFrame, text="Continue", command= root.destroy).pack(side=RIGHT, anchor='se')
    button3 = Button(bottomFrame, text="Cancel", command = root.destroy).pack(side=RIGHT, anchor='se')
    button1 = Button(bottomFrame, text="Update Files", command=click_UpdateBlocking).pack(side=RIGHT, anchor='se')

    root.mainloop()


#########################
# WINDOW DISPLAYS THE RESULTS
##########################
def Window_Show_Results():
    root = Tk()  # Creates the window; root is main window
    # Window size & Window priority
    root.geometry('800x500')
    root.attributes("-topmost", True)

    # TITLE OF FRAME & ICON
    root.title("SHIELD: A Next Generation Network Configuration Tool")
    root.iconbitmap("icon.ico")

    Label1=root.Label(root, text="TEST RESULTS \n \n", font="Helvetica 16 bold").pack()  # message on screen

    # CENTERING WINDOW
    # Gets the requested values of the height and width.
    windowWidth = root.winfo_reqwidth()
    windowHeight = root.winfo_reqheight()
    # Gets both half the screen width/height and window width/height
    positionRight = int(root.winfo_screenwidth() / 3.7 - windowWidth / 2)
    positionDown = int(root.winfo_screenheight() / 4 - windowHeight / 2)
    # Positions the window in the center of the page.
    root.geometry("+{}+{}".format(positionRight, positionDown))


    root.mainloop()