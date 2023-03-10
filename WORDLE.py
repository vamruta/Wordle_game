import random 
from collections import Counter
import tkinter as tk
from tkinter import messagebox

class WordleGameGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Wordle Game")
        self.wordle = Wordle()
        self.guess_frame = tk.Frame(self.master)
        self.guess_frame.pack()
        self.prev_guesses_frame = tk.Frame(self.master)
        self.prev_guesses_frame.pack()

        self.guesses_left = 6
        self.create_widgets()
        self.box_list[0].focus_set()
        self.prev_guesses = []
        self.guesses = []

    def validate_box(self, event):
        box = event.widget
        if len(box.get()) > 1:
            box.delete(1, tk.END)           

    def handle_backspace(self, event):
        box = event.widget
        if not box.get():
            index = self.box_list.index(box)
            if index > 0:
                self.box_list[index-1].focus_set()
                self.box_list[index-1].delete(0, tk.END)
            else:
                box.delete(len(box.get())-1, tk.END)
                index = self.box_list.index(box)
                if index > 0:
                    self.box_list[index-1].focus_set()

    def handle_keyrelease(self, event):
        box = event.widget
        index = self.box_list.index(box)
        if box.get():
            if index < 4:
                self.box_list[index + 1].focus_set()

    def create_boxlist(self, ):
        box_list = []
        for i in range(5):
            box = tk.Entry(self.master, width=5, justify='center', font=('Arial', 20))
            box.config(validatecommand=(box.register(lambda text: self.validate_box(box)), '%P'))
            box.pack(side=tk.LEFT, padx=5, in_= self.guess_frame )
            box.bind('<KeyRelease>', self.handle_keyrelease)
            box.bind('<BackSpace>', lambda event, index=i: self.handle_backspace(event))
            box_list.append(box)
            if i == 0:
                box.focus_set()                
            if i == 4:
                box.bind('<KeyRelease-Return>', lambda event: self.guess_btn.invoke())
        return box_list

    def create_widgets(self):
        self.box_list = self.create_boxlist()        

        self.guess_frame.pack(pady=10)
        self.prev_guesses_frame.pack(pady=10)

        self.guess_btn = tk.Button(self.master, text='Guess', command=self.submit_guess)
        #self.guess_btn.pack()

        self.status_label = tk.Label(self.master, text='')
        self.status_label.pack()

        self.guesses_left_label = tk.Label(self.master, text=f"Guesses left: {self.guesses_left} ")
        self.guesses_left_label.pack()

    def is_error(self, guess, res):
        if guess in self.prev_guesses:
            messagebox.showerror("Invalid Guess", f"You already guessed the word : {guess}")
            return True 
        elif isinstance(res, str):
            messagebox.showerror( "Invalid Guess", res )
            return True
        return False

    def show_prev_guesses(self, guess, res):
        if self.prev_guesses:
            prev_guess_frame = tk.Frame(self.prev_guesses_frame)
            prev_guess_frame.pack(side="bottom", padx=10)
        
            # Add labels for displaying the letters and colors
            for letter, color in zip(guess, res):
                prev_guess_label = tk.Label(prev_guess_frame, text=letter, width=2, font=("Arial", 18))
                if color == "green":
                    prev_guess_label.config(bg="green", fg="white")
                elif color == "yellow":
                    prev_guess_label.config(bg="yellow", fg="black")
                else:
                    prev_guess_label.config(bg="gray", fg="black")
                prev_guess_label.pack(side="left")

    def game_ended(self, res):
        if res.count('green') == 5:
            tk.messagebox.showinfo('Congratulations!', 'You guessed the word: ' + self.wordle.target)
            return True 
        elif self.guesses_left == 0 and res.count('green') < 5:
            tk.messagebox.showinfo('Game over', 'You ran out of guesses. The word was: ' + self.wordle.target)
            return True 
        return False

    def submit_guess(self):
        guess = ''.join([box.get() for box in self.box_list])
        res = self.wordle.check(guess)

        if self.is_error( guess, res ):
            return

        for i, box in enumerate(self.box_list):
            if res[i] == 'green':
                box.config(bg='green', fg='white')
            elif res[i] == 'yellow':
                box.config(bg='yellow', fg='black')
            else:
                box.config(bg='gray', fg='black')        

        self.guesses_left -= 1
                
        self.guesses_left_label.config( text = f"Guesses left: {self.guesses_left}", font=('Arial', 10) )

        self.prev_guesses.append( guess )       

        self.show_prev_guesses(guess, res)

        if self.game_ended(res):
            self.master.destroy()     
        
class Wordle:
    def __init__(self):        
        with open("words.txt", "r") as f: words = f.readlines()
        #Filter the words that have exactly 5 letters and return them as a list
        self.word_list = [word.strip() for word in words if len(word.strip()) == 5]
        self.target = random.choice(self.word_list)
        self.word_list = set(self.word_list)    

    def check(self, guess):
        res = []
        target = self.target
        target_letters = Counter(target)

        if guess not in self.word_list:
            return "Invalid word. Please enter a valid 5 letter word."

        for i in range(5):
            if guess[i] == target[i]:
                res.append('green')
                target_letters[guess[i]] -= 1

                if target_letters[guess[i]] == 0:
                    del target_letters[guess[i]]
            else:
                res.append('gray')

        for i in range(5):
            if guess[i] != target[i] and guess[i] in target_letters and target_letters[guess[i]] > 0:
                res[i] = 'yellow'
                target_letters[guess[i]] -= 1

        return res

root = tk.Tk()
game = WordleGameGUI(root)
root.mainloop()
