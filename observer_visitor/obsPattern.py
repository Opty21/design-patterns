from __future__ import annotations

from typing import Callable


class Observer:
    def observe(self, sub: Subject, callback: Callable) -> None:
        sub.add(self, callback)

    def unobserve(self, sub: Subject) -> None:
        sub.remove(self)

class Subject:
    def __init__(self):
        self.observers = {}

    def add(self, observer: Observer,callback:Callable) -> None:
        self.observers[observer] = callback

    def remove(self, observer: Observer) -> None:
        if observer in self.observers:
            del self.observers[observer]

    def notify(self,*args) -> None:
        for callback in self.observers.values():
            callback(self)

