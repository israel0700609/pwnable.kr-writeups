# Write-up: input2

## Challenge Description

This challenge presents a C program divided into 5 stages. To get the flag, we must pass all stages in sequence. Each stage checks a different way a program can receive input from the outside world: arguments, standard I/O, environment variables, files, and network.

## Stage Analysis and Solution

### Stage 1: Arguments (argv)

The program checks three conditions on the argv array:

- The number of arguments (argc) must be exactly 100.
- `argv['A']` (index 65) must be an empty string (`\x00`).
- `argv['B']` (index 66) must contain the bytes: space, newline, and carriage return.

**Solution:** Create a list of 100 strings in Python, setting the exact values at indices 65 and 66.

### Stage 2: Standard I/O (stdio)

The program tries to read 4 bytes from stdin (FD 0) and another 4 bytes from stderr (FD 2).
**Challenge:** Normally, stderr is used for output only.

**Solution:** Use pipes. Create two pipes with `os.pipe()`, write the required data to them, and attach their read ends to the program's FDs using `subprocess.Popen`.

### Stage 3: Environment Variables (env)

The program uses `getenv` to look for an environment variable named with the bytes `\xde\xad\xbe\xef`.

**Solution:** Create a dictionary of environment variables. Since both name and value are raw bytes, use the `b"..."` format in Python to avoid Unicode issues.

### Stage 4: Files (file)

The program tries to open a file named `\x0a` (newline) and checks if it contains 4 null bytes.

**Solution:** Create a physical file in the working directory with the required name and content before running the program.

### Stage 5: Network (network)

The program opens a server socket and waits for a connection on the port specified in `argv[67]`.

**Solution:** After starting the program, the script waits a second (to ensure the server is up), connects to 127.0.0.1 on the correct port, and sends the bytes `\xde\xad\xbe\xef`.


## Summary

This challenge demonstrates that pwn is not just about finding bugs in code, but also about manipulating the operating system environment to your advantage. Combining Python with Linux system functions is a powerful tool for any security researcher.
