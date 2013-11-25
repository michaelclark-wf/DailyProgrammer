#!/usr/bin/python
# fallingSand.py - Python script to solve http://www.reddit.com/r/dailyprogrammer/comments/1rdtky/111113_challenge_142_easy_falling_sand/

import sys

class ClassName():
    STONE = "#"
    SAND = "."
    EMPTY = ' '

    def main(self):
    	all_input = sys.stdin.readlines()
    	grid_size = all_input[0]
    	grid = all_input[1:]
     return falling_sand(self, grid_size, grid, 0)


    def falling_sand(self, size, grid, index):
    	grid_y = index    	
    	grid_x = 0 
    	last_line = False if index != size else True
    	for grid_line in grid:
    		for grid_x in xrange(0,size):
    			if not next_is_rock   			


    def next_is_rock(self, next_line, index):
    	return next_line[index] == self.STONE


    	






if __name__ == '__main__':
    main()
