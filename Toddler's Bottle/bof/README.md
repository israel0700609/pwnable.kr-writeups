# bof Challenge Writeup

## Challenge Overview

In this challenge, you are given SSH access to a remote server. Upon connecting, you find three files in the directory:

- `flag` — The file containing the flag (not directly readable)
- `bof` — The executable file
- `bof.c` — The source code for the executable

## Solution Steps

1. **Connect via SSH**
	- Use the provided SSH credentials to access the remote machine.

2. **Explore the Files**
	- Run `ls` to list the files. You will see `flag`, `bof`, and `bof.c`.

3. **Read the Service Info**
	- Use `cat README` to see that a service is running on port 9000, which receives input and runs the `bof` program with the provided input.

4. **Analyze the Source Code**
	- Use `cat bof.c` to read the source code.
	- The code uses the unsafe `gets` function to read input into a buffer, allowing for a buffer overflow.
	- The goal is to overwrite the `key` variable on the stack, which is located just after the buffer.

5. **Debug and Find the Offset**
	- Use a debugger to set breakpoints at the call to `gets` and at the start of the vulnerable function.
	- Run the program and determine the offset needed to overwrite `key`.
	- It is found that 52 bytes of junk, followed by the value `cafebabe` (in little-endian), will overwrite `key` as desired.

6. **Craft the Exploit**
	- Use the following command to generate the payload and send it to the service:
	  ```sh
	  (python3 -c "import sys; sys.stdout.buffer.write(b'A'*52 + b'\xbe\xba\xfe\xca')") | nc 0 9000
	  ```
	- This sends 52 dummy bytes followed by the string `cafebabe` in little-endian format, overwriting `key`.

7. **Get the Flag**
	- If successful, you will get a shell as a user with permission to read the `flag` file.
	- Use `cat flag` to print the flag.

## Summary

By exploiting a buffer overflow vulnerability in the use of `gets`, you can overwrite the `key` variable on the stack and gain access to the flag.
