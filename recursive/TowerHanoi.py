def hanoi(disks,src,dest,spare):
	if disks >0:
		hanoi(disks-1,src,spare,dest)
		if src:
			dest.append(src.pop())
		hanoi(disks-1,spare,dest,src)

source = [7,6,5,4,3,2,1]
dest = []
spare = []
hanoi(4,source,dest,spare)

print source, dest, spare
