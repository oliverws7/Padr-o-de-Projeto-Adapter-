# Padrão de Projeto Adapter - Sistema de Pagamentos

Este projeto demonstra a aplicação do padrão de projeto Adapter através de um sistema de processamento de pagamentos que integra serviços modernos e legados.

## 📌 Visão Geral

O sistema ilustra duas abordagens para integrar interfaces incompatíveis:
1. **Implementação direta** (sem Adapter) - com acoplamento alto e adaptação manual
2. **Implementação com Adapter** - usando o padrão para encapsular a conversão de interfaces

## 🛠️ Estrutura do Projeto

adapter-pattern/
│
├── without_adapter.py # Implementação sem o padrão Adapter
├── with_adapter.py # Implementação utilizando o padrão Adapter
└── README.md # Este arquivo


## 🔧 Como Executar

1. Clone o repositório:
```bash
git clone https://github.com/oliverws7/adapter-pattern.git

Execute os exemplos:

python without_adapter.py
python with_adapter.py

📋 Cenário Implementado
O sistema processa pagamentos usando:

Serviço moderno: Stripe (StripePayment)

Serviço legado: Sistema bancário tradicional (LegacyBankPayment)

As interfaces possuem diferenças significativas:

# Interface moderna
make_payment(amount, currency, description)

# Interface legada
pay(value, currency_code, payment_reason)

⚖️ Análise Comparativa
Critério	Sem Adapter	Com Adapter
Clareza	Lógica de adaptação no cliente	Adaptação encapsulada
Acoplamento	Alto	Baixo
Manutenção	Complexa (alterações dispersas)	Fácil (mudanças localizadas)
Extensibilidade	Requer modificar cliente	Novo adapter = zero mudanças cliente
Reuso	Código duplicado	Lógica de adaptação reutilizável
🎯 Benefícios do Padrão Adapter
✅ Isola o código de adaptação

✅ Permite integração sem modificar código existente

✅ Facilita testes unitários

✅ Reduz impacto de mudanças

✅ Segue o Princípio SOLID (OCP)

📚 Padrões Relacionados
Bridge: Separa abstração de implementação

Facade: Fornece interface simplificada

Decorator: Adiciona responsabilidades dinamicamente

✉️ Contato
Para dúvidas ou sugestões: seu.email@mateusoliveiranunes2@gmail.com

