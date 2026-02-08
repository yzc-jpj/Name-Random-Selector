import tkinter as tk
import random 
import time
from tkinter import ttk
from tkinter import messagebox
import pandas as pd  # 添加pandas库用于读取Excel
from tkinter import filedialog  # 添加文件对话框
import sys
import os

# 添加资源路径处理函数
def resource_path(relative_path):
    """获取资源的绝对路径。用于PyInstaller打包后找到资源文件"""
    try:
        # PyInstaller创建的临时文件夹路径
        base_path = sys._MEIPASS
    except Exception:
        # 正常运行的路径
        base_path = os.path.abspath(".")
    
    return os.path.join(base_path, relative_path)

#函数
def fuck():
    global text2,infomation
    text2=text.get('1.0','end-1c').split()
    if len(text2) > 0 :#判断列表是否为空，应该判断列表长度
        name=random.choice(text2)
        label2.config(text=name,fg='yellow')
        print('用户太聪明了，已执行函数fuck')
    else:
        messagebox.showerror('傻逼(除了杨子超)',
                             '没输名字我给你想啊？')
        time.sleep(0.2)
        tips='用户未输入名字，如果不是杨子超，那么这位用户一定是傻逼'
        for t in tips:
            time.sleep(0.2)
            print(t)

# 添加导入Excel的函数
def import_excel():
    try:
        # 打开文件选择对话框
        file_path = filedialog.askopenfilename(
            title="选择Excel文件",
            filetypes=[("Excel文件", "*.xlsx *.xls"), ("所有文件", "*.*")]
        )
        
        if file_path:  # 如果用户选择了文件
            # 读取Excel文件
            df = pd.read_excel(file_path)
            
            # 查找包含"姓名"的列
            name_column = None
            for col in df.columns:
                if "姓名" in str(col):
                    name_column = col
                    break
            
            if name_column is not None:
                # 获取姓名列的数据，过滤空值
                names = df[name_column].dropna().astype(str).tolist()
                
                # 将姓名添加到文本框中
                current_text = text.get('1.0', 'end-1c')
                if current_text:
                    # 如果已有文本，先换行
                    text.insert('end', '\n')
                
                # 添加所有姓名
                for name in names:
                    text.insert('end', name + ' ')
                
                messagebox.showinfo('成功', f'已导入{len(names)}个姓名')
            else:
                messagebox.showerror('错误', '未找到包含"姓名"的列')
                
    except Exception as e:
        messagebox.showerror('错误', f'导入Excel失败: {str(e)}')

def Courage():
    def NeverGiveUp():
        messagebox.showinfo('加油，Never give up!','你一定可以实现梦想')
    def check():
        messagebox.showinfo('加油，Never give up!')
    def check_button():
        an=entry.get()#如果变量无法识别，将其放入函数内
        if an == '金山':
            win2.withdraw()#使窗口退出
            root=tk.Toplevel()
            root.geometry('300x420+410+100')
            root.title('彩蛋')
            img2=tk.PhotoImage(file=resource_path('888.png'))
            img2_small=img2.subsample(7,
                                  7)#要在单独窗口内
            img5=tk.PhotoImage(file=resource_path('555.gif'))
            img4=tk.PhotoImage(file=resource_path('333.gif'))
            img5_small=img5.subsample(2,2)
            img4_small=img4.subsample(3,3)
            memory="他从中关村到港股大厅，只为让好东西便宜点。"
            memory2='走了三十年，'
            memory3='只为让好东西便宜点。'
            label_color=tk.Label(root,
                                 text=memory).pack()
            label_color2=tk.Label(root,
                                  text=memory2).pack()
            label_color3=tk.Label(root,
                                  text=memory3).pack()
            button=ttk.Button(root,
                              text='加油',
                              command=NeverGiveUp)
            button.pack(padx=5,
                        pady=5)
            notebook2=ttk.Notebook(root)
            notebook2.pack()#单独写，要不然会报错
            frame_color=tk.Frame(notebook2)
            frame_color3=tk.Frame(notebook2)
            frame_color4=tk.Frame(notebook2)
            notebook2.add(frame_color,
                          text='感想')
            notebook2.add(frame_color3,
                          text='确认')
            notebook2.add(frame_color4,
                      text='练习')
            text2=tk.Text(frame_color,
                          font='10')
            text2.pack()
            button4=ttk.Button(frame_color3,
                               text='确认',
                               command=check)
            button4.pack(padx=5,pady=5)
            label_photo=tk.Label(frame_color3,
                                 image=img2_small)
            label_photo.pack(padx=5,pady=5) 
            label_photo2=tk.Label(frame_color3,
                                  text='加油你可以')
            label_photo2.pack(padx=5,pady=5)
            label_practise=tk.Label(frame_color4,
                                    image=img5_small)
            label_practise.pack()
            button1=ttk.Button(frame_color4,text='练习')
            button1.bind('<ButtonPress>',
                         lambda e: label_practise.config(image=img4_small))
            button1.bind('<ButtonRelease>',
                         lambda e: label_practise.config(image=img5_small))  
            button1.pack(padx=5,
                         pady=5)  
            root.mainloop() 
        else:
            messagebox.showwarning('撒比','不是雷军死忠粉还想看彩蛋（除了杨子超）？')
    win2=tk.Tk('300x400+410+100')
    win2.title('验证')
    label_Check=tk.Label(win2,
                         text='雷军加入的第一个公司是什么')
    label_Check.pack()
    entry=tk.Entry(win2)
    entry.pack(padx=5,
               pady=5)
    button=ttk.Button(win2,
                      text='确定',
                      command=check_button).pack()
               
#基本窗口
win=tk.Tk()
win.geometry('300x470+100+100')
win.title('随机抽取学生')
#全局变量
infomation='等待选择...'
text2=[]
img=tk.PhotoImage(file=resource_path('641.gif'))#用PhotoImage方法导入gif图片
img_small=img.subsample(3,
                        3)#把图片缩小到原来的1/3
imgq=tk.PhotoImage(file=resource_path('999.gif'))
imgw=imgq.subsample(1,1)
#窗口布局
label=tk.Label(win,
               text='学生抽取器',
               font='12')
label.pack(padx=5,pady=5)
notebook=ttk.Notebook(win)
notebook.pack()
RandomFrame=tk.Frame(notebook)
CheckFrame=tk.Frame(notebook)
OkFrame=tk.Frame(notebook)
OkFrame1=tk.Frame(notebook)
notebook.add(RandomFrame,
             text='输入')
notebook.add(OkFrame,
             text='交付')
notebook.add(OkFrame1,
             text='彩蛋')

# 第一个页面布局（输入页面）
# 创建容器框架，用于更好的布局控制
input_top_frame = tk.Frame(RandomFrame)
input_top_frame.pack(fill='x', padx=10, pady=(10, 5))


# 创建按钮框架，将按钮放在文本框上方
button_frame = tk.Frame(RandomFrame)
button_frame.pack(fill='x', padx=10, pady=5)

# 添加导入Excel按钮（放在文本框上方）
import_button = ttk.Button(button_frame,
                          text='📂 导入Excel文件',
                          command=import_excel,
                          width=15)
import_button.pack(side='left', padx=(0, 10))

# 添加说明标签
import_label = tk.Label(button_frame, 
                       text="导入包含'姓名'列的Excel文件", 
                       font=('Arial', 9),
                       fg='gray')
import_label.pack(side='left')

# 文本框（放在按钮下方）
text=tk.Text(RandomFrame,
             font='10',
             height=8,
             width=30)
text.pack(fill='both', expand=True, padx=10, pady=(0, 10))

# 可选：添加滚动条
scrollbar = tk.Scrollbar(RandomFrame)
scrollbar.pack(side='right', fill='y')
text.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=text.yview)

# 可选：添加文本框提示文字
text.insert('1.0', '例如：张三 李四 王五\n或点击上方按钮导入Excel文件')
text.config(fg='gray')

def on_text_click(event):
    if text.get('1.0', 'end-1c') == '例如：张三 李四 王五\n或点击上方按钮导入Excel文件':
        text.delete('1.0', 'end')
        text.config(fg='black')

def on_text_leave(event):
    if text.get('1.0', 'end-1c') == '':
        text.insert('1.0', '例如：张三 李四 王五\n或点击上方按钮导入Excel文件')
        text.config(fg='gray')

text.bind('<FocusIn>', on_text_click)
text.bind('<FocusOut>', on_text_leave)

# 第二个页面布局（交付页面）
label1=tk.Label(OkFrame,
                text='本期幸运儿是',font='15')
label1.pack(pady=(20, 10))
label2=tk.Label(OkFrame,
                text=infomation,font=('Arial', 14, 'bold'))
label2.pack(pady=(0, 20))
labelr=tk.Label(OkFrame,
                image=imgw)
labelr.pack(pady=(0, 20))
button=ttk.Button(OkFrame,
                 text='🎲 开始抽取',
                 command=fuck,
                 width=15)
button.pack(pady=10)

# 第三个页面布局（彩蛋页面）
label=tk.Label(OkFrame1,
               image=img_small,
               ).pack(pady=(20, 10))
label3=tk.Label(OkFrame1,
                text='雷军小时候的照片',
                font=('Arial', 11))
label3.pack(pady=(0, 10))
ttk.Button(OkFrame1,
           text='LeiJun',
           command=Courage,
           width=12).pack(pady=10)

#窗口保持开启
win.mainloop()