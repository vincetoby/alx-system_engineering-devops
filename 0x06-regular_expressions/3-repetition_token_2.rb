#!/usr/bin/env ruby
# A regular expression that is matches a given pattern
# t+, accounts for any number of t

puts ARGV[0].scan(/hbt+n/).join
