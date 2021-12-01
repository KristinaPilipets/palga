def lists()->list:
	"""Из файла делаем список/tegi listid failist
	"""
	palgad=[]
	with open("palgad.txt", "r") as f1: #avame fail
		for s in f1:
			palgad.append(s.strip()) # tegi listid
	inimesed=[]
	with open ("inimesed.txt", "r") as inimene:
		for q in inimene:
			inimesed.append(q.strip())
	return palgad,inimesed

def add_person ():
	""" добавление человека и зарплаты (готово)
	"""
	nimi=input("Siseta nimi: ")
	palga=input("Siseta palgad: ")
	with open("inimesed.txt", "a") as inimesed: #Добавляем человека в конец файла/lisame nimi failisse 
		inimesed.write(nimi+"\n")	
	with open("palgad.txt", "a") as palgad: #Добавляем зарплату в конец файла/lisame palk failisse
		palgad.write(palga+"\n")

def delete_person ():
	"""Удаление человека и зарплаты (готово)
	"""
	palgad,inimesed=lists() #открытие файлов и использывание списка через функцию/ avame failid ja kasutamine lsitid 
	nimi=input("Siseta nimi: ")
	if nimi not in inimesed: #проверка есть ли такой человек в списке
		print("Kas sa tahad lisada nimi ja palgad?") #если нет предлагаем зарегестрировать/добавить имя и зарплату
		c=input("Y = jah, N = ei")
		if c.upper=="Y":
			add_person() #перенаправляем в функцию добавления 
		else:
			pass
	else:
		a=inimesed.index(nimi) # если имя есть в списке ищем индекс 
		inimesed.pop(a) #удаляем по индексу имя
		palgad.pop(a) #удаляем по индексу
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
	palgad,inimesed=lists()
	suurim=max(palgad) # поиск и прирвынивание самого большого числа к переменной
	b=palgad.index(suurim) # приравниваем индекс к переменной для дальнейшего использывания
	print("kõike suured palga on "+inimesed[b]+" palga")

def smallest_salary():
	"""вычисление самой маленькой зарплаты (готово)
	"""
	palgad,inimesed=lists()
	palgadS=palgad.copy()
	palgadS.sort()
	a=palgadS[0]
	b=palgad.index(a)
	print("kõike väiksem palga on "+inimesed[b]+" palga ja see on "+ palgadS[0]+" euro")

def sorting():
	"""сортировка зарполат с именами в порядке возрастания (готово)
	"""
	palgadS=[]
	palgad,inimesed=lists()
	palgadS=palgad.copy()
	palgadS.sort()
	for palk in palgadS:
		a=palgad.index(palk) # ищем индекс по переменной и приравниваем к другой переменной чтобы найти имя и зарплату в несортированых списках
		print(palgad[a]+" "+inimesed[a])

def same_salary():
	"""поиск людей с одинаковой зарплатой (не готово тк два раза записывает одно и то же)
	"""
	palgad,inimesed=lists()
	t=[]
	for palk in palgad:
		n=palgad.count(palk)
		b=0
		if n==0 or n==1:
			pass
		else:
			for i in range(n):
				k=palgad.index(palk,b)
				nimi=inimesed[k]
				b+=k+1
				t.append(nimi+" "+str(palk))
	print(t)

def search_name():
	"""Поиск зарплаты по человеку (готово)
	"""
	palgad,inimesed=lists()
	nimi=input("Siseta nimi: ")
	t=[]
	for inimene in inimesed:
		if inimene==nimi:
			n=inimesed.count(nimi)
			b=0
			for i in range(n):
				k=inimesed.index(nimi,b)
				palk=palgad[k]
				b+=k+1
				t.append(nimi+" "+str(palk))
		else:
			pass
	print(t)
def tulumaks():
	"""Вычисление зарплвты с налогом(Готово)
	"""
	palgad,inimesed=lists()
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

def keskmine():
	"""
	"""
	palgad,inimesed=lists()
	summa=0
	for palk in palgad:
		summa+=float(palk)
	kesk=summa/len(palgad)#вычисляем среднюю зарплату
	print("keskmine palk "+kesk)
	vahe=0
	if kesk in palgad:
		kesk=inimesed[palgad.index(kesk)]
		print(kesk)
	else:
		kesk="puudub"
		print(kesk)
