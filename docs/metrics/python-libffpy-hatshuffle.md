# An Efficient Pairing-Based Shuffle Argument Draft -
    Python (libffpy)
| Operation | Short Description | Time per 1000 voters |
|-----------|-------------------|----------------------|
| Initialization | Creates the elliptic Curve and private keys | 0.53s | 
| Encryption | Encrypts the votes | 1.07s | 
| Random Permutations | Creates random numbers | 0.01s | 
| Proof | The shuffle | 5.91s | 
| Verification | Verification of the shuffle | 8.00s | 
| Decryption | Decrypts the votes | 0.89s | 
| Total | total time ellapsed | 16.96 | 
