def combinelist (list1, list2):
    list1.extend(list2)
    return list1


Hockey = ['Penguins', 'Wild', 'Kings']
Baseball = ['Pirates', 'Yankees', 'Astros']

print(combinelist(Hockey, Baseball))
