
# Buttons

PATH = []
OUTPUT_PATH = ""
RESPONSE_TEXT = ""

def add_path(new_path):
    global PATH
    if len(PATH) == 2:
        PATH.clear()
        return {
            "msg": "Error!",
            "status": 0
        } # Добавить вывод ошибки в UI
    PATH.append(new_path)
    return {
        "new_path": new_path[0],
        "PATH": PATH,
        "status": 1
    }
