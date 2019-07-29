
listplace = ["ming", "zhao", "sun"]


list1={"ming":{"mac1":10,"mac2":12, "mac3":22}}
list2={"zhao":{"mac1":100,"mac3":12}}
list3={"sun":{"mac1":56,"mac2":12, "mac4":22}}

restrack = [list1, list2, list3]


mac_list = []
mac_crash = []
for i in range(len(restrack)):
	for key in restrack[i]:
		if mac_list:
			mac_temp = list(restrack[i][key].keys())
			print "frist mac list: ", mac_list, "second mac list: ", mac_temp
			for i in range(len(mac_temp)):
				if mac_temp[i] in mac_list:
					mac_crash.append(mac_temp[i])
			mac_list = mac_crash
			mac_crash = []	
		else:	
			mac_list = list(restrack[i][key].keys())


print "Finaly: ", mac_list
