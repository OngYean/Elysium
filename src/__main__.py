# __main__.py

import sys
import random

#from sensor import Sensor, generate_vital_params
from gui import GUI

def main():
    """ Main program """
    window = GUI(env={
        "FONT_DEFAULT": "Arial",
        "INTERVAL": 5000,
        "NORMAL_CHANCE": 0.95
    })
    window.render_mainwindow()
    window.mainloop()

    return 0

if __name__ == "__main__":
    sys.exit(main())