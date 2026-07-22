"""
Glen Ernstrom
CS 1210
July 22, 2026



"""
# thought stream:

# The gameplan. Modeling the genetic code and the concept
# of reading frames. Not sure if reading frame is
# relevant but going with a hunch ...

# For DNA there are six possible reading frames
# 3 forward, 3 reverse because DNA is double-stranded with
# anti-parallel complementary strands. Fortunately we are only
# dealing with a single strand in one left-right direction.
# So for a triplet codon there is a set of three different
# groupings of a triplet.
# ATG CCC CGA - 1
#  TGC CCG A  - 2
#   GCC CGA   - 3
#     CCC CGA - 1 Then we are back in reading frame 1

# Example from the assignment prompt:

# gact acta ggac ta  1
#   acta ctag gact a 2
#    ctac tagg acta  3
#     tact agga cta  4
#      acta ggac ta  1

# searching for a quartet
# acta, 3 acta substrings, found in frames 1,2, and 3

# g a c t a c t a g g a c t a
# searching for 'a'
# there is only one reading frame
# 5 instances of 'a' found

# gac tac tag gac ta     1
#   act act agg act      2
#    cta cta gga ct      3
#      tac tag gac ta    1
# searching for 'tag'
# only one instance in frame 1 found

# OK! I am convinced this is the correct approach. Now how
# to write it: create a set of lists in all possible
# "reading frames" and query for "hits"

# let's generate lists for each frame with each element
# equal to the length of the substring
# we could create a test condition that says any item
# in the list is perfectly divisible by the length of
# the substring and discard all the rest

# a fuzzy idea popped into mind: modular math - put a pin
# -> revist that module - thinking there might be a
# clever way to use that ...

# we need to increment the frame. generally speaking,
# a for-loop seems to be the tool for the job since
# we have a finite number of iterations to explore

# then it's just a matter of asking if the substring in the
# newly established lists and counting the number of "hits"
# for-in loop with a counter

# the key component is the "slicer". substring_count() should
# be straightforward once we have "the search space" setup

# 1. get the string then substring from the user

# 2. assign some variables based on the lengths of the strings

string_length = len(string)
frame_length = len(substring)

# ***collect slices in lengths (not steps!) equal to the
# length of the substring***

# then repeat by starting at the next index (if neeeded)

# that's it! it'll work!

# playing in the shell to test this idea out ...

# we increment the start and stop slice indicies by
# the length of the substring

# we can set the number of iterative slicing to do
# based on integer division result between string_length // frame_length (?)
# i don't think that's it.

# let me just say out loud: how many chunks equal to the frame size
# can we get given the string length? there is no need to iterate
# slicing more than than total number of possible frame-sized chunks

# maybe its just slicing in frame-sized lengths and stop the loop when
# it hits an empty string in which case a while loop would suffice or
# break out of the while loop if the slice is empty. 
