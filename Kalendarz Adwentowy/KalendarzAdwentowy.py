import random
from datetime import datetime, timedelta
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

class AdventCalendarGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Kalendarz Adwentowy")
        self.master.geometry("600x400")

        # Dodanie tła jako zdjęcia
        background_image = Image.open("obrazy\\6169028.jpg").convert("RGBA")
        background_image = background_image.resize((600, 400), Image.Resampling.LANCZOS)

        # Ustawienie mniejszej przeźroczystości - zmień wartość alpha według potrzeb
        alpha = 255  # Zakres od 0 do 255, gdzie 0 to całkowita przeźroczystość, a 255 to brak przeźroczystości
        background_image.putalpha(alpha)

        self.background_image = ImageTk.PhotoImage(background_image)
        background_label = tk.Label(master, image=self.background_image)
        background_label.place(relwidth=1, relheight=1)

        self.tasks_file = "Kalendarz Adwentowy.txt"
        self.tasks = self.load_tasks()

        # Czcionka, kolor tekstu, i tło
        self.label = tk.Label(master, text=f"Do Świąt zostało: {self.count_days_until(datetime(2024, 12, 25))} dni!", font=("Calibri", 14, "bold"), fg='#402E21', bg='#fff2e9')  
        self.label.pack(pady=60, anchor='center')

        # Dodanie ikony programu
        icon_image = Image.open("obrazy\christmas-tree.png")
        icon_image = icon_image.resize((32, 32), Image.Resampling.LANCZOS)
        icon_image = ImageTk.PhotoImage(icon_image)
        self.master.iconphoto(False, icon_image)

        # Zmiana rozmiaru przycisku
        self.draw_button = tk.Button(master, text="Wylosuj zadanie na dzisiejszy dzień!", command=self.draw_task, height=2, width=30, font=("Calibri", 18, "bold"), fg='#402E21', bg='#fff2e9')  
        self.draw_button.pack(pady=20, anchor='center')

    def load_tasks(self):
        try:
            with open(self.tasks_file, 'r', encoding='utf-8') as file:
                tasks = [line.strip() for line in file.readlines()]
            return tasks
        except FileNotFoundError:
            messagebox.showerror("Error", "File not found!")
            self.master.destroy()

    def save_tasks(self):
        with open(self.tasks_file, 'w', encoding='utf-8') as file:
            for task in self.tasks:
                file.write(task + '\n')

    def draw_task(self):
        if not self.tasks:
            messagebox.showinfo("Wszystkie zadania ukończono!", "Wszystkie zadania ukończono!")
            self.master.destroy()
        else:
            selected_task = random.choice(self.tasks)
            self.tasks.remove(selected_task)
            self.save_tasks()

            task_window = tk.Toplevel(self.master)
            task_window.title("Dzisiejsze zadanie")
            task_window.geometry("1000x666")

            # Dodanie ikony do okna
            task_icon_image = Image.open("obrazy\christmas-tree.png")
            task_icon_image = task_icon_image.resize((32, 32), Image.Resampling.LANCZOS)
            task_icon_image = ImageTk.PhotoImage(task_icon_image)
            task_window.iconphoto(False, task_icon_image)

            # Dodanie tła jako zdjęcia dla okna z zadaniem
            task_background_image = Image.open("obrazy\\6169028.jpg")
            task_background_image = task_background_image.resize((1000,666), Image.Resampling.LANCZOS)
            self.task_background_image = ImageTk.PhotoImage(task_background_image)
            task_background_label = tk.Label(task_window, image=self.task_background_image)
            task_background_label.place(relwidth=1, relheight=1)

            # Kontener do wyśrodkowania etykiet na środku okna
            center_frame = tk.Frame(task_window, bg='#fff2e9')
            center_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

            task_label = tk.Label(center_frame, text=f"Dzisiejsze zadanie:", font=("Calibri", 14), fg='#402E21', bg='#fff2e9')  
            task_label.pack(pady=10)

            task_content = tk.Label(center_frame, text=selected_task, font=("Calibri", 24, "bold"), fg='#402E21', bg='#fff2e9' , wraplength=800, justify=tk.CENTER)  
            task_content.pack(pady=10)

            self.label.config(text=f"Do Świąt zostało: {self.count_days_until(datetime(2023, 12, 25))} dni!")

    def count_days_until(self, target_date):
        today = datetime.now()
        days_until = target_date - today
        return days_until.days

def main():
    root = tk.Tk()
    app = AdventCalendarGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
