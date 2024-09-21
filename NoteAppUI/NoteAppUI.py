import tkinter as tk

class NoteAppUI:
    def __init__(self, root):
        self.root = root
        root.title("Приложение NoteAppUI")

        self.label = tk.Label(root, text = "Добро пожаловать в NoteAppUI!")
        self.label.pack()

        self.entry = tk.Entry(root)
        self.entry.pack()

        self.button = tk.Button(root, text = "Сохранить", command=self.save)
        self.button.pack()

    def save(self):
        # Логика сохранения записи
        print("Запись сохранена: ", self.entry.get())

if __name__ == "__main__":
    root = tk.Tk()
    app = NoteAppUI(root)
    root.mainloop()
