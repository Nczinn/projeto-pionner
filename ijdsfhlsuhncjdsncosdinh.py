print('Média dos capetinhas("alunos")')

nota1 = float(input('Insira a nota do primeiro bimestre: '))

nota2 = float(input('Insira a nota do segundo bimestre: '))

nota3 = float(input('Insira a nota do terceiro bimestre: '))

nota4 = float(input('Insira a nota do quarto bimestre: '))

media = (nota1 + nota2 + nota3 + nota4)/ 4
print(f'A média do aluno é: {media}')
if media >= 5:
    print(f'Parabéns você foi aprovado!!')
else:
    print(f'Você está reprovado!!')