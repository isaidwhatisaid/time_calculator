def add_time(start, duration, day = None):

    # Split the start and duration into hours and minutes and make them integers and separate am/pm
    start_time, am_pm = start.split()[0], start.split()[1]
    start_hr, start_min = int(start_time.split(':')[0]), int(start_time.split(':')[1])
    duration_hr, duration_min = int(duration.split(':')[0]), int(duration.split(':')[1])

    # Add the duration times to the start times
    plus_hr, plus_min = start_hr + duration_hr, start_min + duration_min
    
    # Roll over hours if combined minutes go over 59
    # Not possible to ever add more than one hour this way
    if plus_min > 59:
        new_min = plus_min % 60
        plus_hr += 1
    else: 
        new_min = plus_min
    
    # Rollover hours if combined hours go over 12 and count the number of times the rollover happens
    roll_count = 0
    while plus_hr >= 12:
        roll_count += 1
        plus_hr -= 12  
    new_hr = plus_hr

    # Sort out AM/PM
    if am_pm == 'AM' and roll_count % 2 != 0:
        new_am_pm = 'PM'
    elif am_pm == 'PM' and roll_count % 2 != 0:
        new_am_pm = 'AM'
    else: new_am_pm = am_pm

    # Calculate the number of days passed
    # Make a day counter by halving the am/pm rollover counter created earlier
    day_count = day_display = int((roll_count / 2) - (roll_count % 2)/2)
    # Ensure the day counter is in the range of the day name/index dictionaries
    while day_count > 7:
        day_count -= 7
    # Allow for extra day if starting in PM
    if am_pm == 'PM' and new_am_pm == 'AM':
        day_count += 1
        day_display += 1
    
    # Add the optional day tracker
    if day:
        #Make lowercase
        day = day.lower()
        # Create dictionary of day names with index as values
        day_names = {'monday':1, 'tuesday':2, 'wednesday':3, 'thursday':4, 'friday':5, 'saturday':6, 'sunday':7}
        day_value = day_names[day]
        new_day_value = (day_value + day_count) % 7
        if new_day_value == 0:
            new_day_value = 7
        # Create a dictionary that will have reverse keys/values as the day_names dictionary
        reverse_day_names = {}
        for i in day_names:
            reverse_day_names.update({day_names[i]:i})
        # Assign the new day as a variable
        if day_count == 0:
            new_day = ', ' + day.capitalize()
        else: new_day =', ' + reverse_day_names[new_day_value].capitalize()
    else: new_day = ''
    
    # Turn the output back into a string and clean up loose ends with 00/12
    if new_hr == 0:
        new_hr = '12'
    if new_min < 10:
        new_min = str(new_min).zfill(2)
    new_clock = str(new_hr) + ':' + str(new_min) +  ' ' + new_am_pm

    # Format everything ready for display
    if day_count == 1:
        count_display = " (next day)"
    elif day_count == 0:
        count_display = ''
    else: count_display = " (" + str(day_display) + " days later)"
    new_time = new_clock + new_day + count_display
    
    return new_time