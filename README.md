# Interest arithmetic exercises

A fork of IBM's **Introduction to Git and GitHub** final project. The original compound-growth example is credited to Upkar Lidder; this fork adds input validation, tests and an explicit distinction between interest earned and final balance.

## Run

The Python example requires Python 3.11+. It supports prompts or arguments:

```sh
python compound_interest.py --principal 1000 --years 2 --rate 10
```

```text
Principal: 1000.00
Interest: 210.00
Amount: 1210.00
```

The annual rate is a percentage, so `10` means 10%. The formula is `amount = principal × (1 + rate / 100) ^ years`. Interest is `amount − principal`. The legacy function named `compound_interest` continues to return the final balance for compatibility; new callers should use `calculate`.

For the separate Bash simple-interest exercise:

```sh
bash simple-interest.sh
```

Enter the principal, annual rate, and number of years when prompted. The calculator accepts decimal inputs.
It uses `principal × rate × years / 100` and requires Bash and awk.

## Limits

These are educational calculations, without payments, fees, taxes or changing rates. Inputs must be finite and nonnegative. The Python example bounds principal to 10¹² and years/rate to 1,000. Decimal arithmetic is used internally; terminal results display two decimal places.

## Development

```sh
python -m unittest discover -s tests -v
```

Tests check worked examples, decimal input, invalid values, compatibility and CLI exits. The inherited workflow that automatically closed every PR was removed so contributions can be reviewed.

[Contribution guide](CONTRIBUTING.md) · [Code of conduct](CODE_OF_CONDUCT.md) · [Apache 2.0 license](LICENSE)
