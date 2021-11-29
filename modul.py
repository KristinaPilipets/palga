def add_person ():
	""" добавление человека и зарплаты (готово)
	"""
	nimi=input("Siseta nimi: ")
	palga=input("Siseta palgad: ")
	with open("inimesed.txt", "a") as inimesed:
		inimesed.write(nimi+"\n")	
	with open("palgad.txt", "a") as palgad:
		palgad.write(palga+"\n")

def delete_person ():
	"""Удаление человека и зарплаты (готово)
	"""
	f=open("inimesed.txt", "r")
	inimesed=[]
	for stroka in f:
		inimesed.append(stroka.strip())
	f.close
	nimi=input("Siseta nimi: ")
	if nimi not in inimesed:
		print("Kas sa tahad добавить nimi ja palgad/?")
		c=input("Y = jah, N = ei")
		if c.upper=="Y":
			add_person()
		else:
			pass
	else:
		palgad=[]
		with open("palgad.txt", "r") as f1:
			for stro in f1:
				palgad.append(stro.strip())
		a=inimesed.index(nimi)
		inimesed.pop(a)
		palgad.pop(a)
	f=open("inimesed.txt", "w")
	for g in inimesed:
		f.write(g+"\n")
	f.close()
	d=open("palgad.txt", "w")
	for i in palgad:
		d.write(i+"\n")
	d.close()

def biggest_salary():
	"""Вычисление самой большой зарплаты (готово)
	"""
	palgad=[]
	with open("palgad.txt", "r") as f1:
		for stro in f1:
			palgad.append(stro.strip())
	f=open("inimesed.txt", "r")
	inimesed=[]
	for stroka in f:
		inimesed.append(stroka.strip())
	f.close
	palgadS=palgad.copy()
	palgadS.sort()
	palgadS.reverse()
	a=palgadS[0]
	b=palgad.index(a)
	print("kõike suured palga on "+inimesed[b]+" palga")

def smallest_salary():
	"""вычисление самой маленькой зарплаты (готово?)
	"""
	palgad=[]
	with open("palgad.txt", "r") as f1:
		for s in f1:
			palgad.append(s.strip())
	inimesed=[]
	with open ("inimesed.txt", "r") as inimene:
		for q in inimene:
			inimesed.append(q.strip())
	palgadS=palgad.copy()
	palgadS.sort()
	a=palgadS[0]
	b=palgad.index(a)
	print("kõike suured palga on "+inimesed[b]+" palga ja see on "+ palgadS[0]+" euro")

def sorting():
	"""сортировка зарполат с именами в порядке возрастания (готово)		p.s. чтобы сделать в порядке убывания добавить сточку palgadS.reverse() после palgadS.sort() 
	"""
	palgadS=[]
	palgad=[]
	with open("palgad.txt", "r") as f1:
		for s in f1:
			palgad.append(s.strip())
	inimesed=[]
	with open ("inimesed.txt", "r") as inimene:
		for q in inimene:
			inimesed.append(q.strip())
	palgadS=palgad.copy()
	palgadS.sort()
	for palk in palgadS:
		a=palgad.index(palk)
		print(palgad[a]+" "+inimesed[a])

def search_name():
	"""Поиск зарплаты по человеку (готово)
	"""
	palgad=[]
	with open("palgad.txt", "r") as f1:
		for s in f1:
			palgad.append(s.strip())
	inimesed=[]
	with open ("inimesed.txt", "r") as inimene:
		for q in inimene:
			inimesed.append(q.strip())

	nimi=input("Siseta nimi: ")
	for inimene in inimesed:
		if inimene==nimi:
			n=inimesed.count(nimi)
			b=0
			t=[]
			for i in range(n):
				k=inimesed.index(nimi,b)
				palk=palgad[k]
				b+=k+1
				t.append(nimi+" "+str(palk))
			print(t)
		else:
			print("nimi ei ole")

def tulumaks():
	"""Вычисление зарплвты с налогом(Готово)
	"""
	palgad=[]
	with open("palgad.txt", "r") as f1:
		for s in f1:
			palgad.append(s.strip())
	inimesed=[]
	with open ("inimesed.txt", "r") as inimene:
		for q in inimene:
			inimesed.append(q.strip())
	nimi=input("Siseta nimi keda palk te tahate arvutada: ")
	if nimi in inimesed:
		a=inimesed.index(nimi)
		b=palgad[a]
		b=float(b)
		if b<=1200:
			h=b-500
			if h==0 or h<0:
				ans="käes palk on "+str(round(b,2))
			else:
				d=h*0.2
				e=b-d
				ans="käes palk on"+str(round(e,2))
		elif b>=1200:
			e=500-0.55556*(b-1200)
			d=b-e
			c=d*0.2
			f=b-c	
			ans="käes palk on"+str(round(f,2))
		else:
			e=b*0.2
			a=b-e
			ans="käes palk on"+str(round(a,2))
		print(ans)