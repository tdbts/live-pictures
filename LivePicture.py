from kivy.uix.video import Video


class LivePicture(Video):

    def __init__(self, filename, **kwargs):
        super(LivePicture, self).__init__(**kwargs)
        self.height = 0
        self.source = filename
        self.create_video()
        self.state = 'pause'

    def create_video(self):
        self.options = {'eos': 'loop'}
        self.allow_stretch = True
        self.volume = 0

    def play(self):
        self.state = 'play'

    def pause(self):
        self.state = 'pause'

    def stop(self):
        self.state = 'stop'

    def is_showing(self):
        return self.height == 1
