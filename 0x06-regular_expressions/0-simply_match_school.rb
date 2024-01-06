#!/usr/bin/env ruby
# A regular expression that is simply matching School
# puts prints to standardoutput
# scan scan the stdin of argv[0]
# join, concatenates the different occurences of School INTO A STRING

puts ARGV[0].scan(/School/).join
