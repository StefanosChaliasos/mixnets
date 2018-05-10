import matplotlib.pyplot as plt


f = plt.figure()
prover = [16912, 111850, 1060492, 2113272]
verifier = [38036, 332308, 3232716, 6421144]
decryption = [12704, 76676, 685596, 1367660]
votes = [1000, 10000, 100000, 200000]
plt.plot(votes, prover)
plt.plot(votes, verifier)
plt.plot(votes, decryption)

plt.title('Memory Consumption')
plt.legend(['prover', 'verifier', 'decryption'], loc='upper left')
plt.xlabel('Votes Number')
plt.ylabel('Maximum resident set size (kbytes)')

#  plt.show()
f.savefig("memory.pdf", bbox_inches='tight')
