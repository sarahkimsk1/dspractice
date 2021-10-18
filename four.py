def best_hero(num_truncate, hero_scores):   
    assert(num_truncate % 2 == 0)

    best_player = ''
    avg = 0
    for hero in hero_scores:
        scores = hero_scores[hero]
        sum = 0
        for i in range(int(num_truncate/2), len(scores) - int(num_truncate/2)):
            assert(isinstance(scores[i], int) or isinstance(scores[i], float))
            sum += int(scores[i])
        average = sum / (len(scores) - num_truncate)
        if average > avg:
            best_player = hero
            avg = average

    return best_player
