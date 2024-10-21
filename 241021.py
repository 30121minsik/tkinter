import tkinter as tk

# 기본 윈도우 생성
window = tk.Tk()
window.title("Login Form")

# 사용자 이름 레이블 및 입력 상자
username_label = tk.Label(window, text="Username:", font='Arial 12')
username_label.grid(row=0, column=0, padx=10, pady=10)

username_entry = tk.Entry(window, width=30)
username_entry.grid(row=0, column=1, padx=10, pady=10)

# 비밀번호 레이블 및 입력 상자
password_label = tk.Label(window, text="Password:", font='Arial 12')
password_label.grid(row=1, column=0, padx=10, pady=10)

password_entry = tk.Entry(window, show="*", width=30)
password_entry.grid(row=1, column=1, padx=10, pady=10)

# 로그인 버튼
login_button = tk.Button(window, text="Login", width=10, font='Arial 12')
login_button.grid(row=2, column=1, padx=10, pady=10, sticky='e')

# 메인 루프 시작
window.mainloop()
