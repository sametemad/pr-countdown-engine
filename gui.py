import tkinter as tk
from main import calculate, save_log


def update():
    result = calculate()

    text = f"""
Days Used: {result['days_passed']}
Days Remaining: {result['days_remaining']}

CEC: {result['cec']}%
CELPIP: {result['celpip']}%
Docs: {result['docs']}%

Status: {result['status']}
"""

    result_label.config(text=text)

    # رنگ وضعیت
    if "CRITICAL" in result['status']:
        result_label.config(fg="red")
    elif "WARNING" in result['status']:
        result_label.config(fg="orange")
    else:
        result_label.config(fg="green")

    save_log(result)


# UI
root = tk.Tk()
root.title("PR Countdown Engine")
root.geometry("300x300")

title = tk.Label(root, text="PR COUNTDOWN", font=("Arial", 16))
title.pack(pady=10)

btn = tk.Button(root, text="Update", command=update)
btn.pack(pady=10)

result_label = tk.Label(root, text="", justify="left")
result_label.pack(pady=10)

root.mainloop()