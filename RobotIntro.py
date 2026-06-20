# Robot Instruction using OOP

# Create a Robot class
class Robot:

    # Constructor
    def __init__(self, name):
        self.name = name
        print(self.name, "is ready!")

    # Methods (robot actions)
    def move_forward(self):
        print(self.name, "moves forward.")

    def turn_left(self):
        print(self.name, "turns left.")

    def turn_right(self):
        print(self.name, "turns right.")

    def stop(self):
        print(self.name, "stops.")


# Create an object
robot1 = Robot("Robo")

# Give instructions to the robot
robot1.move_forward()
robot1.turn_left()
robot1.move_forward()
robot1.turn_right()
robot1.stop()