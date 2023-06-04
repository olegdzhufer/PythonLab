class MaxOfAngleChair(Exception):
    """Exception raised when the chair reached is max angle of chair"""
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

