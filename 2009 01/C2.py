import sys
from itertools import *
lines = (len(sys.argv) > 1 and open(sys.argv[1]) or sys.stdin).xreadlines()
tests_len = int(lines.next().strip())
phrase = 'welcome to codejam'
phrase_set, phrase_len = set(phrase), len(phrase)
for tests_num in xrange(1, tests_len + 1):
    test = [letter for letter in lines.next().strip() if letter in phrase_set]
    test_len = len(test)
    if test_len < phrase_len or any(l not in test for l in phrase_set):
        count = 0
    elif test == phrase:
        count = 1
    else:
        pp = list(list(test_i for (test_i, test_letter) in enumerate(test) if test_letter == phrase_letter) for phrase_letter in phrase)
        if any(not p for p in pp):
            count = 0
        else:
            for i in xrange(1, phrase_len):
                p_min = min(pp[i - 1])
                pp[i] = list(p for p in pp[i] if p > p_min)
            for i in reversed(range(0, phrase_len - 1)):
                p_max = max(pp[i + 1])
                pp[i] = list(p for p in pp[i] if p < p_max)
            def permute(m, i):
                if i == phrase_len:
                    return 1
                return sum(permute(n, i + 1) for n in pp[i] if pp[i] > m)
            count = permute(-1, 0)
    print 'Case #%d: %s' % (tests_num, ('%04d' % (count))[-4:])
