"""Observer Pattern"""

# Libraries
from abc import ABCMeta, abstractmethod


class Publisher(metaclass=ABCMeta):
    def add_observer(self, observer):
        pass

    def remove_observer(self, observer):
        pass

    def notify_all(self):
        pass

    def write_post(self, text):
        pass


class PlatziForum(Publisher):
    def __init__(self):
        self.users_list = []
        self.post = None

    def add_observer(self, observer):
        if observer not in self.users_list:
            self.users_list.append(observer)

    def remove_observer(self, observer):
        self.users_list.remove(observer)

    def notify_all(self):
        for observer in self.users_list:
            observer.notify(self.post)

    def write_post(self, text):
        self.post = text
        self.notify_all()


class Subscriber:
    def notify(self, post):
        pass


class UserA(Subscriber):
    def __init__(self):
        pass

    def notify(self, post):
        print('User A ha sido notificado - {}'.format(post))


class UserB(Subscriber):
    def __init__(self):
        pass

    def notify(self, post):
        print('User B ha sido notificado - {}'.format(post))


if __name__ == '__main__':
    foro = PlatziForum()
    user1 = UserA()
    user2 = UserB()

    foro.add_observer(user1)
    foro.add_observer(user2)

    foro.write_post('Post en Platzi')
