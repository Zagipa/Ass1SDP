from abc import ABC, abstractmethod


class Observer(ABC):
    @abstractmethod
    def update(self, message):
        pass

class MessagePublisher:
    def __init__(self):
        self._observers = []

    def add_observer(self, observer):
        self._observers.append(observer)

    def remove_observer(self, observer):
        self._observers.remove(observer)

    def publish_message(self, message):
        for observer in self._observers:
            observer.update(message)


class EmailSubscriber(Observer):
    def update(self, message):
        print(f"Email: {message}")

class SMSSubscriber(Observer):
    def update(self, message):
        print(f"SMS: {message}")

class PushSubscriber(Observer):
    def update(self, message):
        print(f"Push: {message}")

# Factory Pattern
class MessagingSystemFactory:
    def create_message_publisher(self):
        return MessagePublisher()

if __name__ == "__main__":
    factory = MessagingSystemFactory()

    publisher = factory.create_message_publisher()
    email_subscriber = EmailSubscriber()
    sms_subscriber = SMSSubscriber()
    push_subscriber = PushSubscriber()

    publisher.add_observer(email_subscriber)
    publisher.add_observer(sms_subscriber)
    publisher.add_observer(push_subscriber)

    message = "Hello, this is 4th assignment."
    publisher.publish_message(message)
