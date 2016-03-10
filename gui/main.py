from tkinter import Tk
from tkinter import ttk
from tkinter import filedialog
from xls2db import xls2db

root = Tk()
fnm = ''
def Quit(ev):
    global root
    root.destroy()

def LoadFile(ev):
    global fnm
    fn = filedialog.Open(root, filetypes = [('*.xls XLS Files', '.xls')]).show()
    if fn == '':
        return
    fnm = fn

def SaveFile(ev):
    global fnm
    fn = filedialog.SaveAs(root, filetypes = [('*.db sqlite3 files', '.db')]).show()
    if fn == '':
        return
    if not fn.endswith(".db"):
        fn += ".db"


    xls2db(fnm,fn)

loadBtn = ttk.Button(root, text = 'XLS Load')
saveBtn = ttk.Button(root, text = 'DB Save')
quitBtn = ttk.Button(root, text = 'Quit')

loadBtn.bind("<Button-1>", LoadFile)
saveBtn.bind("<Button-1>", SaveFile)
quitBtn.bind("<Button-1>", Quit)

loadBtn.pack()
saveBtn.pack()
quitBtn.pack()

root.mainloop()
