import os

accepted_audio_extensions = ['.wav', '.mp3', '.flac', '.aif', '.ogg']


def is_accepted_audio_file(filename):
    _, extension = os.path.splitext(filename)
    return extension.lower() in accepted_audio_extensions, extension
