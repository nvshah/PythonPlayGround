def seive_of_erantosthesis(n):
    '''
    Time Complexity := O(n * log(log n))
    aim : distinguish all primes & non-primes seperately
    '''
    visited = [False] * (n+1)
    # all the non-primes will hold True value at the end
    # False -> Prime
    # True -> Non-Prime
    i = 2
    while i*i <= n:
        if not visited[i]:
            for j in range(i*2, n+1, i):
                visited[j] = True  # mark all multiple of i as non-prime
        i += 1

    primes = []
    composites = []

    for i, v in enumerate(visited):
        if v:
            composites.append(i)
        else:
            primes.append(i)

    print('Primes : ', primes)
    print('Composites : ', composites)
