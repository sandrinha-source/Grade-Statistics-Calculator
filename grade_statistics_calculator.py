soma = 0 
for num in range (10):
    nota=float(input("Digite a nota do aluno(a): "))
    soma=soma+nota
    if num == 0:
        maior=nota
        menor=nota
    else:
        if nota > maior:
            maior=nota
        if nota < menor:
            menor=nota
                   
média=soma/10
 
print ("A soma de todas as notas é: " , soma)
print ("A média da turma é: " , média)
print ("A maior nota digitada é: " , maior)
print ("A menor nota digitada é: " , menor)
            