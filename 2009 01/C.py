import sys
from itertools import *
lines = (len(sys.argv) > 1 and open(sys.argv[1]) or sys.stdin).xreadlines()
tests_len = int(lines.next().strip())
s = 'welcome to codejam'
for tests_num in xrange(1, tests_len + 1):
    count = 0
    test = [letter for letter in lines.next().strip() if letter in s]
    def counter(s_iter, test_iter, s_depth=0, test_depth=0):
        s_iter, s_iter_again = tee(s_iter)
        s_letter = next(s_iter, None)
        if s_letter is None:
            return 1
        for test_letter in test_iter:
            test_depth += 1
            if test_letter == s_letter:
                test_iter, test_iter_again = tee(test_iter)
                return counter(s_iter, test_iter, s_depth + 1, test_depth) + counter(s_iter_again, test_iter_again, s_depth + 1, test_depth)
        return 0
    count = counter(iter(s), iter(test))
    print 'Case #%d: %s' % (tests_num, ('%04d' % (count))[-4:])
