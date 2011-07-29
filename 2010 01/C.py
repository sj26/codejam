# Google CodeJam, Qualification Round 2010, Problem C - sj26@sj26.com
import sys
from itertools import *
lines = (len(sys.argv) > 1 and open(sys.argv[1]) or sys.stdin).xreadlines()
tests_len = int(lines.next().strip())
for tests_num in xrange(0, tests_len):
    circuits, capacity, groups_len = map(int, lines.next().strip().split())
    groups = map(int, lines.next().strip().split())
    groups_iter = cycle(groups)
    groups_next = groups_iter.next()

    sys.stderr.write('Test #%d: %dx%d, %r;' % (tests_num + 1, circuits, capacity, groups))
    if all(a == b for (a, b) in izip(islice(groups, 1, None), iter(groups))):
        sys.stderr.write(' simple1;')
        earnings = circuits * min(groups_len * groups[0], capacity // groups[0])
    elif sum(groups) < capacity:
        sys.stderr.write(' simple2;')
        earnings = circuits * sum(groups)
    else:
        sys.stderr.write(' complex;')
        offset = 0
        rides = []
        passengers = 0
        while not rides or offset != 0:
            if passengers + groups[offset] > capacity:
                rides.append(passengers)
                passengers = groups[offset]
            else:
                passengers += groups[offset]
            offset += 1
            offset %= groups_len
        rides_len = len(rides)
        rides_sum = sum(rides)
        rides_circuits = (circuits // rides_len)
        earnings = rides_circuits * rides_sum
        rides_iter = iter(rides)
        for circuit in xrange(rides_len * rides_circuits, circuits + 1):
            earnings += rides_iter.next()
    sys.stderr.write(' %d.\n' % (earnings,))
    
    print 'Case #%d: %d' % (tests_num + 1, earnings)