import kivy
kivy.require('1.2.0')

from sys import argv
from os.path import dirname, join
from kivy.app import App
from kivy.uix.video import Video
from kivy.core.window import Window
from kivy.uix.label import Label

# check what formats are supported for your targeted devices
# for example try h264 video and acc audo for android using an mp4
# container


class VideoPlayerApp(App):

    def get_filename(self):
        if len(argv) > 1:
            return argv[1]
        else:
            raise ValueError("Must specify video.")

    @staticmethod
    def create_video(filename):
        video = Video(source=filename)
        video.state = 'play'
        video.options = {'eos': 'loop'}
        video.allow_stretch = True
        video.volume = 0

        return video

    def create_label(self):
        return Label(text="Broooooooklyyyyyyyyn!!!")

    def configure_window(self):
        Window.borderless = True
        Window.rotation += 270

    def get_root_widget(self):
        video = self.create_video(self.get_filename())

        video.add_widget(self.create_label())

        return video

    def build(self):
        self.configure_window()

        return self.get_root_widget()


if __name__ == '__main__':
    VideoPlayerApp().run()
