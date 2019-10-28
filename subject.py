import os
class subject(object):
    def __init__(self):
        self.observers = []
        self.state = False
        self.DOWNLOAD_DIR = "D:\\userdata\\arpitm\\Downloads"


    def attach(self, observe_object):
        self.observers.append(observe_object)

    def notify(self):
        if os.path.exists(self.DOWNLOAD_DIR):
            if len(os.listdir(self.DOWNLOAD_DIR)) > 0:
                self.state = True
            else:
                self.state = False
        for observer in self.observers:
            observer.update(self.state)

    def detach(self, observer_object):
        self.observers.remove(observer_object)



