import yaml
import time
import random
import string

uuid = lambda k=16: "".join(random.choices(string.ascii_letters, k=k))


class Chat:
    def __init__(self, file="chat.yaml"):
        self.file = file
        self.load_chat()

    def save_chat(self):
        yaml.dump(self.chat, open(self.file, "w"))

    def load_chat(self):
        try:
            self.chat = yaml.safe_load(open(self.file))
        except FileNotFoundError:
            self.chat = []

    def purge_chat(self, amount):
        self.chat = self.chat[:-amount]

    def chat_revive(self):
        self.chat.append("@everyone")

    def send(self, user, message):
        self.chat.append({"user": user.uid, "at": time.time(), "content": message})


class User:
    def __init__(self, chat, roles=[]):
        self.uid = uuid()

        self.isMuted = False
        self.canChat = True
        self.isBanned = False
        self.warnings = 0
        self.mute_time = 0
        self.warn_reason = []
        self.roles = roles
        self.chat = chat
        self.muted_at = 0

        self.isMod = False
        self.isAdmin = False
        self.isPerson = True
        self.isBot = False
        self.isMad = False

    def send(self, message):
        if self.canChat:
            self.chat.send(self, message)

    def warn(self, reason):
        self.warnings += 1
        self.warn_reason.append(reason)

    def pardon(self):
        self.warnings -= 1
        self.warn_reason.pop()

    def mute(self, period):
        self.mute_time = period
        self.muted_at = time.time()
        self.isMuted = True
        self.canChat = False

    def unmute(self):
        self.mute_time = 0
        self.isMuted = False
        self.canChat = True

    def is_muted(self):
        if self.muted_at + self.mute_time < time.time():
            self.unmute()


class Jon(User):
    def __init__(self, chat):
        super().__init__(chat, [None])
        self.uid = None

        self.isMod = True
        self.isAdmin = True
        self.isPerson = True
        self.isBot = False
        self.isMad = False

    def purge(self, amount, user=None):
        if self.isMad:
            self.chat.purge_chat(amount)
            if user is not None:
                user.warn("You can't send that thing")
        else:
            pass

    def jwarn(self, user, reason):
        user.warn(reason)

    def jpardon(self, user):
        user.pardon()

    def jmute(self, user, time):
        if self.isMad:
            user.mute(time)


if __name__ == "__main__":
    chat = Chat()
    jon = Jon(chat)
    jon.isMad = True
    user1 = User(chat)
    user2 = User(chat)
    user1.send("Something")
    user2.send("Something racist")
    jon.purge(1, user2)
    user2.send("Something racist")
    jon.jmute(user2, 10000000000000000)
    user2.send("Something")
    print(chat.chat)
    print(user2.warnings, user2.warn_reason)
