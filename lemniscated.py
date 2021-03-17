class Chat:
    def __init__(self, message):
        self.message = message
        self.chat_file_w = open('lemniscated\chat.txt', 'w')
    
    def save_chat(self):
        self.chat_file_w.write(self.message)

class User:
    warnings = 0
    warn_reason = []
    mute_time = 0

    def __init__(self, message):
        self.isMuted = False
        self.canChat = True
        self.message = message

    def warn(self, reason):
        warnings += 1
        warn_reason.append(reason)

    def pardon(self):
        warnings -= 1
        warn_reason = ''
    
    def mute(self, time):
        mute_time = time
        self.isMuted = True
        self.canChat = False

class Jon:
    def __init__(self):
        self.isMod = True
        self.isAdmin = True
        self.isPerson = True
        self.isBot = False
        self.isMad = False

    def purge(self, amount):
        if self.isMad:
            
            User.warn('You can\'t send that thing')
        else:
            pass

    def warn(self, reason):
        User.warn(reason)

    def pardon(self):
        User.pardon()
    
    def mute_member(self, time):
        if self.isMad:
            User.mute(time)
