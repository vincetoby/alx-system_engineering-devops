#!/usr/bin/env ruby
# A regular expression that is matches 10 digit phone number
# ^ asserts beginning of string
# [0-9] scans number from 0 to 9
# {10} means that the numbers can only be 10
# $ asserts the end of string
# puts print to STDOUT

puts ARGV[0].scan(/^[0-9]{10}$/).join
