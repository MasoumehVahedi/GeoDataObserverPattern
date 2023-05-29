
# Subject (Observable) class
class Observable:
    def __init__(self):
        self._observers = []
        self.status = None

    # add observer
    def attach(self, observer):
        self._observers.append(observer)

    # remove observer
    def detach(self, observer):
        self._observers.remove(observer)

    # notify observers
    def notify(self):
        for observer in self._observers:
            observer.updateData(self.status)


# Observer interface
class Observer:
    def updateData(self, status):
        pass

