messages = []
chat = [' ']
message = ' '
user = ''

class User:
    warnings = 0
    warn_reason = ''

    def __init__(self):
        pass
    def warn(self, reason):
        warnings += 1
        warn_reason + reason
    def pardon(self):
        warnings -= 1
        warn_reason = ''

class Jon:
    def __init__(self):
        self.isMod = True
        self.isAdmin = True
        self.isPerson = True
        self.isBot = False
        self.isMad = False
    def purge(self):
        if self.isMad:
            messages.append(message)
            chat.pop(messages.index(message))
            User.warn('You can\'t send that thing')
        else:
            pass
    def warn(self):
        User.warn('Just don\'t...')
    def pardon(self):
        User.pardon()