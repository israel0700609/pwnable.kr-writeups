# Write-up: blackjack

## Challenge Description

The challenge presents a Blackjack game written in C. The goal is to reach a cash balance of over $1,000,000. Once the player crosses this threshold, the `cash_test` function reads the flag file and prints it to the screen. The player starts with only $500.

## Vulnerability Analysis

The main vulnerability is in the `betting()` function, which asks the user for the bet amount. The programmer tried to ensure the player cannot bet more money than they have, but the check is incomplete:

```c
int betting()
{
	printf("\n\nEnter Bet: $");
	scanf("%d", &bet);

	if (bet > cash)
	{
		printf("\nYou cannot bet more money than you have.");
		//...
		return bet;
	}
	else return bet;
}
```

**Logical flaw:**
The code checks if the bet is greater than the cash, but does not check if the bet is negative. In C, `bet` is an `int` (signed integer), so it can take negative values.

## Exploitation

The logic for updating the cash balance on a loss is:

```
cash = cash - bet;
```

If we enter a large negative number (e.g., `bet = -100000000`):

- **Bypassing the check:** The expression `(-100000000 > 500)` is false, so the program accepts the bet.
- **Mathematical manipulation:** If we intentionally lose the round, the program calculates:
  `500 - (-100000000) = 100000500`

## Getting the Flag

After a "deliberate" loss with a negative bet, the cash balance becomes millions. Immediately after, the `cash_test()` function is called:

```c
if (cash > 1000000) {
	FILE* fp = fopen("flag", "r");
    }
```

Since our new balance is much greater than a million, the condition is true and the server prints the flag.

## Summary

This challenge demonstrates the importance of full input sanitization. A small mistake in not checking the sign of the number turned a tough gambling game into a flag-dispensing ATM.
