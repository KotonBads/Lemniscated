class Guild:
    def __init__(self):
        self.members = open('lemniscated\members.txt', 'r')
        self.banned = open('lemniscated\\banned.txt')
        self.lines = self.members.readlines()
    
    def add_member(self, username):
        with open('lemniscated\members.txt', 'a') as f:
            f.write(f'{username}\n')
    
    def kick_member(self, username):
        for line in self.lines:
            if line.strip('\n') != username:
                self.members.write(line) #doesn't work yet lmao

class Chat:
    def __init__(self, message):
        self.message = message
    
    def save_chat(self):
        with open('lemniscated\chat.txt') as f:
            f.write(self.message)
    
    def purge_chat(self, amount):
        with open('lemniscated\chat.txt', 'w') as f:
            f.writelines(lines[:-amount])
    
    def chat_revive(self):
        print('@everyone')

class User:
    def __init__(self, username, role):
        self.isMuted = False
        self.canChat = True
        self.isBanned = False
        self.warnings = 0
        self.mute_time = 0
        self.warn_reason = []
        self.role = role

    def send_message(self, message):
        self.message = message

    def warn(self, reason):
        self.warnings += 1
        self.warn_reason.append(reason)

    def pardon(self):
        self.warnings -= 1
        self.warn_reason = ''
    
    def mute(self, time):
        self.mute_time = time
        self.isMuted = True
        self.canChat = False
    
    def unmute(self):
        self.mute_time = 0
        self.isMuted = False
        self.canChat = True

class Jon:
    def __init__(self):
        self.isMod = True
        self.isAdmin = True
        self.isPerson = True
        self.isBot = False
        self.isMad = False

    def purge(self, amount):
        if self.isMad:
            Chat.purge_chat(amount)
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

guild = Guild()
guild.add_member('test')