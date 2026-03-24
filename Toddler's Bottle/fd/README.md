# fd Challenge Writeup

## Challenge Overview

In this challenge, you are provided with SSH access to a remote machine. Upon connecting, you can see three files in the directory:

- `flag` — The file containing the flag (not readable with your current permissions)
- `fd` — An executable file
- `fd.c` — The source code for the executable (readable)

## Solution Steps

1. **Connect via SSH**
   - Use the provided SSH credentials to access the remote machine.

2. **Explore the Files**
   - Run `ls` to list the files. Notice the `flag`, `fd`, and `fd.c` files.
   - The `flag` file cannot be read directly due to permission restrictions.

3. **Read the Source Code**
   - Use `cat fd.c` to view the source code of the executable.
   - Analyzing the code reveals that the program checks input against the string `"LETMEWIN"`.
   - The program reads input from a file descriptor, which by default is not `STDIN`.

4. **Redirect Input to STDIN**
   - To make the program read from `STDIN`, you need to set the file descriptor variable `fd` to `0` (the value for `STDIN`).
   - The code sets `fd` to the value of the first argument minus `0x1234`.
   - Therefore, to make `fd` equal to `0`, you must provide `0x1234` (which is `4660` in decimal) as the argument.

5. **Run the Exploit**
   - Execute the program with the correct argument and provide the required input:
     ```sh
     ./fd 4660
     LETMEWIN
     ```
   - If the input is correct, the program will print the flag.

## Summary

By analyzing the source code and understanding how file descriptors work in Linux, you can redirect the program's input to `STDIN` by passing the correct argument. This allows you to provide the string `LETMEWIN` and receive the flag, successfully solving the challenge.
