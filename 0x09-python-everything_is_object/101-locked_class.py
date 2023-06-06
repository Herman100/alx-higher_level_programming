#!/usr/bin/python3
class LockedClass:
    __slots__ = ["first_name"]

    def __setattr__(self, name, value):
        if name != "first_name":
            msg = "'LockedClass' object has no attribute '{}'"
            raise AttributeError(msg.format(name))

        super().__setattr__(name, value)
