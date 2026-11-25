class Notification:
    def send_notification(self):
          pass
class EmailNotification(Notification):
    def send_notification(self):
          email_servvice.send_email(customer)
          
Class PushNotification(Notification):
    def send_notification(Self):
     firebase.send_push_notification(customer)
Class SmsNotification(Notification):
    def send_notification(self):
    africastalking.sendsms(customer)


          
     