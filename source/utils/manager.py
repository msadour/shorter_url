import string
from random import choice


class Url:

    @staticmethod
    def generate_short_url():
        """Function to generate short_id of specified number of characters"""
        return ''.join(choice(string.ascii_letters + string.digits) for _ in range(10))

    def check_url_exist(self):
        pass

    def create_url(self):
        pass
