import tkinter

def buttonPressed():
    print("hello")


window = tkinter.Tk()
window.title("my window!")
label1 = tkinter.Label(window, text="Hello")
button1 = tkinter.Button(window, text="Press here", bg="red", fg="blue", command=buttonPressed)
label1.pack()
button1.pack()
window.mainloop()