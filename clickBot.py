import pyautogui
import json
import argparse
import os
import time


DEBUG=False


def ArgParseActivity():
    parser=argparse.ArgumentParser()
    parser.add_argument("FILE")
    parser.add_argument("DATASET")
    return parser.parse_args()

def MainActivity():
    args=ArgParseActivity()
    with open("./banner.txt") as handle:
        print(handle.read())
    with open(os.path.join(os.getcwd(),args.FILE)) as handle:
        jsonData=json.load(handle)
    dataset=-1
    for data in jsonData:
        if data["macro-id"]==args.DATASET:
            dataset=data
    
    if dataset==-1:
        print(f"Dataset `{args.DATASET}` not found in `{args.FILE}`")
        exit(1)

    TimeCounter=-1
    while True:
        try:
            for hotplace in dataset["hotplaces"]:
                if TimeCounter%hotplace[1]==0:
                    pyautogui.click(hotplace[0][0],hotplace[0][1])
                    if DEBUG:
                        print(TimeCounter)
            time.sleep(1)
            TimeCounter+=1    
        except KeyboardInterrupt:
            print("Exit Command Received From User. Exitting....")
            exit(0)


if __name__=="__main__":    
    MainActivity()