# signalrgb-web-api
Simple web server application for translating web requests into SignalRGB application addresses

This script allows you to launch SignalRGB with specific effects and settings from the web browser using custom URLs.

## Installation

1. Download and install the latest version of Python for Windows from the official website: https://www.python.org/downloads/windows/
2. Or install Python3 from MS Store
2. Install the required Python packages by running the following command in the terminal: `pip install Flask`


## How to Start the Script

1. Clone this repository to your local machine.
2. Open the terminal and navigate to the project directory.
3. Run the following command to start the Flask server: python main.py
This will start the server at `http://localhost:8080`.

## How to Run the Script at Windows Load

1. Create a new shortcut for the `main.py` file.
2. Right-click on the shortcut and select "Properties".
3. In the "Target" field, add the following text at the end of the path: /minimized
This will start the script in a minimized window.
4. Press the "Windows" key + "R" to open the Run dialog box.
5. Type "shell:startup" and press Enter.
6. Copy and paste the shortcut into the Startup folder.
7. Restart your computer.

## How to Use the Script with Example URLs

The script provides the following endpoints:

- `http://localhost:8080/effect/apply/<effect_name>` - Launches SignalRGB with the specified effect (silent launch key is not necessary, it is added by default)
- Example URL: `https://localhost:8080/effect/apply/Rainbow%20Rise?reverse=false&scale=1&speed=50&xPos=298&yPos=200`
- `http://localhost:8080/view/<view_name>` - Launches SignalRGB with the specified view.
- Example URL: `http://localhost:8080/view/devices`

To use these endpoints, simply open your web browser and navigate to the appropriate URL. The SignalRGB software should launch automatically with the specified effect or view.

Note: Make sure that SignalRGB is installed and running on your computer before using this script.
SignalRGB app urls can be found here: `https://docs.signalrgb.com/v2.2.27.0/troubleshooting/application-urls`






