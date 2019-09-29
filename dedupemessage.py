"""
Input:
bound = 15
window = 10
Queue((14, "foo"),
 (2, "bar"),
 (5, "baz"),
 (8, "foo"),
 (13, "bar"),
 (0, "foo"),
 (20, "foo"),
 ...)


{
foo: 0, 8, 14
}


Output:
Queue((0, "foo"), (2, "bar"), (5, "baz"), (13, "bar"), (14, "foo"),..

"""

from heapq import heappush, heappop


class MessageLogger:
	def __init__(self, window):
		self.messages = {}
		self.window = window

	def receiveMessage(self, message):
		# we've never seen it, output it and save it
		# we've seen it but outside the window, output and save it
		# we've seen it but inside the window, ignore
		if message[1] in self.messages and message[0] - self.messages[message[1]] < self.window:
			return None
		self.messages[message[1]] = message[0]
		return message

	def removeOldMessages(self, currentTime):
		remove = []
		for message, time in self.messages.items():
			if currentTime - time > self.window:
				remove.append(message)
		for message in remove:
			del self.messages[message]




class MessageTuple:
	def __init__(self, message, time):
		self.message = message
		self.time = time

	def __lt__(self, other):
		return self.time < other.time

def dedupeMessages(outQueue, inQueue, window):
	msgHeap = []
	messageLogger = MessageLogger(window)
	for message in inQueue:
		while msgHeap[0].time < message[0] - bound:
			messageLogger.recieveMessage(heappop(msgHeap))
		msgTuple = MessageTuple(message[1], message[0])
		heappush(msgHeap, msgTuple)
