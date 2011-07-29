# Google CodeJam, Qualification Round 2010, Problem B - sj26@sj26.com
import sys
from fractions import gcd
from itertools import *
lines = (len(sys.argv) > 1 and open(sys.argv[1]) or sys.stdin).xreadlines()
tests_len = int(lines.next().strip())
for tests_num in xrange(1, tests_len + 1):
    line = imap(int, lines.next().strip().split())
    events_len, events = line.next(), sorted(line)
    events_normalised = list(events[i] - events[0] for i in xrange(0, len(events)))
    events_gcd = max(1, reduce(gcd, imap(gcd, islice(events_normalised, 1, None), iter(events_normalised))))
    future, future_offset = 0, events[0] % events_gcd
    if future_offset > 0:
        future = events_gcd - future_offset
    print 'Case #%d: %d' % (tests_num, future)