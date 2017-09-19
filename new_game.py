class Game(object):
    steps = []

    def __init__(self):
        pass

    def start(self):
        pass

    def stop(self):
        pass

    def restart(self):
        self.stop()
        self.start()

    def pause(self):
        self.stop()

    def reply(self):
        for each_step in self.steps:
            self.print_screen(each_step)

    def print_screen(self, step):
        pass
