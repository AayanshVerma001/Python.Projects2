import tkinter as tk
import time
from tkinter import messagebox

sample_text = (
    "The quick brown fox jumps over the lazy dog. "
    "Typing speed tests are a great way to improve your keyboard skills. "
    "Keep practicing to get faster and more accurate!"
)

class TypingSpeedTest:
    def __init__(self, master):
        self.master = master
        master.title("Typing Speed Test")
        master.geometry("700x400")

        self.text_to_type = sample_text
        self.start_time = None

        self.label = tk.Label(master, text="Type the text below:", font=("Arial", 14))
        self.label.pack(pady=10)

        self.text_display = tk.Text(master, height=5, width=80, wrap='word', font=("Arial", 12), state='disabled')
        self.text_display.pack()
        self.text_display.configure(state='normal')
        self.text_display.insert(tk.END, self.text_to_type)
        self.text_display.configure(state='disabled')

        self.entry = tk.Text(master, height=5, width=80, wrap='word', font=("Arial", 12))
        self.entry.pack(pady=10)
        self.entry.bind("<KeyPress>", self.start_timer)

        self.result_label = tk.Label(master, text="", font=("Arial", 14), fg="blue")
        self.result_label.pack(pady=5)

        self.check_button = tk.Button(master, text="Check Speed", command=self.calculate_speed)
        self.check_button.pack(pady=5)

        self.reset_button = tk.Button(master, text="Reset", command=self.reset)
        self.reset_button.pack(pady=5)

    def start_timer(self, event):
        if self.start_time is None:
            self.start_time = time.time()

    def calculate_speed(self):
        typed_text = self.entry.get("1.0", tk.END).strip()
        end_time = time.time()

        if not typed_text:
            messagebox.showinfo("Typing Test", "Please type something first.")
            return

        time_taken = end_time - self.start_time
        time_taken_minutes = time_taken / 60

        word_count = len(typed_text.split())
        wpm = word_count / time_taken_minutes

        correct_chars = sum(1 for i, c in enumerate(typed_text) if i < len(self.text_to_type) and c == self.text_to_type[i])
        accuracy = (correct_chars / len(self.text_to_type)) * 100

        self.result_label.config(text=f"Speed: {wpm:.2f} WPM | Accuracy: {accuracy:.2f}%")

    def reset(self):
        self.start_time = None
        self.entry.delete("1.0", tk.END)
        self.result_label.config(text="")


if __name__ == "__main__":
    root = tk.Tk()
    app = TypingSpeedTest(root)
    root.mainloop()
