from tkinter import *
import os

from Models import HumanData

class EncryptGUI(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.grid()
        self.Var = IntVar()
        self.createWidgets()
    def createWidgets(self):
#1
        self.employeeIDText = Label(self)
        self.employeeIDText["text"] = "職工代碼:"
        self.employeeIDText.grid(row=0, column=0)
        self.employeeIDField = Entry(self)
        self.employeeIDField["width"] = 15
        self.employeeIDField.grid(row=0, column=1, columnspan=1)

        self.IDText = Label(self)
        self.IDText["text"] = "身份證字號:"
        self.IDText.grid(row=0, column=2)
        self.IDField = Entry(self)
        self.IDField["width"] = 15
        self.IDField.grid(row=0, column=3, columnspan=1)
#2
        self.nameText = Label(self)
        self.nameText["text"] = "職工名字:"
        self.nameText.grid(row=1, column=0)
        self.nameField = Entry(self)
        self.nameField["width"] = 15
        self.nameField.grid(row=1, column=1, columnspan=1)

        self.emailText = Label(self)
        self.emailText["text"] = "E-mail:"
        self.emailText.grid(row=1, column=2)
        self.emailField = Entry(self)
        self.emailField["width"] = 15
        self.emailField.grid(row=1, column=3, columnspan=1)
#3
        self.phoneText = Label(self)
        self.phoneText["text"] = "手機號碼:"
        self.phoneText.grid(row=2, column=0)
        self.phoneField = Entry(self)
        self.phoneField["width"] = 15
        self.phoneField.grid(row=2, column=1, columnspan=1)

        self.birthplaceText = Label(self)
        self.birthplaceText["text"] = "出生地:"
        self.birthplaceText.grid(row=2, column=2)
        self.birthplaceField = Entry(self)
        self.birthplaceField["width"] = 15
        self.birthplaceField.grid(row=2, column=3, columnspan=1)
#4
        self.nationText = Label(self)
        self.nationText["text"] = "籍貫:"
        self.nationText.grid(row=3, column=0)
        self.nationField = Entry(self)
        self.nationField["width"] = 15
        self.nationField.grid(row=3, column=1, columnspan=1)

        self.sexText = Label(self)
        self.sexText["text"] = "性別:"
        self.sexText.grid(row=3, column=2)
        self.sexRadio = Radiobutton(self)
        self.sexRadio["text"]="男"
        self.sexRadio["variable"] = self.Var
        self.sexRadio["value"]=1
        self.sexRadio.grid(row=3, column=3,columnspan=1)
        self.sexRadio = Radiobutton(self)
        self.sexRadio["text"]="女"
        self.sexRadio["variable"] = self.Var
        self.sexRadio["value"]=0
        self.sexRadio.grid(row=3, column=4,columnspan=1)
#5
        self.accept = Button(self)
        self.accept["text"] = "確認"
        self.accept.grid(row=4, column=0)
        self.accept["command"] =  self.acceptEvent

        self.select = Button(self)
        self.select["text"]="選擇"
        self.select.grid(row=4,column=1)
        self.select["command"] = self.selectEvent

        self.displayText = Label(self)
        self.displayText["text"] = "something happened"
        self.displayText.grid(row=4, column=2, columnspan=7)
#6

        self.scrollbar = Scrollbar(self,orient=VERTICAL)
        self.scrollbar.grid(sticky=N+S+E,row=5)
        self.scrollbarx = Scrollbar(self,orient=HORIZONTAL)
        self.scrollbarx.grid(sticky=W+S+E,row=6,column=1,columnspan=8)
        self.listBox=Listbox(self)
        self.listBox['width']=70
        self.listBox.grid(row=5,column=1,columnspan=8)
        self.listBox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.listBox.yview)
        self.listBox.config(xscrollcommand=self.scrollbarx.set)
        self.scrollbarx.config(command=self.listBox.xview)
        self.comment=person.SELECT()
        self.listBox.insert(0,("職工代碼",
                               "身份證字號",
                               "職工名字",
                               "E-mail",
                               "手機號碼",
                               "出生地",
                               "籍貫",
                               "性別"))
        k=1
        for i in self.comment:
            self.listBox.insert(k,i)

    def acceptEvent(self):
        e = self.employeeIDField.get()
        print(e)
        self.displayText["text"] = e
        self.code=person.INSERT((self.employeeIDField.get(),
                                 self.IDField.get(),
                                 self.nameField.get(),
                                 self.emailField.get(),
                                 self.phoneField.get(),
                                 self.birthplaceField.get(),
                                 self.nationField.get(),
                                 self.Var.get()))
        if self.code == 1062:
            person.UPDATE((self.employeeIDField.get(),
                           self.IDField.get(),
                           self.nameField.get(),
                           self.emailField.get(),
                           self.phoneField.get(),
                           self.birthplaceField.get(),
                           self.nationField.get(),
                           self.Var.get(),
                           self.employeeIDField.get()))
            print("employee data update!")

    def selectEvent(self):
        i = self.listBox.curselection()
        j = self.listBox.get(i[0])

        self.employeeIDField.insert(0,str(j[0]))
        self.IDField.insert(0,str(j[1]))
        self.nameField.insert(0,str(j[2]))
        self.emailField.insert(0,str(j[3]))
        self.phoneField.insert(0,str(j[4]))
        self.birthplaceField.insert(0,str(j[5]))
        self.nationField.insert(0,str(j[6]))
        self.Var.set(j[7])

        print(j)

if __name__ == '__main__':
    person=HumanData.HRIS('root','saxo123','127.0.0.1','HumanResource')
    root = Tk()
    root.resizable(0,0)
    app = EncryptGUI(master=root)
    app.mainloop()
