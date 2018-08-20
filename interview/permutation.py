#!/usr/bin/python2

counter = 0

# The entry point
def main():
    global counter
    
    wrd = raw_input()
    rst = get_permutations(wrd)

    for i in range(0, len(rst)):
        if rst.index(rst[i]) < i:
            print 'Deu ruim'

    print '{size} - ran: {ran}: {rst}'.format(size=len(rst), ran=counter, rst=rst)

# Add some permutations of the word wrd with the letter lt
# A + BC -> ABC, BAC, BCA
def add_permutation(lt, wrd):
    global counter
    rst = []

    for i in range(0, len(wrd)+1):
        counter += 1
        rst.append(wrd[:i] + lt + wrd[i:])
    
    return rst

# Generates all permutations of the word wrd
def get_permutations(wrd):
    length = len(wrd)   # The length of the given word
    rst = [wrd[0]]      # Starts with just one letter

    if length > 1:
        aux = []

        for i in range(1, length):
            aux = rst[:]
            rst = []
            for j in range(0, len(aux)):
                rst += add_permutation(wrd[i], aux[j])
    else:
        return [wrd]
    
    return rst

if __name__ == '__main__':
    main()