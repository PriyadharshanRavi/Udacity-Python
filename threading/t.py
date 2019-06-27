import threading

class messenger(threading.Thread):
	def run(self):
		for _ in range(1000):
			print(threading.currentThread().getName())

send = messenger(name='send out messages')
receive = messenger(name='receive messages')
send.start()
receive.start()


