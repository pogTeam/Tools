#!env ruby
# encoding: UTF-8

# Base64
require 'base64'
data = "U0hDe2lzc29fw6lfdW1hX2ZsYWd9"
plain = Base64.decode64(data)
puts "The plain text of #{data} is"
puts "#{plain}"

# Base32
require 'base32'
data = "KNEEG63JNZUWG2LBNZSG6X3PL5TWC3LFPU======"
plain = Base32.decode(data)
puts "The plain text of #{data} is"
puts "#{plain}"
