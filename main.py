import os
import subprocess
import keyboard
import pyautogui

pyautogui.sleep(1)
global body_point
# fine the coordinates
def templateMatching(imagePath, threshold=0.75):
    findCord = pyautogui.locateOnScreen(imagePath, confidence=threshold)
    body_points = pyautogui.center(findCord)
    return body_points

# Start STREAMING
def startScreaming():

    # Specify the folder where the .exe file is located and the file name
    exe_file_path = "scrcpy-win64-v2.4//scrcpy.exe"

    # Run .exe file for streaming
    try:
        process = subprocess.Popen(
            [
                exe_file_path,
                "--prefer-text",
                "--turn-screen-off",
                "--stay-awake",
            ],  # "--turn-screen-off"
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        print("Exe file executed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while executing the exe file: {e}")

    pyautogui.sleep(5)  # Wait for opening screen at 5 sec

# open the app
def openTelegramApp(imagePath):
    print("-" * 20 + "Opening telegram App" + "-" * 20)
    counter = 3
    while counter > 0:
        try:
            body_point = templateMatching(imagePath)
            pyautogui.click(body_point.x, body_point.y)
            break
        except Exception as e:
            print(e)
            print("Trying again.", "Left Turn:", counter)

        counter -= 1
        pyautogui.sleep(2)


def try_to_find_object(NUMBER_OF_FIND_ATTEPMT, imagePath):
    isFind = False
    while NUMBER_OF_FIND_ATTEPMT > 0:
        try:
            body_point = templateMatching(imagePath)
            pyautogui.click(body_point.x, body_point.y)
            isFind = True
            break
        except Exception as e:
            print(e)
            print("Trying again.", "Left Turn:", NUMBER_OF_FIND_ATTEPMT)
        NUMBER_OF_FIND_ATTEPMT -= 1
        pyautogui.sleep(2)

    return isFind, body_point


def main(NUMBER_OF_FIND_ATTEPMT, IMAGE_COUNTER):

    ## start streaming
    startScreaming()

    # Open Telegram  **this is optional**
    # imagePath = "templates\mobile_icon3.png"
    # openTelegramApp(imagePath)

    ## Hit the boss
    # body_imagePath = "templates\\boss_body_huawei2.png"
    body_imagePath = "templates\\boss2_body_huawei.png"
    claim_imagePath = "templates\\claim_button.png"
    print("-" * 20 + "Hitting the BOSS" + "-" * 20)
    
    
    
    body_point = templateMatching(body_imagePath)
    if body_point:
        counter = 0
        hit_counter = 0
        while True:
            try:     
                pyautogui.click(body_point.x, body_point.y)

                if counter > IMAGE_COUNTER:
                    claim_button_point = templateMatching(claim_imagePath)
                    if claim_button_point:
                        pyautogui.click(claim_button_point.x, claim_button_point.y)
                        pyautogui.sleep(5)
                    
                    body_point = templateMatching(body_imagePath)
                    if body_point:
                        break
                    counter = 0 
                    
                if keyboard.is_pressed("q"):
                    break
                
                pyautogui.sleep(0.02)
                counter += 1
                
            except Exception as e:
                print(e)
                c = 0
                while NUMBER_OF_FIND_ATTEPMT > c:
                    c += 1
                    temp_body_point = templateMatching(body_imagePath)
                    if temp_body_point:  
                        break 
                         
                if not temp_body_point:
                    exit()              
                      


    else:
        print("Object not found.")

if __name__ == "__main__":
    
    # CONSTANTS
    NUMBER_OF_FIND_ATTEPMT = 3
    IMAGE_COUNTER = 50
    
    main(NUMBER_OF_FIND_ATTEPMT, IMAGE_COUNTER)
