import tkinter as tk
from get_pid import get_pid

def run_get_pid(event):
    pid.configure(state='normal')
    pid.delete("0",tk.END)
    resolved_pid = get_pid('main', name.get())
    pid.insert('end', str(resolved_pid))

root = tk.Tk()
root.winfo_toplevel().title("GetPID")
tk.Label(root, text="Enter Business Name").grid(row=0)
tk.Label(root, text="Place ID (PID) Result:").grid(row=1)
root.bind('<Return>', run_get_pid)

name = tk.Entry(root, width=25)
pid = tk.Entry(root, width=25)
pid.configure(state='disabled')


name.grid(row=0, column=1)
pid.grid(row=1, column=1)

tk.Button(root, 
          text='Search', command=run_get_pid).grid(row=3, 
                                                       column=2, 
                                                       sticky=tk.W, 
                                                       pady=4)

tk.Button(root, 
          text='Quit', 
          command=root.quit).grid(row=3, 
                                    column=3, 
                                    sticky=tk.W, 
                                    pady=4)

root.mainloop()

