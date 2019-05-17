from canteens import canteen_list
from user import User
from operator import attrgetter
import pygame


pygame.init()

# Colours that will be used
white = (255, 255, 255)
red = (220, 20, 60)
black = (0, 0, 0)
light_blue = (135, 206, 250)
blue = (100, 149, 237)

# Size of the display window
display_width = 849
display_height = 670

# Create a display surface
appDisplay = pygame.display.set_mode((display_width, display_height))

# Set the window title
pygame.display.set_caption("NTU Food Finder")

# Set the pygame clock
fps = 25  # frame per second
clock = pygame.time.Clock()

# Fonts that will be used
smallfont = pygame.font.SysFont("arial", 20)
mediumfont = pygame.font.SysFont("arial", 40)
largefont = pygame.font.SysFont("arial", 60)


def text_object(msg, colour, size):
    
# Input: msg, colour, size
# Functionality: To render the font in different font sizes
# Output: text_surface, text_surface.get_rect()

    if size == "small":
        text_surface = smallfont.render(msg, True, colour)
    elif size == "medium":
        text_surface = mediumfont.render(msg, True, colour)
    elif size == "large":
        text_surface = largefont.render(msg, True, colour)

    return text_surface, text_surface.get_rect()



def button(msg, buttonx, buttony, button_width, button_height):

# Input: msg, buttonx, buttony, button_width, button_height
# Functionality: To display buttons and when cursor is over the button, button change colour.
# Output: return True when button clicked.

    cursor = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if buttonx <= cursor[0] <= (buttonx + button_width) and buttony <= cursor[1] <= (buttony + button_height):
        pygame.draw.rect(appDisplay, light_blue, (buttonx, buttony, button_width, button_height))
        text_surf, text_rect = text_object(msg, white, size="small")
        text_rect.center = (buttonx + button_width / 2), (buttony + button_height / 2)
        appDisplay.blit(text_surf, text_rect)
        # pygame.display.update()
        if click[0] == 1:
            return True
        else:
            return False
    else:
        pygame.draw.rect(appDisplay, blue, (buttonx, buttony, button_width, button_height))
        text_surf, text_rect = text_object(msg, white, size="small")
        text_rect.center = (buttonx + button_width / 2), (buttony + button_height / 2)
        appDisplay.blit(text_surf, text_rect)



def message_to_screen(msg, colour, y_displace=0, size="small"):

# Input: msg, colour, y_displace=0, size="small"
# Functionality: To display message that is centered on the screen.
# Output: The message that will be displayed.

    text_surf, text_rect = text_object(msg, colour, size)
    text_rect.center = display_width / 2, (display_height / 2) + y_displace  # center of text rect
    appDisplay.blit(text_surf, text_rect)



def close_when_quit():

# Input: None
# Functionality: To allow the user to quit the application after clicking the cross \
#                at top right corner.
# Output: The application closes after user click the cross at top right corner.

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()


def app_start_menu():

# Input: None
# Functionality: To allow the user click on the start button to proceed to the map or \
#                quit the application after clicking on the quit button.
# Output: The map will be displayed if user click start or the application will be closed \
#         if the user click on the quit button.

    while True:
        appDisplay.fill(white)
        message_to_screen("Welcome!", black, -100, "large")
        message_to_screen("Please select your budget and food preference,", black, 0, "small")
        message_to_screen("followed by a set of criteria.", black, 30, "small")
        message_to_screen("We will find the most suitable canteen for you!:)", black, 60, "small")

        if button("Start", 350, 450, 150, 50):
            map_page()
        if button("Quit", 350, 510, 150, 50):
            pygame.quit()
            quit()

        pygame.display.update()
        clock.tick(15)

        close_when_quit()



def map_page():

# Input: None
# Functionality: To allow the user to mark his location with a blue dot by clicking on the map.
# Output: After user mark his location and click the continue button, it will proceed \
#         to the page to ask for user budget.

    while True:
        appDisplay.fill(white)
        ntu_map = pygame.image.load("ntu_map.jpg")
        appDisplay.blit(ntu_map, (0, 0))
        message_to_screen("Please click on the map to mark your location!", black, 300)
        pygame.display.update()
        display_continue_button = False

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                if 0 <= mouse[0] <= 850 and 0 <= mouse[1] <= 600:
                    user.current_location_x = mouse[0]
                    user.current_location_y = mouse[1]
                    user.update_time_date()
                    display_continue_button = True

        while display_continue_button:
            appDisplay.fill(white)
            appDisplay.blit(ntu_map, (0, 0))
            pygame.draw.circle(appDisplay, light_blue, (user.current_location_x, user.current_location_y), 8)

            if button("Continue", 350, 610, 150, 50):
                get_budget_page()
            pygame.display.update()
            clock.tick(15)
            close_when_quit()



def get_budget_page():

# Input: None
# Functionality: To allow the user to input his budget for food.
# Output: After the user indicated his budget, it will proceed to the next page on selecting \
#         his food preferences.

    display_continue_button = False
    while True:
        appDisplay.fill(white)
        message_to_screen("Please select your budget", black, -300, "medium")

        if button("Less than $1", 350, 100, 150, 50):
            user.budget_available = 0.9
            display_continue_button = True
        if button("$1 - $1.9", 350, 160, 150, 50):
            user.budget_available = 1.9
            display_continue_button = True
        if button("$2 - $2.9", 350, 220, 150, 50):
            user.budget_available = 2.9
            display_continue_button = True
        if button("$3 - $3.9", 350, 280, 150, 50):
            user.budget_available = 3.9
            display_continue_button = True
        if button("$4 - $4.9", 350, 340, 150, 50):
            user.budget_available = 4.9
            display_continue_button = True
        if button("$5 - $5.9", 350, 400, 150, 50):
            user.budget_available = 5.9
            display_continue_button = True
        if button("$6 - $6.9", 350, 460, 150, 50):
            user.budget_available = 6.9
            display_continue_button = True
        if button("More than $7", 350, 520, 150, 50):
            user.budget_available = 7.1
            display_continue_button = True
        pygame.display.update()
        clock.tick(15)
        close_when_quit()

        while display_continue_button:
            appDisplay.fill(white)
            message_to_screen("Budget Noted!", black, 0, "medium")
            if button("Continue", 350, 520, 150, 50):
                food_preference_page_intro()
            pygame.display.update()
            clock.tick(15)
            close_when_quit()



def food_preference_page_intro():

# Input: None
# Functionality: To allow the user to choose if he has any food preference.
# Output: If the user click on the Yes button, it will proceed to the food preference choice page \
#         else it will move on to ask user if he wants a single criterion or multiple criteria sort.

    while True:
        appDisplay.fill(white)
        message_to_screen("Do you have any food preferences?", black, -100, "medium")
        pygame.display.update()

        if button("Yes", 200, 500, 150, 50):
            user.food_preference = True
            food_preference_page_choice()

        if button("No", 500, 500, 150, 50):
            user.food_preference = False
            check_available_canteens()

        pygame.display.update()
        close_when_quit()
        clock.tick(15)



def food_preference_page_choice():

# Input: None
# Functionality: To allow the user to select the food type that he prefers to eat.
# Output: After the user click on the food type he prefers, it will proceed to ask for \
#         whether user wants a single criterion or multiple criteria sort.

    display_continue_button = False
    while True:
        appDisplay.fill(white)
        message_to_screen("Which food do you prefer?", black, -300, "medium")
        food = ["Chinese", "Malay", "Japanese", "Korean", "Western", "Indian", "Vegetarian", "Snack", "Beverage",
                "Fast Food"]
        for i, item in enumerate(food):
            if button(item, 350, (100 + 50 * i), 150, 40):
                user.food_preferred = item
                display_continue_button = True

        pygame.display.update()
        clock.tick(15)
        close_when_quit()

        while display_continue_button:
            appDisplay.fill(white)
            message_to_screen("Preference Noted!", black, 0, "medium")
            if button("Continue", 350, 520, 150, 50):
                check_available_canteens()
            pygame.display.update()
            clock.tick(15)
            close_when_quit()




def time_filter(list_canteen):
      
# Input: list_canteen
# Functionality: Filter the list of canteens according to the user approximate time \
#                and the opening hours of the canteens on weekdays and public holidays.
# Output: Returns a list of canteens that will be open when the user reaches the canteen.

    new_canteen_list = []

    for i in range(len(list_canteen)):
        if user.public_holiday:
            if list_canteen[i].open_hour["Public"][0] < user.approx_arrival_time <\
                    list_canteen[i].open_hour["Public"][1]:
                new_canteen_list.append(list_canteen[i])
        else:
            if list_canteen[i].open_hour[user.day_of_week][0] < user.approx_arrival_time < \
                    list_canteen[i].open_hour[user.day_of_week][1]:
                new_canteen_list.append(list_canteen[i])

    return new_canteen_list



def food_type_filter(list_canteen):

# Input: list_canteen
# Functionality: Filter the list of canteens according to the user food preference.
# Output: Returns a list of canteens that sell the type of food that the user wants to eat.

    if user.food_preference:
        filtered_list = []
        for objects in list_canteen:
            if user.food_preferred in objects.food_choices:
                filtered_list.append(objects)
        return filtered_list
    else:
        return list_canteen




def budget_filter(list_canteen):

# Input: list_canteen
# Functionality: Filter the list of canteens according to the budget of the user.
# Output: Returns a list of canteens that sell the food that the user will be able to afford \
#         regardless of whether the user user has any food preference.

    filtered_list = []
    if user.food_preference:
        for objects in list_canteen:
            if user.budget_available >= objects.food_choices[user.food_preferred]:
                filtered_list.append(objects)

    else:
        for objects in list_canteen:
            value = min(zip(objects.food_choices.values(), objects.food_choices.keys()))[0]
            if user.budget_available >= value:
                filtered_list.append(objects)
    return filtered_list



def check_available_canteens():

# Input: None
# Functionality: Obtain the list of available canteens that is in accordance with the user's \
#                budget, food preference and approximate arrival time. 
# Output: Returns a list of canteens that meets the user's budget, food preference and \
#         approximate arrival time. If there are no available canteens, user will be \
#         informed. 

    available_canteens = time_filter(canteen_list)
    available_canteens = food_type_filter(available_canteens)
    available_canteens = budget_filter(available_canteens)

    if len(available_canteens) == 0:
        while True:
            appDisplay.fill(white)
            message_to_screen("Sorry!", red, -210, size="large")
            message_to_screen("According to your current time,", black, -100,
                              size="medium")
            message_to_screen(" budget and food preference", black, -50,
                              size="medium")
            message_to_screen("there are no matching canteens.", black, 0, size="medium")
            if button("End Menu", 350, 420, 150, 50):
                app_end_menu()
            pygame.display.update()
            clock.tick(15)
            close_when_quit()

    else:
        user.available_canteens = available_canteens
        user.selected_criteria = []
        criteria_page_intro()


def criteria_page_intro():

# Input: None
# Functionality: To ask if user prefers a single criterion sort or multiple criteria sort.
# Output: Will move on to the criteria selection page after user made his decision. 

    user.selected_criteria = []
    while True:
        appDisplay.fill(white)
        message_to_screen("Do you want to sort canteens", black, -200, "medium")
        message_to_screen("using a single criterion or multiple criteria?", black, -160, "medium")

        if button("Single Criterion", 175, 300, 150, 50):
            criteria_page_single()

        if button("Multiple Criteria", 524, 300, 150, 50):
            criteria_page_multiple_1()
        pygame.display.update()
        clock.tick(15)
        close_when_quit()




def page_num_call(page_num):

# Input: page_num
# Functionality: To invoke the respective page function using the page number.
# Output: Returns respective page function.

    if page_num == 1:
        return criteria_page_multiple_1()
    elif page_num == 2:
        return criteria_page_multiple_2()
    elif page_num == 3:
        return criteria_page_multiple_3()
    elif page_num == 4:
        return criteria_page_multiple_4()
    elif page_num == 5:
        return criteria_page_multiple_5()



def repetition_alert():

# Input: None
# Functionality: To prevent user from choosing the same criterion again after user \
#                selected multiple criteria sort.
# Output: After prompting user that he has selected the same criterion twice, \
#         user given the option to try again or exit the application.

    while True:
        appDisplay.fill(white)
        message_to_screen("You have already chosen this. Do you want to try again?", black, 100, size="medium")
        if button("Yes", 200, 550, 150, 50):
            criteria_page_intro()
        if button("No", 500, 550, 150, 50):
            pygame.quit()
            quit()
        pygame.display.update()
        clock.tick(15)
        close_when_quit()



def criteria_buttons(x, y, page_num):

# Input: x, y, page_num
# Functionality: To display the buttons for the criteria to allow the user to click on.
# Output: After the user clicks on the criteria buttons, it will display the results of the sorting.

    if user.food_preference:
        criteria = ["Distance", "Environment", "Rank", "Expected Crowd"]
    else:
        criteria = ["Distance", "Environment", "Rank", "No. of Food Choices", "Expected Crowd"]
    for i, item in enumerate(criteria):
        if button(criteria[i], x, (y + 60 * i), 160, 50):

            if criteria[i] not in user.selected_criteria:
                user.selected_criteria.append(criteria[i])

                if page_num == 0 or (user.food_preference and page_num == 4) or page_num == 5:
                    sorting_result_page()
                else:
                    page_num_call(page_num + 1)
            else:
                repetition_alert()



def no_more_criteria_needed(x, y):

# Input: x, y
# Functionality: To allow the user to get the sorting results if he does not \
#                want to include anymore criteria.
# Output: Returns the sorting result page.

    if button("No more criteria", x, y, 160, 50):
        sorting_result_page()
    pygame.display.update()
    clock.tick(15)



def criteria_page_single():

# Input: None
# Functionality: To allow the user to choose a single criterion after he selects \
#                single criterion sort and move on to the sorting result page.
# Output: None

    while True:
        appDisplay.fill(white)
        message_to_screen("Please choose one of the criteria below.", black, -200, "medium")
        criteria_buttons(325, 200, 0)
        pygame.display.update()
        clock.tick(15)
        close_when_quit()



def criteria_page_multiple_1():

# Input: None
# Functionality: To allow the user to select up to 5 criteria after he selects \
#                multiple criteria sort and move on to the sorting result page.
# Output: None

    while True:
        appDisplay.fill(white)
        message_to_screen("Please select 2 ~5 criteria", black, -300, "medium")
        message_to_screen("in descending order of importance.", black, -250, "medium")
        message_to_screen("Please select the most important criteria ", black, -200, "medium")

        criteria_buttons(8.3, 200, 1)
        pygame.display.update()
        clock.tick(15)
        close_when_quit()



def criteria_page_multiple_2():

# Input: None
# Functionality: To allow the user to select up to 5 criteria after he selects \
#                multiple criteria sort and move on to the sorting result page.
# Output: None

    while True:
        appDisplay.fill(white)
        message_to_screen("Please select the second most important criteria ", black, -200, "medium")
        criteria_buttons(176.6, 200, 2)
        pygame.display.update()
        clock.tick(15)
        close_when_quit()



def criteria_page_multiple_3():

# Input: None
# Functionality: To allow the user to select up to 5 criteria after he selects \
#                multiple criteria sort and move on to the sorting result page.
# Output: None

    while True:
        appDisplay.fill(white)
        message_to_screen("Please select the third most important criteria ", black, -200, "medium")
        criteria_buttons(344.9, 200, 3)
        if user.food_preference:
            no_more_criteria_needed(344.9, 440)  # the button "no. of food choices" is omitted
        else:
            no_more_criteria_needed(344.9, 500)

        pygame.display.update()
        clock.tick(15)
        close_when_quit()



def criteria_page_multiple_4():

# Input: None
# Functionality: To allow the user to select up to 5 criteria after he selects \
#                multiple criteria sort and move on to the sorting result page.
# Output: None

    while True:
        appDisplay.fill(white)
        message_to_screen("Please select the fourth most important criteria ", black, -200, "medium")
        criteria_buttons(513.2, 200, 4)
        if user.food_preference:
            no_more_criteria_needed(513.2, 440)  # the button "no. of food choices" is omitted
        else:
            no_more_criteria_needed(513.2, 500)
        pygame.display.update()
        clock.tick(15)
        close_when_quit()



def criteria_page_multiple_5():

# Input: None
# Functionality: To allow the user to select up to 5 criteria after he selects \
#                multiple criteria sort and move on to the sorting result page.
# Output: None

    while True:
        appDisplay.fill(white)
        message_to_screen("Please select the least important criteria ", black, -200, "medium")
        criteria_buttons(681.5, 200, 5)
        if user.food_preference:
            no_more_criteria_needed(681.5, 440)  # the button "no. of food choices" is omitted
        else:
            no_more_criteria_needed(681.5, 500)
        pygame.display.update()
        clock.tick(15)
        close_when_quit()



def sort_expected_crowd(list_canteen):

# Input: list_canteen
# Functionality: To perform a single sort on the expected crowd of the canteens in the list.
# Output: Returns a list of canteens that are sorted from the least crowded to the most crowded.

    return sorted(list_canteen, key=attrgetter('expected_crowd'))



def bubblesortrank(list_canteen):

# Input: list_canteen
# Functionality: To perform a single sort on the rank of the canteens in the list.
# Output: None

    for passnum in range(len(list_canteen) - 1):
        swapped = False
        for i in range(len(list_canteen) - 1):
            if list_canteen[i].rank > list_canteen[i + 1].rank:
                temp = list_canteen[i]
                list_canteen[i] = list_canteen[i + 1]
                list_canteen[i + 1] = temp
                swapped = True
        if not swapped:
            break



def sort_by_rank(list_canteen):

# Input: list_canteen
# Functionality: To perform a single sort on the rank of the canteens in the list by invoking
#                bubblesortrank(list_canteen).
# Output: Returns a list of canteens that are sorted from the highest rank to the lowest rank.

    new_canteen_list = []
    bubblesortrank(list_canteen)
    for i in range(len(list_canteen)):
        new_canteen_list.append(list_canteen[i])
    return new_canteen_list



def sort_range(list_canteen):

# Input: list_canteen
# Functionality: To perform a single sort on the number of food choices sold by \
#                the canteens in the list.
# Output: Returns a list of canteens that are sorted by the canteen that sells the \
#         largest number of food choices to the canteen that sells the least number \
#         of food choices.

    return sorted(list_canteen, key=attrgetter('range_of_food_choices'), reverse=True)



def sort_distance(list_canteen):

# Input: list_canteen
# Functionality: To perform a single sort on the distance of the user to the canteens in the list.
# Output: Returns a list of canteens that are sorted from the nearest to the furthest from user.

    return sorted(list_canteen, key=attrgetter('distance_to_current_location'))



def sort_environ(list_canteen):

# Input: list_canteen
# Functionality: To perform a single sort on the eating environment of canteens in the list.
# Output: Returns a list of canteens that are sorted according from the best eating environment \
#         to the least favourable eating environment.

    return sorted(list_canteen, key=attrgetter('environment'), reverse=True)



def bubblesortmultiple(list_canteen):

# Input: list_canteen
# Functionality: To arrange the elements in the list in ascending order
# Output: None

    for passnum in range(len(list_canteen) - 1):
        swapped = False
        for i in range(len(list_canteen) - 1):
            if list_canteen[i].score < list_canteen[i + 1].score:
                temp = list_canteen[i]
                list_canteen[i] = list_canteen[i + 1]
                list_canteen[i + 1] = temp
                swapped = True
        if not swapped:
            break



def sort_using_multiple_criteria(criteria_list, list_canteen):

# Input: criteria_list, list_canteen
# Functionality: To perform a multiple sort on distance, rank, environment, \
#                range, expected_crowd and assign different weightages based on
#                the order of criteria chosen.
# Output: Returns a list of canteens that are sorted according to the scores
# Give a score based on criterias:
# to generate weightage list, The nth criteria has 2 times weightage of the n+1 th criteria

    no_of_weightage_elements = 0
    counter = 0
    while counter < len(criteria_list):
        no_of_weightage_elements += 2 ** counter
        counter += 1
    weightage_element = 1 / no_of_weightage_elements
    weightage = []

    for i in range(len(criteria_list)):
        weightage.append(weightage_element * (2 ** (len(criteria_list) - i - 1)))

    maximum = len(canteen_list)

    for a in range(len(list_canteen)):
        list_canteen[a].score = 0

        for b in range(len(weightage)):
            if criteria_list[b] == "Rank":
                list_canteen[a].score += weightage[b] * ((maximum - list_canteen[a].rank + 1) / maximum * 100)

            elif criteria_list[b] == "Environment":
                list_canteen[a].score += weightage[b] * (list_canteen[a].environment * 10)

            elif criteria_list[b] == "Distance":

                list_canteen[a].score += weightage[b] * (
                        (maximum - (sort_distance(list_canteen).index(list_canteen[a]))) / maximum * 100)

            elif criteria_list[b] == "No. of Food Choices":

                list_canteen[a].score += weightage[b] * (list_canteen[a].range_of_food_choices / 8 * 100)

            elif criteria_list[b] == "Expected Crowd":

                list_canteen[a].score += weightage[b] * (
                        (maximum - (sort_expected_crowd(list_canteen).index(list_canteen[a]))) / maximum * 100)

    bubblesortmultiple(list_canteen)
    return list_canteen



def sorting_result_page():

# Input: None
# Functionality: To allow the user to select the canteen he wants out of the top 3 canteens \
#                based on the sorting result.
# Output: The screen will display the top 3 canteens based on the sorting result.

    for item in canteen_list:
        item.get_distance(user.current_location_x, user.current_location_y)

    if len(user.selected_criteria) == 1:  # if user only has one criteria:
        if user.selected_criteria[0] == "Distance":
            user.top_canteens_list = sort_distance(user.available_canteens)

        elif user.selected_criteria[0] == "Rank":
            user.top_canteens_list = sort_by_rank(user.available_canteens)

        elif user.selected_criteria[0] == "No. of Food Choices":

            user.top_canteens_list = sort_range(user.available_canteens)

        elif user.selected_criteria[0] == "Environment":
            user.top_canteens_list = sort_environ(user.available_canteens)

        elif user.selected_criteria[0] == "Expected Crowd":
            user.top_canteens_list = sort_expected_crowd(user.available_canteens)

    else:
        user.top_canteens_list = sort_using_multiple_criteria(user.selected_criteria, user.available_canteens)

    while True:
        appDisplay.fill(white)
        message_to_screen("The sorting result is out!", black, -100, size="large")
        message_to_screen("                                                  Based on your budget,food preference",
                          black, -20,
                          size="small")
        message_to_screen("                                                  and estimated arrival time,", black, 0,
                          size="small")
        message_to_screen("                                                  some canteens are filtered out.", black,
                          20,
                          size="small")
        message_to_screen("                                                  The remaining canteens are sorted.", black,
                          60,
                          size="small")
        message_to_screen("                                                  Names of top canteens are given.", black,
                          80,
                          size="small")
        message_to_screen(
            "                                                 Please choose the canteen you want to visit!", black,
            100, size="small")

        if button("1st:" + user.top_canteens_list[0].name, 100, 300, 220, 50):
            user.final_canteen_choice = user.top_canteens_list[0]
            show_canteen_info_page()
        if len(user.top_canteens_list) > 1:
            if button("2nd:" + user.top_canteens_list[1].name, 100, 360, 220, 50):
                user.final_canteen_choice = user.top_canteens_list[1]
                show_canteen_info_page()
        if len(user.top_canteens_list) > 2:
            if button("3rd:" + user.top_canteens_list[2].name, 100, 420, 220, 50):
                user.final_canteen_choice = user.top_canteens_list[2]
                show_canteen_info_page()

        pygame.display.update()
        clock.tick(15)
        close_when_quit()



def show_canteen_info_page():

# Input: None
# Functionality: To give the users more information about the canteen he has selected and \
#                whether he requires the mode of transport to reach his destination.
# Output: Selected Canteen information displayed, together with Show Transport and End Memu button.

    while True:
        appDisplay.fill(white)
        message_to_screen("Selected Canteen: " + user.final_canteen_choice.name, black, -200, size="medium")

        for i in range(5):
            message_to_screen(user.final_canteen_choice.print_info()[i], red, (-100 + 30 * i))

        if button("Show Transport", 350, 400, 150, 50):
            showtransport()
        if button("End Menu", 350, 460, 150, 50):
            app_end_menu()

        pygame.display.update()
        clock.tick(15)
        close_when_quit()



def showtransport():

# Input: None
# Functionality: Assist the user to go to the nearest bus stop if the the selected canteen is \
#                not of walking distance or assist the user to walk to the selected canteen \
#                if it is of walking distance. 
# Output: A straight line will be shown on the map to guide the user to the nearest bus stop \
#         or to walk to the nearest canteen.

    user.get_nearest_bus_stop()
    while True:
        appDisplay.fill(white)

        ntu_map = pygame.image.load("ntu_map.jpg")
        appDisplay.blit(ntu_map, (0, 0))

        pygame.draw.rect(appDisplay, white,
                         (user.final_canteen_choice.coordinate_x - 90, user.final_canteen_choice.coordinate_y, 180, 30))

        text_surf, text_rect = text_object(user.final_canteen_choice.name, black, size="small")
        text_rect.center = (user.final_canteen_choice.coordinate_x, user.final_canteen_choice.coordinate_y + 15)
        appDisplay.blit(text_surf, text_rect)

        pygame.draw.circle(appDisplay, red,
                           (user.final_canteen_choice.coordinate_x, user.final_canteen_choice.coordinate_y), 10)
        if user.final_canteen_choice.walking_distance_from_user:
            message_to_screen("You can walk there! Route is shown!", black, 300)

            pygame.draw.line(appDisplay, black, (user.current_location_x, user.current_location_y),
                             (user.final_canteen_choice.coordinate_x, user.final_canteen_choice.coordinate_y),
                             3)
        else:
            message_to_screen("You can take a bus."+" The nearest bus stop is "+ user.nearest_bus_stop[0]+".", black, 300)

            pygame.draw.rect(appDisplay, white, (user.nearest_bus_stop[1][0] - 60, user.nearest_bus_stop[1][1], 120, 30))
            pygame.draw.circle(appDisplay, red,
                               (user.nearest_bus_stop[1][0], user.nearest_bus_stop[1][1]), 10)
            text_surf, text_rect = text_object("nearest bus stop", black, size="small")
            text_rect.center = (user.nearest_bus_stop[1][0], user.nearest_bus_stop[1][1] + 15)
            appDisplay.blit(text_surf, text_rect)
            pygame.draw.line(appDisplay, red, (user.current_location_x, user.current_location_y),
                             (user.nearest_bus_stop[1][0], user.nearest_bus_stop[1][1]), 3)

        pygame.draw.circle(appDisplay, light_blue, (user.current_location_x, user.current_location_y), 10)

        if button("End Menu", 650, 610, 150, 50):
            app_end_menu()

        pygame.display.update()
        clock.tick(15)
        close_when_quit()



def app_end_menu():

# Input: None
# Functionality: To give the user the choice of whether he wants to find another canteen \
#                or to exit the application
# Output: The option of finding the another canteen or to exit the application will be given.

    while True:
        appDisplay.fill(white)
        message_to_screen("Are you satisfied with the sorting result?", black, -100, size="medium")
        message_to_screen("If not, do you want to try again?", black, 0, size="medium")

        if button("Sort again", 200, 400, 150, 50):
            map_page()
        if button("Quit", 500, 400, 150, 50):
            pygame.quit()
            quit()

        pygame.display.update()
        clock.tick(15)

        close_when_quit()


user = User()
app_start_menu()
