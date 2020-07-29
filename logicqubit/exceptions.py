#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Author Cleoner S. Pietralonga
# e-mail: cleonerp@gmail.com
# Apache License

class LogicQubitError(Exception):

    def __init__(self, message):
        super().__init__(message)
        self.message = message

    def __str__(self):
        return repr(self.message)