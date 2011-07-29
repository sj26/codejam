# Google CodeJam, Qualification Round 2010, Problem A - sj26@sj26.com
import sys
lines = (len(sys.argv) > 1 and open(sys.argv[1]) or sys.stdin).xreadlines()
tests_len = int(lines.next().strip())
for tests_num in xrange(1, tests_len + 1):
    snappers, clicks = map(int, lines.next().strip().split())
    on = ((clicks + 1) % pow(2, snappers)) == 0
    sys.stderr.write('Test #%d: %d, %d; %s.\n' % (tests_num, snappers, clicks, on and 'ON' or 'OFF'))
    print 'Case #%d: %s' % (tests_num, on and 'ON' or 'OFF')