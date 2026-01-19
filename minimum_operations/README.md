# Minimum Operations

## Description
This project contains a solution to the "Minimum Operations" problem. Given a text file with a single character 'H', and only two operations (Copy All and Paste), the task is to calculate the minimum number of operations needed to get exactly n 'H' characters.

## Problem
Starting with one 'H', you can only:
- Copy All: Copy all characters currently in the file
- Paste: Paste the last copied content

## Algorithm
The solution uses prime factorization. The minimum number of operations equals the sum of all prime factors of n.

## Files
- `0-minoperations.py`: Contains the minOperations function
- `0-main.py`: Test file

## Usage
```bash
./0-main.py
```

## Author
- Your Name
