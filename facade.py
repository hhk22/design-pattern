# Facade Pattern
# 복잡한 로직은 안으로 캡슐화하고, Client쪽에서는 일관된 인터페이스를 제공하는것이 주 목적.=


class EmailService:
    def send_email(self, message):
        print(f"Sending email: {message}")


class SMSService:
    def send_sms(self, message):
        print(f"Sending SMS: {message}")


class PushNotifications:
    def send_notification(self, messsage):
        print(f"Sending push notification: {messsage}")


class MessageManager:
    def __init__(self) -> None:
        self.email_service = EmailService()
        self.sms_service = SMSService()
        self.push_service = PushNotifications()

    def send_message(self, message: str, message_type: str):
        if message_type == "email":
            self.email_service.send_email(message)
        elif message_type == "sms":
            self.sms_service.send_sms(message)
        else:
            self.push_service.send_notification(message)


# Client
manager = MessageManager()
manager.send_message("Hi, Hello", 'email')
