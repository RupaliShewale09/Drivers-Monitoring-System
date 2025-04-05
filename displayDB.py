import sqlite3
import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime

def launch_viewer(show_today=False):
    conn = sqlite3.connect("drowsiness_logs.db")
    cursor = conn.cursor()

    def refresh_tables():
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        return cursor.fetchall()

    def load_table_data(table_name):
        for item in tree.get_children():
            tree.delete(item)

        try:
            cursor.execute(f"PRAGMA table_info({table_name})")
            columns = [info[1] for info in cursor.fetchall()]
            
            
            tree["columns"] = columns
            tree["show"] = "headings"
            
            column_widths = {
                "id": 60,
                "timestamp": 160,
                "ear": 90,
                "mar": 90,
                "yaw_angle": 90,
                "status": 130
            }

            for col in columns:
                tree.heading(col, text=col.upper())
                tree.column(col, width=column_widths.get(col, 100),  anchor="center")  # Default width = 100 for any other column

            cursor.execute(f"SELECT * FROM {table_name}")
            rows = cursor.fetchall()
            for row in rows:
                tree.insert("", tk.END, values=row)
        except Exception as e:
            messagebox.showerror("Error", f"Could not load table: {e}")

    def show_today_table():
        today_table = "drowsiness_" + datetime.now().strftime("%Y_%m_%d")
        all_tables = refresh_tables()

        if (today_table,) in all_tables:
            table_var.set(today_table)
            load_table_data(today_table)
        else:
            messagebox.showinfo("No Data", f"No table found for today ({today_table})")

    #GUI setup
    root = tk.Tk()
    root.title("Drowsiness Detection Logs Viewer")
    root.geometry("800x600")
    root.configure(bg='white', highlightthickness=30, highlightcolor="turquoise")

    title_label = tk.Label(root, text="Monitoring System", font=("Cambria", 28,"bold"), bg='white')
    title_label.place_configure(x='230', y='20')

    table_var = tk.StringVar()
    all_table_names = [t[0] for t in refresh_tables()]
    table_dropdown = ttk.Combobox(root, textvariable=table_var, values=all_table_names)
    table_dropdown.set("Select a table")
    table_dropdown.place_configure(width='400',height='30',x='50', y='90')
    table_dropdown.configure(font=("Cambria", 11))

    load_btn = ttk.Button(root, text="Load Table", command=lambda: load_table_data(table_var.get()))
    load_btn.place_configure(height='30', x='460', y='90')

    today_btn = ttk.Button(root, text="Show Today's Table", command=show_today_table)
    today_btn.place_configure(height='30', x='565', y='90')

    tree = ttk.Treeview(root)
    tree.place_configure(width='620',height='350',x='50', y='150')
    
    
    style = ttk.Style()
    style.configure("TButton", font=("Cambria", 11))
    
    style.configure("Treeview", 
                rowheight=25, 
                font=("Cambria", 10),
                borderwidth=1,
                relief="solid")

    style.configure("Treeview.Heading", 
                    font=("Cambria", 10, "bold"), 
                    anchor="center", 
                    borderwidth=1,
                    relief="solid")

    style.layout("Treeview", [
        ('Treeview.treearea', {'sticky': 'nswe'}) 
    ])

    scroll_y = ttk.Scrollbar(root, orient="vertical", command=tree.yview)
    scroll_y.place_configure(x=670, y=150, height=350)  
    tree.configure(yscrollcommand=scroll_y.set)



    if show_today:
        show_today_table()

    root.mainloop()

# Only run standalone if not imported
if __name__ == "__main__":
    launch_viewer()
