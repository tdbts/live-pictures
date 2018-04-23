class Playlist:

    def __init__(self, videos, start_index=0):
        self.videos = videos
        self.index = start_index

    def next(self):
        self.increment()
        return self.get(self.index)

    def previous(self):
        self.decrement()
        return self.get(self.index)

    def get(self, index):
        return self.videos[index]

    def get_current(self):
        return self.get(self.index)

    def get_index_by_video(self, video):
        return self.videos.index(video)

    def increment(self):
        self.index = self._modify_within_bounds(self.index + 1)

    def decrement(self):
        self.index = self._modify_within_bounds(self.index - 1)

    def _modify_within_bounds(self, value):
        length = len(self.videos)
        return ((value % length) + length) % length
