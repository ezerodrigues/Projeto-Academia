
from fpdf import FPDF


def imc (peso_i, altura_i):
    return peso_i / (altura_i ** 2)



nome = input ('Digite seu nome: ')
idade = input ('Digite a sua idade: ')
peso = float(input('Digite o seu peso: '))
altura = float(input ('Digite a sua altura: '))


calculo = imc(peso, altura)


# Criação do PDF

pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12)


# Adicionando texto ao PDF

pdf.text(10, 10, f'Nome: {nome}')
pdf.text(10, 20, f'Idade: {idade}')
pdf.text(10, 30, f'Peso: {peso} kg')
pdf.text(10, 40, f'Altura: {altura} m')
pdf.text(10, 50, f'IMC: {calculo:.2f}')



# Salvando o PDF

pdf.output("Ficha Aluno.pdf")
print("Dados gerados com sucesso!")