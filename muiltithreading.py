#đang dính bug chưa chạy đc
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

tools = [show_info('Thread 1'), show_info('Thread 2'), show_info('Thread 3')]
listen = keyboard.Listener #đang fix chỗ này
file_path = '/workspaces/tds_auto/pro5_tool_tds.py'

def execute_python_file(profile, sleepTime, file_path):
    if(profile.IsStop):
        print("{} Stop\n" .format(profile.Name))
        return
    if(profile.IsStop):
        print("{} Stop\n" .format(profile.Name))
        return
    #dung tool sau khi nhan phim tat 
    totalRunningThread = any(x.IsStop == False for x in tools)
    print("Total: {}\n".format(totalRunningThread))
    if(totalRunningThread == False):
        listen.stop()
    #chạy file pro5_tool_tds
    try:
        completed_process = subprocess.run(['python', file_path], capture_output=True, text=True)
        if completed_process.returncode == 0:
            print("Execution successful.")
            print(f"{profile.Name} is running")
            print("Output:")
            print(completed_process.stdout)
            time.sleep(sleepTime)
        else:
            print(f"Error: Failed to execute '{file_path}'.")
            print("Error output:")
            print(completed_process.stderr)
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' does not exist.")
    
#nhan phim de dung tool
def on_press(key): # key: phim nhan
    vk = key.vk if hasattr(key, 'vk') else key.value.vk 
    print('vk = ',vk)
    if(vk == None):
        return
    index = vk - 48
    if(index >=0 and index < len(tools) and tools[index].IsStop == False):
        print("Doing Stop: {}".format(tools[index].Name))
        tools[index].IsStop = True
#muiltithreading
if __name__ == "__main__":
    for item in tools:
        p = threading.Thread(target=execute_python_file, args=(item, 3, file_path, ))
        p.start()
        
    with keyboard.Listener(on_press=on_press) as listener:
        listen = listener
        listener.join() 