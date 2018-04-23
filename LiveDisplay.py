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
            self.add_widget(live_picture)

        if self.is_showing_picture(live_picture):
            return

        if self.current.source != live_picture.source:
            self.swap_picture(live_picture)

        self.current.play()

    def is_showing_picture(self, picture):
        return self.current and self.current == picture.source and self.current.state == 'play' and self.current.is_showing()

    def swap_picture(self, picture):
        self.current.unload()
        self.remove_widget(self.current)
        self.add_widget(picture)
        self.current = picture

    # We can use 'sx' and 'sy' touch properties to get the x / y proportions
    # vis-a-vis the widget, where the origin is in the bottom-left hand corner
    def on_touch_down(self, touch):
        navigation_demarcation_x = 0.5
        picture = self.pictures.previous() if touch.sx < navigation_demarcation_x else self.pictures.next()
        self.show_live_picture(LivePicture(picture))
        return True

    def start(self):
        self.show_live_picture(self.current)
        return self
