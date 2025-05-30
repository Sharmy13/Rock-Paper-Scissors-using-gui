import tkinter as tk
import random
#create main window
root=tk.Tk()
root.title("ROCK-PAPER-SCISSORS GAME")
root.geometry("400x350")
root.configure(bg="white")
#title at top of window
title=tk.Label(root,text="Rock-Paper-Scissors Game",font=("Times New Roman",16,"bold"),bg="white")
title.pack(pady=10)
#frame for buttons
button_frame=tk.Frame(root,bg="white")
button_frame.pack()
#label to show result
result_label=tk.Label(root,text="",font=("Comic Sans Ms",18,"bold"))
result_label.pack(pady=20)

def play(user_choice):
    options=["ROCK","PAPER","SCISSORS"]
    computer_choice=random.choice(options) # computer randomly chooses using random.choice()
    result=""
    if user_choice==computer_choice:
        result="👍It's a draw!"    
    elif(user_choice=="ROCK" and computer_choice=="SCISSORS") or (user_choice=="SCISSORS" and computer_choice=="PAPER") or (user_choice=="PAPER" and computer_choice=="ROCK"):
        result="🎉YAY! You Won"
    else:
        result="😒Computer won!"
    result_label.configure(text=f"You chose: {user_choice}\nComputer chose: {computer_choice}\n\n{result}")
    
def reset_game():
    result_label.configure(text="")
    
def exit_game():
    root.destroy()

#creating buttons 
rock_button=tk.Button(button_frame,text="ROCK",width=10,font=("Arial",12,"bold"),bg="grey",command=lambda:play("ROCK"))
rock_button.grid(row=0, column=0, padx=10, pady=10)

paper_button=tk.Button(button_frame,text="PAPER",width=10,font=("Arial",12,"bold"),bg="grey",command=lambda:play("PAPER"))
paper_button.grid(row=0, column=1, padx=10, pady=10)

scissors_button=tk.Button(button_frame,text="SCISSORS",width=10,font=("Arial",12,"bold"),bg="grey",command=lambda:play("SCISSORS"))
scissors_button.grid(row=0, column=2, padx=10, pady=10)

reset_button=tk.Button(button_frame,text="Reset",width=10,font=("Arial",12,"bold"),bg="grey",command=reset_game)
reset_button.grid(row=5, column=0, padx=10,pady=10)

exit_button = tk.Button(button_frame, text="Exit",width=10,font=("Arial",12,"bold"),bg="grey",command=exit_game)
exit_button.grid(row=5, column=1, padx=10,pady=10)


root.mainloop()
    
    
