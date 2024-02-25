from abc import ABCMeta, abstractmethod

class Subscriber(metaclass=ABCMeta):
    @abstractmethod
    def update(self):
        pass

class SMSSubscriber(Subscriber):
    def __init__(self, publisher) -> None:
        self.publisher = publisher
        self.publisher.attach(self)
    
    def update(self):
        print(type(self).__name__, self.publisher.get_news())

class EmailSubscriber(Subscriber):
    def __init__(self, publisher) :
        self.publisher = publisher
        self.publisher.attach(self)

    def update(self):
        print(type(self).__name__, self.publisher.get_news())

class NewsPublisher:
    def __init__(self):
        self.__subscribers = []
        self.__latestNews = None
    
    def attach(self, subscriber):
        self.__subscribers.append(subscriber)
    
    def detach(self):
        self.__subscribers.pop()
    
    def subscribers(self):
        return [type(x).__name__ for x in self.__subscribers]
    
    def notify_subscribers(self):
        for sub in self.__subscribers:
            sub.update()

    def add_news(self, news):
        self.__latestNews = news
    
    def get_news(self):
        return f"Got News >> {self.__latestNews}"

news_publisher = NewsPublisher()
for subscribers in [SMSSubscriber, EmailSubscriber]:
    subscribers(news_publisher)
    print("\nSubscribers:", news_publisher.subscribers())

    news_publisher.add_news("Hello World!")
    news_publisher.notify_subscribers()

news_publisher.detach()
news_publisher.add_news("Second World!")
news_publisher.notify_subscribers()