class Widget(object):
    """docstring for Widget."""
    def __init__(self, name):
        super(Widget, self).__init__()
        self.name = name
        self.width = 50
        self.height = 50

    def size(self):
        return (self.width, self.height)

    def resize(self, width, height):
        self.width = width
        self.height = height

    def dispose(self):
        pass
