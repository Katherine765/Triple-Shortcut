# Triple-Shortcut
Technica 2025 Submission

I made a shortcut keypad using Arduino and Python.

1. Download the entire repository in one folder.
2. Wire an Arduino as pictured in arduinoClipart.png and arduinoPhoto.png.
3. Upload serialOutputer.ino to the Arduino.
4. Run the configurationSetter.py file to choose shortcuts. This can be repeated at any time.
5. With the Ardunino plugged in, run main.py in the background. As Arduino buttons are pressed, they should perform the shortcuts chosen.

Here is a Google Photos link to tripleShortcutDemo.MOV: https://photos.app.goo.gl/UyjyamCriFj13Awp6.

The keyswitch clipart in the banner is edited from https://www.vecteezy.com/vector-art/27577662-mechanical-keyboard-switch-vector-illustration.

## Inspiration
Three of my interests are Python, Arduino, and keyboards. This is a way to combine all of those.

## What it does
It allows its user to configure keyboard shortcuts using a GUI and then execute those shortcuts by pressing the Arduino buttons (provided main.py is running in the background).

## How I built it
I started by wiring the buttons, then used pyautogui to control the keyboard, then worked on the configuration GUI.

## Challenges I ran into
I use an alternate keyboard called Colemak DH, which on my laptop works by having an .exe file run in the background. The .exe and my shortcut keypad were not compatible with each other, but I was able to use my external Colemak DH keyboard to avoid that problem.

## Accomplishments that we're proud of
I am proud that I made a somewhat user-friendly GUI because usually I do not focus on how things look at all.
