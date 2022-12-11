import tkinter as tk
from filter import Filter


class App:
    def __init__(self):
        self.window = tk.Tk()
        # center the window
        self.window.eval('tk::PlaceWindow . center')
        self.window.title("*FutureTeamName* - BEST Coding Marathon 2023")
        self.window.geometry("960x540")
        self.window.resizable(True, True)
        self.window.config(bg="white")

        self.filter = Filter()

        # create label for input field
        label1 = tk.Label(
            self.window, text="Unfiltered text", font=("Arial", 18))

        # create input field
        self.input_field = tk.Text(
            self.window, width=60, height=7, bd=5, relief='groove', wrap=tk.WORD, font=("Arial", 12))

        # create button
        self.button = tk.Button(
            self.window, text="Filter", width=30, height=2, bd=5, command=self.click, font=("Arial", 12))

        # create label for output field
        label2 = tk.Label(
            self.window, text="Filtered text", font=("Arial", 18))

        # create output field
        self.output_field = tk.Text(
            self.window, width=60, height=7, bd=5, relief='groove', wrap=tk.WORD, font=("Arial", 12), state=tk.DISABLED)

        # create label for black list
        label3 = tk.Label(
            self.window, text="Black list", font=("Arial", 18))

        # create black list field
        self.black_list_field = tk.Text(
            self.window, width=30, height=25, bd=5, relief='groove', wrap=tk.WORD, font=("Arial", 12))

        # place widgets
        label1.pack(pady=5, padx=10)
        self.input_field.pack(pady=10, padx=10)
        self.button.pack(pady=30, padx=10)
        label2.pack(pady=5, padx=10)
        self.output_field.pack(pady=10, padx=10)
        label3.pack(pady=5, padx=10)
        self.black_list_field.pack(pady=10, padx=10)

        # change position of widgets
        label1.place(relx=0.35, rely=0.05, anchor=tk.CENTER)
        self.input_field.place(relx=0.35, rely=0.25, anchor=tk.CENTER)
        self.button.place(relx=0.35, rely=0.5, anchor=tk.CENTER)
        label2.place(relx=0.35, rely=0.65, anchor=tk.CENTER)
        self.output_field.place(relx=0.35, rely=0.85, anchor=tk.CENTER)
        label3.place(relx=0.8, rely=0.05, anchor=tk.CENTER)
        self.black_list_field.place(relx=0.8, rely=0.548, anchor=tk.CENTER)

        # set default black list
        self.black_list_field.insert(tk.END, ", ".join(self.filter.black_list))

    def click(self):
        # get input from input field
        input = self.input_field.get(1.0, tk.END)

        input = input.split()
        words_list = []
        output = ""
        for word in input:
            if self.filter.isVulgar(word):
                words_list.append(word[0] + "*" * (len(word) - 1))
            else:
                words_list.append(word)
        output = " ".join(words_list)

        # change text of output field
        self.output_field.config(state=tk.NORMAL)
        self.output_field.delete(1.0, tk.END)
        self.output_field.insert(tk.END, output)
        self.output_field.config(state=tk.DISABLED)

    def run(self):
        self.window.mainloop()
