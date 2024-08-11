import tkinter as tk
from tkinter import messagebox

class my_app(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("800x500+900+50")
        self.iconbitmap("bayrak.ico")
        self.title("First App")
        self.resizable(False,False)
        self.box_left = tk.LabelFrame(text="Settings",width=200,height=500,bg="blue",bd=5)
        self.box_left.grid_propagate(False)
        self.box_left.grid(row=0,column=0)

        self.box_right =  tk.LabelFrame(text="Screen",width=600,height=500,bg="gray73",bd=5)
        self.box_right.grid_propagate(False)
        self.box_right.grid(row=0,column=1)



class root(my_app):
    def __init__(self):
        super().__init__()
        self.btn1 = tk.Button(self.box_left,text = "Users",bd=2,width=15,bg="yellow",command=self.user_func)
        self.btn1.grid(row=0,column=0,padx=36.5,pady=10)

        self.btn2 = tk.Button(self.box_left,text = "Add user",bd=2,width=15,bg="yellow",command=self.add_user_func)
        self.btn2.grid(row=2,column=0,padx=36.5,pady=0)

        self.btn3 = tk.Button(self.box_left,text = "Delete user",bd=2,width=15,bg="yellow",command=self.delete_user_func)
        self.btn3.grid(row=3,column=0,padx=36.5,pady=10)

        self.btn4 = tk.Button(self.box_left,text = "Update user",bd=2,width=15,bg="yellow",command=self.update_user_func)
        self.btn4.grid(row=4,column=0,padx=36.5,pady=0)

class root2(root):
    users = []
    def __init__(self):
        super().__init__()

    def body_remove(self):
        for i in self.box_right.winfo_children():
            i.destroy()
    
    def user_func(self):
        self.body_remove()
        self.box_right["text"] = "users"
        tk.Label(self.box_right,text="Number of users",width=10,bg="blue").grid(row=0,column=0)
        tk.Label(self.box_right,text="Name",width=10,bg="blue").grid(row=0,column=1)
        tk.Label(self.box_right,text="Surname",width=10,bg="blue").grid(row=0,column=2)
        tk.Label(self.box_right,text="Age",width=10,bg="blue").grid(row=0,column=3)
        tk.Label(self.box_right,text="Job",width=10,bg="blue").grid(row=0,column=4)
        tk.Label(self.box_right,text="gender",width=10,bg="blue").grid(row=0,column=5)

        for index,i in enumerate(self.users):

            tk.Label(self.box_right,text=f"User {index+1}").grid(row=index+1,column=0)
            tk.Label(self.box_right,text = i.name).grid(row=index+1,column=1)
            tk.Label(self.box_right,text = i.surname).grid(row=index+1,column=2)
            tk.Label(self.box_right,text = i.age).grid(row=index+1,column=3)
            tk.Label(self.box_right,text = i.job).grid(row=index+1,column=4)
            tk.Label(self.box_right,text = i.gender).grid(row=index+1,column=5)

    
    def add_user_func(self):
        self.body_remove()

        self.box_right["text"] = "Add user"

        self.name_label = tk.Label(self.box_right,text="Name:",bg = "yellow",width=10)
        self.name_label.grid(row=0,column=0)
        self.input_name = tk.Entry(self.box_right)
        self.input_name.grid(row=0,column=1,padx=5,sticky="w")

        self.surname_label = tk.Label(self.box_right,text="Surname:",bg = "yellow",width=10)
        self.surname_label.grid(row=1,column=0)
        self.input_surname = tk.Entry(self.box_right)
        self.input_surname.grid(row=1,column=1,padx=5,sticky="w")

        self.age_label = tk.Label(self.box_right,text="Age:",bg = "yellow",width=10)
        self.age_label.grid(row=2,column=0)
        self.input_age = tk.Entry(self.box_right)
        self.input_age.grid(row=2,column=1,padx=5,sticky="w")

        self.job_label = tk.Label(self.box_right,text="Job:",bg = "yellow",width=10)
        self.job_label.grid(row=3,column=0)
        self.input_job = tk.Entry(self.box_right)
        self.input_job.grid(row=3,column=1,padx=5,sticky="w")

        self.gender_label = tk.Label(self.box_right,text="Gender:",bg = "yellow",width=10)
        self.gender_label.grid(row=4,column=0)
        self.input_gender = tk.Entry(self.box_right)
        self.input_gender.grid(row=4,column=1,padx=5,sticky="w")

        self.tamam_buton = tk.Button(self.box_right,text="okey",bg="yellow",width=10,command= self.create_user_func)
        self.tamam_buton.grid(row=5,column=1)

    def delete_user_func(self):
        self.body_remove()
        self.box_right["text"] = "Delete user"
        
        tk.Label(self.box_right,text="Number of users",width=10,bg="blue").grid(row=0,column=0)
        tk.Label(self.box_right,text="Name",width=10,bg="blue").grid(row=0,column=1)
        tk.Label(self.box_right,text="Surname",width=10,bg="blue").grid(row=0,column=2)
        tk.Label(self.box_right,text="Age",width=10,bg="blue").grid(row=0,column=3)
        tk.Label(self.box_right,text="Job",width=10,bg="blue").grid(row=0,column=4)
        tk.Label(self.box_right,text="Gender",width=10,bg="blue").grid(row=0,column=5)

        for index,i in enumerate(self.users):

            tk.Label(self.box_right,text=f"user {index+1}").grid(row=index+1,column=0)
            tk.Label(self.box_right,text = i.name).grid(row=index+1,column=1)
            tk.Label(self.box_right,text = i.surname).grid(row=index+1,column=2)
            tk.Label(self.box_right,text = i.age).grid(row=index+1,column=3)
            tk.Label(self.box_right,text = i.job).grid(row=index+1,column=4)
            tk.Label(self.box_right,text = i.gender).grid(row=index+1,column=5)
            tk.Button(self.box_right,text="kullanıcı sil",bg="red",command=lambda a = i.name : self.user_del(a)).grid(row=index+1,column=6)

        

    def update_user_func(self):
        self.body_remove()
        self.box_right["text"] = "update user"

        self.new_frame = tk.Frame(self.box_right,width=600,height=300)
        self.box_left.grid_propagate(False)
        self.new_frame.grid(row=0,column=1)
        tk.Label(self.new_frame,text="number of users",width=10,bg="blue").grid(row=0,column=0)
        tk.Label(self.new_frame,text="Name",width=10,bg="blue").grid(row=0,column=1)
        tk.Label(self.new_frame,text="Surname",width=10,bg="blue").grid(row=0,column=2)
        tk.Label(self.new_frame,text="Age",width=10,bg="blue").grid(row=0,column=3)
        tk.Label(self.new_frame,text="Job",width=10,bg="blue").grid(row=0,column=4)
        tk.Label(self.new_frame,text="Gender",width=10,bg="blue").grid(row=0,column=5)

        for index,i in enumerate(self.users):

            tk.Label(self.new_frame,text=f"user {index+1}").grid(row=index+1,column=0)
            tk.Label(self.new_frame,text = i.name).grid(row=index+1,column=1)
            tk.Label(self.new_frame,text = i.surname).grid(row=index+1,column=2)
            tk.Label(self.new_frame,text = i.age).grid(row=index+1,column=3)
            tk.Label(self.new_frame,text = i.job).grid(row=index+1,column=4)
            tk.Label(self.new_frame,text = i.gender).grid(row=index+1,column=5)
            tk.Button(self.new_frame,text="update user",bg="red",
                      command=lambda name= i.name, surname = i.surname, age = i.age, job = i.job, gender = i.gender : self.user_update(name,surname,age,job,gender)).grid(row=index+1,column=6)

        self.new_frame1 = tk.Frame(self.box_right,width=600,height=300,bg="gray")
        self.new_frame1.grid_propagate(False)
        self.new_frame1.grid(row=1,column=1)


        
    def user_update(self,name,surname,age,job,gender):
        for x in self.new_frame1.winfo_children():
            x.destroy()
        


        self.name_label = tk.Label(self.new_frame1,text="Name:",bg = "yellow",width=10)
        self.name_label.grid(row=0,column=0)
        self.input_name = tk.Entry(self.new_frame1)
        self.input_name.grid(row=0,column=1,padx=5,sticky="w")
        self.input_name.insert(0,name)

        self.surname_label = tk.Label(self.new_frame1,text="Surname:",bg = "yellow",width=10)
        self.surname_label.grid(row=1,column=0)
        self.input_surname = tk.Entry(self.new_frame1)
        self.input_surname.grid(row=1,column=1,padx=5,sticky="w")
        self.input_surname.insert(0,surname)

        self.age_label = tk.Label(self.new_frame1,text="Age:",bg = "yellow",width=10)
        self.age_label.grid(row=2,column=0)
        self.input_age = tk.Entry(self.new_frame1)
        self.input_age.grid(row=2,column=1,padx=5,sticky="w")
        self.input_age.insert(10,age)

        self.job_label = tk.Label(self.new_frame1,text="Job:",bg = "yellow",width=10)
        self.job_label.grid(row=3,column=0)
        self.input_job = tk.Entry(self.new_frame1)
        self.input_job.grid(row=3,column=1,padx=5,sticky="w")
        self.input_job.insert(0,job)

        self.gender_label = tk.Label(self.new_frame1,text="Gender:",bg = "yellow",width=10)
        self.gender_label.grid(row=4,column=0)
        self.input_gender = tk.Entry(self.new_frame1)
        self.input_gender.grid(row=4,column=1,padx=5,sticky="w")
        self.input_gender.insert(0,gender)

        self.tamam_buton = tk.Button(self.new_frame1,text="okey",bg="yellow",width=10,command= lambda name = name : self.user_update2(name))
        self.tamam_buton.grid(row=5,column=1)

    def user_update2(self,x):
        for i in self.users:
            if i.name == x:
                i.name = self.input_name.get()
                i.surname = self.input_surname.get()
                i.age = self.input_age.get()
                i.job = self.input_job.get()
                i.gender = self.input_gender.get()
        self.update_user_func()

            

    
    def create_user_func(self):
        user = user_create(self.input_name.get(),self.input_surname.get(),self.input_age.get(),self.input_job.get(),self.input_gender.get())
        self.users.append(user)
        messagebox.showinfo(title="notice",message = "saved")


    @classmethod
    def func(cls,data):
        for i in data:
            user = user_create(i["name"],i["surname"],i["age"],i["job"],i["gender"])
            cls.users.append(user)

    def user_del(self,name):
        for i in self.users:
            if i.name == name:
                self.users.remove(i)
        self.delete_user_func()

                


class user_create:
    def __init__(self,name,surname,age,job,gender):
        self.name = name
        self.surname = surname
        self.age = age
        self.job = job
        self.gender = gender

data= [
    {"name":"yusuf","surname":"yılmaz","age":"22","job":"developer","gender":"erkek"},
    {"name":"yiğit","surname":"altın","age":"20","job":"yazılımcı","gender":"erkek"},
    {"name":"hüsyin","surname":"yalcın","age":"21","job":"dev","gender":"erkek"},
    {"name":"mehmet","surname":"akar","age":"22","job":"doktor","gender":"erkek"},
]

root2.func(data)


window = root2()
window.mainloop()
    

