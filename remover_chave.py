pessoa = {
'Nome':'Giscard Stephanou',
'Idade':49,
'Profissão':'Programador',
'Empresa':'SENAI',
'Gênero':'Masculino',
'Cidade':'Águas Claras'
}
pessoa.pop(input('Informe a chave que deseja excluir: '), None)
# exibe os novos dados na tela
print(pessoa)