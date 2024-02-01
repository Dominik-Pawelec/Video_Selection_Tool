
def clearNumberStr(text):  
    times = text.split(":")
    if len(times) == 2:
        time_sec = int(times[0])*60+int(times[1])
    elif len(times) == 3:
        time_sec = int(times[0])*3600+int(times[1])*60+int(times[2])
    else:
        print(f"Something went wrong with clearNumberStr({text}). function aborted.")
        return
    return time_sec


class timeStamps:
    time_raw = []
    time_list = []
    def __init__(self,data_file):
        with open(data_file, encoding = "utf-8") as data:
            for line in data:
                division = line.find("-")
                nr_1 = "".join([line[x] for x in range(division)])
                nr_1 = nr_1.replace(" ","")
                nr_2 = "".join([line[division + x] for x in range(1,len(line)-division)])
                nr_2 =nr_2.replace(" ","").replace("\n","")

                self.time_raw.append([nr_1,nr_2]) #nit necessaty but maybe we'll be used
                self.time_list.append([clearNumberStr(nr_1),clearNumberStr(nr_2)])
            
    
        



if __name__ == "__main__":
    
    a = timeStamps("Test_Folder/test.txt")

    
    print(a.getTimeList())
    
    
    print("\nFinished testing Selection.py")