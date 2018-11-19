import ConsProdThread
import queue

fileName = 'clip.mp4'

# shared queues
extractionQueue = queue.Queue(10)
grayscaleQueue = queue.Queue(10)
theHelp.finished1 = False
theHelp.finished2 = False
t1 = ConsProdThread('extractFrames',params1=fileName,params2=extractionQueue)
t2 = ConsProdThread('grayScale',params1=extractionQueue, params2=grayscaleQueue)
t3 = ConsProdThread('displayFrames', params1=grayscaleQueue)
