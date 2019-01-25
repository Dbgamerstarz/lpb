import pyscreenshot as ImageGrab
from PIL import Image
import pytesseract
import pickle

def gettxt(words,lan):
    img = ImageGrab.grab(bbox=(300,560,1500,700))
    img.show()
    img.save("f.png")
    print("save1")
    r=Image.open("f.png")
    
    r.save("f.png")
    print("save2")
    f = pytesseract.image_to_string(r,lang=lan)
    
    print(f)
    found=False
    for key,value in words.items(): 
        if f == value:
            
            translate = key
            print("translation:"+translate)
            found=True
  
        
        
    if found==True:
        pyautogui.moveTo(902, 999)
        pyautogui.click()
        if f == "l'histoire-géo, l'histoire-géographie":
            translate = "social studies"
        pyautogui.typewrite(translate, interval=0.1)
        pyautogui.moveTo(1400, 999)
        pyautogui.click()
    else:
        pyautogui.moveTo(1400, 250)
        pyautogui.click()
        import time
        time.sleep(3)
        img = ImageGrab.grab(bbox=(846,500,1280,580))
        img.show()
        img.save("f.png")
        print("save1")
        r=Image.open("f.png")
        
        r.save("f.png")
        print("save2")
        f2 = pytesseract.image_to_string(r,lang=lan)
        
        print(f)
        print(f2)
        words[f2]=f
        pickle.dump(words,open( lan+".p", "wb" ))
        print(words)
        pyautogui.moveTo(1200, 660)
        pyautogui.click()
        pyautogui.moveTo(1200, 680)
        pyautogui.click()
        pyautogui.moveTo(1200, 670)
        pyautogui.click()
                
import pyautogui
import time
languages = ["fra","deu"]
lan = int(input("1)fr 2)de >"))
lan = languages[lan-1]
try:
    words = pickle.load(open( lan+".p", "rb" ))
except:
    words={}
    pickle.dump(words,open( lan+".p", "wb" ))
print(words)
##for key,value in languages.items(): 
##        if lan == value:
##            
##            translate = key
##            print(translate)

while 1==1:
    time.sleep(3)
    gettxt(words,lan)
    time.sleep(5)
