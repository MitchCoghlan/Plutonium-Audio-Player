# Made by Mitch Coghlan
# Bugs might be present

# NOTE: REQUIRES PYGAME TO BE INSTALLED


from tkinter import *
from tkinter import filedialog
import pygame
import os



root = Tk()
root.title("Plutonium Audio Player (Version 0.0.2)")
root.geometry("550x350")

pygame.mixer.init()

songs = []
current_song = ""
paused = False

menubar = Menu(root)
root.config(menu=menubar, bg="black")

def load_music():
    global current_song, songs
    root.directory = filedialog.askdirectory()
    
    for song in os.listdir(root.directory):
        name, ext = os.path.splitext(song)
        if ext == ".mp3" or ext == ".wav" or ext == ".ogg":
            songs.append(song)

    for song in songs:
        songlist.insert("end", song)
        print(song)
        
        
    songlist.selection_set(0)
    current_song = songs[songlist.curselection()[0]]
    
def play_song():
    global current_song, paused
    
    if not paused:
        pygame.mixer.music.load(os.path.join(root.directory, current_song))
        pygame.mixer.music.play()
    else:
        pygame.mixer.music.unpause()
        paused = False
        
        
        
def pause_song():
    global paused
    pygame.mixer.music.pause()
    paused = True
    print("Paused")
    
def next_song():
    global current_song, paused, songs
    try:
        songlist.selection_clear(0, END)
        songlist.selection_set(songs.index(current_song) + 1)
        current_song = songs[songlist.curselection()[0]]
        play_song()
    except:
        pass
    
    
def prev_song():
    global current_song, paused, songs
    try:
        songlist.selection_clear(0, END)
        songlist.selection_set(songs.index(current_song) - 1)
        current_song = songs[songlist.curselection()[0]]
        play_song()
    except:
        pass
    
    
    
    

    
    
file_menu = Menu(menubar, tearoff=False)
file_menu.add_command(label='Open Directory', command=load_music)
menubar.add_cascade(label="File", menu=file_menu)    

songlist = Listbox(root, bg="black", fg="green", width=100, height=15)
songlist.pack()
    
action_bar = Frame(root, bg="black")
action_bar.pack()

image_play = PhotoImage(file="icon_play.png")
image_pause = PhotoImage(file="icon_pause.png")
image_next = PhotoImage(file="icon_next.png")
image_prev = PhotoImage(file="icon_prev.png")

play_button = Button(action_bar, bg='black', borderwidth="0", image=image_play, command=play_song)
pause_button = Button(action_bar, bg='black', borderwidth="0", image=image_pause, command=pause_song)
next_button = Button(action_bar, bg='black', borderwidth="0", image=image_next, command=next_song)
prev_button = Button(action_bar, bg='black', borderwidth="0", image=image_prev, command=prev_song)

play_button.grid(row=0, column=1, padx=7, pady=10)
pause_button.grid(row=0, column=2, padx=7, pady=10)
next_button.grid(row=0, column=3, padx=7, pady=10)
prev_button.grid(row=0, column=0, padx=7, pady=10)

root.mainloop()
