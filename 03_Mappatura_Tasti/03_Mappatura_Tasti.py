from pynput import keyboard

def on_press(key):
    try:
        if key.char.isalpha():      #se il tasto premuto è una lettera allora viene stampato
            print('Lettera {0} premuta'.format(key.char))
    except AttributeError:
        pass        #vengono ignorati tutti i tasti diversi dalle lettere

def on_release(key):
    if key == keyboard.Key.esc:
        return False        #nella documentazione pynput veniva usato l'esc per interrompere il codice

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:       #finché non colleziona esc continua a funzionare
    listener.join()     #è un thread
