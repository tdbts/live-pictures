import kivy
kivy.require('1.2.0')

from sys import argv
from kivy.app import App
from kivy.core.window import Window
from LiveDisplay import LiveDisplay

# check what formats are supported for your targeted devices
# for example try h264 video and acc audo for android using an mp4
# container


class LivePictures(App):

    @staticmethod
    def get_filename():
        if len(argv) > 1:
            return argv[1]
        else:
            raise ValueError("Must specify video.")

    def configure_window(self):
        Window.borderless = True
        Window.rotation += 270

    def get_root_widget(self):
        return LiveDisplay().start(self.get_filename())

    def build(self):
        self.configure_window()

        return self.get_root_widget()


if __name__ == '__main__':
    LivePictures().run()
