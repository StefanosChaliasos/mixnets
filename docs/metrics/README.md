# Metrics

* Measured on a virtual machine hosted on [okeanos](https://okeanos.grnet.gr)
with 8GB of RAM, 4 CPUs and 40GB hard disk; using Ubuntu 16.04 LTS.

* Each test is run and measured at least 5 times.

* ***All times are shown in seconds***

## Papers

* ["A Shuffle Argument Secure in the Generic Model"]
(https://eprint.iacr.org/2016/866.pdf) Fauzi et al.

* ["An Efficient Pairing-Based Shuffle Argument Draft"]
(http://kodu.ut.ee/~lipmaa/papers/flsz17/hat_shuffle.pdf) Fauzi et al.

## Implementations - Libraries

* [libff](https://github.com/scipr-lab/libff)
* [libffpy](https://github.com/eellak/gsoc17module-zeus/tree/master/libffpy)
* [bplib](https://github.com/gdanezis/bplib)
* [flz16](https://github.com/eellak/gsoc17module-zeus/tree/master/flz16) -
SASGM 16
* [hat\_shuffle(CPP)]
(https://bitbucket.org/JannoSiim/hat_shuffle_implementation/) - EPBSA 17 CPP
* [hat\_shuffle(Python libffpy)]
(https://github.com/grnet/hat_shuffle/tree/libffpy) - EPBSA 17 Python (libffpy)
* [hat\_shuffle(Python bplib)](https://github.com/grnet/hat_shuffle) -
EPBSA 17 Python (bplib)

## Tables

1. [BDLO12](#bdlo12)
2. [Bos Coster](#boscoster)
3. [Libff - Libsnark (Hat Shuffle - CPP)](#libfflibsnark)
4. [Libff multi exponentiation routines](#libffmulti)
5. [SASGM 16 - Python (libffpy)](#flz16libffpy)
6. [EPBSA 17 - Python (libffpy)](#hatshufflelibffpy)
7. [EPBSA 17 - Python (bplib)](#hatshufflebplib)
8. [Totals](#totals)

### <a name="bdlo12"></a>BDLO12

| Votes | Time | Parallel |
|-------|------|----------|
| 100 | 0.8808 | 0.5756 |
| 1000 | 4.8239 | 2.9296 |
| 10000 | 38.9441 | 16.7482 |
| 50000 | 182.3213 | 74.6706 |
| 100000 | 364.1626 | 140.0757 |

### <a name="boscoster"></a>Bos Coster

| Votes | Time | Parallel |
|-------|------|----------|
| 100 | 0.7496 | 0.4984 |
| 1000 | 4.6807 | 3.0224 |
| 10000 | 38.7940 | 16.8659 |
| 50000 | 184.3543 | 74.1021 |
| 100000 | 363.5330 | 137.4504 |

### <a name="libfflibsnark"></a>Libff - Libsnark

| library | votes | CRS | Protocol | Parallel Protocol | Total |
|---------|-------|-----|----------|-------------------|-------|
| libff | 100 | 0.1884 | 0.7496 | 0.4984 | 0.9380 |
| libsnark | 100 | 0.1495 | 0.8014 | 0.5331 | 0.9509 |
| libff | 1000 | 0.6740 | 4.6807 | 3.0224 | 5.3547 |
| libsnark | 1000 | 0.6039 | 4.7306 | 3.1762 | 5.3345 |
| libff | 10000 | 3.8045 | 38.7940 | 16.8659 | 42.5985 |
| libsnark | 10000 | 3.8563 | 38.3891 | 21.2168 | 42.2454 |
| libff | 50000 | 15.5390 | 184.3543 | 74.1021 | 199.8933 |
| libsnark | 50000 | 15.2326 | 183.7211 | 96.5089 | 198.9537 |
| libff | 100000 | 26.9253 | 363.5330 | 137.4504 | 390.4583 |
| libsnark | 100000 | 27.0336 | 359.9804 | 191.2344 | 387.0140 |

### <a name="libffmulti"></a>Libff multi exponentiation routines

| votes | naive | naive plain | BDLO12 | bos coster |
|-------|-------|-------------|--------|------------|
| | - | - | Bos and Coster, "Addition chain heuristics", CRYPTO '89 | Bernstein, Doumen, Lange, Oosterwijk, "Faster batch forgery identification", INDOCRYPT 2012  |
| 1000 | 5.9543 | 6.0770 | 4.8239 | 4.6807 |
| 10000 | 51.6209 | 59.5255 | 38.9441 | 38.7940 |
| 100000 | - | - | 364.1626 | 363.5330 |

### <a name="flz16libffpy"></a>SASGM 16 - Python (libffpy)

| Operation | Short Description | Time per 1000 voters |
|-----------|-------------------|----------------------|
| Initialization | Creates the elliptic Curve and private keys | 0.68s |
| Encryption | Encrypts the votes | 1.79s |
| Random Permutations | Creates random numbers | 0.01s |
| Proof | The shuffle | 8.65s |
| Verification | Verification of the shuffle | 11.54s |
| Decryption | Decrypts the votes | 2.78s |
| Total | total time ellapsed | 25.46 |

### <a name="hatshufflelibffpy"></a>EPBSA 17 - Python (libffpy)

| Operation | Short Description | Time per 1000 voters |
|-----------|-------------------|----------------------|
| Initialization | Creates the elliptic Curve and private keys | 0.53s |
| Encryption | Encrypts the votes | 1.07s |
| Random Permutations | Creates random numbers | 0.01s |
| Proof | The shuffle | 5.91s |
| Verification | Verification of the shuffle | 8.00s |
| Decryption | Decrypts the votes | 0.89s |
| Total | total time ellapsed | 16.96 |

### <a name="hatshufflebplib"></a>EPBSA 17 - Python (bplib)

| Operation | Short Description | Time per 1000 voters |
|-----------|-------------------|----------------------|
| Initialization | Creates the elliptic Curve and private keys | 12.50s |
| Encryption | Encrypts the votes | 5.51s |
| Random Permutations | Creates random numbers | 0.01s |
| Proof | The shuffle | 17.48s |
| Verification | Verification of the shuffle | 31.70s |
| Decryption | Decrypts the votes | 3.15s |
| Total | total time ellapsed | 1:09.46 |

### <a name="totals"></a>Totals

| Votes | EPBSA 17 CPP | EPBSA 17 Python (bplib) | EPBSA 17 Python (libffpy) | SASGM 16 Python (libffpy) |
|-------|--------------|-------------------------|---------------------------|---------------------------|
| 1000 | 5.3457s | 48.7663s | 13.9521s |  |
| 10000 | 42.5985s |  | 2:20.3532m | 4:02:7634m |
| 100000 | 6:30.4583m |  | 23:24.4286m | 40:56.3743m |
