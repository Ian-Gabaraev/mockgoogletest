from datetime import time
from datetime import date
from datetime import timedelta
from datetime import datetime

def calculate_good_interval(c1, c2):
    """
    Sample input
    :param c1: c1 = ['9:00', '20:00']
    :param c2: c2 = ['10:00', '18:30']
    :return:
    """
    start = [c1[0].split(':'), c2[0].split(':')]
    end = [c1[1].split(':'), c2[1].split(':')]

    good_start = max(
        time(hour=int(start[0][0]), minute=int(start[0][1])),
        time(hour=int(start[1][0]), minute=int(start[1][1]))
    )

    good_end = min(
        time(hour=int(end[0][0]), minute=int(end[0][1])),
        time(hour=int(end[1][0]), minute=int(end[1][1]))
    )

    return [good_start, good_end]

def generate_intervals(start, end, step, default=0):
    result = list()
    start_time = datetime.combine(date.today(),
                                 start) + timedelta(hours=default)
    end_time = datetime.combine(date.today(),
                                  end)
    while start_time < end_time:
        interval_beginning = [start_time.hour, start_time.minute]
        default+=step
        start_time = datetime.combine(date.today(),
                                      start) + timedelta(hours=default)
        interval_ending = [start_time.hour, start_time.minute]
        result.append([interval_beginning, interval_ending])

    return result

def string_to_time(string):
    split_string = string.split(':')
    return time(hour=int(split_string[0]), minute=int(split_string[1]))

def get_user_intervals(intervals_as_list):
    result = list()
    for timestamp in intervals_as_list:
        result+=generate_intervals(start=string_to_time(timestamp[0]),
                                   end=string_to_time(timestamp[1]),
                                   step=0.5)
    return result

def calculate_possible_meeting_time(user_one_bound, user_two_bound,
                                    user_one_calendar, user_two_calendar, duration):
    sample_interval = calculate_good_interval(user_one_bound, user_two_bound)
    main_interval = generate_intervals(sample_interval[0], sample_interval[1], duration)
    user_one_busy = get_user_intervals(user_one_calendar)
    user_two_busy = get_user_intervals(user_two_calendar)
    result = list(filter(lambda x: x not in user_one_busy and x not in user_two_busy, main_interval))

    return result


print(calculate_possible_meeting_time(
    user_one_bound=['9:00', '20:00'],
    user_two_bound=['10:00', '18:30'],
    user_one_calendar=[
    ['9:00', '10:30'],
    ['12:00', '13:00'],
    ['16:00', '18:00']
],
    user_two_calendar=[
    ['10:00', '11:30'],
    ['12:00', '14:30'],
    ['14:30', '15:00'],
    ['16:00', '17:00']
],
    duration=0.5
))
