from random import randint

class Helpers:
    @staticmethod
    def validate_data(self, contact):
        return True

    @staticmethod
    def validate_background(self, contact):
        return True

    @staticmethod
    def addi_internal_validation(self):

        """
        Score classification service for future
        :param self:
        :param
        :return: Random number between 0 and 100
        """
        random_number = randint(0, 100)
        return random_number