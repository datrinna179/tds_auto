from pro5_tool_tds import *
import os
import threading
import time
import subprocess
try:
    from pynput import keyboard
except:
    os.system("pip install pynput")
from pynput import keyboard

tools = []
i = 1
nhap_so_luong = int(input("Nhập số luồng: "))
while i <= nhap_so_luong:
    tools.append(show_info(f"Luồng {i}"))
    i += 1
listen = keyboard.Listener 
file_path = 'F:\Project_tool_tds\Prj_tds_auto-testing\pro5_tool_tds.py' #đường dẫn file pro5_tool_tds(down code về nhớ đổi đường dẫn)

def execute_python_file(profile, sleepTime, file_path):
    #dừng luồng
    if(profile.IsStop):
        print("{} Stop\n" .format(profile.Name))
        return
    #dừng tool sau khi nhấn phím 
    totalRunningThread = any(x.IsStop == False for x in tools)
    print("Total: {}\n".format(totalRunningThread))
    if(totalRunningThread == False):
        listen.stop()
    #chạy file pro5_tool_tds
    try:
        completed_process = subprocess.run(['python', file_path], capture_output=True, text=True)
        if completed_process.returncode == 0:
            print("Thành công.")
            print(f"{profile.Name} đang chạy")
            print("Output:")
            print(completed_process.stdout)
            time.sleep(sleepTime)
        else:
            print(f"Lỗi: Không thực thi được '{file_path}'.")
            print("Lỗi: ")
            print(completed_process.stderr)
            time.sleep(sleepTime)
    except FileNotFoundError:
        print(f"Lỗi: Tệp '{file_path}' không tồn tại. ")
    
#nhấn phím để dừng tool
def on_press(key): # key: phim nhan
    vk = key.vk if hasattr(key, 'vk') else key.value.vk 
    print('vk = ',vk)
    if(vk == None):
        return
    index = vk - 48
    if(index >=0 and index < len(tools) and tools[index].IsStop == False):
        print("Dừng luồng: {}".format(tools[index].Name))
        tools[index].IsStop = True
#đa luồng
if __name__ == "__main__":
    for item in tools:
        p = threading.Thread(target=execute_python_file, args=(item, 5, file_path, ))
        p.start()
        
    with keyboard.Listener(on_press=on_press) as listener:
        listen = listener
        listener.join() 