import socket
import pyautogui as auto
from time import sleep
import keyboard as key

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(("192.168.1.172", 9093))
sock.listen(1)
print("Управление доступно...")

while True:
    conn, addr = sock.accept()

    while True:
        data = conn.recv(1024).decode("utf-8")
        if not data:
            break
        print(f"Пользователь запрашивает {data}")

        if "Search" in data:
        	info = data[7:]
        	auto.press("esc")
        	sleep(1)
        	auto.click(700, 100)
        	auto.hotkey('ctrlleft', 'a')
        	auto.press("backspace")
        	key.write(info)
        	auto.press("Enter")

        elif data == "Volume-Up":
            auto.press("Up")

        elif data == "Volume-Down":
            auto.press("Down")

        elif data == "Roll-Up-and-on-Main":
            key.press("i")

        elif data == "on-Main":
            auto.press("esc")
            sleep(1)
            auto.click(100, 100)

        elif data == "Scroll-Up":
            auto.scroll(300)

        elif data == "Scroll-Down":
            auto.scroll(-300)

        elif data == "Rewind-Back":
            key.press("j")

        elif data == "Rewind-Forward":
            key.press("l")

        elif data == "Expand":
            auto.press("f")

        elif data == "Pause":
            key.press("space")

        elif data == "OK":
            auto.click()

        elif data == "Up":
            auto.move(0, -80, 0.15)

        elif data == "Down":
            auto.move(0, 80, 0.15)

        elif data == "Left":
            auto.move(-80, 0, 0.15)

        elif data == "Right":
            auto.move(80, 0, 0.15)

        else:
        	print("Неизвестная команда!")