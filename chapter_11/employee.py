
class Employee():
    """Employee类"""

    def __init__(self, first_name, last_name, wage):
        """初始化"""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.wage = wage

    def give_raise(self, amount=5000):
        self.wage += amount