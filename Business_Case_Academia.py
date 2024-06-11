
import pdf_reports


nome = input ('Digite seu nome: ')
idade = input ('Digite a sua idade: ')
peso = float(input('Digite o seu peso: '))
altura = float(input ('Digite a sua altura: '))


imc = float(peso) / (float(altura) ** 2)

status = 'dentro do peso'

if imc > 25:
    status = "sobrepeso"

dados_aluno = {
    "nome" : nome,
    "idade" : idade,
    "peso" : peso,
    "altura": altura,
    "imc" : round(imc, 2),
    "status" : status
}

template = pdf_reports.pug_to_html("template.pug", dados = dados_aluno)

pdf_reports.write_report(template, "ficha_aluno.pdf", use_default_styling=False)
