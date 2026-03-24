# Challenge: <challenge_name>

## Challenge Description

- Tier:
- Challenge URL:
- Objective:
- Initial observations:

## Security Protections (Checksec)

```bash
checksec --file=./<binary_name>
```

Example output:

```text
RELRO           STACK CANARY      NX            PIE             RPATH      RUNPATH      Symbols
Full RELRO      Canary found      NX enabled    PIE enabled     No RPATH   No RUNPATH   85 Symbols
```

Interpretation:

- RELRO:
- Canary:
- NX:
- PIE:

## Analysis

### Static Analysis

- Tools used (file, strings, objdump, ghidra, ida, rizin):
- Key functions and control flow:
- Vulnerable code path:

### Dynamic Analysis

- Runtime setup:
- Breakpoints and memory observations:
- Crash behavior and offsets:

## Exploitation Strategy

- Vulnerability class:
- Primitive gained (read/write/leak/control-flow hijack):
- Bypass strategy for mitigations:
- Step-by-step exploit plan:

## Final Code

```python
# Paste final exploit or reference exploit.py in this directory.
```

## Post-Exploitation Notes

- Reliability considerations:
- Lessons learned:
- Defensive remediation suggestions:
