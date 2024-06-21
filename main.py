import os
import subprocess
import keyboard
import pyautogui


pyautogui.sleep(1)


def templateMatching(imagePath, threshold=0.8):
    findCord = pyautogui.locateOnScreen(imagePath, confidence=threshold)
    resultPoints = pyautogui.center(findCord)
    return resultPoints


### Start STREAMING
def startScreaming():

    # Specify the folder where the .exe file is located and the file name
    exe_file_directory = "C:\\Dev\\tapToEarnBotForTelegram\\scrcpy-win64-v2.4"
    exe_file_name = "scrcpy.exe"
    exe_file_path = os.path.join(exe_file_directory, exe_file_name)

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


def openTelegramApp(imagePath):
    print("-" * 20 + "Opening telegram App" + "-" * 20)
    counter = 3
    while counter > 0:
        try:
            resultPoint = templateMatching(imagePath)
            pyautogui.click(resultPoint.x, resultPoint.y)
            break
        except Exception as e:
            print(e)
            print("Trying again.", "Left Turn:", counter)

        counter -= 1
        pyautogui.sleep(2)


def main():

    ## start streaming
    startScreaming()

    ## Open Telegram
    # imagePath = "templates\mobile_icon3.png"
    # openTelegramApp(imagePath)

    ## Hit the boss
    imagePath = "templates\\boss_body2.png"
    print("-" * 20 + "Hitting the BOSS" + "-" * 20)
    counter = 3
    while counter > 0:
        try:
            resultPoint = templateMatching(imagePath)
            pyautogui.click(resultPoint.x, resultPoint.y)
            break
        except Exception as e:
            print(e)
            print("Trying again.", "Left Turn:", counter)
        counter -= 1
        pyautogui.sleep(2)

    while True:
        pyautogui.click(resultPoint.x, resultPoint.y)
        if keyboard.is_pressed("q"):
            break
        pyautogui.sleep(0.02)


main()
