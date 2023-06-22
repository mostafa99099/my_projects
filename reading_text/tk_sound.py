from tkinter import *
from functools import partial
from gtts import gTTS
import playsound
import os


def printDetails(usernameEntry):
    i = 1
    while i > 0:
        x = usernameEntry.get()
        tts = gTTS(text=x, lang="en")
        file1 = str("sound" + str(i) + ".mp3")
        tts.save(file1)
        playsound.playsound(file1, True)

        os.remove(file1)
        i += 1
        break

    return


# window
tkWindow = Tk()
tkWindow.geometry("500x500")
tkWindow.title("Python Examples")

# label
usernameLabel = Label(tkWindow, text="Enter your text")
# entry for user input
usernameEntry = Entry(tkWindow)

# define callable function with printDetails function and usernameEntry argument
printDetailsCallable = partial(printDetails, usernameEntry)

# submit button
submitButton = Button(tkWindow, text="Enter", command=printDetailsCallable)

# place label, entry, and button in grid
usernameLabel.grid(row=0, column=0)
usernameEntry.grid(row=0, column=1)
submitButton.grid(row=1, column=1)

# main loop
tkWindow.mainloop()
