
import time
import numpy as np

from mission_controller.mission_controller import MissionController
from mission_controller.simulated_robot import SimulatedRobot, SimulatedRobotWithCommunicationDelay


def test_normal_operation():

    simulated_robot = SimulatedRobotWithCommunicationDelay(np.array([0.0, 0.0]))
    controller = MissionController(simulated_robot)

    controller.set_trajectory(np.array([[2.0, 1.0], [1.0, 0.0]]))
    time.sleep(3)

    print(f'Final Robot Position is: {simulated_robot.get_position()}')
    print("Test 1 complete")

    # exit(0)

def test_change_trajectory():

    simulated_robot = SimulatedRobotWithCommunicationDelay(np.array([0.0, 0.0]))
    controller = MissionController(simulated_robot)

    controller.set_trajectory(np.array([[0.0, 0.0], [1.0, 0.0]]))
    time.sleep(2)

    controller.set_trajectory(np.array([[2.0, 0.0], [3.0, 0.0], [6.0,9.0]]))
    time.sleep(4)
    
    controller.set_trajectory(np.array([[2.0, 1.0], [5.0, 9.0], [7.0,4.5], [9.0,7.0]]))
    time.sleep(5)

    print(f'Final Robot Position is: {simulated_robot.get_position()}')
    print("Test 2 complete")

def test_stop_operation():
    simulated_robot = SimulatedRobotWithCommunicationDelay(np.array([0.0, 0.0]))
    controller = MissionController(simulated_robot)

    controller.set_trajectory(np.array([[2.0, 0.0], [1.0, 0.0]]))
    time.sleep(2)

    #enter stop command before previous trajectory is finished
    controller.set_trajectory(np.array([]))
    print(f'Final Robot Position is: {simulated_robot.get_position()}')
    print("Test 3 complete")

def test_incorrect_input():
    simulated_robot = SimulatedRobotWithCommunicationDelay(np.array([0.0, 0.0]))
    controller = MissionController(simulated_robot)

    controller.set_trajectory(np.array([[2.0, 0.0], [1.0, 0.0]]))
    time.sleep(2)

    #enter incorrect trajectory before previous trajectory is finished
    controller.set_trajectory(['test_string'])
    print(f'Final Robot Position is: {simulated_robot.get_position()}')
    print("Test 4 complete")
    exit(0)


if __name__ == "__main__":
    #execute one at a time, otherwise daemon prints will interfere with each other

    test_normal_operation()
    # test_change_trajectory()
    # test_stop_operation()
    # test_incorrect_input()
