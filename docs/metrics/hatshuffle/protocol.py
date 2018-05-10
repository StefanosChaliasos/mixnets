import matplotlib.pyplot as plt


f = plt.figure()
protocol = [57, 525, 1061]
votes = [10000, 100000, 200000]
plt.plot(votes, protocol)

plt.title('Protocol Benchmark')
plt.xlabel('Votes Number')
plt.ylabel('Protocol time (seconds)')

#  plt.show()
f.savefig("protocol.pdf", bbox_inches='tight')
