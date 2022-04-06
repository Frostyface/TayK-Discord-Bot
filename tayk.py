from datetime import date

today = date.today()

#July 23, 2019 is when Lil Tay K was locked up

jailDate = date(2019, 7, 23)

inJail = today - jailDate

inJail = str(inJail)[:-9]

def tayk():
	message = 'Tay K has been in jail for ' + inJail + "! Wow, that's a long time!"
	return message




