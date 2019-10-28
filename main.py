from file_sorter.subject import subject
from file_sorter.observer import observer
if __name__ == "__main__":
    sub = subject()
    observer_obj = observer()
    sub.attach(observe_object=observer_obj)
    sub.notify()
    sub.detach(observer_obj)