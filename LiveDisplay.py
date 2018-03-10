from kivy.uix.video import Video


class LiveDisplay(Video):

    def __init__(self, filename):
        super(LiveDisplay, self).__init__()

        self.source = filename
        self.create_video()

    def create_video(self):
        self.state = 'play'
        self.options = {'eos': 'loop'}
        self.allow_stretch = True
        self.volume = 0

    def on_touch_down(self, touch):
        print("Brrrrr")

    def on_touch_move(self, touch):
        print("ooooo")

    def on_touch_up(self, touch):
        print("lyyyyyyyyn!!!!")

    def build(self):
        return self.create_video()
