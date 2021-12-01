from modul import*
while True:
	a=input("Funktsioonid: lisama-1, kastuta-2, suurim palk-3, vähim palk-4, sorteerimine-5, saama palk-6, otsing-7, tulumaks-8, keskmine palk-9, lõpetanud-E")
	if a=="1":
		add_person()
	elif a=="2":
		delete_person()
	elif a=="3":
		biggest_salary()
	elif a=="4":
		smallest_salary()
	elif a=="5":
		sorting()
	elif a=="6":
		same_salary()
	elif a=="7":
		search_name()
	elif a=="8":
		tulumaks()
	elif a=="9":
		keskmine()
	elif a.upper=="E":
		break
	else:
		("See funktsioon ei tööta või ei olema")
