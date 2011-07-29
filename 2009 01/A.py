import sys
lines = (len(sys.argv) > 1 and open(sys.argv[1]) or sys.stdin).xreadlines()
letters_len, words_len, tests_len = map(int, lines.next().strip().split())
words = list()
for word in (lines.next().strip() for i in xrange(0, words_len)):
    words.append(word)
for tests_num in xrange(1, tests_len + 1):
    test = lines.next().strip()
    tests = []
    appender = tests
    for letter in test:
        if letter == '(':
            tests.append([])
            appender = tests[-1]
        elif letter == ')':
            appender = tests
        else:
            appender.append(letter)
    matches = range(0, words_len)
    for letters_num in xrange(0, letters_len):
        letter = test[letters_num]
        matches = filter(lambda match: words[match][letters_num] in tests[letters_num], matches)
        if not matches: break
    matches_len = len(matches)
    print 'Case #%d: %d' % (tests_num, matches_len)