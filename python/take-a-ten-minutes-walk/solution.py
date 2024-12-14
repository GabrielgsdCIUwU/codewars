def is_valid_walk(walk):

    totalWalk = len(walk)
    if totalWalk != 10: return False
    northSouthCount = walk.count('n') - walk.count('s')
    eastWstCount = walk.count('e') - walk.count('w')

    if northSouthCount != 0 or eastWstCount != 0: return False
    return True