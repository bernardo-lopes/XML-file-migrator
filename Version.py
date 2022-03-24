import xml.etree.ElementTree as ET
from termcolor import colored

class Version:
    def __init__(self, nbr):
        self.nbr = nbr
        self.changes = []

    def add_change(self, change):
        self.changes.append(change)