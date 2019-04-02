'''
5opt
'''


def dist_squared(c1, c2):
	t1 = c2[0] - c1[0]
	t2 = c2[1] - c1[1]

	return t1**2 + t2**2


def calc_length(route2, path):
	length = 0
	for i in range( len(path) ):
		length += dist_squared( cities[ path[i-1] ], cities[ path[i] ] )

	return length


def run_5opt(route2):

    x=[list(l) for l in route2]
    order =  range(x[0])
    length = calc_length(route2, order)


    changed = True
    while changed:

        changed = False

        for a in range(route2[0]):

            for b in range(a+1, route2[0] - 1):

                c =  choice( list( range(b+1, route2[0]) ) )

                a, b, c = choice( list( permutations( (a, b, c) ) ) )

                new_order = order[:a] + order[a:b][::-1] + order[b:c][::-1] + order[c:]
                new_length = calc_length(route2, new_order)

                if new_length < length:
                    length = new_length
                    order = new_order
                    changed = True

    return order, length
