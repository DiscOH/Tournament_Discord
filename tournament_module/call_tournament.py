import bracket

poc = bracket.Tournament()
poc.add_participant('A', id=1)
poc.add_participant('B', id=2)
poc.add_participant('C', id=3)
poc.add_participant('D')

poc.add_match('A', 2, 1, 1)
poc.add_match('B', 3, 2, 0)
poc.add_match('C', 'D', 0, 2)
poc.add_match('D', 1, 2, 0)

poc.score_simple()

print(poc.determine_winner())