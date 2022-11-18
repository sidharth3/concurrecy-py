
import numpy as np
import time
from threading import Thread, Lock


class MissionController:

    def __init__(self, robot):
        print("Creating MissionController!")

        thread_poll_position = Thread(target=self._poll_position, daemon=True)
        self.lock = Lock()

        thread_poll_position.start()

        self.robot = robot

        self.current_waypoint_idx = 0
    
    def set_default_waypoint_idx(self):
        self.current_waypoint_idx = 0
        return
    
    def set_trajectory(self, trajectory):
        with self.lock:
            self.current_waypoint_idx = 0

        self.trajectory = trajectory
        
    def _poll_position(self):

        time.sleep(1)

        position = self.robot.get_position()
        
        if self.current_waypoint_idx < len(self.trajectory[:]):
            self._send_navigation_command()
            
        if not (self.current_waypoint_idx == len(self.trajectory[:])):
            if not(np.all(position == self.trajectory[:][self.current_waypoint_idx])):
                with self.lock:
                    self.current_waypoint_idx += 1

        self._poll_position()

    def _send_navigation_command(self):
        self.robot.set_navigation_command(self.trajectory[self.current_waypoint_idx])