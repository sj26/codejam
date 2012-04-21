lines = open('B-large-practice.in').xreadlines()
output = open('B-large-practice.out', 'w')
cases = int(lines.next().strip())
for case in xrange(1, cases + 1):
    print >>output, 'Case #%d:' % (case,),
    towns, office_town = (int(s) for s in lines.next().strip().split())
    town_employees = dict((n, []) for n in xrange(1, towns + 1))
    employees = int(lines.next().strip())
    for employee in xrange(0, employees):
        town, passengers = (int(s) for s in lines.next().strip().split())
        town_employees[town].append(passengers)
    # Check there are enough car spots for all employees in each town
    if any(sum(town_employees[town]) < len(town_employees[town]) for town in town_employees if town != office_town):
        print >>output, 'IMPOSSIBLE'
        continue
    for town in xrange(1, towns + 1):
        if town == office_town:
            print >>output, '0',
            continue
        # Sort by passenger count so we shift off the drivers with the most passengers first and pop off the passengers who can take the least passengers themselves.
        town_employees[town].sort(reverse=True)
        cars = 0
        while len(town_employees[town]):
            cars += 1
            # How many passengers can the next driver take?
            passengers = town_employees[town].pop(0) - 1
            # Last batch? We're done!
            if len(town_employees[town]) <= passengers:
                break
            # This car takes as many of the employees who can carry the least passengers as possible.
            del town_employees[town][-passengers:]
        print >>output, cars,
    print >>output, ''
        