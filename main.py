"""
@file:      main.py
@author:    Matthew Yu (matthewjkyu@gmail.com)
@brief:     Instantiates and begins polling sensing data from the home sensor hub.
@version:   0.0.0
@date:      2024-10-03
@copyright: Copyright (c) 2024.
"""

import sys
import time
from home_sensor_hub import Home_Sensor_Hub


if __name__ == "__main__":
    if sys.version_info[0] < 3:
        raise Exception("This program only supports Python 3.")

    try:
        import pretty_traceback

        pretty_traceback.install()
    except ImportError:
        pass  #

    hub = Home_Sensor_Hub()

    # TODO: look for keyboard interrupt to quit gracefully
    # while True:
    #     time.sleep(1)

    hub.quit()