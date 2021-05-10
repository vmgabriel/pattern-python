"""Use of Layer Patter"""


class PresentationLayer:
    """This is the Presentation Layer"""
    def __init__(self):
        self.name = "Presentation Layer"

    def set_lower_layer(self, lowerlayer):
        """setter to lower layer"""
        self.lowerlayer = lowerlayer

    def s3(self, param):
        """Load to s3"""
        print('I to service s3')
        self.lowerlayer.s2(param)
        print('exit to service s3')


class LogicalLayer:
    """This is the Logical Layer"""
    def __init__(self):
        self.name = "Logical Layer"

    def set_lower_layer(self, lowerlayer):
        """setter to lower layer"""
        self.lowerlayer = lowerlayer

    def s2(self, param):
        """Load to s2"""
        print('I to service s2')
        self.lowerlayer.s1(param)
        print('exit to service s2')


class DataLayer:
    """This is the Data Layer"""
    def __init__(self):
        self.name = "Data Layer"

    def set_lower_layer(self, lowerlayer):
        """setter to lower layer"""
        self.lowerlayer = lowerlayer

    def s1(self, param):
        """Load to s1"""
        print('I to service s1')
        print('exit to service s1')


if __name__ == '__main__':
    print('The APP')
    ui = PresentationLayer()
    logic = LogicalLayer()
    data = DataLayer()

    logic.set_lower_layer(data)
    ui.set_lower_layer(logic)

    ui.s3('example of lower layer')
