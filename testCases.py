from theatreClass import Theatre
from getInput import readFile

class Test_TheatreClass:
    def __init__(self):
        self.test_obj = Theatre()
    
    def test_reservation_with_zero_tickets(self):
        output = []
        if self.test_obj.booking([["R001", "0"]]) == []:
            print("First test case passed")
        else:
            print("First test case failed")

    def test_reservation_with_negative_ticket_count(self):
        output = []
        if self.test_obj.booking([["R001", "-1"]]) == output:
            print("Second test case passed")
        else:
            print("Second test case failed")

    def test_reservation_with_count_more_than_max_capacity(self):
        output = []
        if self.test_obj.booking([["R001", "201"]]) == output:
            print("Third test case passed")
        else:
            print("Third test case failed")

    def test_reservation_with_only_one_ticket(self):
        output = ["R001 I1 I2 I3 I4 I5"]
        if self.test_obj.booking([["R001", "5"]]) == output:
            print("Fourth test case passed")
        else:
            print("Fourth test case failed")

    def run_all_tests(self):
        test_obj.test_reservation_with_zero_tickets()
        
        test_obj.test_reservation_with_negative_ticket_count()
        test_obj.test_reservation_with_count_more_than_max_capacity()
        test_obj.test_reservation_with_only_one_ticket()

test_obj = Test_TheatreClass()
test_obj.run_all_tests()

    
