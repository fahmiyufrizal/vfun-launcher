import win32gui

win2find = input('VFUNLauncher')
whnd = win32gui.FindWindowEx(None, None, None, win2find)
if not (whnd == 0):
  print('FOUND!')