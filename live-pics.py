import kivy
kivy.require('1.2.0')

from sys import argv
from os.path import dirname, join
from kivy.app import App
from kivy.uix.video import Video
from kivy.core.window import Window

# check what formats are supported for your targeted devices
# for example try h264 video and acc audo for android using an mp4
# container


class VideoPlayerApp(App):

    def build(self):
        
        if len(argv) > 1:
            filename = argv[1]
        else:
            raise ValueError("Must specify video.")
        
        video = Video(source=filename)
        video.state = 'play'
        video.options = {'eos': 'loop'}
        video.allow_stretch=True
        video.volume = 0

        Window.borderless = True
        Window.rotation += 270

        return video


if __name__ == '__main__':
    VideoPlayerApp().run()
