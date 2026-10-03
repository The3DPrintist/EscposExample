import requests
import time
from escpos.printer import Usb
# Documentation for escpos: https://python-escpos.readthedocs.io/en/latest/index.html

# --- CONFIGURATION ---
# Replace with your actual printer details
# the vendor id of epson is 0x04b8, you can also supply product id if you want a specific model only, but this SHOULD catch all the models of TM88s. If it wont print, look here first.
VENDORID = 0x04b8
#PRODUCTID = 0x0202

# The URL from which you want to fetch the print data
SERVER_URL = "https://baconipsum.com/api/?type=meat-and-filler&paras=1&format=text"

# How often to check the server (in seconds)
POLL_INTERVAL = 10

# --- INITIALIZATION ---
try:
    # Initialize the printer using escpos library
    printer = Usb(VENDORID)
    #printer = Usb(VENDORID,PRODUCTID)
except Exception as e:
    print(f"Could not connect to printer. Error: {e}")
    printer = None

def print_text(text):
    print("-" * 20)
    print(text)
    print("-" * 20)
    if printer is not None:
        printer.set(align='left')
        printer.text(text)
        printer.cut()

        #some more ideas:
        #printer.set(align='left')
        #printer.text("Hello World\n")
        #printer.image("logo.gif")
        #printer.barcode('4006381333931', 'EAN13', 64, 2, '', '')
        #printer.cut()

def main():
    print(f"Starting server polling every {POLL_INTERVAL} seconds...")
    
    while True:
        try:
            # Fetch data from the remote server
            response = requests.get(SERVER_URL)
            
            if response.status_code == 200:
               
                # The content is assumed to be a string or simple text, but you could also receive json and use it to make something fancy looking
                data = "example text: " + response.text
                print_text(data)
            else:
                print(f"Server returned status code {response.status_code}")

        except Exception as e:
            print(f"Error connecting to server: {e}")

        # Fixed delay between polls
        time.sleep(POLL_INTERVAL)

if __name__ == "__main__":
    main()
