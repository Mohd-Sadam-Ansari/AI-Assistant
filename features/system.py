import os,signal
import subprocess
import cv2
import pyautogui
import time
import shutil
import schedule
import sys
from playsound import playsound
sys.path.append('/tts')
from tts import speak

def launch_app(app_name):
    app_name=app_name.replace('alan','')
    app_name=app_name.replace('open','')
    app_name=app_name.replace('ellen','')
    app_name=app_name.replace('start','')
    app_name=app_name.replace('launch','')
    app_name=app_name.replace('please','')

    APP_LIST = {
    'gedit': ['gedit', 'g-edit', 'g edit', 'editor', 'text editor'],
    'libreoffice': ['ms office', 'ms-office', 'm s office', 'm-s-office', 'office'],
    'libreoffice --writer': ['word', 'word document', 'rich text', 'rich text editor', 'ms word', 'ms-word', 'm s word', 'm-s-word'],
    'libreoffice --calc': ['excel', 'exel', 'excel document', 'exel document' 'calc', 'spreadsheet', 'spread sheet', 'spread-sheet' 'ms excel', 'ms-excel', 'm s excel', 'ms-exel', 'm s exel', 'm-s-exel'],
    'libreoffice --draw': ['powerpoint', 'power point', 'power-point', 'presentation', 'powerpoint presentation', 'power point presentation', 'power-point presentation', 'p p t', 'p-p-t', 'presentation document', 'p p t document' 'powerpoint presentation document', 'power point presentation document', 'power-point presentation document', 'spread-sheet'],
    'gnome-terminal': ['terminal', 'c m d', 'command prompt', 'bash', 'shell', 'shell prompt', 'bash prompt'],
    'vlc': ['vlc', 'v l c', 'v-l-c', 'vlc player', 'v l c player', 'v-l-c player', 'vlc media player', 'v l c media player', 'v-l-c media player'],
    'gnome-calculator': ['calculator', 'calculate', 'calci', 'calcy', 'calsi', 'calsy']
    }
    for key,value in APP_LIST.items():
        if app_name.lower() in value:
            app_name=key
            break
        else:
            app_name=app_name
    try:
        os.system(app_name)
        return True
    except:
        return "Application not found."

def take_picture():
    cap=cv2.VideoCapture(0)
    speak.speak('press s for click a pitcure or press q to quit')
    playsound('test.wav')
    os.remove('test.wav')
    while True:
        ret,img=cap.read()
        cv2.imshow('img',img)
        if cv2.waitKey(1) & 0xFF==ord('s'):
            cv2.imwrite('picture.png',img)
            break
        elif cv2.waitKey(1) & 0xFF==ord('q'):
            break
    
    cap.release()
    cv2.destroyAllWindows()

def shutdown():
    try:
        os.system("shutdown now")
        return True
    except OSError as error:
        return error

def restart():
    try:
        os.system("reboot")
        return True
    except OSError as error:
        return error

def manual(command):
    command.replace('man','')
    command.replace('alan','')
    command.replace('ellen','')
    command.replace('manual','')
    command.replace('command','')
    command.replace('of','')
    command.replace('provide','')
    command.replace('instructions about','')
    command_dict={'ls':['list'],
    'cat':['concatenate'],
    'pwd':['print working directory'],
    'cp':['copy'],
    'mv':['move'],
    'mkdir':['make directory','make folder','make directories'],
    'rmdir':['remove directory','remove directories','remove folder']
    ,'rm':['rmove files']
    }

    for key,value in command_dict.items():
        if command.lower() in value :
            command=key
            break
        else:
            command=command
    try:
        output=os.popen(f"man {command}").read()
        return output
    except:
        return "No manual found."

def create_directories(dir_name):
    dir_name=dir_name=replace('alan','')
    dir_name=dir_name=replace('ellen','')
    dir_name=dir_name=replace('make directoy','')
    dir_name=dir_name=replace("create a directory","")
    dir_name=dir_name=replace("construct a directory","")
    dir_name=dir_name=replace("devise a directory","")
    dir_name=dir_name=replace("form a directory","")
    dir_name=dir_name=replace("generate a directory","")
    dir_name=dir_name=replace( "produce a directory","")
    dir_name=dir_name=replace("build a directory","")
    dir_name=dir_name=replace("design a directory","")
    dir_name=dir_name=replace("fabricate a directory","")
    dir_name=dir_name=replace('make folder','')
    dir_name=dir_name=replace("create a folder","")
    dir_name=dir_name=replace("construct a folder","")
    dir_name=dir_name=replace("devise a folder","")
    dir_name=dir_name=replace("form a folder","")
    dir_name=dir_name=replace("generate a folder","")
    dir_name=dir_name=replace( "produce a folder","")
    dir_name=dir_name=replace("build a folder","")
    dir_name=dir_name=replace("design a folder","")
    dir_name=dir_name=replace("fabricate a folder","")
    if len(dir_name)==0:
        dir_name='test'
    try:
        cwd=os.path.expanduser('~')
        user_dir=f"{cwd}/{dir_name}"
        os.makedirs(user_dir,exist_ok=True)
        return f'{user_dir} successfully created.'
    except:
        return f'something went wrong while creating {user_dir}'

def delete_directories(dir_name):
    dir_name=dir_name=replace('alan','')
    dir_name=dir_name=replace('ellen','')
    dir_name=dir_name=replace("delete a folder","")
    dir_name=dir_name=replace("remove a folder","")
    dir_name=dir_name=replace("destroy a folder","")
    dir_name=dir_name=replace("erase a folder","")
    dir_name=dir_name=replace("delete a directory","")
    dir_name=dir_name=replace("remove a directory","")
    dir_name=dir_name=replace("destroy a directory","")
    dir_name=dir_name=replace("trash a directory","")
    dir_name=dir_name=replace("erase a directory","")
    dir_name=dir_name=replace("trash a folder","")
    if len(dir_name)==0:
        dir_name=='test'
    try:
        cwd=os.path.expanduser('~')
        user_dir=f"{cwd}/{dir_name}"
        os.rmdir(user_dir)
        return f"{user_dir} successfully removed."
    except:
        return f"directorie can't be deleted as it is not present or not empty"

def create_files(filename):
    filename=filename.replace('alan','')
    filename=filename.replace('ellen','')
    filename=filename.replace("make file","")
    filename=filename.replace("create a file","")
    filename=filename.replace("construct a file","")
    filename=filename.replace("generate a file","")
    filename=filename.replace(".txt","")
    if len(filename)==0:
        filename='test'
    try:
        cwd=os.path.expanduser('~')
        file_path=f"{cwd}/{filename}.txt"
        subprocess.run(["touch",file_path])
        return f'{filename} successfully created.'
    except:
        return f"something went wrong while creating {filename}"
        
def delete_files(filename):
    filename=filename.replace('alan','')
    filename=filename.replace('ellen','')
    filename=filename.replace("delete file","")
    filename=filename.replace("remove file","")
    filename=filename.replace("destroy a file","")
    filename=filename.replace("trash a file","")
    filename=filename.replace("erase a file","")
    filename=filename.replace("delete a file","")
    if len(filename)==0:
        filename=='test'
    try:
        cwd=os.path.expanduser('~')
        file_path=f"{cwd}/{filename}.txt"
        os.system(f'rm {file_path}')
        return f'{filename} successfully deleted.'
    except:
        return f"something went wrong while removing {filename}"

def switch_window():
    pyautogui.keyDown("alt")
    pyautogui.press("tab")
    time.sleep(1)
    pyautogui.keyUp("alt")

def ip_address():
    try:
        routing_table=os.popen('ip route')
        for line in routing_table:
            if "default via" in line:
                default_route=line.strip().split()
        default_gateway=default_route[2]
        interface_config=os.popen('ip addr')
        for line in interface_config:
            if default_gateway in line:
                ip_add=line.strip().split()[1].split('/')[0]
        return ip_add
    except:
        return f"device is not connected to network"

def job_schedule():
    def job():
        print("Hello World")
    schedule.every().day.at("20:48").do(job)
    while True:
        schedule.run_pending()
        time.sleep(1)

def take_note(query):
    message=query.replace("remember that","")
    message=message.replace("alan","")
    message=message.replace("ellen","")
    message=message.replace("take a note","")
    message=message.replace("note down","")
    message=message.replace("make a note","")
    message=message.replace("write down","")

    cwd=os.getcwd()                                                   
    remember=f"{cwd}/note.txt"
    subprocess.run(["touch",remember])
    remember_file=open("note.txt","w")
    remember_file.write(message)
    remember_file.close()

def read_note():
    remember_file=open("note.txt","r")
    message=remember_file.read()
    remember_file.close()
    os.remove("note.txt")
    return f"You tell me that {message}"

if __name__=="__main__":
    print(manual("cat"))
   
    