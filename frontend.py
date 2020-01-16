from tkinter import *

window = Tk()

auth_frame = Frame(window)
auth_frame.pack()

cluster_label = Label(auth_frame, text='Cluster:')
cluster_label.grid(row=0, column=0, sticky='nw')

clusters = ['dev', 'qa', 'stg01', 'stg02']
variable = StringVar(auth_frame)
variable.set(clusters[0])

cluster_dropdown = OptionMenu(auth_frame, variable, *clusters)
cluster_dropdown.config(width=10)
cluster_dropdown.grid(row=0, column=1, sticky='n')

email_label = Label(auth_frame, text='Email:')
email_label.grid(row=1, column=0, sticky='nw')

email_entry = Entry(auth_frame, width=35)
email_entry.grid(row=1, column=1, sticky='nw')

password_label = Label(auth_frame, text='Password:')
password_label.grid(row=2, column=0, sticky='nw')

password_entry = Entry(auth_frame, width=35)
password_entry.grid(row=2, column=1, sticky='nw')

token_button = Button(auth_frame, text='Get token', width=15)
token_button.grid(row=3, column=0, columnspan=2)

feed_label = Label(auth_frame, text='FeedId: ')
feed_label.grid(row=4, column=0, columnspan=2, sticky='w')


# def ok():
#     print("value is:" + variable.get())
# button = Button(window, text="OK", command=ok)
# button.grid(row=1, column=0)

window.mainloop()
