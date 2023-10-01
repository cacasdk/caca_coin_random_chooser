import json

class CacaError(IndexError):
    pass
class CoinRandomChooser5:
    def __init__(self, roster_file_path, coin_list):
        self.roster_file_path = roster_file_path
        self.coin_list = coin_list

    @property
    def make_student_number(self):
        output = 0
        for i in range(0, 5):
            if self.coin_list[i] != 0:
                output += 2 ** (i + 1)
        return output

    @property
    def read_roster(self):
        read = open(self.roster_file_path, "r")
        output = json.loads(read.read())
        return output

    def chooser(self):
        try:
            output = self.read_roster[self.make_student_number]
        except IndexError:
            raise CacaError("Opps!The roster doesn't has that student!")
        return output


class CoinRandomChooser6(CoinRandomChooser5):
    @property
    def make_student_number(self):
        output: int = 0
        for i in range(0, 6):
            if self.coin_list[i] == 1:
                output += 2 ** (i + 1)
        return output
