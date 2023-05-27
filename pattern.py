
# Subject (Observable) class
class Observable:
    def __init__(self):
        self._observers = []
        self.status = None

    # add observer
    def add(self, observer):
        self._observers.append(observer)

    # remove observer
    def remove(self, observer):
        self._observers.remove(observer)

    # notify observers
    def notify(self):
        for observer in self._observers:
            observer.update(self.status)

    def get_status(self, status):
        print("Setting GeoData to: ", status)
        self.status = status
        self.notify()


# Observer interface
class Observer:
    def update(self, status):
        pass

