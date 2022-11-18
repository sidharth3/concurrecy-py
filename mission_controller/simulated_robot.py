
import numpy as np

import time

from threading import Thread

import random

class MyThread(Thread):
    
    def __init__(self, *args, **kwargs):
        super(MyThread, self).__init__(*args, **kwargs)
        
        
class SimulatedRobot:

    def __init__(self, initial_position, update_position_callback=None):
        print("Creating SimulatedRobot!")

        self.position = initial_position
        self.update_position_callback = update_position_callback

    def get_position(self):
        return self.position

    def set_navigation_command(self, waypoint):

        def update():

            print(f"Robot is now at {waypoint}")

            self.position = waypoint

            self.update_position_callback(waypoint)
            return

        thread_update = MyThread(target=update)
        thread_update.start()
        thread_update.join()


class SimulatedRobotWithCommunicationDelay:

    def __init__(self, initial_position):

        self._robot = SimulatedRobot(initial_position, self.set_position)

        self.position = initial_position

    def set_position(self, position):
        def update():
            self.position = position
            return

        thread_update = MyThread(target=update)
        thread_update.start()
        thread_update.join()

    def get_position(self):
        return self.position

    def set_navigation_command(self, waypoint):

        # print(f"Commanding robot to move to {waypoint}")

        def update():
            self._robot.set_navigation_command(waypoint)
            return 

        thread_update = MyThread(target=update)
        thread_update.start()
        thread_update.join()