#!/usr/bin/python3

class Classe1:

    def __init__(self):
        print(':D')

    def start(self, status):
        return 'All right!'

    def stop(self):
        return 'Off...'

class Classe2:

    def __init__(self, engine):
        self.engine = engine
    
    def start(self, status):
        return 'All right!'

    def stop(self):
        return 'Off...'