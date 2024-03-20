import Selection as Sel

import moviepy.editor as mp
import os


def mergeClips(clip_list):
    videos = [mp.VideoFileClip(file) for file in clip_list if os.path.splitext(file)[1]==".mp4"]
    if len(videos) != 0:
        return mp.concatenate(videos)
    return None

def exportClip(clip:mp.VideoFileClip, path):
    clip.write_videofile(path)
    
def exportClipList(clip_list, export_path, folder_name):
    #print(os.getcwd()) //dont delete, useful reminder later that hose are indirect paths not direct
    os.mkdir(export_path + folder_name)
    
    for i in range(len(clip_list)):
        name = f"file_{i}.mp4"
        exportClip(clip_list[i],f"{export_path}{folder_name}/",name)
    
    
def cutVideo(clip:mp.VideoFileClip, begin_t, end_t, precise_t = False):
    if not precise_t:
        return clip.subclip(begin_t,end_t+1)
    else:
        return clip.subclip(begin_t,end_t)

def cutTimeStampClips(clip:mp.VideoFileClip, timestamps : Sel.timeStamps, precise_t = False):
    list_of_vid = []
    for times in timestamps.time_list:
        list_of_vid.append(cutVideo(clip,times[0],times[1]))
    
    #security checks: what if list gives thing out of order and others
    return list_of_vid

def changeRes(clip:mp.VideoFileClip,res):
    clip = clip.resize(res)
    return clip



        
        




#All rewrite as class, not functions seperate from object??


#=====TESTING=====
if __name__ == "__main__":
    """
    timestamps = Sel.timeStamps("Test_Folder/test.txt")
    temp = cutVideo(mergeClips("Test_Folder/"),35,40)
    #exportClip(temp,"Test_Folder/","h.mp4",(1000,800))
    
    temp2 = cutVideo(mergeClips("Test_Folder/"),10,20)
    
    l = []
    l.append(temp)
    l.append(temp2)
    
    exportClipList(l,"Test_Folder/","export_folder4")
    
    
    print("Finished testing Video_Manipulations.py")
    """

    video = mergeClips(["Test_Folder/a.mp4","Test_Folder/b.mp4"])
    
    exportClip(video,"Test_Folder/test_h.mp4")

    #changeRes(video,(640,480))

    #exportClip(video,"temp/","selekcja_lowRes.mp4")

    #x = mergeClips(["C:/Users/domin/Desktop/aaaprojekt/Video_Selection_Tool/Test_Folder/h.mp4","C:/Users/domin/Desktop/aaaprojekt/Video_Selection_Tool/Test_Folder/test_video2.mp4"])
    #exportClip(x,"C:/Users/domin/Desktop/aaaprojekt/Video_Selection_Tool/Test_Folder/22h.mp4")

    