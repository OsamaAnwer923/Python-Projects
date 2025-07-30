import tkinter


screen = tkinter.Tk()
screen.minsize(width=100,height=100)
screen.config(padx=20,pady=20)
screen.title('Mile to Kilometer Converter')


mile_entry = tkinter.Entry(width=20)
mile_entry.grid(column=2,row=1)

miles_label = tkinter.Label(text='Mile')
miles_label.grid(column=3,row=1)


equal_label = tkinter.Label(text='is equal to')
equal_label.grid(column=1,row=2)

kmvalue_label = tkinter.Label(text=0)
kmvalue_label.grid(column=2,row=2)

km_label = tkinter.Label(text='Kilometer')
km_label.grid(column=3,row=2)

def mile_converter(mile):
    km = mile * 1.609
    return km

def on_click():
    mile = float(mile_entry.get())
    answer_in_km = mile_converter(mile)
    kmvalue_label.config(text=answer_in_km)

button = tkinter.Button(text='Calculate',command=on_click)
button.grid(column=2,row=3)

screen.mainloop()