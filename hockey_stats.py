import pprint

hockey = {
    'Nikita Kucherov': {'Team': 'TBL', 'POS': 'RW', 'Goals': 30, 'Assists': 41, 'Points': 71, '+/-': 12, 'PIM': 32},
    'Connor McDavid': {'Team': 'EDM', 'POS': 'C', 'Goals': 23, 'Assists': 43, 'Points': 66, '+/-': 12, 'PIM': 22},
    'Johnny_Gaudreau': {'Team': 'CGY', 'POS': 'LW', 'Goals': 18, 'Assists': 48, 'Points': 66, '+/-': 19, 'PIM': 10},
    'Phil Kessel': {'Team': 'PIT', 'POS': 'RW', 'Goals': 24, 'Assists': 41, 'Points': 65, '+/-': -5, 'PIM': 34},
    'Steven Stamkos': {'Team': 'TBL', 'POS': 'C', 'Goals': 21, 'Assists': 44, 'Points': 65, '+/-': 18, 'PIM': 20},
    'Claude Giroux': {'Team': 'PHI', 'POS': 'C', 'Goals': 18, 'Assists': 46, 'Points': 64, '+/-': 11, 'PIM': 16},
    'Jakub Voracek': {'Team': 'PHI', 'POS': 'RW', 'Goals': 11, 'Assists': 53, 'Points': 64, '+/-': 6, 'PIM': 42},
    'Evgeni Malkin': {'Team': 'PIT', 'POS': 'C', 'Goals': 30, 'Assists': 33, 'Points': 63, '+/-': 4, 'PIM': 51},
    'John Tavares': {'Team': 'NYI', 'POS': 'C', 'Goals': 28, 'Assists': 34, 'Points': 62, '+/-': -5, 'PIM': 22},
    'Sidney Crosby': {'Team': 'PIT', 'POS': 'C', 'Goals': 19, 'Assists': 43, 'Points': 62, '+/-': -8, 'PIM': 44},
    'Nathan MacKinnon': {'Team': 'COL', 'POS': 'C', 'Goals': 24, 'Assists': 37, 'Points': 61, '+/-': 10, 'PIM': 38},
    'Alex Ovechkin': {'Team': 'WSH', 'POS': 'LW', 'Goals': 33, 'Assists': 27, 'Points': 60, '+/-': 8, 'PIM': 20},
    'Blake Wheeler': {'Team': 'WPG', 'POS': 'RW', 'Goals': 14, 'Assists': 46, 'Points': 60, '+/-': 6, 'PIM': 38},
    'Josh Bailey': {'Team': 'NYI', 'POS': 'RW', 'Goals': 14, 'Assists': 46, 'Points': 60, '+/-': -6, 'PIM': 13},
    'Anze Kopitar': {'Team': 'LAK', 'POS': 'C', 'Goals': 22, 'Assists': 37, 'Points': 59, '+/-': 21, 'PIM': 14},
    'Mathew Barzal': {'Team': 'NYI', 'POS': 'C', 'Goals': 16, 'Assists': 43, 'Points': 59, '+/-': 3, 'PIM': 16},
    'Sean Couturier': {'Team': 'PHI', 'POS': 'C', 'Goals': 28, 'Assists': 29, 'Points': 57, '+/-': 21, 'PIM': 15},
    'Taylor Hall': {'Team': 'NJD', 'POS': 'LW', 'Goals': 21, 'Assists': 36, 'Points': 57, '+/-': 4, 'PIM': 28},
    'Jonathan Marchessault': {'Team': 'VGK', 'POS': 'C', 'Goals': 20, 'Assists': 34, 'Points': 54, '+/-': 24, 'PIM': 26},
    'Brayden Schenn': {'Team': 'STL', 'POS': 'C', 'Goals': 23, 'Assists': 30, 'Points': 53, '+/-': 17, 'PIM': 45}
          }

user_input = input('Welcome to Hockey Stats.  Please select a key: ')
if user_input in hockey:
    print(hockey[user_input])
    player = hockey[user_input]
    stats = player.keys
    requested_stat = input('Enter a key: ')
    print(player[requested_stat])
    pprint.pprint(hockey)
    rank_input = input('Rank players from favorite to least favorite: ')
