debug = False
lines = open('C-small-practice.in').xreadlines()
output = open('C-small-practice.out', 'w')
cases = int(lines.next().strip())
for case in xrange(1, cases + 1):
    answered = [int(s) for s in lines.next().strip().split()]
    questions, minimum = answered.pop(0), answered.pop(0)
    if questions == 1:
        print >>output, 'Case #%d: %d' % (case, answered[0]),
    elif questions == 2:
        print >>output, 'Case #%d: %d' % (case, min(answered)),
    else:
        print >>output, 'Case #%d: %d' % (case, sum(answered) // minimum),
    