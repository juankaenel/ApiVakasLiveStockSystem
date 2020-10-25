from django.core.mail import EmailMessage
import socket
socket.getaddrinfo('localhost', 8080)
class Utils:
    @staticmethod
    def send_email(data):
        email = EmailMessage(subject=data['email_subject'],body=data['email_body'],to=[data['to_email']])
        email.send()
