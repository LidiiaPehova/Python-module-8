from datetime import datetime, timedelta

def get_birthdays_per_week(users: list) -> None:
    today = datetime.now().date()
    birthdays = {}
    for user in users:
        if user['birthday'].date() > today and user['birthday'].date() <= (today + timedelta(days=7)):
            birthdays[user['name']] = user['birthday'].weekday()

    weekdays = {
        0 : 'Monday',
        1 : 'Tuesday',
        2 : 'Wednesday',
        3 : 'Thursday',
        4 : 'Friday',
        5 : 'Saturday',
        6 : 'Sunday'
    }

    congradulations_dict = {}
    for name, birthday in birthdays.items():
        if birthday > 4:
            birthday = 0

        if birthday not in congradulations_dict.keys():
            congradulations_dict[birthday] = [name]
        else:
            congradulations_dict[birthday].append(name)
        
    for day, names in congradulations_dict.items():
        res = weekdays[day] + ': '
        for name in names:
            res += name + ', '
        print(res[0:-2])
        

def main():
    users = [
        {
            'name' : 'name1',
            'birthday' : datetime(2022, 11, 5)
        },
        {
            'name' : 'name2',
            'birthday' : datetime(2022, 11, 4)
        },
        {
            'name' : 'name3',
            'birthday' : datetime(2022, 12, 10)
        },
        {
            'name' : 'name4',
            'birthday' : datetime(2022, 11, 7)
        },
        {
            'name' : 'name5',
            'birthday' : datetime(2022, 11, 11)
        }
    ]
    get_birthdays_per_week(users=users)

if __name__ == '__main__':
    main()