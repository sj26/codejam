import string, sys
lines = (len(sys.argv) > 1 and open(sys.argv[1]) or sys.stdin).xreadlines()
tests_len = int(lines.next().strip())
for tests_num in xrange(1, tests_len + 1):
    height, width = map(int, lines.next().strip().split())
    graph = [map(int, lines.next().strip().split()) for y in xrange(0, height)]
    basin = [[None for x in xrange(0, width)] for y in xrange(0, height)]
    basins = iter(string.ascii_letters)
    def basin_for(y, x):
        already = basin[y][x]
        if already:
            return already
        this = graph[y][x]
        lowest, lowest_coords = this, None
        if y > 0 and graph[y - 1][x] < lowest: # North
            lowest, lowest_coords = graph[y - 1][x], (y - 1, x)
        if x > 0 and graph[y][x - 1] < lowest: # West
            lowest, lowest_coords = graph[y][x - 1], (y, x - 1)
        if x < width - 1 and graph[y][x + 1] < lowest: # East
            lowest, lowest_coords = graph[y][x + 1], (y, x + 1)
        if y < height - 1 and graph[y + 1][x] < lowest: # South
            lowest, lowest_coords = graph[y + 1][x], (y + 1, x)
        if lowest_coords:
            return basin_for(*lowest_coords)
        else:
            this_basin = basin[y][x] = basins.next()
            return this_basin
    for y in xrange(0, height):
        for x in xrange(0, width):
            basin[y][x] = basin_for(y, x)
    print 'Case #%d:\n%s' % (tests_num, '\n'.join(' '.join(map(str, basin[y])) for y in xrange(0, height)))
