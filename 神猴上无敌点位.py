import ctypes
import time
import win32api
import win32con
import win32gui
def jump():
    win32api.keybd_event(32, ctypes.windll.user32.MapVirtualKeyA(32, 0), 0, 0)
    win32api.keybd_event(32, ctypes.windll.user32.MapVirtualKeyA(32, 0), win32con.KEYEVENTF_KEYUP, 0)
def mwindow():  # 将窗口移动到左上角
    # 获取窗口句柄
    hwnd = win32gui.FindWindow(None, '穿越火线')
    # 获取窗口左上角坐标和右下角坐标
    left, top, right, bottom = win32gui.GetWindowRect(hwnd)
    # 输出坐标信息
    # print('窗口左上角坐标：({}, {})'.format(left, top))
    # print('窗口右下角坐标：({}, {})'.format(right, bottom))
    ck = win32gui.FindWindow(None, '穿越火线')  # “CabinetWClass”是窗口的类，"此电脑"是窗口的名
    win32gui.SetWindowPos(ck, win32con.HWND_NOTOPMOST, 0, 0, right - left, bottom - top, win32con.SWP_SHOWWINDOW)
def mouseclick(x,y):
    win32api.SetCursorPos([x, y])
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
def keyboard(k,t):
    win32api.keybd_event(k, ctypes.windll.user32.MapVirtualKeyA(k, 0), 0, 0)
    time.sleep(t)
    win32api.keybd_event(k, ctypes.windll.user32.MapVirtualKeyA(k, 0), win32con.KEYEVENTF_KEYUP, 0)
def mousemove(x,y):
    win32api.mouse_event(win32con.MOUSEEVENTF_MOVE,x,y,0,0)
def color(x,y,r1,g1,b1):
    hdc = ctypes.windll.user32.GetDC(None)
    pixel = ctypes.windll.gdi32.GetPixel(hdc, x,y)
    r = pixel & 0x0000ff
    g = (pixel & 0x00ff00) >> 8
    b = pixel >> 16
    if r==r1 and g==g1 and b==b1:
        return True
    else:
        return False
def first():
    win32api.keybd_event(87, ctypes.windll.user32.MapVirtualKeyA(87, 0), 0, 0)  # ctrl的键位码是17
    time.sleep(0.4)
    jump()
    time.sleep(0.3)
    jump()
    time.sleep(0.3)
    jump()
    time.sleep(0.5)
    win32api.keybd_event(87, ctypes.windll.user32.MapVirtualKeyA(87, 0), win32con.KEYEVENTF_KEYUP, 0)
def seller():
    win32api.keybd_event(51, ctypes.windll.user32.MapVirtualKeyA(51, 0), 0, 0)
    win32api.keybd_event(51, ctypes.windll.user32.MapVirtualKeyA(51, 0), win32con.KEYEVENTF_KEYUP, 0)
    time.sleep(0.1)
    win32api.keybd_event(87, ctypes.windll.user32.MapVirtualKeyA(87, 0), 0, 0)
    win32api.keybd_event(65, ctypes.windll.user32.MapVirtualKeyA(65, 0), 0, 0)
    time.sleep(2.5)
    win32api.keybd_event(65, ctypes.windll.user32.MapVirtualKeyA(65, 0), win32con.KEYEVENTF_KEYUP, 0)
    win32api.keybd_event(87, ctypes.windll.user32.MapVirtualKeyA(87, 0), win32con.KEYEVENTF_KEYUP, 0)
    time.sleep(0.5)
def buy():
    keyboard(69,0)
    time.sleep(0.5)
    if color(803,548,228,230,232):
        mouseclick(803,548)
        time.sleep(0.5)
        mouseclick(803, 548)
    time.sleep(0.5)
    if color(626,287,255,255,255):
        mouseclick(626,287)
        time.sleep(0.5)
        mouseclick(638,558)
        time.sleep(0.2)
    mouseclick(1009,180)
def move():
    keyboard(83,1.5)
    time.sleep(0.2)
    keyboard(68,7.5)
    time.sleep(0.2)
    keyboard(83,6)
    time.sleep(0.2)
    keyboard(68,4)
    time.sleep(0.2)
    keyboard(83, 0.5)
    time.sleep(0.2)
    keyboard(68, 5)
    time.sleep(0.2)
    keyboard(83,2)
    time.sleep(0.2)
    keyboard(68,2)
    time.sleep(0.2)
    keyboard(87,1.5)
    time.sleep(0.2)
    keyboard(68,4)
    time.sleep(0.2)
    keyboard(83, 0.5)
    time.sleep(0.2)
def main():
    seller()
    buy()
    move()
    mousemove(3550,0)
    time.sleep(2)
    time.sleep(0.5)
    keyboard(70,0)
    time.sleep(0.2)
    keyboard(16,0)
    time.sleep(0.5)
    mousemove(-3550, 0)
    time.sleep(2)
    while not color(688,706,216,249,255):
        time.sleep(1)
    time.sleep(0.2)
    keyboard(70, 0)
    time.sleep(0.2)
    keyboard(16, 0)
    time.sleep(0.5)
    mousemove(3580, 0)
    while not color(688,706,216,249,255):
        time.sleep(1)
    time.sleep(0.2)
    keyboard(70, 0)
    keyboard(16, 0)
    time.sleep(1)
    keyboard(16, 0)
    time.sleep(0.2)
    mousemove(-2000,800)
if __name__=='__main__' :
    time.sleep(2)
    mwindow()
    main()