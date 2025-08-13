# Interfaces existentes (mesmas do exemplo anterior)
class StripePayment:
    def make_payment(self, amount, currency, description):
        print(f"Processando pagamento via Stripe: {amount} {currency} - {description}")
        return "stripe_" + str(hash(f"{amount}{currency}{description}"))

class LegacyBankPayment:
    def pay(self, value, currency_code, payment_reason):
        print(f"Processando pagamento bancário legado: {value} {currency_code} - {payment_reason}")
        return "bank_" + str(hash(f"{value}{currency_code}{payment_reason}"))

# Interface alvo que queremos usar
class PaymentTarget:
    def pay(self, amount, currency, description):
        pass

# Adapter para o Stripe (não é estritamente necessário, mas mantemos para consistência)
class StripeAdapter(PaymentTarget):
    def __init__(self, stripe_payment):
        self.stripe = stripe_payment
    
    def pay(self, amount, currency, description):
        return self.stripe.make_payment(amount, currency, description)

# Adapter para o sistema bancário legado
class BankAdapter(PaymentTarget):
    def __init__(self, bank_payment):
        self.bank = bank_payment
    
    def pay(self, amount, currency, description):
        # Adaptação da interface
        value = amount
        currency_code = currency.upper()
        payment_reason = description.upper()
        return self.bank.pay(value, currency_code, payment_reason)

# Cliente que usa apenas a interface unificada
class PaymentProcessor:
    def __init__(self, payment_service):
        self.payment_service = payment_service
    
    def process_payment(self, amount, currency, description):
        return self.payment_service.pay(amount, currency, description)

# Uso
stripe_adapter = StripeAdapter(StripePayment())
bank_adapter = BankAdapter(LegacyBankPayment())

# Processamento com Stripe via adapter
stripe_processor = PaymentProcessor(stripe_adapter)
stripe_result = stripe_processor.process_payment(100.50, "USD", "Compra de livro")
print(f"Resultado Stripe (via adapter): {stripe_result}")

# Processamento com banco via adapter
bank_processor = PaymentProcessor(bank_adapter)
bank_result = bank_processor.process_payment(100.50, "USD", "Compra de livro")
print(f"Resultado Banco (via adapter): {bank_result}")