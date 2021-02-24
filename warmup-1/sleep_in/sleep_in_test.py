# import the code to be tested
from sleep_in import sleep_in

def describe_the_sleep_in_function():
    
    def it_lets_us_know_if_we_can_sleep_in_or_not():
        # should return True because we are on vacation
        is_weekday = True
        is_on_vacation = True
        assert sleep_in(is_weekday, is_on_vacation) == True
        # should return False because it is a weekday and not on vacation
        is_weekday = True
        is_on_vacation = False
        assert sleep_in(is_weekday, is_on_vacation) == False
        # should return True because it is a weekend and we are on vacation
        is_weekday = False
        is_on_vacation = True
        assert sleep_in(is_weekday, is_on_vacation) == True
        # should return True because it is a weekend and not on vacation
        is_weekday = False
        is_on_vacation = False
        assert sleep_in(is_weekday, is_on_vacation) == True