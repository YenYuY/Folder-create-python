import os
import tkinter as tk
from tkinter import messagebox
from datetime import datetime

def create_folder():
    name = name_entry.get().strip()
    if not name:
        messagebox.showwarning("警告", "請輸入名子！")
        return
    
    # 取得當前日期
    today = datetime.now()
    folder_name = f"請款-{today.year}-{today.month:02d}-{today.day:02d}-{name}"
    
    # 建立資料夾
    try:
        os.makedirs(folder_name)
        messagebox.showinfo("成功", f"已成功建立資料夾：\n{folder_name}")
    except FileExistsError:
        messagebox.showwarning("警告", "資料夾已存在！")
    except Exception as e:
        messagebox.showerror("錯誤", f"無法建立資料夾：{e}")

# 建立 GUI 視窗
root = tk.Tk()
root.title("資料夾產生器")

# 標籤
name_label = tk.Label(root, text="請輸入名子：")
name_label.pack(pady=5)

# 名字輸入框
name_entry = tk.Entry(root, width=30)
name_entry.pack(pady=5)

# 按鈕
create_button = tk.Button(root, text="生成資料夾", command=create_folder)
create_button.pack(pady=10)

# 啟動主程式迴圈
root.mainloop()
