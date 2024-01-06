#!/usr/bin/env ruby
# A regular expression that is matches a given pattern
# puts, prints to STDOUT
# ARGV[0], ACCESSES THE FIRST string passed to stdin
# scan, scans the stdin for occureences of hbtn
# h looks for matches of 'h' literallly
# b the same as h
# t{2,5}, indicates that t can occur with 2 to 5 times in the string
# n, same as h and b
# join, does concatenation of all ocuurences into string

puts ARGV[0].scan(/hbt{2,5}n/).join
