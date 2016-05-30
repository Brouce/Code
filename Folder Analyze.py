## The following function accepts a folder path within a computer system and outputs the following to the user; the extension of each of file, the the number of files that include that particular extension, the total size of all the files with that extension. The maximum, minimum, and average sizes of each unique extension.








import os
>>> def ext(path):
	newlist=[]
	newlist2=[]
	newlist3=[]
	for root,dirs,files in os.walk(path):
		for i in files:
			filepath=os.path.join(root,i)
			filextension=os.path.splitext(filepath)
			filebase=os.path.basename(filepath)
			newlist.append(filebase)
			extension=filextension[-1:]
			extension=str(extension)
			ext=extension[2:-3]
			newlist2.append(ext)
		for x in newlist2:
			if x not in newlist3:
				newlist3.append(x)
		for y in newlist3:
			newlist4=[]
			newlist5=[]
			count=0
			size=0
			totalsize=0
			maxx=0
			minn=0
			avgg=0
			for h in newlist:
				if y in h:
					newlist5.append(h)
				else:
					continue
			for t in newlist5:
				size=os.path.getsize(os.path.join(root,t))
				count=len(newlist5)
				newlist4.append(size)
				for g in newlist4:
					totalsize=sum(newlist4)
					maxx=max(newlist4)
					minn=min(newlist4)
					avgg=totalsize/count
			print("extension: ",y, "count: ",count, "total size of files with extension: ",totalsize, "max size: ", maxx, "min size: ", minn, "average :", avgg)

	
