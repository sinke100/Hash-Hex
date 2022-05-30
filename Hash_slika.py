import PySimpleGUI as sg
from random import randrange as r, seed as s
sg.theme('Python')

def infor(info):
	if type(info) == tuple: win = window('bravo', info)
	elif type(info) == bytes: win = window('bravo', (info, ''))
	elif type(info) == str: win = window('bravo', (b'', info))
	else: win = window('krivo', 0)
	return pogodi(win)

'''
def prikaz(win):
        e = win.read()[0]
        if e != None:
                win.close()
                return True
'''

def display(podatci, upis, dalje):
	s(upis.strip().capitalize())
	data = ''.join(podatci.split('\n'))
	data = bytes([int(data[i:i+2], 16) for i in range(0,len(data),2)])
	k = [r(10) for i in range(len(data))]
	data = [data[i]+k[i] if data[i]+k[i] <= 255 else data[i]+k[i]-256 for i in range(len(data))]
	data = bytes(data)
	if data[:4] == b'\x89PNG':
	               data, poruka = data.split(b'\xae\x42\x60\x82')
	               data = data+b'\xae\x42\x60\x82'
	               poruka = poruka.decode()
	               if dalje == 'Slika i poruka': return data, poruka
	               if dalje == 'Slika': return data
	               if dalje == 'Poruka': return poruka
	else: return False 
	
def window(x, info):
    if x == 'pogodi': return sg.Window('', [[sg.Text('Upiši šifru da dobiješ sliku:', font=('Verdana',15))],[sg.Input('', size=(40, 1))],[sg.Button('Slika i poruka'), sg.Button('Slika'), sg.Button('Poruka')]])
    if x == 'bravo':
    	pokazuje = True
    	if info[1] == '':
    		pokazuje = False 
    	return sg.Window('', [[sg.Image(info[0])],[sg.Text(info[1], visible=pokazuje,font=('Verdana',30))], [sg.Button('Ponovo')]],element_justification='center')
    if x == 'krivo': return sg.Window('', [[sg.Text('Nije točno!', font=('Verdana',50))],[sg.Button('Ponovo')]])
    
def pogodi(data):
    if type(data) != sg.PySimpleGUI.Window: win = window('pogodi', 0)
    else: win = data
    e, v = win.read()
    if e == 'Ponovo':
            win.close()
            return True
    if e != None:
            info = display(data, v[0], e)
            win.close()
            return infor(info)
        
if __name__ == '__main__':
        with open('hex hash upis.txt', 'r') as f: file = f.read()
        ponovo = True
        while ponovo: ponovo = pogodi(file)
