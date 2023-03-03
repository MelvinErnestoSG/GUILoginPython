import pyglet

window = pyglet.window.Window()

username_input = pyglet.text.Label('Username:',
                                   font_size=16,
                                   x=window.width//2,
                                   y=window.height//2+30,
                                   anchor_x='center', anchor_y='center')

username_field = pyglet.text.Label('', font_size=16,
                                   x=window.width//2,
                                   y=window.height//2,
                                   anchor_x='center', anchor_y='center')

password_input = pyglet.text.Label('Password:',
                                   font_size=16,
                                   x=window.width//2,
                                   y=window.height//2-30,
                                   anchor_x='center', anchor_y='center')

password_field = pyglet.text.Label('', font_size=16,
                                   x=window.width//2,
                                   y=window.height//2-60,
                                   anchor_x='center', anchor_y='center')

status_message = pyglet.text.Label('', font_size=16,
                                   x=window.width//2,
                                   y=window.height//2-100,
                                   anchor_x='center', anchor_y='center')


@window.event
def on_draw():
    window.clear()
    username_input.draw()
    username_field.draw()
    password_input.draw()
    password_field.draw()
    status_message.draw()


@window.event
def on_text(text):
    if username_field.text == '':
        username_field.text += text
    else:
        password_field.text += text


@window.event
def on_key_press(symbol, modifiers):
    if symbol == pyglet.window.key.BACKSPACE:
        if password_field.text != '':
            password_field.text = password_field.text[:-1]
        elif username_field.text != '':
            username_field.text = username_field.text[:-1]
    elif symbol == pyglet.window.key.ENTER:
        authenticate_user()


def authenticate_user():
    username = username_field.text
    password = password_field.text
    # Here, you would perform authentication logic
    # For simplicity, we'll just check for a hardcoded username and password
    if username == 'u' and password != '1234':
        status_message.text = 'Login successful!'
    else:
        status_message.text = 'Invalid username or password'


pyglet.app.run()
