# Write-up: coin1

## Challenge Description

We participate in a game: we must find one fake coin among N coins, using a balance and only C weighings.

- Real coin: weighs 10.
- Fake coin: weighs 9.
- Constraint: We must solve 100 such rounds within 60 seconds.

## The Problem

It is impossible to solve the challenge manually. The pace requires less than 0.6 seconds per round (including calculations, input, and output). The solution must be fully automated.

## Strategy: Binary Search

Since the weight of a group of real coins will always end with 0 (K×10), and a group containing the fake coin will end with 9, we can use binary search to eliminate half the coins in each weighing:

1. Split the range of coins into two halves.
2. Weigh the first half (indices 0 to mid).
3. If the result is not divisible by 10 (`result % 10 != 0`), the fake coin is in this half.
4. Otherwise, it is in the other half.

This algorithm guarantees finding the fake coin in log₂(N) steps, which matches the value of C provided by the server.

## Exploitation and Automation

The solution is written in Python using the pwntools library to manage communication with the port.

Technical highlights:

- **Networking:** Connect to 127.0.0.1 (localhost) from the SSH server itself to minimize network latency. Running from a personal computer would fail due to the time limit.
- **Parsing:** Extract N and C from the server's text using `recvuntil` and `split`.
- **I/O:** Send a space-separated list of indices at each step of the binary search.

## Solution Steps

1. Connect to the challenge server via SSH.
2. Write a Python script in the `/tmp` directory (where write permissions exist).
3. Run the script to perform 100 rounds of binary search against port 9007.
4. Receive the flag after the 100th round.
