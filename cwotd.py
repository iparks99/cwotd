#!/usr/bin/python

# Chinese Word of the Day
# Reads from HSK lists and selects random word, pinyin, and definition

import datetime
import random
import sys

def load_csv(filename):
  try:
    words = open(filename, "r")
  except IOError:
    print "Could not read file: %s" % filename
    sys.exit(2)
  return words.readlines()

def get_rand_word(lines, seed=None):
  max_lines = len(lines)
  random.seed(seed)
  r_line = random.randint(0, max_lines)
  return lines[r_line].split(',')

def pretty_print(wotd, date):
  output = "Chinese Word of the Day for %i-%i-%i\n" % (date.year, date.month, date.day)
  output += "Today's word is: %s (%s)\n" % (wotd[0], wotd[1])
  output += "Pinyin: %s\n" % wotd[3]
  output += "English: %s" % wotd[4]
  return output

def main(argv):
  lines = []
  now = datetime.datetime.now()
  seed = now.year * now.month * now.day

  if (len(argv) < 1):
    print "Too few arguments!"
    sys.exit(2)

  for arg in argv:
    if arg == "-r":
      seed=None
      continue
    lines += load_csv(arg)

  print pretty_print(get_rand_word(lines, seed), now)

if __name__ == "__main__":
  main(sys.argv[1:])
