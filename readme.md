# Automated Receipt Printing System

A Python-based service that fetches data from a remote server and automatically prints it via a USB thermal printer using the `python-escpos` library.

## Overview

This script is designed to act as a bridge between a web service (or any API) and a physical thermal printer. It polls a specified URL at regular intervals; every time new data is successfully fetched, it is formatted and sent to the connected printer.

## Features
- **Automatic Polling:** Automatically fetches data from a defined URL at a configurable interval.
- **ESC/POS Support:** Utilizes the `python-escpos` library to handle standard thermal printer commands (cutting paper, text alignment, etc.).
- **Robust Connections:** Includes error handling for both network requests and printer connectivity issues.

## Prerequisites
Before running the script, ensure you have the following:
- Python 3.x installed.
- A USB Thermal Printer connected to your machine.
- Access to the `escpos` library (which requires some system dependencies like `libusb`).

## Installation

1. **Clone or download** this repository.
2. **Install dependencies:**
   ```bash
   pip install python-escpos[all]
   ```
   ```bash
   pip install requests
   ```
3. **System Dependencies:**
   Depending on your OS, you may need to install `libusb` (e.g., `sudo apt-get install libusb-dev` on Linux).

## Configuration

Open `printerFeed.py` and modify the following variables in the **CONFIGURATION** section:

| Variable | Description |
| :--- | :--- |
| `VENDORID` | The ID of your printer (default is set to `0x04b8` for Epson). |
| `PRODUCTID` | (Optional) Specific product ID if you have multiple printers from the same vendor. |
| `SERVER_URL` | The URL to fetch text/data from (currently set to a sample meat-and-filler text generator). |
| `POLL_INTERVAL` | How many seconds to wait between each server check. |

## Usage

Run the script from your terminal:

```bash
python printerFeed.py
```

The console will display a message indicating it has started polling, and every successful fetch will print a receipt containing the received text.