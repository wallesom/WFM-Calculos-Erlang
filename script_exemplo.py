from wfm import ErlangCalculations

calc = ErlangCalculations()

# Exemplo de uso:
# Calcular a probabilidade de uma chamada aguardar em fila
prob_fila = calc.erlang_c(10, 5)
print("Probabilidade de aguardar em fila:", prob_fila)

# Calcular a probabilidade de uma chamada ser bloqueada
prob_bloqueio = calc.erlang_b(5, 10)
print("Probabilidade de bloqueio:", prob_bloqueio)

# Calcular o nível de serviço
nivel_servico = calc.service_level(prob_fila, 5, 10, 60, 300)
print("Nível de serviço:", nivel_servico)

# Calcular a quantidade de agentes necessários
agentes_necessarios = calc.agents(10, 90.0, 300)
print("Agentes necessários:", agentes_necessarios)
