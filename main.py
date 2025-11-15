import json, os, pyautogui, serial, serial.tools.list_ports, time
folder = os.path.dirname(os.path.abspath(__file__))
os.chdir(folder)

with open('configurations.json') as file:
    configurations = json.load(file)

for port in serial.tools.list_ports.comports():
    if "Arduino" in port.description:
        arduino = serial.Serial(port=port.device, baudrate=9600, timeout=1)
        time.sleep(2)
        break
else:
    print('No Arduino detected')
    quit()


while True:
    arduino.flushInput() # so that the most recent line is read
    data = [int(n) for n in list(arduino.readline().decode().strip())]
    # if button is pressed
    if sum(data) == 1:
        button = data.index(1)
        # wait until button is released
        while sum(data) == 1:
            arduino.flushInput() # so that the most recent line is read
            data = [int(n) for n in list(arduino.readline().decode().strip())]
            time.sleep(.01)
        pyautogui.hotkey(*configurations[str(button)])