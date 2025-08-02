import tkinter
from tkinter import messagebox
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
import random
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letter = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_symbol = [random.choice(symbols) for _ in range(random.randint(2,4))]
    password_numbers = [random.choice(numbers) for _ in range(random.randint(2,4))]
    password_list = password_letter + password_symbol + password_numbers
    random.shuffle(password_list)
    password = ''.join(password_list)
    password_entry.insert(0,password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_values():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title='Error',message='Yor left some field empty')
    else:
        is_ok=messagebox.askokcancel(title='Confirmation',message=f'Details Entered are \n \t Website:{website} \n \t Username/Email:{username} \n \t Password:{password}')
        if is_ok:
            with open(r'G:\osama\TO DO OSAMA\Python Projects(100 Days of Python Boot Camp)\30-password-manager-start\password.txt','a') as file:
                file.write(f'{website} | {username} | {password}\n' )
                website_entry.delete(0,tkinter.END)
                username_entry.delete(0,tkinter.END)
                password_entry.delete(0,tkinter.END)

# ---------------------------- UI SETUP ------------------------------- #

window = tkinter.Tk()
window.title('Password Manager')
window.config(padx=20,pady=20)

canvas = tkinter.Canvas(width=200,height=200)
logo_image = tkinter.PhotoImage(file=r'G:\osama\TO DO OSAMA\Python Projects(100 Days of Python Boot Camp)\30-password-manager-start\logo.png')
canvas.create_image(100,100,image=logo_image)
canvas.grid(row=1,column=2)

website_Label = tkinter.Label(text='Website:')
website_Label.grid(column=1,row=2)

website_entry = tkinter.Entry(width=48)
website_entry.grid(row=2,column=2,columnspan=2)
website_entry.focus()

username_Label = tkinter.Label(text='Email/Username:')
username_Label.grid(column=1,row=3)

username_entry = tkinter.Entry(width=48)
username_entry.grid(row=3,column=2,columnspan=2)
username_entry.insert(0,'username@gmail.com')

password_Label = tkinter.Label(text='Password:')
password_Label.grid(column=1,row=4)

password_entry = tkinter.Entry(width=30)
password_entry.grid(row=4,column=2)

generate_button = tkinter.Button(text='Generate Password',command=generate_password)
generate_button.grid(row=4,column=3)

add_button = tkinter.Button(text='Add',width=40,command=add_values)
add_button.grid(row=5,column=2,columnspan=2)

window.mainloop()


