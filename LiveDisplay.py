from kivy.uix.gridlayout import GridLayout
from LivePicture import LivePicture
from Playlist import Playlist


class LiveDisplay(GridLayout):

    def __init__(self, videos, **kwargs):
        super(LiveDisplay, self).__init__(**kwargs)
        self.pictures = Playlist(videos)
        self.current = LivePicture(self.pictures.get_current())

    def show_live_picture(self, live_picture):
        if len(self.children) == 0:
            self.add_widget(self.current)
            # self.add_widget(live_picture)

        if self.is_showing_picture(live_picture):
            return

        # if self.current.source != live_picture.source:
        if self.current.source != live_picture:
            self.swap_picture(live_picture)

        self.current.play()

    def is_showing_picture(self, picture):
        return self.current and self.current.source == picture and self.current.state == 'play' and self.current.is_showing()
        # return self.current and self.current == picture.source and self.current.state == 'play' and self.current.is_showing()

    def swap_picture(self, picture):
        print("self.current:", self.current)
        self.current.source = picture
        # self.current.unload()
        # self.remove_widget(self.current)
        # self.add_widget(picture)
        # self.current = picture

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
        picture = self.pictures.previous() if touch.sx < navigation_demarcation_x else self.pictures.next()
        # self.show_live_picture(LivePicture(picture))
        self.show_live_picture(picture)
        return True

    def start(self):
        self.show_live_picture(self.current.source)
        return self
