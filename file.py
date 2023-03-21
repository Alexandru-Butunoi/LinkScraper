import tkinter
import webbrowser
from data import getting_data


def print_input():
	file = open('Links.txt', 'w')
	data = getting_data(str(user_input.get()))
	for l in data:
		file.write(str(l) + "\n")


root = tkinter.Tk()
root.geometry("400x300")
root.title('Link_Finder')

frame = tkinter.Frame(root)
frame.pack()

first_section = tkinter.LabelFrame(frame, text="first_Section", padx= 20, pady= 10)
first_section.grid(row=0, column=0)

web_page = tkinter.Label(first_section, text="example: https://www.google.co.uk/", padx=30, font= 2)
web_page.grid(row=0, column=0)

web_button = tkinter.Button(first_section, text= "search links", padx= 20, command = print_input)
web_button.grid(row=1, column=0)

user_input = tkinter.Entry(first_section, cursor = 'arrow', width = 50)
user_input.grid(row = 2, column = 0)


root.mainloop()