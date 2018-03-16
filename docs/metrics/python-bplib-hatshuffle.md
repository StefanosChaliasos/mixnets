# An Efficient Pairing-Based Shuffle Argument Draft -
    Python (bplib)
| Operation | Short Description | Time per 1000 voters |
|-----------|-------------------|----------------------|
| Initialization | Creates the elliptic Curve and private keys | 12.50s | 
| Encryption | Encrypts the votes | 5.51s | 
| Random Permutations | Creates random numbers | 0.01s | 
| Proof | The shuffle | 17.48s | 
| Verification | Verification of the shuffle | 31.70s | 
| Decryption | Decrypts the votes | 3.15s | 
| Total | total time ellapsed | 1:09.46 | 
