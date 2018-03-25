from kivy.uix.gridlayout import GridLayout
from LivePicture import LivePicture


class LiveDisplay(GridLayout):

    def __init__(self, filename, **kwargs):
        super(LiveDisplay, self).__init__(**kwargs)
        self.current = self.create_picture(filename)

    def create_picture(self, filename):
        return LivePicture(filename)

    def show_live_picture(self, source):
        if len(self.children) == 0:
            self.add_widget(self.current)

        if self.is_showing_source(source):
            return

        if self.current.source != source:
            self.swap_picture(self.create_picture(source))

        self.current.play()

    def is_showing_source(self, source):
        return self.current and self.current.source == source and self.current.state == 'play'

    def swap_picture(self, picture):
        self.unload_picture()
        self.remove_widget(self.current)
        self.current = picture
        self.add_widget(self.current)

    def unload_picture(self):
        if self.current:
            self.current.unload()

    def on_touch_down(self, touch):
        self.show_live_picture("/home/tdbts/Videos/vinny-and-kaytee-and-the-city.mp4")
        return True

    def start(self):
        self.show_live_picture(self.current.source)
        return self
