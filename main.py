import pyperclip
import keyboard
import time

additional_symbols = '!@#$%^&*()_+{}:"?<>|QWERTYUIOPASDFGHJKLZXCVBNM'

exit_flag = False


def get_last_one_from_clipboard():
    return pyperclip.paste()


def run_main_cycle():
    global exit_flag

    def prepare_space(lines_count):
        for _ in range(lines_count):
            click('enter', False)

        for _ in range(lines_count):
            click('up', False)

    def click(key, shifted):
        if shifted:
            keyboard.press('shift')
        keyboard.press(key)
        time.sleep(0.1)
        keyboard.release(key)
        if shifted:
            keyboard.release('shift')

    def on_exit():
        global exit_flag
        exit_flag = True

    def on_paste():
        time.sleep(0.3)
        clipboard = get_last_one_from_clipboard()
        text = clipboard.replace("\n", "").replace("\t", "    ").split("\r")
        prepare_space(len(text))
        for line in text:
            keyboard.write(line, delay=0.09)
            click("down", False)

    keyboard.add_hotkey('ctrl+alt+e', on_exit)
    keyboard.add_hotkey('ctrl+alt+p', on_paste)

    while not exit_flag:
        time.sleep(0.1)


if __name__ == "__main__":
    run_main_cycle()
