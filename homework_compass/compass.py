import tkinter
window = tkinter.Tk()
window.title("compass")
window.geometry("500x500")
label = tkinter.Label(text = "north", font = "arial 22")
label.place(x= 200, y= 10)
label = tkinter.Label(text = "south", font = "arial 22")
label.place(x= 200, y= 300)
label = tkinter.Label(text = "west", font = "arial 22")
label.place(x= 20, y= 150)
label = tkinter.Label(text = "east", font = "arial 22")
label.place(x= 340, y= 150)
label = tkinter.Label(text = "/\ \n| \n| \n| \n\/ ", font= "arial 22")
label.place(x= 210, y= 110)
window.mainloop()