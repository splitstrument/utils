import os
from pydub import AudioSegment


def load_file(path):
    # simpleaudio is a trash library that just doesn't play any sound when we feed it 4 byte data!?
    return AudioSegment.from_file_using_temporary_files(path).set_sample_width(2)


class StemLoader:
    cache = {}
    stems = []
    current_loader = None

    def __init__(self, source_folder=None, tracks=[], instruments=[]):
        if source_folder is not None and len(tracks) > 0:
            self.prepare_stem_list(instruments, source_folder, tracks)

    def prepare_stem_list(self, instruments, source_folder, tracks):
        for track in tracks:
            track_path = os.path.join(source_folder, track)
            if os.path.isdir(track_path):
                if len(instruments) > 0:
                    for instrument in instruments:
                        instrument_path = os.path.join(track_path, instrument)
                        if os.path.isdir(instrument_path):
                            for stem in os.listdir(instrument_path):
                                file_path = os.path.join(instrument_path, stem)
                                self.stems.append(file_path)
                else:
                    for stem in os.listdir(track_path):
                        file_path = os.path.join(track_path, stem)
                        self.stems.append(file_path)

    def get_stem(self, path):
        if path in self.cache:
            return self.cache.pop(path)
        else:
            return load_file(path)

    def preload_next(self, path):
        if len(self.stems) <= 0:
            if path in self.cache:
                self.cache.pop(path)
            next_index = self.stems.index(path) + 1
            if next_index < len(self.stems):
                next_path = self.stems[next_index]
                if next_path not in self.cache:
                    self.cache[next_path] = load_file(next_path)
