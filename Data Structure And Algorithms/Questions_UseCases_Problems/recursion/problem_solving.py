def dice_roll(faces, target):
    '''
    :param faces: number of faces on a dice
    :param target: target val to achieve via multiple rolls of dice
    :return: possible ways
    '''
    ans = []
    def rec_comb(p, t):
        if not t:
            return [p]
        l = []
        u = min(faces, t)
        for i in range(1, u+1):
            l.extend(rec_comb(f'{p}{i}', u-i))
        return l
    return rec_comb('', target)

a = dice_roll(6, 4)
print(a)
