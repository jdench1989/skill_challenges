from lib.challenge_six import *
import pytest

# given a track_name ,add track_name to track_list
def test_given_track_name_adds_track_to_list():
    music_tracker=MusicTracker()
    music_tracker.add_track("Happy song")
    assert music_tracker.get_track_list()==["Happy song"]

# add two track_names ,return track_list with both tracks
def test_given_two_track_names_adds_both_tracks_to_list():
    music_tracker=MusicTracker()
    music_tracker.add_track("Happy song")
    music_tracker.add_track("Sad song")
    assert music_tracker.get_track_list()==["Happy song","Sad song"]

# test given empty string does not add to track_list
def test_given_empty_string_does_not_add_to_track_list():
    music_tracker=MusicTracker()
    with pytest.raises(Exception) as e:
        music_tracker.add_track("")
    error_message=str(e.value)
    assert error_message=="Track name can not be empty"