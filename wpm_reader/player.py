import tkinter as tk
from tkinter import filedialog
import time
import typer
#from pydantic import BaseModel


class TextPlayer():
    window: tk.Tk
    text: str = ""
    current_word: int = 0
    is_playing: bool = False
    speed: int = 60

    def __init__(self):
        super().__init__()
        self.text_label = None
        self.play_button = None
        self.stop_button = None
        self.slider_label = None
        self.slider = None
        self.menu_bar = None
        self.file_menu = None

        self._scale_min = 30
        self._scale_max = 1000

        self._full_text = ""

        self._create_interface()

    def _create_interface(self):
        self.window = tk.Tk()
        self.window.attributes('-type', 'dialog')
        self.window.title("WPM Player")

        self.text_label = tk.Label(self.window, text=self.text)
        self.text_label.pack()

        self.play_button = tk.Button(self.window, text="Play", command=self.play)
        self.play_button.pack(side="left")

        self.stop_button = tk.Button(self.window, text="Stop", command=self.stop)
        self.stop_button.pack(side="left")

        self.slider_label = tk.Label(self.window, text="WPM:")
        self.slider_label.pack(side="left")

        self.slider = tk.Scale(
            self.window, from_=self._scale_min, to=self._scale_max, orient="horizontal", variable=self.speed
        )
        self.slider.pack(side="left")

        self.menu_bar = tk.Menu(self.window)
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(label="Load File", command=self.load_file)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)

        self.window.config(menu=self.menu_bar)

    def load_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
        if file_path:
            with open(file_path, "r") as file:
                self._full_text = file.read()
            self.text_label.config(text="Ready")

    def play(self):
        self.is_playing = True
        words = self._full_text.split()
        while self.is_playing and self.current_word < len(words):
            word = words[self.current_word]
            self.text_label.config(text=word)
            self.current_word += 1
            self._update()

    def stop(self):
        self.is_playing = False
        self.current_word = 0
        self.text_label.config(text="Stopped")

    def run(self):
        self.window.mainloop()
    
    def _update(self):
        self.speed = self.slider.get()
        self.window.update()
        wait_time = float(60 / self.speed)
        time.sleep(wait_time)



def main():
    typer.echo("Welcome to WPM Player!")

    player = TextPlayer()
    player.run()


if __name__ == "__main__":
    typer.run(main)
