from datetime import datetime
from canteens import canteen_list
import math

list_public_holiday = ["01-01", "05-02", "06-02", "19-04", "01-05", "19-05", "05-06", "09-08", "11-08", "27-10",
                       "25-12"]
red_line = {"LWN Library": [311, 181], "SBS": [115, 246], "WKWSCI": [35, 363], "Hall 7": [54, 526],
            "Innovation Center": [218, 518], "Hall 4": [370, 559], "Hall 1": [509, 548],
            "Food Court 2": [541, 353], "Hall 8&9": [648, 256], "Hall 11": [815, 190],
            "Grad Hall 1&2": [846, 109], "Crescent Hall": [740, 71], "Hall 12&13": [466, 45]}


class User(object):
    approx_arrival_time = 0
    current_location_x = 0
    current_location_y = 0
    budget_available = 0
    food_preference = False
    food_preferred = ""
    selected_criteria = []
    day_of_week = ""
    public_holiday = False
    available_canteens = []  # created after going through time budget and food type filters
    top_canteens_list = []  # created after sorting is done
    final_canteen_choice = canteen_list[0]
    nearest_bus_stop = ["nameofbusstop",[0, 0]]

    def update_time_date(self):

# Input: self
# Functionality: To get the current date and time.
# Output: None

        # get the current date and time
        hour = datetime.now().strftime("%H")
        minute = datetime.now().strftime("%M")
        date = datetime.now().strftime("%d-%m")

        # translate into integer
        if hour[0] == "0":
            hour = int(hour[1])
        else:
            hour = int(hour)
        if minute[0] == "0":
            minute = int(minute[1])
        else:
            minute = int(minute)

        # calculate the approximate arrival time
        current_time = hour + (minute / 60)
        self.approx_arrival_time = current_time + 0.5

        # get which day of the week is today
        if 0 <= datetime.today().weekday() <= 4:
            self.day_of_week = "Weekday"
        elif datetime.today().weekday() == 5:
            self.day_of_week = "Saturday"
        elif datetime.today().weekday() == 6:
            self.day_of_week = "Sunday"

        # check whether today is public holiday

        if date in list_public_holiday:
            self.public_holiday = True

    def get_nearest_bus_stop(self):

# Input: self
# Functionality: To determine the nearest bus stop from the user location.
# Output: None

        stops_distance = {}
        for key, value in red_line.items():
            stops_distance[key] = math.sqrt(
                (value[0] - self.current_location_x) ** 2 + (value[1] - self.current_location_y) ** 2)

        nearest_bus_stop_name = min(zip(stops_distance.values(), stops_distance.keys()))[1]
        self.nearest_bus_stop = [nearest_bus_stop_name, red_line[nearest_bus_stop_name]]
