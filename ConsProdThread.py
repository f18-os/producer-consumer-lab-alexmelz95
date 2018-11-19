from threading import Thread
import queue
import theHelp

class ConsProdThread(Thread):
    def __init__(self, functionName, params1=None, params2=None):
        ''' Constructor. '''

        Thread.__init__(self)
        self.functionName = functionName
        self.params1 = params1
        self.params2 = params2
        self.start()


    def run(self):
        try:
            func = getattr(theHelp, self.functionName)
            if self.params2 == None:
                func(self.params1)
            else:
                func(self.params1, self.params2)
        except queue.Full:
            time.sleep(.00001)



fileName = 'clip.mp4'

# shared queues
extractionQueue = queue.Queue(10)
grayscaleQueue = queue.Queue(10)
theHelp.finished1 = False
theHelp.finished2 = False
t1 = ConsProdThread('extractFrames',params1=fileName,params2=extractionQueue)
t2 = ConsProdThread('grayScale',params1=extractionQueue, params2=grayscaleQueue)
t3 = ConsProdThread('displayFrames', params1=grayscaleQueue)
