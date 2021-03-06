import turtle
from Node import Node

class Tank(turtle.Turtle):
    def __init__(self, team="User", start_pos=(0,0), direction=None):
        super().__init__()
        self.team = team
        self.curr_node = self.__generate_list(direction)

        self.shape(self.curr_node.val)
        self.up()
        self.goto(start_pos[0], start_pos[1])

    def move_up(self):
        if self.ycor() <= 220:
            self.sety(self.ycor()+60)

    def move_down(self):
        if self.ycor() >= -220:
            self.sety(self.ycor()-60)

    def move_left(self):
        if self.xcor() > -350:
            self.setx((self.xcor()-60))

    def move_right(self):
        if self.xcor() <= 350:
            self.setx((self.xcor()+60))

    def rotate_right(self):
        self.curr_node = self.curr_node.next
        self.draw(self.curr_node.val)

    def rotate_left(self):
        self.curr_node = self.curr_node.prev
        self.draw(self.curr_node.val)

    def draw(self, asset):
        self.shape(asset)

    def __generate_list(self, direction):
        front_node = Node(f"Assets/{self.team}/tank.gif")
        right_node = Node(f"Assets/{self.team}/tankright.gif")
        left_node = Node(f"Assets/{self.team}/tankleft.gif")
        down_node = Node(f"Assets/{self.team}/tankdown.gif")

        front_node.next = right_node
        front_node.prev = left_node

        right_node.next = down_node
        right_node.prev = front_node

        down_node.next = left_node
        down_node.prev = right_node

        left_node.next = front_node
        left_node.prev = down_node
        
        if not direction or direction == "U":
            return front_node
        elif direction == "R":
            return right_node
        elif direction == "D":
            return down_node
        else:
            return left_node