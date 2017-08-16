#requires root
import tkinter as tk

canvas_width=100
canvas_height=10
top=tk.Tk()

f0=open("/etc/resolv.conf","w")
x="nameserver 8.8.8.8\nnameserver 8.8.4.4"
f0.writelines(x)
w= tk.Label(top,text="etc has been changed please run service network-manager restart",bg="lightblue",fg="black",width=canvas_width,height=canvas_height)
w.pack()


top.mainloop()
