from api import cpf, cnpj, rg, cep_consulta

print ("                        ")
print ("========================")
print ("                   ")
print ("CRIADOR - MR NOBODY")
print ("TEAM - FSOCIETY")
print ("CANAL - MR NOBODY TERMUX")
print ("                        ")
print ("========================")
print("""
==================
1- Gerador de CPF
==================
2- Gerador de CNPJ
==================
3- Gerador de RG
==================
4- Consulta CEP
==================
   """)

menu = int(input('Digite uma opcao: '))

if menu == 1:
   quant = int(input('Quantidade de cpf: '))
   uf = input('Estado: \n')
   resposta = cpf(quant, uf)

if menu == 2:
   quant = int(input('Quantidade de CNPJ: \n'))
   resposta = cnpj(quant)

if menu ==3:
   quant = int(input('Quantidade de RG: \n'))
   resposta = rg(quant)

elif menu == 4:
     cep_entrada = input('Digite o CEP:')
     resposta = cep_consulta(cep_entrada)
else:
    print('Digite um valor valido: ')
