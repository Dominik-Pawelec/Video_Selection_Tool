import Selection as Sel

import moviepy.editor as mp
import os


def mergeClips(path):
    file_list = os.listdir(path)
    videos = [mp.VideoFileClip(path+file) for file in file_list]
    if len(videos) != 0:
        return mp.concatenate(videos)
    return None

def exportClip(clip:mp.VideoFileClip, export_path, file_name,render_res = None):
    path_file = export_path + file_name
    if os.path.exists(path_file):
        print(f"path {path_file} already exists, change name of the file to proceed")
        return #TO DO: auto change name
    if render_res != None:
        clip = clip.resize(render_res)
    clip.write_videofile(path_file)
    
def cutVideo(clip:mp.VideoFileClip, begin_t, end_t, precise_t = False):
    if not precise_t:
        return clip.subclip(begin_t,end_t+1)
    else:
        return clip.subclip(begin_t,end_t)

def cutTimeStampClips(clip:mp.VideoFileClip, timestamps : Sel.timeStamps, precise_t = False):
    list_of_vid = []
    for times in timestamps.time_list:
        list_of_vid.append(cutVideo(clip,times[0],times[1]))
    
    #security checks: what if list gives thing out of order
    return list_of_vid
        





#=====TESTING=====
if __name__ == "__main__":
    
    timestamps = Sel.timeStamps("Test_Folder/test.txt")
    
    print("Testing: video_manipulations.py ;")
    temp = cutVideo(mergeClips("Test_Folder/"),35,40)
    exportClip(temp,"Test_Folder/","h.mp4",(1000,800))
    
    
    print("Finished testing Video_Manipulations.py")