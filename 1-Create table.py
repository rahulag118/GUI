import sqlite3

from scrollingarea import*
from tkinter import*
tk=Tk()
tk.geometry("1366x768+0+0")
#tk.mainloop()
def home():
    frame1=Frame(tk,width=1366,height=768)
    frame1.pack()
    scrolling_area = Scrolling_Area(frame1,height=220)
    scrolling_area.place(x=0, y=0)
    table = Table(scrolling_area.innerframe,
                  ["Name", "Course", "Contact", "College", "Email", "Year"],
                  column_minwidths=[222, 222, 222, 220, 220, 220, 220])
    table.pack(expand=True, fill=X)

    #table.on_change_data(scrolling_area.update_viewpor)
    frame1.mainloop()

home()