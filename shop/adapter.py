
"""Implement the Adapter(s) so our app can speak to 3rd-party SDKs.

Goal: Make StripeAPI and PayPalClient usable via the PaymentProcessor interface without
changing the app code in app.checkout.
"""
from .payments import PaymentProcessor
from .third_party_providers import StripeAPI, PayPalClient

class StripeAdapter(PaymentProcessor):
    """Adapt StripeAPI(charge amount_cents) -> dict to PaymentProcessor(pay amount_eur) -> str."""
    def __init__(self, client: StripeAPI):
        self.client = client

    def pay(self, amount: float) -> str:
        result = self.client.charge(int(amount * 100))
        amount = float(result.get("amount_cents", 0))/100
        if not result.get("ok"):
            raise RuntimeError("Stripe charge failed")
        return f"paid {amount:.2f} EUR via Stripe ({self.client.merchant_id})"

class PayPalAdapter(PaymentProcessor):
    """Adapt PayPalClient(make_payment total: float) -> (bool, total) to PaymentProcessor interface."""
    def __init__(self, client: PayPalClient):
        self.client = client

    def pay(self, amount: float) -> str:
        success, total_paid = self.client.make_payment(amount)
        if not success:
            raise RuntimeError("PayPal payment failed")
        return f"paid {total_paid:.2f} EUR via PayPal ({self.client.account_email})"
