#!/usr/bin/env bash
set -e

gcc -Wall -Wextra -std=c11 src/complete_subarrays.c src/main.c -o complete_subarrays

echo "Build Successful"
echo
echo "Running example:"
./complete_subarrays
