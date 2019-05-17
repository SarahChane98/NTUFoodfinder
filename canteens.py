import math


class Canteens(object):

    def __init__(self, name, x, y, rank, dic_food, dic_open, environm, capacity, telenum):
        self.name = name
        self.coordinate_x = x
        self.coordinate_y = y
        self.rank = rank
        self.food_choices = dic_food
        self.range_of_food_choices = len(dic_food)
        self.open_hour = dic_open
        self.environment = environm
        self.capacity = capacity
        self.expected_crowd = 1 / capacity
        self.tele_number = telenum
        self.distance_to_current_location = 0
        self.walking_distance_from_user = False
        self.score = 0

    def print_info(self):

# Input: self
# Functionality: To allow the user to know more information about the canteen he \
#                selected.
# Output: The information of the canteen that user selected will be displayed.

        print_string_1 = "The Canteen is ranked " + str(self.rank)+"."
        print_string_2 = "The Canteen provides following type of food: "
        print_string_3 = ""
        for key in self.food_choices.keys():
            print_string_3 = print_string_3 + key + "  "

        print_string_4 = "The rating for its environment is " + str(self.environment)+"."
        print_string_5 = "Its capacity is  " + str(self.capacity)+"."
        print_string_6 = "Its contact number is " + self.tele_number+"."
        messages = [print_string_1, print_string_2, print_string_3, print_string_4, print_string_5, print_string_6]
        return messages

    def get_distance(self, current_x, current_y):

# Input: self, current_x, current_y
# Functionality: To determine the distance of the user from the canteen selected.
# Output: If the distance from the user to canteen is short enough, user will be \
#         suggested to walk, otherwise, user will be suggested to take a bus.

        self.distance_to_current_location = math.sqrt(
            (self.coordinate_x - current_x) ** 2 + (self.coordinate_y - current_y) ** 2)

        if self.distance_to_current_location < 200:
            self.walking_distance_from_user = True
        else:
            self.walking_distance_from_user = False


canteen_1 = Canteens("Canteen 1", 476, 439, 6,
                     {"Chinese": 2, "Korean": 4, "Japanese": 5, "Western": 6, "Malay": 3.5, "Beverage": 1.5},
                     {"Weekday": [7, 21], "Saturday": [7, 21], "Sunday": [7, 21], "Public": [7, 21]},
                     8, 310, "63343033")

canteen_2 = Canteens("Canteen 2", 525, 358, 1,
                     {"Chinese": 3.5, "Korean": 4.8, "Japanese": 5.3, "Western": 6.5, "Malay": 4.5, "Indian": 4,
                      "Beverage": 1.5},
                     {"Weekday": [7, 21], "Saturday": [7, 21], "Sunday": [7, 21],
                      "Public": [7, 21]},
                     8, 446, "63343033")

canteen_9 = Canteens("Canteen 9", 678, 205, 14,
                     {"Chinese": 4, "Japanese": 4.8, "Western": 5.5, "Beverage": 1.5},
                     {"Weekday": [7, 21], "Saturday": [7, 21], "Sunday": [7, 21],
                      "Public": [7, 21]},
                     6, 293, "96923456")

canteen_11 = Canteens("Canteen 11", 811, 146, 5,
                      {"Chinese": 3.5, "Japanese": 4.8, "Western": 5.5, "Korean": 5, "Indian": 4, "Beverage": 1.5},
                      {"Weekday": [7, 21], "Saturday": [7, 21], "Sunday": [7, 21],
                       "Public": [7, 21]},
                      7, 210, "97866726")

canteen_13 = Canteens("Canteen 13", 481, 63, 13,
                      {"Chinese": 4, "Western": 5, "Korean": 6, "Malay": 4.5, "Beverage": 1.5},
                      {"Weekday": [7, 21], "Saturday": [7, 21], "Sunday": [7, 21],
                       "Public": [7, 21]},
                      7, 210, "98510908")
canteen_14 = Canteens("Canteen 14", 572, 70, 7,
                      {"Chinese": 3, "Western": 7, "Korean": 6.5, "Malay": 3, "Japanese": 5, "Beverage": 1.5},
                      {"Weekday": [7, 21], "Saturday": [7, 21], "Sunday": [7, 21],
                       "Public": [7, 21]},
                      6, 270, "81127239")
canteen_16 = Canteens("Canteen 16", 425, 120, 2,
                      {"Chinese": 2.5, "Western": 3.5, "Korean": 4.5, "Japanese": 5.5, "Beverage": 1.5},
                      {"Weekday": [7, 21], "Saturday": [7, 21], "Sunday": [7, 21],
                       "Public": [7, 21]},
                      9, 304, "94505893")
ananda_kitchen = Canteens("Ananda Kitchen", 840, 222, 10,
                          {"Indian": 7},
                          {"Weekday": [12, 22.5], "Saturday": [12, 22.5], "Sunday": [12, 22.5],
                           "Public": [12, 22.5]},
                          6, 90, "88888888")

foodgle = Canteens("Foodgle Canteen", 737, 88, 8,
                   {"Chinese": 3.5, "Western": 5, "Korean": 6, "Malay": 4, "Japanese": 5.5, "Beverage": 1.5},
                   {"Weekday": [7, 21], "Saturday": [7, 21], "Sunday": [7, 21],
                    "Public": [7, 21]},
                   9, 440, "82963633")
north_hill = Canteens("North Hill Food Court", 846, 254, 4,
                      {"Chinese": 3, "Western": 6, "Vegetarian": 4, "Beverage": 1.5},
                      {"Weekday": [7, 21], "Saturday": [7, 21], "Sunday": [7, 21],
                       "Public": [7, 21]},
                      7, 440, "85080232")

pioneer = Canteens("Pioneer Food Court", 552, 554, 3,
                   {"Chinese": 4, "Korean": 5, "Beverage": 1.5},
                   {"Weekday": [7, 21], "Saturday": [7, 21], "Sunday": [7, 21],
                    "Public": [7, 21]},
                   6, 408, "99999999")

quad_cafe = Canteens("Quad Cafe", 154, 271, 9,
                     {"Chinese": 5, "Western": 6.5, "Japanese": 4, "Beverage": 1.5},
                     {"Weekday": [7, 21], "Saturday": [7, 15], "Sunday": [25, 25],
                      "Public": [25, 25]},
                     10, 500, "83333333")

koufu = Canteens("Koufu", 177, 470, 12,
                 {"Chinese": 3, "Western": 4, "Korean": 5, "Malay": 4.5, "Japanese": 2.5, "Indian": 3,
                  "Vegetarian": 2, "Beverage": 1.5},
                 {"Weekday": [7, 21], "Saturday": [7, 15], "Sunday": [25, 25],
                  "Public": [7, 15]},
                 6, 1050, "67900355")

north_spine_food_court = Canteens("North Spine Food Court", 246, 211, 11,
                                  {"Chinese": 4, "Western": 5, "Korean": 4, "Malay": 5, "Japanese": 3, "Indian": 5,
                                   "Vegetarian": 4, "Beverage": 1.5},
                                  {"Weekday": [7, 21], "Saturday": [7, 15], "Sunday": [25, 25], "Public": [25, 25]},
                                  7, 1838, "65555555")

bakery_cuisine = Canteens("Bakery Cuisine", 288, 223, 15,
                          {"Snack": 2},
                          {"Weekday": [7, 21], "Saturday": [9, 19], "Sunday": [9, 19], "Public": [9, 19]},
                          8, 100, "65534555")

each_a_cup = Canteens("Each A Cup", 288, 223, 16,
                      {"Beverage": 3.5},
                      {"Weekday": [9, 21], "Saturday": [9, 18], "Sunday": [9, 18], "Public": [25, 25]},
                      6, 20, "91829307")

grande_cibo = Canteens("Grande Cibo", 246, 211, 17,
                       {"Western": 5, "Beverage": 1.5},
                       {"Weekday": [11, 20], "Saturday": [11, 20], "Sunday": [11, 20], "Public": [25, 25]},
                       7, 48, "91459307")

kfc = Canteens("KFC", 270, 188, 18,
               {"Fast Food": 3, "Beverage": 1.5},
               {"Weekday": [7.5, 22], "Saturday": [11, 20], "Sunday": [11, 20], "Public": [25, 25]},
               9, 1161, "91459307")

long_john_silvers = Canteens("Long John Silver's", 270, 188, 19,
                             {"Fast Food": 5, "Beverage": 1.5},
                             {"Weekday": [7.5, 22], "Saturday": [7.5, 22], "Sunday": [7.5, 22], "Public": [25, 25]},
                             5, 999, "63140181")

mcdonalds = Canteens("McDonald's", 270, 188, 20,
                     {"Fast Food": 4, "Beverage": 1.5},
                     {"Weekday": [7, 23.99], "Saturday": [7, 23.99], "Sunday": [10, 22], "Public": [10, 22]},
                     5, 999, "63142341")

mr_bean = Canteens("Mr Bean", 288, 223, 21,
                   {"Snack": 1.9, "Beverage": 2.5},
                   {"Weekday": [7.5, 20.5], "Saturday": [7.5, 17], "Sunday": [25, 25], "Public": [25, 25]},
                   6, 20, "63166341")

paiks_bibim = Canteens("Paik's Bibim", 288, 223, 22,
                       {"Korean": 6},
                       {"Weekday": [10, 21], "Saturday": [10, 15], "Sunday": [25, 25], "Public": [25, 25]},
                       9, 40, "62620567")

peach_garden = Canteens("Peach Garden", 270, 188, 23,
                        {"Chinese": 7},
                        {"Weekday": [11, 22], "Saturday": [11, 22], "Sunday": [11, 22], "Public": [11, 22]},
                        10, 180, "62199398")

pen_inc = Canteens("PEN & INC", 270, 188, 24,
                   {"Western": 6, "Beverage": 1.5},
                   {"Weekday": [11, 23], "Saturday": [11, 17], "Sunday": [25, 25], "Public": [25, 25]},
                   10, 144, "63140158")

pizza_hut = Canteens("Pizza Hut", 270, 188, 25,
                     {"Fast Food": 4.5},
                     {"Weekday": [11, 22], "Saturday": [11, 21], "Sunday": [11, 20], "Public": [11, 20]},
                     8, 1161, "67626124")

starbucks_coffee = Canteens("Starbucks Coffee", 270, 188, 26,
                            {"Beverage": 4},
                            {"Weekday": [7, 22], "Saturday": [7, 17], "Sunday": [7, 17], "Public": [25, 25]},
                            7, 1033, "69101245")

subway = Canteens("Subway", 270, 188, 27,
                  {"Fast Food": 5.9, "Beverage": 1.5},
                  {"Weekday": [8, 21], "Saturday": [11, 18], "Sunday": [11, 18], "Public": [25, 25]},
                  6, 999, "64625238")

the_house = Canteens("The House", 288, 223, 28,
                     {"Chinese": 7},
                     {"Weekday": [9, 21], "Saturday": [9, 18], "Sunday": [25, 25], "Public": [10, 16]},
                     8, 34, "88213302")

sandwich = Canteens("Sandwich Guys", 288, 223, 29,
                    {"Snack": 4},
                    {"Weekday": [10, 20], "Saturday": [10, 15], "Sunday": [25, 25], "Public": [25, 25]},
                    6, 20, "90991412")

soup_spoon_union = Canteens("The Soup Spoon Union", 288, 223, 30,
                            {"Chinese": 5},
                            {"Weekday": [11, 21], "Saturday": [11, 15], "Sunday": [25, 25], "Public": [25, 25]},
                            9, 104, "62687566")

# a list of canteens objects
canteen_list = [canteen_1, canteen_2, canteen_9, canteen_11, canteen_13, canteen_14, canteen_16,
                foodgle, quad_cafe, north_hill, north_spine_food_court, ananda_kitchen, pioneer, koufu, bakery_cuisine,
                each_a_cup, grande_cibo, kfc, long_john_silvers, mcdonalds, mr_bean, paiks_bibim, peach_garden,
                pen_inc, pizza_hut, starbucks_coffee, subway, the_house, sandwich, soup_spoon_union]
