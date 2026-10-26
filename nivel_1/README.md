# PDV com Descontos (Nível 1)

## O que o código faz
Este programa simula a lógica de um Ponto de Venda (PDV) que aplica regras de descontos progressivos sobre compras. Ele recebe o valor da compra e a idade do cliente, calcula eventuais descontos por faixa etária e por valor total, registra o histórico das compras e, ao final, exibe um resumo consolidado do dia.

## Como ele faz
1. **Entrada e Validação:** Solicita o valor da compra e a idade do cliente. Se valores negativos forem digitados, o programa avisa o usuário e solicita a entrada novamente.
2. **Critério de Parada:** O loop de compras continua em execução até que o usuário digite `0` como valor da compra.
3. **Regra 1 (Desconto por Idade):** Se a idade do cliente for maior ou igual a 65 anos, aplica 20% de desconto sobre o valor da compra.
4. **Regra 2 (Desconto por Valor):** Se o valor obtido após o desconto da idade for estritamente maior que R$ 100,00, aplica mais 10% de desconto sobre esse valor já recalculado.
5. **Histórico:** Cada transação é adicionada a uma lista utilizando o método `.append()`.
6. **Resumo Final:** Ao encerrar com `0`, o programa itera sobre o histórico acumulado e exibe:
   - Quantidade total de compras registradas
   - Total bruto (soma dos valores originais)
   - Total de descontos concedidos
   - Total final a pagar (soma dos valores com desconto)

## Como rodar
Certifique-se de estar dentro da pasta `nivel_1` ou no diretório raiz do projeto:

```bash
cd nivel_1
python pdv.py
```

## Tabela de Casos de Teste

| Caso | Valor Compra (R$) | Idade | Desconto Idade (20%) | Valor pós-idade | Desconto Valor (10% se > 100) | Valor Final Esperado (R$) | Observações |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| 1 | 50.00 | 25 | Não | 50.00 | Não (<= 100) | R$ 50.00 | Sem descontos |
| 2 | 100.00 | 40 | Não | 100.00 | Não (não é > 100) | R$ 100.00 | Limite exato de 100 |
| 3 | 150.00 | 30 | Não | 150.00 | Sim (10%) | R$ 135.00 | Apenas desconto por valor |
| 4 | 80.00 | 70 | Sim (20%) | 64.00 | Não (<= 100) | R$ 64.00 | Apenas desconto por idade |
| 5 | 125.00 | 70 | Sim (20%) | 100.00 | Não (não é > 100) | R$ 100.00 | Caso-limite: 125 * 0.8 = 100 |
| 6 | 200.00 | 70 | Sim (20%) | 160.00 | Sim (10%) | R$ 144.00 | Ambos os descontos aplicados |
| 7 | 101.00 | 30 | Não | 101.00 | Sim (10%) | R$ 90.90 | Caso-limite: 101 * 0.9 = 90.90 |
| 8 | 50.00 | 65 | Sim (20%) | 40.00 | Não (<= 100) | R$ 40.00 | Idade limite exata (65 anos) |
| 9 | 100.00 | 65 | Sim (20%) | 80.00 | Não (<= 100) | R$ 80.00 | Idade limite exata (65 anos) |
| 10 | 200.00 | 64 | Não | 200.00 | Sim (10%) | R$ 180.00 | Caso-limite: 64 anos não tem desc. idade |

