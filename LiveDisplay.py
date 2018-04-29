from kivy.uix.gridlayout import GridLayout
from LivePicture import LivePicture
from Playlist import Playlist


class LiveDisplay(GridLayout):

    def __init__(self, videos, **kwargs):
        super(LiveDisplay, self).__init__(**kwargs)
        self.playlist = Playlist(videos)
        self.picture = LivePicture(self.playlist.get_current())

    def show_live_picture(self, source):
        if len(self.children) == 0:
            self.add_widget(self.picture)

        if self.is_showing_picture(source):
            return

        if self.picture.source != source:
            self.swap_picture(source)

        self.picture.play()

    def is_showing_picture(self, picture):
        return self.picture and self.picture.source == picture and self.picture.state == 'play' and self.picture.is_showing()

    def swap_picture(self, source):
        self.picture.source = source

    # Note: In order to receive touch events, need to add the following lines to
    # Kivy's 'config.ini' file:
    #   mouse = mouse
    #   mtdev_%(name)s = probesysfs,provider=mtdev
    #   hid_%(name)s = probesysfs,provider=hidinput
    # See https://github.com/mrichardson23/rpi-kivy-screen for more information.

    # We can use 'sx' and 'sy' touch properties to get the x / y proportions
    # vis-a-vis the widget, where the origin is in the bottom-left hand corner
    def on_touch_down(self, touch):
        print("touch:", touch)
        navigation_demarcation_x = 0.5
        picture = self.playlist.previous() if touch.sx < navigation_demarcation_x else self.playlist.next()
        self.show_live_picture(picture)
        return True

    def start(self):
        self.show_live_picture(self.picture.source)
        return self
