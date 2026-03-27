# Write-up: mistake

## Challenge Description

The goal is to read the `flag` file, but we do not have direct permissions to access it. The program `mistake` compares a password stored in a file on the server with user input. If the input matches, it prints the flag.

## Vulnerability Analysis

The main vulnerability is a syntax error in the file opening line:
```c
if(fd=open("/home/mistake/password",O_RDONLY,0400) < 0)
```
In C, the comparison operator `<` has higher precedence than the assignment operator `=`.

- The program first executes the `open` call. If successful, it returns a positive file descriptor (e.g., 3).
- Then, it evaluates the comparison: `3 < 0`, which is false (0 in C).
- The value 0 is then assigned to the variable `fd`.

On Linux, file descriptor 0 is standard input (stdin). As a result, the subsequent call to `read(fd, pw_buf, PW_LEN)` reads from stdin instead of the password file, allowing us to inject any password we want.

## Exploitation

Since `fd` is set to 0 (stdin), we can provide any input as the password. The program then asks for another input via `scanf` and performs an XOR operation with the value 1 (`XORKEY`). To pass the check:

1. **First input (read):** Provide any string (e.g., `cccccccccc`).
2. **Second input (scanf):** Provide a string that, after XOR with 1, matches the first input.

In ASCII, the character 'b' (98) and 'c' (99) differ only in the least significant bit. Therefore:

$$
'b' \oplus 1 = 'c'
$$

So, if the first input is `cccccccccc`, the second input should be `bbbbbbbbbb`.

## Solution

1. When prompted for the password, enter:
	```
	cccccccccc
	```
2. When prompted for the second input, enter:
	```
	bbbbbbbbbb
	```
3. The program will print the flag.
