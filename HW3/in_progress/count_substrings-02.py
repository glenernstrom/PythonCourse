"""
Glen Ernstrom
CS 1210
July 21, 2026

formatting reviewed and checked by
running ruff (0.15.20) at the command line,
reviewing any errors in vim, then running
ruff format *.py prior to submission

"""


def count_substrings(slices_, substring_):
    substring_count = 0
    for i,e in enumerate(slices_):
        if e == substring:
            substring_count += 1
        else:
            substring_count += 0
    return(substring_count)
 
 
if __name__ == "__main__":
    string = str(input("Enter a string: "))
    substring = str(input("Enter a substring: "))

    string_length = len(string)
    frame_length = len(substring)

    # initialize slice boundaries
    start = 0
    stop = frame_length

    # create an iterable object determined by frame_length
    frames = [0]
    for i in range(frame_length):
        i += 1
        frames.append(i)

    # print(frames) -> used for testing
 
    # initialize the slicer
    slices = [] # slices accumulate here
    incr = 0 # number of passes of slicing bound by frame legnth
    
    # the string slicer in all foward reading frames
    for incr in range(0, max(frames)):
        start = 0 + incr # start at reading frame 1
        stop  = frame_length + incr
        for num in range(string_length // frame_length):
            element = string[start:stop]
            slices.append(element)
            start += frame_length
            stop  += frame_length
          
    print(count_substrings(slices, substring))







