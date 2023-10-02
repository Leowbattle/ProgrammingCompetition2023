n, q, s = map(int, input().split())

queue_to_send_to = list(map(lambda x: int(x) - 1, input().split()))
queue_size = list(map(int, input().split()))

windows = []
for i in range(n):
	windows.append(list(map(int, input().split())))

queues = [0 for _ in range(q)]
for (wi, window) in enumerate(windows):
	d = window[0]
	sensors = window[1:]
	for (i, mb) in enumerate(sensors):
		dest_queue = queue_to_send_to[i]
		queues[dest_queue] += mb
		if queues[dest_queue] > queue_size[dest_queue]:
			print('impossible')
			exit()

	next_window = wi + 1
	while d > 0 and next_window < len(windows):
		space_in_queues = [queue_size[i] - mb for (i, mb) in enumerate(queues)]
		data_incoming = windows[next_window][1:]
		needed_from_queue = [max(0, data_incoming[i] - space_in_queues[i]) for i in range(len(queues))]
		for (i, mb) in enumerate(needed_from_queue):
			if queues[i] == 0 or mb == 0:
				continue

			if d == 0:
				break
			elif d < mb:
				if queues[i] < d:
					d -= queues[i]
					queues[i] = 0
				else:
					queues[i] -= d
					d = 0
			else:
				if queues[i] < mb:
					d -= queues[i]
					queues[i] = 0
				else:
					queues[i] -= d
					d -= mb

		if sum(queues) == 0:
			break

		next_window += 1

	if sum(queues) == 0:
		continue

	for (i, mb) in enumerate(queues):
		if d == 0:
			break

		if d >= mb:
			d -= mb
			queues[i] = 0
		elif d < mb:
			queues[i] -= d
			d = 0
			break

if any(queues):
	print('impossible')
else:
	print('possible')
