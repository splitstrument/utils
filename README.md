# Utilities

Common code used in multiple different places. Included through local packages into rest of code. Installed by executing
`pip install -e helper_utils` in this folder.

## boolean_argparse

Used to neatly get boolean values from the command line. In Python 3.9, `BooleanOptionalAction` can be used for neater
handling of boolean arguments, but because of other libraries we were forced to use Python 3.8.

Simply us `str2bool` as type of `argparse argument`. Example: `parser.add_argument("--cautious-mode", type=str2bool)`

## stemloader

Used for easier loading of stems. Also supports preloading loading of stems when processed in the same order as they are
passed into it. Additionally, this can be used to load only some instruments when the track folder is organized as
described in the [`data_organizer` script](https://github.com/splitstrument/dataset-creation/tree/main/data_organizer). 

Example for simplifying stem loading: `StemLoader().get_stem(track_path)`

Example for stem loading with preloading: `StemLoader(source_folder, track_folder_names).get_stem(track_path)`

Example for stem loading with preloading and instrument selection: `StemLoader(source_folder, track_folder_names, instruments).get_stem(track_path)`

## audio_file_checker

Used to check file names for a valid audio extension.

Example: `is_audio_file, extension = is_accepted_audio_file(path)`