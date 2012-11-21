#!/usr/bin/env python
#coding:utf8

import queue
import threading
class Worker(threading.Thread):
	def __init__(self,work_queue,word,number):
		super().__init__()
		self.work_queue=work_queue
		self.word=word
		self.number=number
	def run(self):
		while True:
			try:
				filename=self.work_queue.get()
				self.process(filename)
			finally:
				self.work_queue.task_done()
def main():
	opts,word,args=parse_options()
	filelist=get_files(args,opts.recurse)
	work_queue=queue.Queue()
	for i in range(opts.count):
		number="{0}: ".format(i+1) if opts.debug else ""
		worker=Worker(work_queue,word,number)
		worker.daemon=True
		worker.start()

	for filename in filelist:
		work_queue.put(filename)
	work_queue.join()

if __name__ == '__main__':
	main()

