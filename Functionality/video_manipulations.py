import moviepy.editor as mp
import os

def mergeClips(path):
    file_list = os.listdir(path)
    videos = [mp.VideoFileClip(path+file) for file in file_list]
    if len(videos) != 0:
        return mp.concatenate(videos)
    else:
        return None

def exportClip(clip:mp.VideoFileClip, export_path, file_name):
    path_file = export_path + file_name
    clip.write_videofile(path_file)
    

if __name__ == "__main__":
    print("Testing: video_manipulations.py ;")
    temp = mergeClips("Test_Folder/")
    exportClip(temp,"Test_Folder/","test.mp4")
    # path is "nice"