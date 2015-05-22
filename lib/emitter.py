class Emitter(object):
    def __init__(self):
        self._events = {}
        self.on = self.register
        self.off = self.unregister

    def _get_listeners(self, event):
        if not self._events.get(event, False):
            self._events[event] = []
        return self._events[event]

    def register(self, event, fn=None):
        if not fn in self._get_listeners(event) and fn:
            self._events[event].append(fn)
        if not fn:
            def add(fn):
                self._events[event].append(fn)
            return add

    def unregister(self, event, fn):
        i = fn in self._get_listeners(event)
        print(i)

    def emit(self, event, *args):
        for listener in self._get_listeners(event):
            if listener(*args) is True:
                self.unregister(event, listener)
        return self