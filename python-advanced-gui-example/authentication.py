import os
import json
import tkinter as tk

from helpers import clear_screen


def register(**user):
    # TODO: handle already existing usernames
    with open(os.path.join('db', 'user_store.txt'), 'a') as f:
        f.write(f'{user["username"]} - {user["password"]}\n')


def render_register(screen: tk.Tk, on_success):
    clear_screen(screen)
    inputs = [
        ('username', tk.Entry(screen)),
        ('password', tk.Entry(screen)),
        ('first_name', tk.Entry(screen)),
        ('last_name', tk.Entry(screen)),
    ]

    for idx, (label, input_widget) in enumerate(inputs):
        input_widget.grid(row=idx, column=0)

    def on_click():
        error = register(**{user_attribute: widget.get() for (user_attribute, widget) in inputs})

        if not error:
            clear_screen(screen)
            on_success(screen)
        else:
            tk.Label(screen, text=error, background='red', foreground='white').grid(row=5, column=0)

    tk.Button(
        screen,
        text='Submit',
        command=on_click
    ).grid(row=len(inputs), column=1)


def render_login(screen: tk.Tk, on_success):
    clear_screen(screen)
    username = tk.Entry(screen)
    username.grid(row=0, column=0)
    password = tk.Entry(screen, show='*')
    password.grid(row=1, column=0)

    def on_click():
        if login(username.get(), password.get()):
            on_success(screen)
        else:
            tk.Label(screen, text='Invalid username or password', foreground='red').grid(row=3, column=0)

    tk.Button(
        screen, text='Login',
        command=on_click
    ).grid(row=2, column=0)


def login(username, password):
    with open(os.path.join('db', 'user_store.txt')) as f:
        for row in f:
            user = json.loads(row)
            if user['username'] == username and user['password'] == password:
                with open(os.path.join('db', 'current_user.txt'), 'w') as f:
                    f.write(json.dumps(user))

                return True

    return False
