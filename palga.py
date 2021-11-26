from modul import*
while True:
	a=input("Funktsioonid: Add-1, remove-2, biggest-3")
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
	elif a=="7":
		search_name()
	elif a=="11":
		tulumaks()