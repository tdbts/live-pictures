import kivy
kivy.require('1.2.0')

from sys import argv
from kivy.app import App
from kivy.core.window import Window
from LiveDisplay import LiveDisplay
from os import listdir
from os.path import isdir, isfile, join

# check what formats are supported for your targeted devices
# for example try h264 video and acc audo for android using an mp4
# container


class LivePictures(App):

    def __init__(self, **kwargs):
        super(LivePictures, self).__init__(**kwargs)
        self.videos = self.get_video_files()

    @staticmethod
    def get_videos_location():
        if len(argv) > 1:
            return argv[1]
        else:
            raise ValueError("Must specify video file or directory.")

    # for item in os.listdir(root):
    #     if os.path.isfile(os.path.join(root, item)):
    #         print item

    def get_video_files(self):
        files = []
        location = self.get_videos_location()

        if isfile(location):
            files.append(location)
        elif isdir(location):
            files.extend(self.retrieve_files_from_directory(location))
        else:
            raise ValueError("Invalid video(s) location specified.")

        return files

    @staticmethod
    def retrieve_files_from_directory(location):
        videos = []

        for item in listdir(location):
            if isfile(join(location, item)):
                videos.append(join(location, item))
        print("videos:", videos)
        return videos

    @staticmethod
    def configure_window():
        Window.borderless = True
        Window.rotation += 270

    def get_root_widget(self):
        return LiveDisplay(self.videos).start()

    def build(self):
        self.configure_window()

        return self.get_root_widget()


if __name__ == '__main__':
    LivePictures().run()
