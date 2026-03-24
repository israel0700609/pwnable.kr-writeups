# pwnable.kr Writeups

A professionally organized repository of pwnable.kr challenge writeups focused on binary exploitation, reverse engineering, and practical offensive security techniques.

## Repository Goals

- Document a repeatable methodology for solving CTF pwn challenges.
- Track progression from foundational exploitation to advanced techniques.
- Build a clean portfolio for security research and interview discussions.

## Tier Layout

- Toddler's Bottle
- Rookiss
- Grotesque
- Hacker's Secret

## Skills Learned

- Linux process internals and memory layout
- Stack-based and heap-based exploitation fundamentals
- Return-oriented programming (ROP)
- Dynamic analysis with gdb, pwndbg, and runtime tracing
- Mitigation bypass concepts (NX, PIE, Canary, RELRO)
- pwntools automation for reliable exploit development
- Payload staging and debugging workflows

## Progress Tracker

| Challenge Name | Tier | Difficulty | Link to Writeup |
|---|---|---|---|
| fd | Toddler's Bottle | Easy | [Writeup](./Toddler's%20Bottle/fd/README.md) |
| collision | Toddler's Bottle | Easy | [Writeup](./Toddler's%20Bottle/collision/README.md) |
| bof | Toddler's Bottle | Easy | [Writeup](./Toddler's%20Bottle/bof/README.md) |
| passcode | Rookiss | Medium | [Writeup](./Rookiss/passcode/README.md) |
| brainfuck | Rookiss | Medium | [Writeup](./Rookiss/brainfuck/README.md) |
| coin1 | Grotesque | Medium | [Writeup](./Grotesque/coin1/README.md) |
| rsa_calculator | Hacker's Secret | Hard | [Writeup](./Hacker's%20Secret/rsa_calculator/README.md) |

> Update this table as you complete each challenge.

## Suggested Workflow

1. Create a folder for the challenge inside its tier.
2. Copy the template files from that tier's `_template` directory.
3. Record checksec output, analysis notes, and exploitation steps.
4. Add tested exploit code and remediation insights.
