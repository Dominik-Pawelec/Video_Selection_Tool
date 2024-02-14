from proglog import ProgressBarLogger
from moviepy.editor import VideoFileClip

class Logger(ProgressBarLogger):
    def __init__(self):
        self.percentage = 0

    def callback(self, **changes):
        for (parameter, value) in changes.items():
            print ('Parameter %s is now %s' % (parameter, value))

    def bars_callback(self, bar, attr, value,old_value=None): 
        self.percentage = (value / self.bars[bar]['total']) * 100
        
    
    def drawBar(self):
        bar = "█"*int(self.percentage) + " "*(100-int(self.percentage))
        return bar

