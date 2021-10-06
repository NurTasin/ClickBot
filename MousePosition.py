import pyautogui

def AddPad(xy):
    return (" "*(4-len(str(xy)))+str(xy))

def MainActivity():
    preX,preY=0,0
    while True:
        try:
            curX,curY=pyautogui.position()
            if curX!=preX or curY!=preY:
                print(f"Mouse Position = ({AddPad(curX)},{AddPad(curY)})",end="\r")
                preX=curX
                preY=curY
        except KeyboardInterrupt:
            print("\nExiting.......")
            exit(0)


if __name__=="__main__":
    MainActivity()