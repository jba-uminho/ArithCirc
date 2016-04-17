# -*- coding: utf-8 -*-
#split(' ', 1) faz split com o caracter ' ' mas só 1 vez!

#######produzir os polinomios
#print P.lagrange_polynomial([(0,0),(2,4)]) % construirT([1,2,3])
#print P.lagrange_polynomial([(0,0),(2,4)]) % P.lagrange_polynomial([(0,0),(1,1)])


#from aux import * # importar tudo que esta no ficheiro aux.py
from sage.all import * # importar tudo do sage


def construirT(listaRaizes):
	x = var('x')
	t = 0
	t = prod((x - ri) for ri in listaRaizes)
	return t


def construirConjPolinomios(ops,V,W,Y,nRaizes):
	contaRaiz = 0 #diz-nos qual gate de mutiplicacao (raiz) estamos
	contaOps = 0 # conta operaçoes de input e multiplicacao,diz-nos qual operacao estamos (input,mult)

	#neste momento este for esta a produzir o Y, o conjunto de polinomios de saida das gates de mutiplicacao
	for i in range(0,len(ops)):
		if ops[i].split(' ', 1)[0] == "input":
			aux = []
			for j in range (0,nRaizes):
				aux.append((j+1,0))

			Y[contaOps] = P.lagrange_polynomial(aux)
			contaOps += 1

		elif ops[i].split(' ', 1)[0] == "mult":
			contaRaiz += 1

			aux = []
			for j in range (0,nRaizes):
				if j+1 == contaRaiz:
					aux.append((contaRaiz,1))
				else:
					aux.append((j+1,0))

			Y[contaOps] = P.lagrange_polynomial(aux)
			contaOps += 1
	return Y



#conjunto de polinomios
V = []
W = []
Y = []

P = PolynomialRing(QQ, 'x')

Zn = IntegerModRing(111) 
condicao = True # condicao do ciclo que vai receber as linhas de texto do ficheiro
outPut = None # se no fim outPut for None então algo correu mal ou entao nao foi encontrada a operacao output

ops = [] # vetor que guarda as operaçoes vindas do ficheiro (operaçoes são: input x,add x y,mult x y)
valores = [] # valores de todas as operacoes
C = [] # valores dos inputs e dos resultados das multiplicacoes, ira ser usado na construcaao do polinomio p
nRaizes = 0

try:
	strLida = raw_input()
	ops.append(strLida)
	while condicao :
		# [0] = "input"            [1] = valor do input
		if strLida.split(' ', 1)[0] == "input":
			# vai buscar o valor do input e passa para inteiro
			valores.append(int(strLida.split(' ', 1)[1]))
			C.append(int(strLida.split(' ', 1)[1]))

			# colocamos '#' para ir preenchendo as posicoes dos vetores para mais tarde poder usar os indices desses vetores e colocar lá o respectivo polinomio 
			V.append('#')
			W.append('#')
			Y.append('#')

			strLida = raw_input()
			ops.append(strLida)
		elif strLida.split(' ', 1)[0] == "add":
			# (ex "add 1 2" soma o que esta na posicao 0 com o da posicao 1 do vetor valores e faz o correspontende modulo) 
			valores.append(Zn(valores[int(strLida.split(' ', 2)[1]) -1] + valores[int(strLida.split(' ', 2)[2]) -1]))
			strLida = raw_input()
			ops.append(strLida)
		elif strLida.split(' ', 1)[0] == "mult":
			nRaizes += 1 
			# (ex "mult 1 2" mutiplica o que esta na posicao 0 com o da posicao 1 do vetor valores e faz o correspontende modulo) 
			valores.append(Zn(valores[int(strLida.split(' ', 2)[1]) -1] * valores[int(strLida.split(' ', 2)[2]) -1]))
			C.append(Zn(valores[int(strLida.split(' ', 2)[1]) -1] * valores[int(strLida.split(' ', 2)[2]) -1]))

			V.append('#')
			W.append('#')
			Y.append('#')

			strLida = raw_input()
			ops.append(strLida)
		elif strLida.split(' ', 1)[0] == "output":
			outPut = valores[int(strLida.split(' ', 2)[1]) -1]
			condicao = False
		else:
			print "Operacao nao conhecida (operacao recebida do ficheiro nao e input,add, ou mult)"
			condicao = False
except EOFError:
	pass # se der esta exepçao EOF ele vai continuar e ignorar


#contruir a lista de raizes, caso tenha 2 raizes por exemplo esta lista tera os elementos [1,2],servira para contruir o polinomio t
listaRaizes = []
for i in range(0,nRaizes):
	listaRaizes.append(i+1)

print ops
print valores
print C
print "outPut = " + str(outPut)

print nRaizes
print construirT(listaRaizes)

print V,W,Y

print construirConjPolinomios(ops,V,W,Y,nRaizes)

