def minion_game(string):
    # your code goes here
    my_dict = {}
    score = {'Stuart':0, 'Kevin':0}
    vowels = 'AEIOU'
    for i in range(len(string)):
        for j in range(i+1, len(string)+1):
            sub_string = string[i:j]
            if sub_string in my_dict:
                my_dict[sub_string] += 1
            else:
                my_dict[sub_string] = 1

    for key in my_dict:
        if key[0] in vowels:
            score['Kevin'] += my_dict[key]
        else:
            score['Stuart'] += my_dict[key]

    result = ''
    if score['Kevin'] > score['Stuart']:
        result = 'Kevin {0}'.format(score['Kevin'])
    elif score['Stuart'] > score['Kevin']:
        result = 'Stuart {0}'.format(score['Stuart'])
    else:
        result = 'Draw'

    print(result)
    # print(my_dict)

if __name__ == '__main__':
    s = input()
    minion_game(s)