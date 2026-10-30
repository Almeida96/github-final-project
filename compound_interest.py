"""Annual compounding example, originally authored by Upkar Lidder (IBM)."""

import argparse
import math
from decimal import Decimal, DecimalException, localcontext


def calculate(principal, years, rate):
    """Return principal, earned interest and final balance as Decimal values."""
    values = []
    for name, value, maximum in (("principal", principal, "1e12"),
                                 ("years", years, "1000"), ("rate", rate, "1000")):
        if isinstance(value, bool):
            raise ValueError(f"{name} must be a finite nonnegative number.")
        try:
            parsed = Decimal(str(value))
        except DecimalException as error:
            raise ValueError(f"Invalid {name}.") from error
        if not parsed.is_finite() or not 0 <= parsed <= Decimal(maximum):
            raise ValueError(f"{name} must be between 0 and {maximum}.")
        values.append(parsed)
    principal, years, rate = values
    try:
        with localcontext() as context:
            context.prec = 50
            amount = principal * (1 + rate / 100) ** years
            return {"principal": principal, "interest": amount - principal, "amount": amount}
    except DecimalException as error:
        raise ValueError("Calculation exceeds decimal precision limits.") from error


def compound_interest(p, t, r):
    """Compatibility function: the original API returns the final balance."""
    amount = float(calculate(p, t, r)["amount"])
    if not math.isfinite(amount):
        raise ValueError("Balance exceeds the compatibility API's float range; use calculate().")
    return amount


def main(argv=None):
    parser = argparse.ArgumentParser(description="Annual compound-growth arithmetic example.")
    parser.add_argument("--principal")
    parser.add_argument("--years")
    parser.add_argument("--rate")
    args = parser.parse_args(argv)
    try:
        result = calculate(
            args.principal if args.principal is not None else input("Principal: "),
            args.years if args.years is not None else input("Years: "),
            args.rate if args.rate is not None else input("Annual rate (%): "),
        )
        for name, value in result.items():
            print(f"{name.capitalize()}: {value:.2f}")
        return 0
    except (ValueError, EOFError) as error:
        parser.error(str(error))


if __name__ == "__main__":
    raise SystemExit(main())
