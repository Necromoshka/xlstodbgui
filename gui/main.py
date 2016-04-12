from tkinter import Tk
from tkinter import ttk
from tkinter import filedialog
from xls2db import xls2db

root = Tk()
fnm = ''


def quit_f():
    global root
    root.destroy()


def loadfile():
    global fnm
    fn = filedialog.Open(root, filetypes=[('*.xls XLS Files', '.xls')]).show()
    if fn == '':
        return
    fnm = fn


def savefile():
    global fnm
    fn = filedialog.SaveAs(root, filetypes=[('*.db sqlite3 files', '.db')]).show()
    if fn == '':
        return
    if not fn.endswith(".db"):
        fn += ".db"
    xls2db(fnm, fn)

loadBtn = ttk.Button(root, text='XLS Load')
saveBtn = ttk.Button(root, text='DB Save')
quitBtn = ttk.Button(root, text='quit_f')
loadBtn.bind("<Button-1>", loadfile)
saveBtn.bind("<Button-1>", savefile)
quitBtn.bind("<Button-1>", quit_f)
loadBtn.pack()
saveBtn.pack()
quitBtn.pack()
root.mainloop()
