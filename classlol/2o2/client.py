from tkinter import *
from threading import Thread
import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


ip_address = '127.0.0.1'
port = 8000


client.connect((ip_address, port))


class GUI:
    def __init__(self):
        self.window=Tk()
        self.window.withdraw()

        self.login=Toplevel()
        self.login.title("chat application")
        self.login.resizable(width=False,height=False)
        self.login.configure(bg="gold",width=380,height=400)
        self.app_label=Label(self.login,text="Login Page",fg="red",bg="gold",font=("Calibri",30))
        self.app_label.place(relx=0.2,rely=0.7,relheight=0.15)
        self.name_label=Label(self.login,text="Username:", fg="black",bg="gold",font=("Calibri",20))
        self.name_label.place(relx=0.1,rely=0.2,relheight=0.2,)
        self.userName= Entry(self.login,text="",bd=2,width=25)
        self.userName.place(relx=0.55,rely=0.25,relheight=0.12,relwidth=0.4)

        self.login_button=Button(self.login,text="Login",fg="black",bg="lightblue",font=("Calibri",12),command=lambda:self.navigate_chatRoom(self.userName.get()))
        self.login_button.place(relx=0.4,rely=0.55)
        self.window.mainloop()

    def navigate_chatRoom(self,name):
        self.login.destroy()
        self.chatRoom(name)
        r= Thread(target=self.receive)
        r.start()
        
    def chatRoom(self,name):
        self.name=name
        self.window.deiconify()
        self.window.title("chat r00m")
        self.window.resizable(width=False,height=False)
        self.window.configure(bg="gold",width=470,height=550)

        self.labelhead=Label(self.window,bg="red",fg="white",text=self.name,font="Helvetica 13 bold",pady=5)
        self.labelhead.place(relwidth=1)

        self.line=Label(self.window,width=400,bg="gray")
        self.line.place(relwidth=1,rely=0.07,relheight=0.012)

        self.textCons=Text(self.window,width=20,height=2,bg="blue",fg="white",font="Helvtica 13 bold",padx=5,pady=5)
        self.textCons.place(relheight=0.75,relwidth=1,rely=0.08)

        self.labelBottom=Label(self.window,bg="yellow",height=80)
        self.labelBottom.place(relwidth=1,rely=0.825)

        self.entryMsg=Entry(self.labelBottom,bg="pink",fg="white",font="Helvetica 13 bold")
        self.entryMsg.place(relwidth=0.75,relheight=0.06,rely=0.008,relx=0.011)

        self.sendButton=Button(self.labelBottom,text="send",font="Helvetica 10 bold",width=20,bg="skyblue",command=lambda:self.sendingMessage(self.entryMsg.get()))
        self.sendButton.place(relheight=0.06,relwidth=0.22,relx=0.77,rely=0.008)

        self.textCons.config(cursor="arrow")
        
        scrollbar=Scrollbar(self.textCons)
        scrollbar.place(relheight=1,relx=0.95)
        scrollbar.config(command=self.textCons.yview)

        self.textCons.config(state=DISABLED)

    def sendingMessage(self,msg):
         self.textCons.config(state=DISABLED)
         self.msg=msg
         self.textCons.delete(0,END)
         send=Thread(target=self.write)
         send.start()

    def show_message(self,message):
        self.textCons.config(state=NORMAL)
        self.textCons.insert(END,message+"\n\n")
        self.textCons.config(state=DISABLED)
        self.textCons.see(END)

    def write(self):
        self.textCons.config(state=DISABLED)
        while True:
            message=(f"{self.name}:{self.msg}")
            client.send(message.encode('utf-8'))
            self.show_message(message)
            break
    def receive(self):
        while True:
            try:
                message=client.recv(2046).decode('utf-8')
                if message=='NICKNAME':
                    client.send(self.name.encode('utf-8'))
                else:
                    self.show_message(message)
            except:
                print("An error occured...")
                client.close()
                break


g=GUI()

