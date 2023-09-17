from tkinter import *
import os 

def restart():
    os.system("shutdown -r -t 1")

def shutdown():
    os.system("shutdown -s -t 1")

def shutdown_time():
    os.system("shutdown -s -t 20")


st = Tk()
st.title( " shut down app ")
st.geometry("500x500")
st.config(bg= "gray")
#reatart
r_button = Button(st,text = "restart", font=("aria",30, "bold"), bg = "red" , cursor = "plus" , command = restart )
r_button.place(x=160, y = 80, width= 200, height=40 )
#restart with time 
r_button = Button(st,text = "shutdown", font=("aria",30, "bold"), bg = "red" ,cursor = "plus", command = shutdown )
r_button.place(x=160, y = 160, width= 200, height=40 )
#shutdown
r_button = Button(st,text = "shutdown_time", font=("aria",30, "bold"), bg = "red" ,cursor = "plus", command = shutdown_time )
r_button.place(x=110, y = 240, width= 300, height=40 )
#sleep
r_button = Button(st,text = "close", font=("aria",30, "bold"), bg = "red" ,cursor = "plus",command= st.destroy )
r_button.place(x=160, y = 320, width= 200, height=40 )


st.mainloop()
