# Binary Code Sets and String Matching

A combinatorial solution to the problem of finding valid prefix-free binary code sets that can decode a given binary string into lowercase English letters.

---

## Overview

This project addresses a theoretical computer science problem involving binary codes and bijective mappings to the English alphabet. Given a binary string `T` (of length at most 100), the goal is to compute two values:

1. The number of distinct valid code sets `X` that can decode `T` into at least one valid string `S` of lowercase letters.
2. The number of distinct codes that appear in at least one such valid set `X`.

All results are reported modulo \(10^9 + 7\).

---

## Problem Definition

A code is a binary string of length at most 3. A set of codes `X` is considered **valid** if it satisfies the following conditions:

- It is non-empty
- Every code consists only of `0`s and `1`s
- No code is a prefix of another code (prefix-free property)
- There exists a one-to-one correspondence between the codes in `X` and the distinct letters in some string `S`

The task is to count all such valid sets that can successfully decode the input string `T`, as well as the total number of unique codes used across those sets.

---

## Approach

The solution is divided into four main stages:

### 1. Generating Valid Code Sets
All binary strings of length 1 to 3 are enumerated (14 codes in total). All non-empty subsets are generated and filtered to retain only those that are prefix-free. This preprocessing step is performed once.

### 2. Checking Decodability
For a given valid set `X` and input string `T`, a dynamic programming approach with bitmasks is used to determine whether `T` can be fully decoded using the codes in `X` under a bijective mapping to letters.

### 3. Counting Valid Mappings
The same DP framework is extended to count the number of distinct strings `S` that can be produced by a given code set. When handling multiple overlapping sets, the principle of inclusion is applied to avoid double-counting.

### 4. Collecting Unique Codes
After identifying all valid sets that successfully decode `T`, the distinct codes appearing in those sets are collected and counted.

---

## Project Structure

| File | Description |
|------|-------------|
| `project1.py` | First part of the implementation |
| `project2.py` | Second part of the implementation |
| `docs/` | Project documentation |

---

## Documentation

The full project description is available here:

[Project Documentation](docs/)

---

## Technical Notes

- The limited code length (≤ 3) results in a small search space of only 14 possible codes, making exhaustive enumeration feasible.
- Dynamic programming with bitmasks efficiently handles the assignment of codes to letters.
- All computations are performed under modulo \(1\,000\,000\,007\).
