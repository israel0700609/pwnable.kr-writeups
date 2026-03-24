# collision Challenge Writeup

## Challenge Overview

In this challenge, you are given SSH access to a remote server. Upon connecting, you find three files in the directory:

- `flag` — The file containing the flag (not directly readable)
- `col` — The executable file
- `col.c` — The source code for the executable

## Solution Steps

1. **Connect via SSH**
   - Use the provided SSH credentials to access the remote machine.

2. **Explore the Files**
   - Run `ls` to list the files. You will see `flag`, `col`, and `col.c`.

3. **Analyze the Source Code**
   - Use `cat col.c` to read the source code.
   - The code requires an argument (password) of exactly 20 bytes.
   - The sum of the 4-byte integers (interpreted from the 20 bytes) must equal the constant `hashcode = 0x21DD09EC`.

4. **Construct the Password**
   - To satisfy the condition, split the 20 bytes into five 4-byte integers.
   - If you use four integers with the value `0x01010101` (which is 16843009 in decimal), their sum is `0x04040404`.
   - Subtract this from `0x21DD09EC` to get the value for the fifth integer:
     $$
     0x21DD09EC - 0x04040404 = 0x1DD905E8
     $$
   - So, the password should be 16 bytes of `0x01` and the last 4 bytes as `0x1DD905E8` (in little-endian order).

5. **Run the Exploit**
   - Use the following command to generate and pass the correct password:
     ```sh
     ./col "$(python3 -c "import sys; sys.stdout.buffer.write(b'\x01' * 16 + b'\xe8\x05\xd9\x1d')")"
     ```
   - This will provide the correct input and the program will print the flag.

## Summary

By analyzing the source code and understanding how the password is validated, you can construct the required 20-byte input to satisfy the hashcode check and obtain the flag.
