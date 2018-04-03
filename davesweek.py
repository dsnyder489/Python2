def getDavesWeek(day):
    '''Return the activity Dave did over the break week by inputting the day of the week'''
    dave = {
        'Monday': 'Work in Greensburg',
        'Tuesday': 'Work in Homestead',
        'Wednesday': 'Work in South Hills',
        'Thursday': 'Work in North Hills',
        'Friday': 'Oil Change and Tire Rotation at Baierl, then enjoyed some local ales and pizza in Lawrenceville in the evening.',
        'Saturday': 'Went to the Penguin game', 'Sunday': 'Spent Easter in Akron, OH with family'
    }

    # exception handling approach
    if not day in dave:
        return "Day not found."
    else:
        return dave[day]
