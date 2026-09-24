from voice import speak, listen
from agent import ask_ai

import webbrowser
import pyautogui
from datetime import datetime
import os

speak("Jarvis started")

while True:

    user = listen()

    if not user:
        continue

    user = user.lower()

    # Applications
    if "notepad" in user:
        os.system("notepad")

    elif "chrome" in user:
        os.system("start chrome")

    elif "calculator" in user:
        os.system("calc")

    elif "paint" in user:
        os.system("mspaint")

    elif "vs code" in user:
        os.system("code")

    # Websites
    elif "youtube" in user:
        webbrowser.open("https://youtube.com")
        speak("Opening YouTube")

    elif "google" in user:
        webbrowser.open("https://google.com")
        speak("Opening Google")

    elif "github" in user:
        webbrowser.open("https://github.com")
        speak("Opening GitHub")

    # Time
    elif "time" in user:
        current_time = datetime.now().strftime("%I:%M %p")
        speak(f"The time is {current_time}")

    # Date
    elif "date" in user:
        current_date = datetime.now().strftime("%d %B %Y")
        speak(f"Today is {current_date}")

    # Screenshot
    elif "screenshot" in user:
        pyautogui.screenshot().save("screenshot.png")
        speak("Screenshot saved")

    # Google Search
    elif user.startswith("search"):
        query = user.replace("search", "").strip()

        if query:
            webbrowser.open(
                f"https://www.google.com/search?q={query}"
            )
            speak(f"Searching {query}")

    # Downloads Folder
    elif "downloads" in user:
        os.system("explorer shell:Downloads")

    # Exit
    elif "exit" in user or "bye" in user:
        speak("Goodbye")
        break

    # AI Chat
    else:
        reply = ask_ai(user)
        print("Jarvis:", reply)
        speak(reply)