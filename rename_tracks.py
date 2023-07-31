import os
import re


def remove_numbers(track_file_name):
    '''Removes the numbers at the beginning of the track file name'''

    numberless_track = ""

    for char in track_file_name:
        if char.isalpha():
            numberless_track = track_file_name[track_file_name.index(char):] 

            #If the track name is already numberless
            if numberless_track != "":
                break

    return numberless_track


if __name__ == "__main__":

    # Get folder 
    # tracks_folder = os.listdir("D:\\Users\\Philippe Lamy\\Music\\Downloads")
    tracks_folder = os.listdir("/home/lamiphil/Music/")

    for track in tracks_folder:

        track_name = track
        # Remove the track number
        track = remove_numbers(track)

        # Replace underscores with spaces
        track = track.replace("_", " ") 

        # Add spaces around the dash only if there are no spaces
        if "-" in track and " - " not in track:
            track = track.replace("-", " - ")

        # Replace dots with spaces except for the extension
        track =  track.replace(".", " ", track.count(".") - 1)

        # Capitalize the first letter of each word
        track = track.title()
        track = track.replace("Mp3", "mp3")
        track = track.replace("'T", "'t")
        track = track.replace("  ", " ")
        track = track.replace("(Original Mix)", "")
        track = track.replace("And", "and")
        
        # Remove the brackets and its content
        track = re.sub(r'\[.*?\]', '', track)

        # Find the last occurrence of the substring " - " to identify the section to remove
        last_occurrence_index = track.rfind(" - ")
        base, extension = os.path.splitext(track)
        last_separator_index = base.rfind(" - ")
        if last_separator_index != -1 and not extension:
            track =  base[:last_separator_index] + extension

        track = track.replace(" .mp3", ".mp3")

        print(track)
        os.rename("/home/lamiphil/Music/" + track_name, "/home/lamiphil/Music/" + track)
        # input("Press enter to continue...")

