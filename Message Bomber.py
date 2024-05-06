import time
import pyautogui

def send_whatsapp_message( message, num_times):
    # Wait for user to open WhatsApp Web
    print("Please open WhatsApp Web and select the chat window...")
    time.sleep(10)  # Wait for 10 seconds for user to switch to WhatsApp Web

    # Type and send the message multiple times
    print("\n")
    for _ in range(num_times):
        pyautogui.write(message)
        pyautogui.press('enter')
        time.sleep(0.5)  # Add a small delay between each message
        print(f"message {_+1} is sent")

# usage
print('''
      
      
      
 ███▄ ▄███▓▓█████   ██████   ██████  ▄▄▄        ▄████ ▓█████     ▄▄▄▄    ▒█████   ███▄ ▄███▓ ▄▄▄▄   ▓█████  ██▀███  
▓██▒▀█▀ ██▒▓█   ▀ ▒██    ▒ ▒██    ▒ ▒████▄     ██▒ ▀█▒▓█   ▀    ▓█████▄ ▒██▒  ██▒▓██▒▀█▀ ██▒▓█████▄ ▓█   ▀ ▓██ ▒ ██▒
▓██    ▓██░▒███   ░ ▓██▄   ░ ▓██▄   ▒██  ▀█▄  ▒██░▄▄▄░▒███      ▒██▒ ▄██▒██░  ██▒▓██    ▓██░▒██▒ ▄██▒███   ▓██ ░▄█ ▒
▒██    ▒██ ▒▓█  ▄   ▒   ██▒  ▒   ██▒░██▄▄▄▄██ ░▓█  ██▓▒▓█  ▄    ▒██░█▀  ▒██   ██░▒██    ▒██ ▒██░█▀  ▒▓█  ▄ ▒██▀▀█▄  
▒██▒   ░██▒░▒████▒▒██████▒▒▒██████▒▒ ▓█   ▓██▒░▒▓███▀▒░▒████▒   ░▓█  ▀█▓░ ████▓▒░▒██▒   ░██▒░▓█  ▀█▓░▒████▒░██▓ ▒██▒
░ ▒░   ░  ░░░ ▒░ ░▒ ▒▓▒ ▒ ░▒ ▒▓▒ ▒ ░ ▒▒   ▓▒█░ ░▒   ▒ ░░ ▒░ ░   ░▒▓███▀▒░ ▒░▒░▒░ ░ ▒░   ░  ░░▒▓███▀▒░░ ▒░ ░░ ▒▓ ░▒▓░
░  ░      ░ ░ ░  ░░ ░▒  ░ ░░ ░▒  ░ ░  ▒   ▒▒ ░  ░   ░  ░ ░  ░   ▒░▒   ░   ░ ▒ ▒░ ░  ░      ░▒░▒   ░  ░ ░  ░  ░▒ ░ ▒░
░      ░      ░   ░  ░  ░  ░  ░  ░    ░   ▒   ░ ░   ░    ░       ░    ░ ░ ░ ░ ▒  ░      ░    ░    ░    ░     ░░   ░ 
       ░      ░  ░      ░        ░        ░  ░      ░    ░  ░    ░          ░ ░         ░    ░         ░  ░   ░     
                                                                      ░                           ░                 


      ''')
message = input("Enter message to send: ")
num_times = int(input("Enter number of times to send the message: "))

send_whatsapp_message( message, num_times)
print("\n****** Done ******")
