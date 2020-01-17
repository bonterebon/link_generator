from tkinter import *
from backend import *

window = Tk()
token = ''
feed_id = ''


def get_token_click():
    global token, feed_id
    token = get_token(variable.get(), email_entry.get(), password_entry.get())
    feed_id = get_feed_id(variable.get(), token)
    feed_id_label['text'] = feed_id
    token_entry.delete(0, END)
    token_entry.insert(END, token)


def generate_link_click():
    global token, feed_id
    link = generate_link(variable.get(), feed_id, start_entry.get(), end_entry.get(), token)
    print(link)
    link_entry.delete(0, END)
    link_entry.insert(END, link)


cluster_label = Label(window, text='Cluster:')
cluster_label.grid(row=0, column=0, sticky='nw', pady=5)

clusters = ['dev', 'qa', 'stg01', 'stg02']
variable = StringVar(window)
variable.set(clusters[0])

cluster_dropdown = OptionMenu(window, variable, *clusters)
cluster_dropdown.config(width=10)
cluster_dropdown.grid(row=0, column=1, sticky='n')

email_label = Label(window, text='Email:')
email_label.grid(row=1, column=0, sticky='nw', pady=5)

email_entry = Entry(window, textvariable='olatest_1@protonmail.com', width=40)
email_entry.grid(row=1, column=1, sticky='nw', pady=5)
email_entry.insert(END, 'olatest_1@protonmail.com')

password_label = Label(window, text='Password:')
password_label.grid(row=2, column=0, sticky='nw')

password_entry = Entry(window, text='Qw23er!!', width=40)
password_entry.grid(row=2, column=1, sticky='nw')
password_entry.insert(END, 'Qw23er!!')

token_button = Button(window, text='Get token', width=15, command=get_token_click)
token_button.grid(row=3, column=0, columnspan=2, sticky='e')

feed_label = Label(window, text='FeedId: ')
feed_label.grid(row=4, column=0, sticky='w', pady=5)

feed_id_label = Label(window, text='')
feed_id_label.grid(row=4, column=1, sticky='w', pady=5)

token_label = Label(window, text='Token: ')
token_label.grid(row=5, column=0, sticky='w', pady=5)

token_entry = Entry(window, text='', width=40)
token_entry.grid(row=5, column=1, sticky='e', pady=5)

start_label = Label(window, text='Start:')
start_label.grid(row=6, column=0, sticky='nw', pady=5)

start_entry = Entry(window, width=40)
start_entry.grid(row=6, column=1, sticky='ne', pady=5)
start_entry.insert(END, '2020-01-17T08:01:36.76')

end_label = Label(window, text='End:')
end_label.grid(row=7, column=0, sticky='nw')

end_entry = Entry(window, width=40)
end_entry.grid(row=7, column=1, sticky='ne')
end_entry.insert(END, '2020-01-17T08:01:57.96')

link_button = Button(window, text='Generate link', width=15, command=generate_link_click)
link_button.grid(row=8, column=0, columnspan=2, sticky='e')

link_label = Label(window, text='Link:')
link_label.grid(row=9, column=0, sticky='nw', pady=5)

link_entry = Entry(window, width=40)
link_entry.grid(row=9, column=1, sticky='ne', pady=5)

window.mainloop()
