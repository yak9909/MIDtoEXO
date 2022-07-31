from .filter import *


class Object:
    def __init__(self, filters, start=1, end=2, layer=1, overlay=1):
        self.start = start
        self.end = end
        self.layer = layer
        self.overlay = overlay
        
        self.filters = filters
