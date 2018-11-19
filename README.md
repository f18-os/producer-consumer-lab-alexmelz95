# Producer Consumer Lab

This lab performs a grayscale video conversion and display using the producer -
consumer method. The program uses queues as semaphores to regulate how quickly
the frames are converted and displayed. The Queue class has built in locking
semantics to regulate use of shared resources between threads.

There are 3 main files relating to this conversion:
1) main.py
2) theHelp.py
3) ConsProdThread.py

# Instructions
1) Run 'python3 main.py' in terminal to perform the conversion
