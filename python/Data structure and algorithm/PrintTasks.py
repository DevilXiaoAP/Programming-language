from stack import Queue

import random

class Printer:
    def __init__(self, ppm):
        self.pagerate = ppm
        self.currentTask = None
        self.timeRemaining = 0

    def tick(self):
        if self.currentTask != None:
            self.timeRemaining = self.timeRemaining - 1
            if self.timeRemaining <= 0:
                self.currentTask = None

    def busy(self):
        if self.currentTask != None:
            return True
        else:
            return False

    def startNext(self,newtask):
        self.currentTask = newtask
        self.timeRemaining = newtask.getPages() * 60/self.pagerate


class Task:
    def __init__(self,time):
        self.timestamp = time
        self.pages = random.randrange(1, 21)

    def getStamp(self):
        return self.timestamp

    def getPages(self):
        return self.pages

    def waitTime(self, currenttime):
        return currenttime - self.timestamp

def newPrintTask():
    num = random.randrange(1,2)
    if num == 1:
        return True
    else:
        return False

def simulation(numSeconds, pagePerMinute):

    labprinter = Printer(pagePerMinute)
    printQueue = Queue()
    waitngtimes = []

    for currentSecond in range(numSeconds):

        if newPrintTask():#查看是否有打印任务
            task = Task(currentSecond)#若有则记录当前时间，初始化打印任务
            printQueue.enqueue(task)#把打印任务加入到队列里

        if (not labprinter.busy()) and (not printQueue.isEmpty()):#如果打印机空闲，且队列不为空
            nexttask = printQueue.dequeue()#将下一个任务从打印队列中取出
            waitngtimes.append(nexttask.waitTime(currentSecond))#记录该任务的已经在队列中的等待时间
            labprinter.startNext(nexttask)#初始化当前任务需要打印的时间

        labprinter.tick()
    averageWait = sum(waitngtimes)/len(waitngtimes)
    print("Average Wait %6.2f secs %3d tasks remaining."\
          %(averageWait, printQueue.size()))

for i in range(10):
    simulation(3600, 5)
