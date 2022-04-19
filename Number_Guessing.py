from tkinter import *
import random

#CREATING THE WINDOW FOR GAME

root = Tk()
root.title("NUMBER GUESSING GAME")
root.geometry('540x450')
root.configure(bg='lavender blush')

chance_var = IntVar()



def new_game():
    global num, chance
    chance = 0
    #clear the content of entry
    guessInput.delete(0, "end")
    comment.delete(0, "end")
    chanceentry.delete(0, "end")
    guessButton.config(state='normal')
    num = random.randint(1 , 100)


def play_game():
    global chance
    numGuess = int(guessInput.get())
    chance += 1
    if numGuess < num:
        comment.delete(0, "end")
        comment.insert(0, "Hint:Try a Higher number!")
    elif numGuess > num:
        comment.delete(0, "end")
        comment.insert(0, "Hint:Try a smaller number!")
    else:
        comment.delete(0, "end")
        comment.insert(0, "      YOU WON!!   ")
        guessButton.configure(state='disabled')
    chance_var.set(chance)


textLabel = Label(text="   Guess a number between 1 and 100", font=("Atlas", 20, "bold"), bg = 'lavender blush')
textLabel.grid(row=0, column=0)
guessInput = Entry(font=("bold", 15), width=8)
guessInput.grid(row=2, column=0, padx=10, pady=10)
comment = Entry(font=("bold", 15),bg='lavender blush',fg='navy',bd=0)
comment.grid(row=4, column=0,  padx=20, pady=20)
chancelabel = Label(text="Number of guesses you have made:", font=("bold, italic",14) , bg ='lavender blush', bd =0)
chancelabel.grid(row=5, column=0)
chanceentry = Entry(font=("bold",14), width=4, textvariable= chance_var, bd=0, bg = 'lavender blush')
chanceentry.grid(row=5, column=0, sticky='e')
chanceentry.delete(0, "end")



startButton = Button(text="Start/Restart Game", bg = "steel blue", fg="white", font= ("bold",14), command=new_game)
startButton.grid(row=1, column=0, padx=20, pady=20)
guessButton = Button(text="GUESS", bg ="dark olive green", fg="white", font=("bold",14), state='disabled', command=play_game)
guessButton.grid(row = 3, column=0, padx = 10, pady = 10)
exitButton = Button(text="Exit", bg="brown", fg="white", font=("bold",14), command= root.destroy)
exitButton.grid(row=6, column=0, pady=20)

root.mainloop()
