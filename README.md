# Cálculos de Erlang para Call Centers

Este projeto em Python realiza cálculos de Erlang essenciais para a operação e planejamento de call centers. As fórmulas de Erlang ajudam a determinar a probabilidade de filas, níveis de serviço e o número necessário de agentes, permitindo uma gestão eficiente dos recursos.

## Funcionalidades

# O projeto inclui cálculos para:
- **Erlang C**: Calcula a probabilidade de uma chamada aguardar em fila.
- **Erlang B**: Calcula a probabilidade de uma chamada ser bloqueada devido a todos os canais estarem ocupados.
- **Service Level**: Calcula o nível de serviço com base na fórmula de Erlang C.
- **Agents**: Determina a quantidade de agentes necessários para atingir um nível de serviço específico.

## Usos Operacionais e de Planejamento

### Erlang C

A fórmula de Erlang C é usada para calcular a probabilidade de chamadas aguardarem em fila quando todos os agentes estão ocupados. Isso é fundamental para prever tempos de espera e ajustar o número de agentes disponíveis.

### Erlang B

A fórmula de Erlang B calcula a probabilidade de bloqueio de chamadas, importante para dimensionar corretamente a capacidade do sistema e garantir que os clientes não encontrem linhas ocupadas.

### Nível de Serviço

O cálculo do nível de serviço permite determinar a porcentagem de chamadas atendidas dentro de um tempo especificado, uma métrica crítica para medir a eficácia e a satisfação do cliente.

### Número de Agentes

Determinar o número correto de agentes é essencial para balancear os custos operacionais com a qualidade do serviço. Este projeto usa a fórmula de Erlang C para calcular a quantidade necessária de agentes para atingir um nível de serviço desejado.

## Como Usar

### Pré-requisitos

- Python 3.x
- Bibliotecas: math

### Instalação

- Clone este repositório em sua máquina local
- Importe a classe ErlangCalculations no seu script e utilize os métodos disponíveis

[Exemplo de uso]()
