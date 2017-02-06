import sys

class stack:
	def __init__(self):
		self.items = []

	def isEmpty(self):
		return self.items == []

	def push(self, item):
		self.items.append(item)

	def pop(self):
		return self.items.pop()

	def peek(self):
		return self.items[len(self.items)-1]

	def size(self):
		return len(self.items)

class gearbox:
	def __init__(self, prevw_cin, w_cin, mfgplan, w_cout)
		self.prevw_cin = prevw_cin
		self.w_cin = w_cin
		self.mfgplan = mfgplan
		self.w_cout = w_cout
		
def calc_error(win, wout, wc):
    return abs(wout - wc) / abs(wout - win) * 100	
	
def main():
	
	w_in = 100
	w_out = [-117, 77, 377, -20, -2345, 2]
	w_c = w_in
	error = 2.5
	gears = [11,23,31,47,59,71,83,97,109,127]
	
	#Loop for DFS while searching
	for problem = 0 to 5
		while
			w_c = new
			gear
			depth = XX
			recent 
			d
			#if a solution is found
			if  calc_error(w_in, w_out[problem+1], w_c) <= error
				#add to solutions
				continue
			
			#if at depth 10, do not add children
			if depth < 10
				#add mated children to stack
				for i in range(9)
					#if gear teeth are not within 30, do not add
					if gears[i]-recent >30
						continue
						
					#if w_c is something it equaled before ata lower depth along that branch, do not add
					if 
						continue
					
					#push onto stack
				#if previous operation was a pair, do not add paired children
				if
				#add paired children to stack
					for i in range(9)
						#do not pair with same gear
						if gears[i] = recent
							continue
	
main()