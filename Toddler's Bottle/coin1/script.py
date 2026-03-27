from pwn import *

r = remote("127.0.0.1", 9007)

for round_num in range(100):
    try:
        r.recvuntil(b"N=")
        n_val = int(r.recvuntil(b" ", drop=True))

        r.recvuntil(b"C=")
        c_val = int(r.recvline().strip())

        print(f"Round {round_num + 1}: N={n_val}, C={c_val}")

        low = 0
        high = n_val - 1

        for _ in range(c_val):
            mid = (low + high) // 2

            search_range = range(low, mid + 1)
            payload = " ".join(map(str, search_range))

            r.sendline(payload.encode())

            response = r.recvline().decode().strip()

            if not response.isdigit():
                break

            weight = int(response)

            if weight % 10 != 0:
                high = mid
            else:
                low = mid + 1

        r.sendline(str(low).encode())

        feedback = r.recvline().decode().strip()
        if "Correct" not in feedback:
            print(feedback)

    except Exception as e:
        print(f"Error: {e}")
        break

print(r.recvall().decode())
