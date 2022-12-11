import tkinter as tk
from filter import Filter


class App:
    def __init__(self):
        self.window = tk.Tk()
        # Center the window
        self.window.eval('tk::PlaceWindow . center')

        self.window.title("*FutureTeamName* - BEST Coding Marathon 2023")
        self.window.geometry("960x540")
        self.window.resizable(True, True)
        self.window.config(bg="white")

        self.filter = Filter()

        # Create label for input field
        label1 = tk.Label(
            self.window, text="Unfiltered text", font=("Arial", 18))

        # Create input field
        self.input_field = tk.Text(
            self.window, width=60, height=7, bd=5, relief='groove', wrap=tk.WORD, font=("Arial", 12))

        # Create button
        self.button = tk.Button(
            self.window, text="Filter", width=30, height=2, bd=5, command=self.click, font=("Arial", 12))

        # Create label for output field
        label2 = tk.Label(
            self.window, text="Filtered text", font=("Arial", 18))

        # Create output field
        self.output_field = tk.Text(
            self.window, width=60, height=7, bd=5, relief='groove', wrap=tk.WORD, font=("Arial", 12), state=tk.DISABLED)

        # Create label for black list
        label3 = tk.Label(
            self.window, text="Black list", font=("Arial", 18))

        # Create black list field
        self.black_list_field = tk.Text(
            self.window, width=30, height=25, bd=5, relief='groove', wrap=tk.WORD, font=("Arial", 12))

        # Place widgets
        label1.pack(pady=5, padx=10)
        self.input_field.pack(pady=10, padx=10)
        self.button.pack(pady=30, padx=10)
        label2.pack(pady=5, padx=10)
        self.output_field.pack(pady=10, padx=10)
        label3.pack(pady=5, padx=10)
        self.black_list_field.pack(pady=10, padx=10)

        # Set position of widgets
        label1.place(relx=0.35, rely=0.05, anchor=tk.CENTER)
        self.input_field.place(relx=0.35, rely=0.25, anchor=tk.CENTER)
        self.button.place(relx=0.35, rely=0.5, anchor=tk.CENTER)
        label2.place(relx=0.35, rely=0.65, anchor=tk.CENTER)
        self.output_field.place(relx=0.35, rely=0.85, anchor=tk.CENTER)
        label3.place(relx=0.8, rely=0.05, anchor=tk.CENTER)
        self.black_list_field.place(relx=0.8, rely=0.548, anchor=tk.CENTER)

        # Set default black list
        self.black_list_field.insert(tk.END, ", ".join(self.filter.black_list))

    def click(self):
        self.update()

        # get input from input field
        input_str = self.input_field.get(1.0, tk.END)

        # split input into a list of words
        words = input_str.split()

        # create a list of processed words
        processed_words = []

        # loop through each word in the input
        for word in words:
            # check if the word is vulgar
            if self.filter.isVulgar(word, lemmatized=False) or self.filter.isVulgar(word, lemmatized=True):
                # if the word is vulgar, replace it with asterisks
                processed_words.append("*" * len(word))
            else:
                # if the word is not vulgar, keep it as is
                processed_words.append(word)

        # join the processed words into a single string
        output_str = " ".join(processed_words)

        # change text of output field
        self.output_field.config(state=tk.NORMAL)
        self.output_field.delete(1.0, tk.END)
        self.output_field.insert(tk.END, output_str)
        self.output_field.config(state=tk.DISABLED)

    def update(self):
        # get input from black list field
        black_list_str = self.black_list_field.get(1.0, tk.END)

        # split input into a list of words
        black_list = black_list_str.split(",")

        # remove leading and trailing whitespace from each word
        black_list = [word.strip() for word in black_list]

        # update the filter's black list with the new words
        self.filter.black_list = black_list

        # preprocess the black list words
        lemmatized_black_list = [
            self.filter.preprocess(word) for word in black_list]

        # update the filter's lemmatized black list with the preprocessed words
        self.filter.black_list_lemmatized = lemmatized_black_list

    def run(self):
        # start the main event loop for the window
        self.window.mainloop()
