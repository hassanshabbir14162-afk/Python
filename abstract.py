from abc import ABC, abstractmethod

class Animal(ABC):

    def __init__(self, name, habitat):
        self.name=name
        self.habitat=habitat

    def display(self):
        print