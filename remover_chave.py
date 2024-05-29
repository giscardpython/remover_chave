pessoa = {
'Nome':'Giscard Stephanou',
'Idade':49,
'Profissão':'Programador',
'Empresa':'SENAI',
'Gênero':'Masculino',
'Cidade':'Águas Claras'
}

# Se digitar uma chave inválida dá erro na execução
#del pessoa[input('Informe a chave que deseja excluir: ')]

# Se digitar uma chave inválida NÃO dá erro na execução
pessoa.pop(input('Informe a chave que deseja excluir: '), None)

# exibe os novos dados na tela
for chave in pessoa:
    print(f'{chave}: {pessoa.get(chave)}')