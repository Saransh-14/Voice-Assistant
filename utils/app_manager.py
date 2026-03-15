import os
from core.speaker import speak

start_menu_paths = [
    r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs",
    os.path.expanduser(r"~\AppData\Roaming\Microsoft\Windows\Start Menu\Programs")
]
ms_apps = {"whatsapp":"start whatsapp:", "notepad":"start notepad","file explorer":"start explorer", 
           "command prompt": "start cmd", "microsoft edge":"start msedge"}

fun_calls = {"start":"starting", "open":"opening", "launch":"launching"}
found = 0
def open_app(app_name, verb):
    if app_name.lower() in ms_apps.keys():
        speak(f"{fun_calls[verb]} {app_name}")
        os.system(ms_apps[app_name])
        return 1
    elif app_name.lower() not in ms_apps.keys():
        for path in start_menu_paths:
            for root, dirs, files in os.walk(path):
                for file in files:
                    if app_name.lower() in file.lower():
                        full_path = os.path.join(root, file)
                        speak(f"{fun_calls[verb]}{app_name}")
                        os.startfile(full_path)
                        return 1
    return 0
