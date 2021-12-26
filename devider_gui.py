import os
import tkinter.ttk as ttk
from tkinter import *
import tkinter.messagebox as msgbox
from tkinter import filedialog
import socket


#host 이름 가져오기
def host_name():
    host = socket.gethostname()
    host_name = host.split('-')[0]
    return host_name

#시나리오 파일 찾기
def add_file():
    global file
    host = host_name()
    print(f'C:/user/{host}/desktop')
    file = filedialog.askopenfilename(title='ScenarioSet 파일을 선택해주세요.',filetypes=(("call files", "*.call"),("all files", "*.*")),initialdir=f'C:/user/{host}/desktop')
    if file != '':
        file_check(file)
        if file_check == True:
            text_file_path.insert(END,file)
            scenario_list_view(file)

#파일 확장자 확인
def file_check(file):
    extention = os.path.splitext(file)
    if extention != '.call':
        msgbox.showerror('Error','ScenarioSet.call 파일만 사용가능합니다.')
        return False
    else:
        return True

#시나리오 파일 확인
def scenario_list_view(file):
    scenarioFile = open(file,'r')
    readScenario = scenarioFile.read()
    devideScenario = readScenario.split('[')

    for scenario in devideScenario:
        lines = scenario.split('\n')
        for line in lines:
            if 'ScenarioName' in line:
                need = line.split('=')
                need_name = need[1]
                print(need_name)
                list_file.insert(END,need_name)
            
    scenarioFile.close()

def finishInfo():
    msgbox.showinfo('확인','시나리오 분할 완료')


#시나리오 파일 분할
def devide_scenario():
    scenarioFile = open(file,'r')
    readScenario = scenarioFile.read()
    devideScenario = readScenario.split('[')

    for scenario in devideScenario:
        lines = scenario.split('\n')
        for line in lines:
            if 'ScenarioName' in line:
                need = line.split('=')
                need_name = need[1]
                new = open(f'{need_name}.call','w')
                new.write('['+scenario)
            

            
    scenarioFile.close()
    finishInfo()
    

root=Tk()
root.title("Scenario Devider")
root.geometry("640x400")
root.resizable(False, False)


#파일찾기 UI
path_frame = LabelFrame(root, text='시나리오파일 경로')
path_frame.pack(fill='x',padx=5,pady=5,ipady=5)

text_file_path = Entry(path_frame)
text_file_path.pack(side='left',expand=True,fill='x',pady=5,padx=5,ipady=4)

btn_file_path = Button(path_frame,text='찾아보기',width=10,command=add_file)
btn_file_path.pack(side='right',padx=5,pady=5)

#리스트박스 UI
list_frame = Frame(root)
list_frame.pack(fill='both',pady=5,padx=5)

scroll = Scrollbar(list_frame)
scroll.pack(fill='y',side='right')

list_file = Listbox(list_frame,selectmode='expanded',yscrollcommand=scroll.set,height=15)
list_file.pack(side='left',fill='both',expand=True)
scroll.config(command=list_file.yview)

# 시나리오 분할 버튼
start_btn = Button(root,text='진행',command=devide_scenario)
start_btn.pack()

root.mainloop()