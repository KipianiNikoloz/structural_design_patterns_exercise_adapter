# Python Adapter Pattern Exercise

## Context

Our app (`shop.app.checkout`) expects a `PaymentProcessor` with a `pay(amount: float) -> str` method.
Unfortunately, two third‑party SDKs (`StripeAPI` and `PayPalClient`) expose *different* interfaces.
Your task is to write **adapters** so the app can use those SDKs without any changes to the app code.

## What you implement

Edit `shop/adapter.py` and implement:

- `StripeAdapter.pay`
- `PayPalAdapter.pay`

### Requirements

- Pay method should return a string like: `"paid 12.34 EUR via <processor> (<transaction_id>)"`
- Transaction id is account email for Paypal.
- Transaction id is merchant id for Stripe.

## Run tests

```bash
pip install pytest
pytest -q
```

All tests are in `tests/test_adapter.py`. They currently fail until you implement the adapters.

## Hints

- Stripe expects integer cents; convert 12.34 EUR -> 1234 (round to nearest cent).
- Format the returned receipt strings to exactly two decimals.
- Keep the app code (`shop/app.py`) unchanged to demonstrate the Adapter idea.
