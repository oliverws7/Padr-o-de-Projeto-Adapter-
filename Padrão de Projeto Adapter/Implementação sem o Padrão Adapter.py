# Serviço moderno de pagamento (Stripe)
class StripePayment:
    def make_payment(self, amount, currency, description):
        print(f"Processando pagamento via Stripe: {amount} {currency} - {description}")
        # Lógica real de processamento Stripe
        return "stripe_" + str(hash(f"{amount}{currency}{description}"))

# Serviço legado de pagamento bancário
class LegacyBankPayment:
    def pay(self, value, currency_code, payment_reason):
        print(f"Processando pagamento bancário legado: {value} {currency_code} - {payment_reason}")
        # Lógica real de processamento bancário
        return "bank_" + str(hash(f"{value}{currency_code}{payment_reason}"))

# Cliente que precisa usar ambos os serviços
class PaymentProcessor:
    def __init__(self):
        self.stripe = StripePayment()
        self.bank = LegacyBankPayment()
    
    def process_stripe_payment(self, amount, currency, description):
        return self.stripe.make_payment(amount, currency, description)
    
    def process_bank_payment(self, amount, currency, description):
        # Precisamos adaptar manualmente os parâmetros
        value = amount
        currency_code = currency.upper()
        payment_reason = description.upper()
        return self.bank.pay(value, currency_code, payment_reason)

# Uso
processor = PaymentProcessor()

# Processamento com Stripe (interface moderna)
stripe_result = processor.process_stripe_payment(100.50, "USD", "Compra de livro")
print(f"Resultado Stripe: {stripe_result}")

# Processamento com banco legado (interface diferente)
bank_result = processor.process_bank_payment(100.50, "USD", "Compra de livro")
print(f"Resultado Banco: {bank_result}")