#!/usr/bin/env python

'''
已知N个人（以编号1,2,3...n分别表示）围坐在一张圆桌周围.
	从编号为k的人开始报数,数到m的那个人出列.
	他的下一个人又从1开始报数,数到m的那个人又出列.
	依此规律重复下去,直到圆桌周围的人全部出列.
'''

def solve(ring, start, stop):
	length = len(ring)
	if start > 1:
		ring = ring[start-1:] + ring[0:start-1]

	print('start counting...')

	count = 0
	while length > 1:
		for i in range(0, stop):
			print(i+1, end=' ')
			count += 1
			if count > length:
				count = count % length
		quit = ring.pop(count-1)
		ring = ring[count-1:] + ring[:count-1]
		length = len(ring)
		print('quit the ring: ', quit)
		count = 0

	return ring

if __name__ == '__main__':
	print(solve([1,2,3,4,5,6,7,8,9],1,5))
	print(solve([i for i in range(1,9)],3,5))
	print(solve([chr(i) for i in range(67,67+9)],1,3))
