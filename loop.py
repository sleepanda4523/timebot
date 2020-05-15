import threading
import time
import requests

URL = 'https://dsm6timebot.herokuapp.com' 
def print_apple():
    requests.get('https://dsm6timebot.herokuapp.com')
    threading.Timer(1200, print_apple).start()
    
print_apple()

