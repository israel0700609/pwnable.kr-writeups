# Write-up: lotto

## Challenge Description

The challenge presents a simple Lotto game in C. We need to guess 6 numbers (bytes) in the range 1-45. If our guess matches all 6 numbers randomly drawn from /dev/urandom, the program prints the flag. The server notes the mathematical chance to win is 1 in 8,145,060.

## Vulnerability Analysis

The vulnerability is not in the randomness, but in how the program counts matches. Instead of comparing each index in the guess array to the corresponding index in the lotto array, the code uses a nested loop:

```c
int match = 0, j = 0;
for(i=0; i<6; i++){
	for(j=0; j<6; j++){
		if(lotto[i] == submit[j]){
			match++;
		}
	}
}
```

**Logical flaw:**
Because of this structure, if a number appears in `lotto[i]`, the program checks it against all six numbers we entered in `submit`. If all six of our submitted numbers are the same, a single match in the lotto array will increment `match` by 6 at once.

## Exploitation

Instead of trying to guess 6 different numbers (with almost no chance), we enter 6 identical values within the valid range (1-45).

For example, using the character `!` (ASCII value 33):

- We send: `submit = [33, 33, 33, 33, 33, 33]`.
- If the random lotto array contains 33 even once (in any position), the inner loop will count 6 matches and set `match` to 6 immediately.

**Probability change:**
The chance that at least one of 6 random numbers (in 1-45) is 33 is about 13%. This means, on average, we should win within 7-8 manual attempts.

## Manual Solution Steps

1. Run the program `./lotto`.
2. Choose option 1 in the menu.
3. Enter 6 identical characters from the lower ASCII range (e.g., `!!!!!!`).
4. Repeat until the lotto draw includes the value 33.
