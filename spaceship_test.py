'''
Clara Kim
CS5001
November 7, 2018
HW5
'''
from spaceship import generate_word
def test_generate_word(file_name, expected):
    '''function test_generate_word
    Parameters: str (file_name from which to generate words),
                list of expected outputs
    Returns: nothing
    Does: executes generate_word function and checks whether in expected list
    Eventualities Covered: words in .txt that are capitalized, have punctuation,
                           very long, very short'''

    passed = 0
    failed = 0

    for i in range(50):
        output = generate_word(file_name)
        print('Generated the word...', output)
        if output in expected:
            passed += 1
            print('...PASSED!')
        else:
            failed += 1
            print('...FAILED!')
            
    print('\nTotal tests:', passed + failed, '\n'
          'Passed:', passed, '\n'
          'Failed', failed, '\n')

def main():
    
    expected = ['nap', 'taco', 'PIZZA', 'supercalifragilisticexpialidocious',
                'fire-proof', 'hElLo', 'cool.beans']

    test_generate_word('dummy_wordlist.txt', expected)

main()


from spaceship import find_letters
def test_find_letters(letters_input, words_input, expected):
    '''function test_find_letters
    Parameters: list of letters input, list of word input, and list of expected
    Returns: nothing
    Does: executes find_letters function, compares them to expected results,
          and reports passed/failed
    Eventualities Covered: multiple instances of a letter in a word, numbers,
                            punctuation marks, letter not contained in word'''

    passed = 0
    failed = 0
    
    for i in range(len(expected)):
        output = find_letters(letters_input[i],words_input[i])
        print('The result of testing letter', letters_input[i], 'and',
              words_input[i], 'is', output)
        if output == expected[i]:
            passed += 1
            print('...PASSED!')
        else:
            failed +=1
            print('...FAILED!')

    print('\nTotal tests:', passed + failed, '\n'
          'Passed:', passed, '\n'
          'Failed', failed, '\n')

def main():

    letters_input = ['p', 'e', "'", '.', 'a', 'p', 'f', 'p', 'y', '8', '-']
    words_input = ['apple', 'delta', "it's", 'some.thing', 'very', 'happy',
                   'food', 'pumpkin', 'harry', 'books', 'ice-cream']
    expected = [[1,2],[1],[2],[4],[],[2,3],[0],[0,3],[4],[],[3]]
    
    test_find_letters(letters_input, words_input, expected)

main()

from spaceship import new_score
def test_new_score(name_inputs, score_inputs, expected, file_name):
    '''function is test_new_score
    Parameters: list of name inputs, list of score inputs,
                list of expected, and str (file name)
    Returns: nothing
    Does: executes new_score function and checks whether new file was created
          and whether information matches expected
    Eventualities Covered: large scores, negative scores, capital letters,
                            hyphens, periods'''
    passed = 0
    failed = 0

    for i in range(len(expected)):
        print('Writing new scores', name_inputs[i], 'and', score_inputs[i])
        output = new_score(name_inputs[i], score_inputs[i], file_name)
        open_file = open(file_name, 'r')
        check_file = open_file.readlines()
        open_file.close()
        if expected[i] in check_file:
            passed += 1
            print('...PASSED!')
        else:
            failed +=1
            print('...FAILED!')

    print('\nTotal tests:', passed + failed, '\n'
          'Passed:', passed, '\n'
          'Failed', failed, '\n')    
        

def main():

    name_inputs = ['vampire', 'ghoul', 'fiend', 'SCARY-GHOST', 'P.S.L.',
                   'Werewolf', 'will-o-wisp', 'candy', 'cavities', 'harvest']
    score_inputs = [25, 50, 100, 0, -10, 7, 2, 4, 6, 9999]
    expected = ['vampire 25\n', 'ghoul 50\n', 'fiend 100\n', 'SCARY-GHOST 0\n',
                'P.S.L. -10\n', 'Werewolf 7\n', 'will-o-wisp 2\n', 'candy 4\n',
                'cavities 6\n', 'harvest 9999\n']

    test_new_score(name_inputs, score_inputs, expected, 'dummy_scores.txt')

main()

from spaceship import high_score
def test_high_score(name_inputs, score_inputs, expected, file_name):
    '''function is test_high_score
    Parameters: list of name inputs, list of score inputs,
                list of expected, and str (file name)
    Returns: nothing
    Does: executes new_score function to add the scores to the file and then
          executes high_score function and checks whether the appropriate
          score/name is at the top of the list
    Eventualities Covered: new high score, not high score, equal to high score'''

    passed = 0
    failed = 0

    for i in range(len(expected)):
        print('Testing high score status of', name_inputs[i], score_inputs[i])
        new_score(name_inputs[i], score_inputs[i], file_name)
        high_score(name_inputs[i], score_inputs[i], file_name)
        open_file = open(file_name, 'r')
        check_file = open_file.readlines()
        open_file.close()
        if check_file[0] == expected[i]:
            passed += 1
            print('...PASSED!')
        else:
            failed += 1
            print('...FAILED!')

    print('\nTotal tests:', passed + failed, '\n'
          'Passed:', passed, '\n'
          'Failed', failed, '\n')

def main():

    name_inputs = ['shaggy', 'velma', 'daphney', 'scooby', 'fred']
    score_inputs = [10, 10, 0, 12, 2]
    expected = ['shaggy 10\n', 'velma 10\n', 'velma 10\n',
                'scooby 12\n', 'scooby 12\n']

    test_high_score(name_inputs, score_inputs, expected, 'dummy_highscore.txt')

main()
