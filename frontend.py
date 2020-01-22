from tkinter import *
from backend import *

window = Tk()
window.title('Link generator')
token = ''
feed_id = ''


def open_alert(message):
    alert_window = Toplevel(window)
    x = window.winfo_x()
    y = window.winfo_y()
    alert_window.geometry(
        "%dx%d+%d+%d" % (250, 70, x + window.winfo_width() / 2 - 125, y + + window.winfo_height() / 2 - 35))
    alert_window.title('Warning')
    mes = Label(alert_window, text=message)
    mes.pack(pady=20)


def get_token_click():
    global token, feed_id
    token = get_token(variable.get(), email_entry.get(), password_entry.get())
    if token[0] == 200:
        token = token[1]
        feed_id = get_feed_id(variable.get(), token)
        feed_id_label['text'] = feed_id
        token_entry.delete(0, END)
        token_entry.insert(END, token)
    else:
        open_alert(token[1])


def generate_link_click():
    global token, feed_id
    if token_entry.get() != '':
        link = generate_link(variable.get(), feed_id, start_entry.get(), end_entry.get(), token)
        print(link)
        link_entry.delete(0, END)
        link_entry.insert(END, link)
    else:
        open_alert('You are unauthorized')


def show_menu(e):
    menu.entryconfigure('Copy',
                        command=lambda: e.widget.event_generate('<<Copy>>'))
    menu.entryconfigure('Paste',
                        command=lambda: e.widget.event_generate('<<Paste>>'))
    # menu.tk.call("tk_popup", menu, entry.x_root, entry.y_root)
    menu.post(e.x_root, e.y_root)


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
start_entry.bind_class("Entry", "<Button-3><ButtonRelease-3>", show_menu)

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

menu = Menu(window, tearoff=0)
menu.add_command(label='Copy')
menu.add_command(label='Paste')

window.mainloop()
