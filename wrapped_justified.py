import textwrap
import argparse


def full_justify(line, width):
    words = line.split()

    # EDGE CASE: one word
    if len(words) == 1:
        return line.ljust(width)    
    
    # add initial space to each words, EXCEPT last word
    for i in range(len(words) - 1):
        words[i] += ' '

    # calculate number of spaces to add
    line_len = len(''.join(words))
    spaces_to_add = width - line_len

    # add extra spaces to each word, EXCEPT last word
    while spaces_to_add > 0 and len(words) > 1:
        # loop starts at second to last word
        # this means any non symmetric extra spaces will be loaded at the end first
        for i in range(len(words) - 2, -1, -1):
            words[i] += ' '
            spaces_to_add -= 1
            if spaces_to_add < 1:  
                break

    return ''.join(words)


def wrapper(paragraph, width):
    '''
    align paragraph to specified width,
    returns list of paragraph lines
    '''

    wrapper = textwrap.TextWrapper(width=width, break_long_words=False)
    wrapped = wrapper.wrap(text=paragraph) 

    return wrapped


def wrapper_justified(paragraph, width):
    # get array with wrapped lines
    wrapped = wrapper(paragraph, width)

    for i, line in enumerate(wrapped):
        # justify line
        justified = full_justify(line, width)

        # print results
        formatted = 'Array [{0}] = "{1}"'.format(i+1, justified)
        print(formatted)    


if __name__ == '__main__':
    P1 = "This is a sample text but a complicated problem to be solved, so we are adding more text to see that it actually works."
    WIDTH = 20

    wrapper_justified(P1, WIDTH) 
