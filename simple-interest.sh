#!/bin/bash
# Simple interest calculator.
# Inputs: principal amount (p), annual interest rate in percent (r), and time in years (t).
# Formula: simple interest = p * r * t / 100

read -r -p "Enter the principal: " p
read -r -p "Enter rate of interest per year (%): " r
read -r -p "Enter time period in years: " t

if ! [[ $p =~ ^[0-9]+([.][0-9]+)?$ && $r =~ ^[0-9]+([.][0-9]+)?$ && $t =~ ^[0-9]+([.][0-9]+)?$ ]]; then
  echo "Error: enter non-negative numeric values." >&2
  exit 1
fi

awk -v p="$p" -v r="$r" -v t="$t" 'BEGIN { printf "The simple interest is: %.2f\n", p * r * t / 100 }'
