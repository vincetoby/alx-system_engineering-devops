#!/usr/bin/env ruby
# A regular expression that is matches a given pattern
# bt*, Matches the characters 'bt' followed by zero or
# more occurrences of the character 't'.

puts ARGV[0].scan(/hbt*n/).join
