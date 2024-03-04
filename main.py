from tkinter import *
import tkinter
root = Tk()
root.title("CALCULADORA")
root.geometry("490x546")
root.resizable(False,False)

fonte = ('Helvetica', 75)

topo = Entry(root, width=9, bg="#000000", fg="#ffffff", font=fonte)
topo.place(x=0, y=0)


n1 = tkinter.Button(root,
                    text="1",
                    width=17,
                    height=5
                    )
n1.place(x=0, y=116)

n2 = tkinter.Button(root,
                    text="2",
                    width=17,
                    height=5
                    )
n2.place(x=126, y=116)

n3 = tkinter.Button(root,
                    text="3",
                    width=17,
                    height=5
                    )
n3.place(x=242, y=116)

n4 = tkinter.Button(root,
                    text="4",
                    width=17,
                    height=5
                    )
n4.place(x=0, y=202)

n5 = tkinter.Button(root,
                    text="5",
                    width=17,
                    height=5
                    )
n5.place(x=126, y=202)

n6 = tkinter.Button(root,
                    text="6",
                    width=17,
                    height=5
                    )
n6.place(x=242, y=202)

n7 = tkinter.Button(root,
                    text="7",
                    width=17,
                    height=5
                    )
n7.place(x=0, y=288)

n8 = tkinter.Button(root,
                    text="8",
                    width=17,
                    height=5
                    )
n8.place(x=126, y=288)

n9 = tkinter.Button(root,
                    text="9",
                    width=17,
                    height=5
                    )
n9.place(x=242, y=288)

n0 = tkinter.Button(root,
                    text="0",
                    width=34,
                    height=5
                    )
n0.place(x=0, y=374)

virgula = tkinter.Button(root,
                    text=".",
                    width=17,
                    height=5
                    )
virgula.place(x=242, y=374)

dele = tkinter.Button(root,
                    text="c",
                    width=17,
                    height=5
                    )
dele.place(x=0, y=460)

divi = tkinter.Button(root,
                    text="÷",
                    width=17,
                    height=5,
                    bg="#2A9DF4"
                    )
divi.place(x=365, y=116)

multi = tkinter.Button(root,
                    text="X",
                    width=17,
                    height=5,
                    bg="#2A9DF4"
                    )
multi.place(x=365, y=202)

soma = tkinter.Button(root,
                    text="+",
                    width=17,
                    height=5,
                    bg="#2A9DF4"
                    )
soma.place(x=365, y=288)

sub = tkinter.Button(root,
                    text="-",
                    width=17,
                    height=5,
                    bg="#2A9DF4"
                    )
sub.place(x=365, y=374)

igual = tkinter.Button(root,
                    text="=",
                    width=17,
                    height=5,
                    bg="#2A9DF4"
                    )
igual.place(x=365, y=460)

root.mainloop()