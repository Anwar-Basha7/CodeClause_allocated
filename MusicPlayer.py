import os
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QListWidget, QPushButton, QSlider, QLabel
from PyQt5.QtGui import QColor
import pygame

class MusicPlayer(QMainWindow):
    def __init__(self):
        super().__init__()

        self.music_directory = ""
        self.current_file = None
        self.playing = False

        self.init_ui()

    def init_ui(self):
        self.setGeometry(200, 200, 500, 300)
        self.setWindowTitle("Music Player")

        # Buttons
        self.play_button = QPushButton("Play", self)
        self.play_button.setGeometry(50, 220, 75, 30)
        self.play_button.clicked.connect(self.play_music)
        self.play_button.setStyleSheet("background-color: lightgreen;")

        self.stop_button = QPushButton("Stop", self)
        self.stop_button.setGeometry(150, 220, 75, 30)
        self.stop_button.clicked.connect(self.stop_music)
        self.stop_button.setStyleSheet("background-color: lightcoral;")

        self.select_button = QPushButton("Select Music", self)
        self.select_button.setGeometry(250, 220, 100, 30)
        self.select_button.clicked.connect(self.select_music)
        self.select_button.setStyleSheet("background-color: lightblue;")

        # Volume slider
        self.volume_slider = QSlider(Qt.Horizontal, self)
        self.volume_slider.setGeometry(400, 220, 80, 30)
        self.volume_slider.setValue(50)
        self.volume_slider.valueChanged.connect(self.set_volume)

        # Progress bar
        self.progress_slider = QSlider(Qt.Horizontal, self)
        self.progress_slider.setGeometry(50, 260, 430, 30)

        # Playlist
        self.playlist = QListWidget(self)
        self.playlist.setGeometry(50, 30, 430, 150)
        self.playlist.itemDoubleClicked.connect(self.play_selected)

        # Song label
        self.song_label = QLabel("Currently Playing: ", self)
        self.song_label.setGeometry(50, 10, 400, 20)

    def play_music(self):
        if not self.playing and self.current_file:
            pygame.mixer.init()
            pygame.mixer.music.load(self.current_file)
            pygame.mixer.music.set_volume(self.volume_slider.value() / 100)
            pygame.mixer.music.play()
            self.playing = True
            self.song_label.setText(f"Currently Playing: {os.path.basename(self.current_file)}")

    def stop_music(self):
        if self.playing:
            pygame.mixer.music.stop()
            self.playing = False
            self.song_label.setText("Currently Playing: ")

    def set_volume(self):
        if self.playing:
            pygame.mixer.music.set_volume(self.volume_slider.value() / 100)

    def select_music(self):
        self.music_directory = QFileDialog.getExistingDirectory(self, "Select Music Directory")

        if self.music_directory:
            music_files = [file for file in os.listdir(self.music_directory) if file.endswith(".mp3")]
            self.playlist.clear()
            self.playlist.addItems(music_files)

    def play_selected(self):
        selected_item = self.playlist.currentItem()
        if selected_item:
            selected_file = os.path.join(self.music_directory, selected_item.text())
            self.current_file = selected_file
            self.play_music()

if __name__ == "__main__":
    app = QApplication([])
    player = MusicPlayer()
    player.show()
    app.exec_()
