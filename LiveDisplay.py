from kivy.uix.video import Video


class LiveDisplay():

    @staticmethod
    def create_video(filename):
        video = Video(source=filename)
        video.state = 'play'
        video.options = {'eos': 'loop'}
        video.allow_stretch = True
        video.volume = 0

        return video

    def on_touch_down(self, touch):
        print("Brrrrr")

    def on_touch_move(self, touch):
        print("ooooo")

    def on_touch_up(self, touch):
        print("lyyyyyyyyn!!!!")

    def start(self, filename):
        return self.create_video(filename)

