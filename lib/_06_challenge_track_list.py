#  1. Describe the Problem

# _Put or write the user story here. Add any clarifying notes you might have._

# User Story:
# As a user
# So that I can keep track of my music listening
# I want to add tracks I've listened to and see a list of them.


## 2. Design the Class Interface

# _Include the initializer, public properties, and public methods with all parameters, return values, and side-effects._
class MusicTracker():
    def __init__(self):
        self.track_list=[]


    # add_track
    # Parameter:
        # track_name:string
    # Side-Effect:
    #    add track_name to track_list
    def add_track(self,track_name):
        if track_name != "" :
            self.track_list.append(track_name)
        else:
            raise Exception("Track name can not be empty") 




    # get_track_list
    # Params:
    # 0
    # Side- effects
        # return track_list 
    def get_track_list(self):
        return self.track_list