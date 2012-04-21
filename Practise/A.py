lines = open('A-large-practice.in').xreadlines()
output = open('A-large-practice.out', 'w')
cases = int(lines.next().strip())
for case in xrange(1, cases + 1):
    guests = int(lines.next().strip())
    invites = sorted(int(s) for s in lines.next().strip().split()) + [None]
    for invite1, invite2 in zip(*[iter(invites)] * 2):
        if invite1 != invite2:
            print >>output, 'Case #%d: %d' % (case, invite1)
            break