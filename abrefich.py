from tkinter import *
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter import messagebox as mb
from tkinter import scrolledtext as st
import sys


class Aplicacion():
	def __init__(self):
		try:
			self.v1=Tk()
			self.v1.title('CumulusRepair')
			self.v1.state('zoomed')
			self.nombrearch=''

			self.labelframe1=ttk.LabelFrame(self.v1, text='opciones')        
			self.btnAbrir=ttk.Button(self.labelframe1, text='Abrir', command=self.abrir)
			self.btnCerrar=ttk.Button(self.labelframe1, text='Cerrar', command=self.cerrar)
			self.btnBorrar=ttk.Button(self.labelframe1, text='Busca/Borra', command=self.buscarLinea)
			self.btnReparar=ttk.Button(self.labelframe1, text='Genera Log', command=self.reparacionAutomatica)
			self.framel1=ttk.Frame(self.v1)
			self.scrolledtext1=st.ScrolledText(self.v1)

#----Rellena cabeceras en frame1----------------------------------------------------------------------------------
			
			self.lbl1f1=Label(self.framel1, text='LINEA', font=('arial',10, 'bold'), padx=15, pady=3, justify='right', fg='green')
			self.lbl1f2=Label(self.framel1, text='FECHA     HORA  ', font=('arial',10, 'bold'), fg='green')
			self.lbl1f3=Label(self.framel1, text='T.ex   ', font=('arial',10, 'bold'), fg='green')
			self.lbl1f4=Label(self.framel1, text='H.ex    ', font=('arial',10, 'bold'), fg='green')
			self.lbl1f5=Label(self.framel1, text='DewP    ', font=('arial',10, 'bold'), fg='green')
			self.lbl1f6=Label(self.framel1, text='MVie   ', font=('arial',10, 'bold'), fg='green')
			self.lbl1f7=Label(self.framel1, text='MRaf  ', font=('arial',10, 'bold'), fg='green')
			self.lbl1f8=Label(self.framel1, text='MDir   ', font=('arial',10, 'bold'), fg='green')
			self.lbl1f9=Label(self.framel1, text='RLLu   ', font=('arial',10, 'bold'), fg='green')
			self.lbl1f10=Label(self.framel1, text='TLLU ', font=('arial',10, 'bold'), fg='green')
			self.lbl1f11=Label(self.framel1, text='PRES     ', font=('arial',10, 'bold'), fg='green')
			self.lbl1f12=Label(self.framel1, text='tINT    ', font=('arial',10, 'bold'), fg='green')
			self.lbl1f13=Label(self.framel1, text='hINT    ', font=('arial',10, 'bold'), fg='green')
			self.lbl1f14=Label(self.framel1, text='U.Raf ', font=('arial',10, 'bold'), fg='green')
			self.lbl1f15=Label(self.framel1, text='WCh   ', font=('arial',10, 'bold'), fg='green')
			self.lbl1f16=Label(self.framel1, text='HIndx  ', font=('arial',10, 'bold'), fg='green')
			self.lbl1f17=Label(self.framel1, text='TAp     ', font=('arial',10, 'bold'), fg='green')
			self.lbl1f18=Label(self.framel1, text='DirV  ', font=('arial',10, 'bold'), fg='green')
			self.lbl1f19=Label(self.framel1, text='LLMch', font=('arial',10, 'bold'), fg='green')
		
			self.lbl1f1.grid(column=0, row=0, sticky='s')
			self.lbl1f2.grid(column=1, row=0, sticky='w')
			self.lbl1f3.grid(column=2, row=0, sticky='w')
			self.lbl1f4.grid(column=3, row=0, sticky='w')
			self.lbl1f5.grid(column=4, row=0, sticky='w')
			self.lbl1f6.grid(column=5, row=0, sticky='w')
			self.lbl1f7.grid(column=6, row=0, sticky='w')
			self.lbl1f8.grid(column=7, row=0, sticky='w')
			self.lbl1f9.grid(column=8, row=0, sticky='w')
			self.lbl1f10.grid(column=9, row=0, sticky='w')
			self.lbl1f11.grid(column=10, row=0, sticky='w')
			self.lbl1f12.grid(column=11, row=0, sticky='w')
			self.lbl1f13.grid(column=12, row=0, sticky='w')
			self.lbl1f14.grid(column=13, row=0, sticky='w')
			self.lbl1f15.grid(column=14, row=0, sticky='w')
			self.lbl1f16.grid(column=15, row=0, sticky='w')
			self.lbl1f17.grid(column=16, row=0, sticky='w')
			self.lbl1f18.grid(column=17, row=0, sticky='w')
			self.lbl1f19.grid(column=18, row=0, sticky='w')

			self.framel1.pack(side=TOP, fill=BOTH)
			self.btnAbrir.pack(side=LEFT)
			self.btnCerrar.pack(side=LEFT)
			self.btnBorrar.pack(side=LEFT)
			self.btnReparar.pack(side=RIGHT)
			self.labelframe1.pack(side=BOTTOM)			
			self.scrolledtext1.pack(expand=True, fill=BOTH)

			self.creaMenu()
			self.v1.mainloop()

		except AttributeError:
			print('Atribute Error')
			self.fin()


	def creaMenu(self):
		menubar1=Menu(self.v1)
		self.v1.config(menu=menubar1)

		opciones1=Menu(menubar1,tearoff=0)
		menubar1.add_cascade(label='Fichero',menu=opciones1)
		opciones1.add_command(label='Abrir',command=self.abrir,accelerator='Ctrl+A')
		opciones1.add_command(label='cerrar',command=self.cerrar,accelerator='Ctrl+C')
		opciones1.add_separator()
		opciones1.add_command(label='Salir',command=self.fin,accelerator='Ctrl+F')

		opciones2 = Menu(menubar1, tearoff=0)
		menubar1.add_cascade(label='Opciones',menu=opciones2)
		opciones2.add_command(label='Busca/Borra',command=self.buscarLinea, accelerator='Ctrl+B')
		opciones2.add_command(label='Genera Log',command=self.reparacionAutomatica, accelerator='Ctrl+R')

		menubar1.add_command(label='Salir',command=self.fin,accelerator='Ctrl+F')

		self.v1.bind_all('<Control-a>',self.teclado)
		self.v1.bind_all('<Control-c>',self.teclado)
		self.v1.bind_all('<Control-f>',self.teclado)
		self.v1.bind_all('<Control-b>',self.teclado)
		self.v1.bind_all('<Control-r>',self.teclado)

	def teclado(self, event):
		if event.keysym == 'a':
			self.abrir()
		if event.keysym == 'c':
			self.cerrar()
		if event.keysym == 'b':
			self.buscarLinea()
		if event.keysym == 'r':
			self.reparacionAutomatica()
		if event.keysym == 'f':
			self.fin()

	def abrir(self):
		if self.nombrearch!='':
			self.cerrar()

		self.nombrearch=fd.askopenfilename(initialdir='/',title='Seleccione archivo',filetypes=(('txtfiles','*.txt'),('todoslosarchivos','*.*')))
		if self.nombrearch!='':
			try:
				self.archi1=open(self.nombrearch,'r',encoding='utf-8')
				self.borraScrolledText()
				self.imprimirFichero()

			except UnicodeDecodeError:
				mb.showinfo('ERROR', 'Fichero no reconocido.')

	def buscarLinea(self):
		try:
			self.archi1.close()
			self.archi1=open(self.nombrearch,'r',encoding='utf-8')
			lines = self.archi1.readlines()
			longFich=len(lines)
			lineaBuscar=self.dialogo()

			if int(lineaBuscar)>longFich or int(lineaBuscar)<1:
				raise IndexError

			linCon=lineaBuscar+'.0'
			longLin=str(len(lineaBuscar))
			linRes=lineaBuscar+'.'+longLin
			linStop=lineaBuscar+'.'+str(longFich)

			self.scrolledtext1.tag_add('ROJA', linRes, linStop)
			self.scrolledtext1.tag_config('ROJA', foreground='white', background='black')

			self.scrolledtext1.see(linCon)

			self.scrolledtext1.tag_config('contadorLinea', background='yellow')

			respuesta=mb.askyesno('Borrar', '¿Quiere borrar la linea?')
			if respuesta==True:
				lines.pop(int(lineaBuscar)-1)
				self.archi1.close()
				self.archi1=open(self.nombrearch,'w',encoding='utf-8')
				self.archi1.writelines(lines)
				mb.showinfo('AVISO', 'LINEA BORRADA---se genera un nuevo LOG para recomponer lineas.')

				if self.v2.winfo_exists():
					self.v2.destroy()
				
			self.archi1.close()
			self.archi1=open(self.nombrearch,'r',encoding='utf-8')
			self.borraScrolledText()	
			self.imprimirFichero()

		except ValueError:
			mb.showinfo('ERROR', 'Introduzca un valor correcto.')
		except AttributeError:
			mb.showinfo('ERROR', 'Abra un fichero LOG de cumulus.')
		except IndexError:
			mb.showinfo('ERROR', 'linea no existe.')
		except FileNotFoundError:
			mb.showinfo('ERROR', 'Abra un fichero LOG de cumulus.')

	def borraScrolledText(self):
		self.scrolledtext1.delete('1.0', END)

	def imprimirFichero(self):		
		try:
			self.v1.title('CumulusRepair'+'--'+self.nombrearch)				
			lineas=self.archi1.readlines()		
			contadorLinea=len(lineas)

			for linea in reversed(lineas):
				nuevaLinea=self.formateaLinea(linea) 
				
				linea = ';'
				linea = linea.join(nuevaLinea)
			
				lin = linea.replace(';', '  ')
				linew = ''
				linew = linew.join(lin)

				cLinea=str(contadorLinea)
				lenCon=len(cLinea)

				lenClinea=str(len(cLinea))
				linSub='1.'+lenClinea

# 			Deja un numero especifico de guiones según sea la longitud del contador para que el encabezado concuerde con
#			el cuerpo de las lineas.

				if lenCon==1:						
					linBlan='----'
				elif lenCon==2:
					linBlan='---'
				elif lenCon==3:
					linBlan='--'
				elif lenCon==4:
					linBlan='-'			
				else:
					linBlan=''

				lenLineW=str(len(linew)+len(cLinea)+1+len(linBlan))
				linStop='1.'+str(lenLineW)

#			parImpar se usa para resaltar una de cada dos lineas y ensombrecerla para distinguirla en la pantalla.

				parImpar=contadorLinea%2

				self.scrolledtext1.insert('1.0', cLinea+linBlan+'--'+linew)

				if parImpar==0:
					self.scrolledtext1.tag_add('contadorLinea', '1.0', linSub)
					self.scrolledtext1.tag_config('contadorLinea', background='yellow')
					self.scrolledtext1.tag_add('resaltada', linSub, linStop)
					self.scrolledtext1.tag_config('resaltada', background='#EAE8E8')
				else:
					self.scrolledtext1.tag_add('contadorLinea', '1.0', linSub)
					self.scrolledtext1.tag_config('contadorLinea', background='yellow')
		
				contadorLinea-=1

		except ValueError:
			mb.showinfo('ERROR', 'Introduzca un valor correcto.')
		except AttributeError:
			mb.showinfo('ERROR', 'Abra un fichero LOG de cumulus.')
		except IndexError:
			mb.showinfo('ERROR', 'linea del log {}'.format(contadorLinea))
		except FileNotFoundError:
			mb.showinfo('ERROR', 'Abra un fichero LOG de cumulus.')


	def formateaLinea(self, lin):   # Da formato a cada linea de pantalla. Añade espacios para que las columnas de los
	 								# datos coincidan.
		linea=lin.split(';')
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Se eliminan varios datos de lecturas solares que no interesan
#
# La Lista a imprimir queda de la siguiente con los siguientes elementos:
#
# 0- FECHA 1-HORA 2-TEMP.EXTERIOR 3-HUMEDAD EXTERIOR 4-DEW POINT 5-VEL VIENTO 6-VIENTO RAFAGA 7-DIR.MED.VIENTO
# 8- RATIO DE LLUVIA 9-TOTAL LLUVIA 10-PRESION 11-TEMP.INTERIOR 12-HUMEDAD INTERIOR 13-ULTIMA RAFAGA 14-WIND CHILL
# 15-HEAT INDEX 16-TEMP.APARENTE 17-DIRECCION VIENTO 18-LLUVIA DESDE MEDIANOCHE
#
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

		linea.pop(11)
		linea.pop(16)
		linea.pop(16)
		linea.pop(16)
		linea.pop(16)
		linea.pop(17)
		linea.pop(17)
		linea.pop(18)
		contElem=0
		for elemento in linea:
				lenElem=len(elemento)
				nuevoElemento=elemento

				if contElem==2:						# Formateo de temperatura.
					if lenElem==1:
						nuevoElemento='   '+elemento
					elif lenElem==2:
						nuevoElemento='  '+elemento
					elif lenElem==3:
						nuevoElemento=' '+elemento
					linea[2]=nuevoElemento

				if contElem==3:						# Formateo de humedad exterior.
					if lenElem==1:
						nuevoElemento='  '+elemento
					elif lenElem==2:
						nuevoElemento=' '+elemento 					
					linea[3]=nuevoElemento

				if contElem==4:						# Formateo de dew-point.
					if lenElem==1:
						nuevoElemento='    '+elemento
					elif lenElem==2:
						nuevoElemento='   '+elemento
					elif lenElem==3:
						nuevoElemento='  '+elemento	
					elif lenElem==4:
						nuevoElemento=' '+elemento					
					linea[4]=nuevoElemento

				if contElem==5:						# Formateo de media del viento.
					if lenElem==1:
						nuevoElemento='   '+elemento
					elif lenElem==2:
						nuevoElemento='  '+elemento
					elif lenElem==3:
						nuevoElemento=' '+elemento
					linea[5]=nuevoElemento

				if contElem==6:						# Formateo de media de ráfaga.
					if lenElem==1:
						nuevoElemento='   '+elemento
					elif lenElem==2:
						nuevoElemento='  '+elemento
					elif lenElem==3:
						nuevoElemento=' '+elemento
					linea[6]=nuevoElemento

				if contElem==7:						# Formateo de media de direccion de viento.
					if lenElem==1:
						nuevoElemento='   '+elemento
					elif lenElem==2:
						nuevoElemento='  '+elemento
					elif lenElem==3:
						nuevoElemento=' '+elemento
					linea[7]=nuevoElemento

				if contElem==8:						# Formateo de ratio de lluvia.
					if lenElem==1:
						nuevoElemento='   '+elemento
					elif lenElem==2:
						nuevoElemento='  '+elemento
					elif lenElem==3:
						nuevoElemento=' '+elemento
					linea[8]=nuevoElemento

				if contElem==9:						# Formateo de de lluvia.
					if lenElem==1:
						nuevoElemento='   '+elemento
					elif lenElem==2:
						nuevoElemento='  '+elemento
					elif lenElem==3:
						nuevoElemento=' '+elemento
					linea[9]=nuevoElemento

				if contElem==10:					# Formateo de Presión.
					if lenElem==5:
						nuevoElemento=' '+elemento
					linea[10]=nuevoElemento

				if contElem==11:					# Formateo de temperatura interior.
					if lenElem==1:
						nuevoElemento='   '+elemento
					elif lenElem==2:
						nuevoElemento='  '+elemento
					elif lenElem==3:
						nuevoElemento=' '+elemento
					linea[11]=nuevoElemento

				if contElem==12:						# Formateo de humedad interior.
					if lenElem==1:
						nuevoElemento='  '+elemento
					elif lenElem==2:
						nuevoElemento=' '+elemento 					
					linea[12]=nuevoElemento

				if contElem==13:						# Formateo de ultima ráfaga.
					if lenElem==1:
						nuevoElemento='   '+elemento
					elif lenElem==2:
						nuevoElemento='  '+elemento
					elif lenElem==3:
						nuevoElemento=' '+elemento
					linea[13]=nuevoElemento

				if contElem==14:						# Formateo de wind chill.
					if lenElem==1:
						nuevoElemento='    '+elemento
					elif lenElem==2:
						nuevoElemento='   '+elemento
					elif lenElem==3:
						nuevoElemento='  '+elemento	
					elif lenElem==4:
						nuevoElemento=' '+elemento					
					linea[14]=nuevoElemento

				if contElem==15:						# Formateo de heat index.
					if lenElem==1:
						nuevoElemento='   '+elemento
					elif lenElem==2:
						nuevoElemento='  '+elemento
					elif lenElem==3:
						nuevoElemento=' '+elemento
					linea[15]=nuevoElemento

				if contElem==16:					# Formateo de temp.aparente.
					if lenElem==1:
						nuevoElemento='   '+elemento
					elif lenElem==2:
						nuevoElemento='  '+elemento
					elif lenElem==3:
						nuevoElemento=' '+elemento
					linea[16]=nuevoElemento

				if contElem==17:						# Formateo de direccion de viento.
					if lenElem==1:
						nuevoElemento='   '+elemento
					elif lenElem==2:
						nuevoElemento='  '+elemento
					elif lenElem==3:
						nuevoElemento=' '+elemento
					linea[17]=nuevoElemento

				if contElem==18:						# Formateo de de lluvia desde medianoche.
					if lenElem==1:
						nuevoElemento='   '+elemento
					elif lenElem==2:
						nuevoElemento='  '+elemento
					elif lenElem==3:
						nuevoElemento=' '+elemento
					linea[18]=nuevoElemento

				contElem+=1

		return linea
	
	def cerrar(self):
		try:
			self.nombrearch=''
			self.archi1.close()
			self.v1.title('CumulusRepair')
			self.scrolledtext1.delete('1.0', END)

		except NameError:
			mb.showinfo('ERROR', 'El fichero no se abrió y por lo tanto no se puede cerrar.')
		except AttributeError:
			mb.showinfo('ERROR', 'El fichero no se abrió y por lo tanto no se puede cerrar.')

	def fin(self):
		sys.exit()

	def dialogo(self):
		self.dialogod=Toplevel(self.v1)
		self.labeld1=Label(self.dialogod, text='Linea a Buscar/Borrar')
		self.datod1=StringVar()
		self.entryd1=ttk.Entry(self.dialogod, textvariable=self.datod1)
		self.botond1=ttk.Button(self.dialogod, text='Confirmar', command=self.dialogod.destroy)

		self.labeld1.grid(column=0, row=0, padx=5, pady=5)
		self.entryd1.grid(column=1, row=0, padx=5, pady=5)
		self.botond1.grid(column=1, row=2, padx=5, pady=5)
		self.entryd1.focus()

		self.dialogod.protocol('WM_DELETE_WINDOW', self.dialogod.destroy)
		self.dialogod.resizable(0,0)
		self.dialogod.grab_set()
		self.dialogod.wait_window()
		return self.datod1.get()
	
			
	def reparacionAutomatica(self):
		try:
			self.nomLog=self.nombrearch[-13:-3]			# Componemos un nombre de LOG al fichero de errores
			nombreLog=self.nomLog+'ERROR.txt'

#		Verifica que todas las lineas cumplen con los elementos correctos.
			
			self.archi1.close()
			self.archi1=open(self.nombrearch,'r',encoding='utf-8')

			lineas=self.archi1.readlines()
			self.archi1.close()

			errorLin=0

			for linea in lineas:
				lin=linea.split(';')
				errorLin+=1
				if len(lin)>27:
					raise TypeError


#		-----------------VERIFICA FECHA------------------------------------------------------------------------------------

			self.archi1.close()
			self.archi1=open(self.nombrearch,'r',encoding='utf-8')
			error=self.verificaFecha()

			if error==[]:
				self.archi2=open(nombreLog,'w', encoding='utf-8')
				self.archi2.write('\n')
				self.archi2.write('-----NO HAY ERRORES DE FECHA\n')
				self.archi2.write('\n')
				self.archi2.close()
			else:
				cont=0
				errLST=[]
				errLST.append('\n')

				for elem in error:
					if cont==3:
						errLST.append(elem)
						errLST.append('\n')
						cont=0
					else:
						errLST.append(elem)
						cont+=1

				errorTemp = '  '
				errorTemp = errorTemp.join(errLST)
				self.archi2=open(nombreLog,'w', encoding='utf-8')
				self.archi2.write('------ERRORES DE FECHA--------------------------------------------------------\n')
				self.archi2.write(errorTemp)
				self.archi2.write('\n')
				self.archi2.close()

#----------VERIFICA TEMPERATURA EXTERIOR-----------------------------------------------------------------------------------
			
			self.archi1.close()
			self.archi1=open(self.nombrearch,'r',encoding='utf-8')
			error=self.verificaTemperatura()

			if error==[]:
				self.archi2=open(nombreLog,'a', encoding='utf-8')
				self.archi2.write('\n')
				self.archi2.write('-----NO HAY ERRORES DE TEMPERATURA EXTERIOR\n')
				self.archi2.write('\n')
				self.archi2.close()
			else:
				cont=0
				errLST=[]
				errLST.append('\n')
				for elem in error:
					if cont==3:
						errLST.append(elem)
						errLST.append('\n')
						cont=0
					else:
						errLST.append(elem)
						cont+=1
				errorTemp = '  '
				errorTemp = errorTemp.join(errLST)
				self.archi2=open(nombreLog,'a', encoding='utf-8')
				self.archi2.write('------ERRORES DE TEMPERATURA EXTERIOR---------------------------------------\n')
				self.archi2.write(errorTemp)
				self.archi2.write('\n')
				self.archi2.close()


#		-----------------VERIFICA HUMEDAD----------------------------------------------------------------------------------

			self.archi1.close()
			self.archi1=open(self.nombrearch,'r',encoding='utf-8')
			error=self.verificaHumedad()

			if error==[]:
				self.archi2=open(nombreLog,'a', encoding='utf-8')
				self.archi2.write('\n')
				self.archi2.write('-----NO HAY ERRORES DE HUMEDAD EXTERIOR\n')
				self.archi2.write('\n')
				self.archi2.close()
			else:
				cont=0
				errLST=[]
				errLST.append('\n')
				for elem in error:
					if cont==3:
						errLST.append(elem)
						errLST.append('\n')
						cont=0
					else:
						errLST.append(elem)
						cont+=1
				errorTemp = '  '
				errorTemp = errorTemp.join(errLST)
				self.archi2=open(nombreLog,'a', encoding='utf-8')
				self.archi2.write('-----ERRORES DE HUMEDAD EXTERIOR---------------------------------------------\n')
				self.archi2.write(errorTemp)
				self.archi2.write('\n')
				self.archi2.close()


#		-----------------VERIFICA DEW POINT--------------------------------------------------------------------------------
			
			self.archi1.close()
			self.archi1=open(self.nombrearch,'r',encoding='utf-8')
			error=self.verificaDewPoint()

			if error==[]:
				self.archi2=open(nombreLog,'a', encoding='utf-8')
				self.archi2.write('\n')
				self.archi2.write('-----NO HAY ERRORES DE PUNTO DE ROCIO\n')
				self.archi2.write('\n')
				self.archi2.close()
			else:
				cont=0
				errLST=[]
				errLST.append('\n')
				for elem in error:
					if cont==3:
						errLST.append(elem)
						errLST.append('\n')
						cont=0
					else:
						errLST.append(elem)
						cont+=1
				errorTemp = '  '
				errorTemp = errorTemp.join(errLST)
				self.archi2=open(nombreLog,'a', encoding='utf-8')
				self.archi2.write('-----ERRORES DE PUNTO DE ROCIO------------------------------------------------\n')
				self.archi2.write(errorTemp)
				self.archi2.write('\n')
				self.archi2.close()


#		-----------------VERIFICA VELOCIDAD VIENTO-------------------------------------------------------------------------
			
			self.archi1.close()
			self.archi1=open(self.nombrearch,'r',encoding='utf-8')
			error=self.verificaVelViento()

			if error==[]:
				self.archi2=open(nombreLog,'a', encoding='utf-8')
				self.archi2.write('\n')
				self.archi2.write('-----NO HAY ERRORES DE VIENTO\n')
				self.archi2.write('\n')
				self.archi2.close()
			else:
				cont=0
				errLST=[]
				errLST.append('\n')
				for elem in error:
					if cont==3:
						errLST.append(elem)
						errLST.append('\n')
						cont=0
					else:
						errLST.append(elem)
						cont+=1
				errorTemp = '  '
				errorTemp = errorTemp.join(errLST)
				self.archi2=open(nombreLog,'a', encoding='utf-8')
				self.archi2.write('------ERRORES DE VIENTO-----------------------------------------------------\n')
				self.archi2.write(errorTemp)
				self.archi2.write('\n')
				self.archi2.close()

#		-----------------VERIFICA MEDIA DE RAFAGA--------------------------------------------------------------------------
			
			self.archi1.close()
			self.archi1=open(self.nombrearch,'r',encoding='utf-8')
			error=self.verificaMediaDeRafaga()

			if error==[]:
				self.archi2=open(nombreLog,'a', encoding='utf-8')
				self.archi2.write('\n')
				self.archi2.write('-----NO HAY ERRORES DE MEDIA DE RAFAGA\n')
				self.archi2.write('\n')
				self.archi2.close()
			else:
				cont=0
				errLST=[]
				errLST.append('\n')
				for elem in error:
					if cont==3:
						errLST.append(elem)
						errLST.append('\n')
						cont=0
					else:
						errLST.append(elem)
						cont+=1
				errorTemp = '  '
				errorTemp = errorTemp.join(errLST)
				self.archi2=open(nombreLog,'a', encoding='utf-8')
				self.archi2.write('------ERRORES DE MEDIA DE RAFAGA-------------------------------------------\n')
				self.archi2.write(errorTemp)
				self.archi2.write('\n')
				self.archi2.close()

#		-----------------VERIFICA DIRECCION MEDIA DEL VIENTO---------------------------------------------------------------
			
			self.archi1.close()
			self.archi1=open(self.nombrearch,'r',encoding='utf-8')
			error=self.verificaDirMediaViento()

			if error==[]:
				self.archi2=open(nombreLog,'a', encoding='utf-8')
				self.archi2.write('\n')
				self.archi2.write('-----NO HAY ERRORES DE DIRECCION MEDIA DEL VIENTO\n')
				self.archi2.write('\n')
				self.archi2.close()
			else:
				cont=0
				errLST=[]
				errLST.append('\n')
				for elem in error:
					if cont==3:
						errLST.append(elem)
						errLST.append('\n')
						cont=0
					else:
						errLST.append(elem)
						cont+=1
				errorTemp = '  '
				errorTemp = errorTemp.join(errLST)
				self.archi2=open(nombreLog,'a', encoding='utf-8')
				self.archi2.write('------ERRORES DE DIRECCION MEDIA DEL VIENTO------------------------------------\n')
				self.archi2.write(errorTemp)
				self.archi2.write('\n')
				self.archi2.close()

#		-----------------VERIFICA RATE RAINFALL----------------------------------------------------------------------------
			
			self.archi1.close()
			self.archi1=open(self.nombrearch,'r',encoding='utf-8')
			error=self.verificaRateRainfall()

			if error==[]:
				self.archi2=open(nombreLog,'a', encoding='utf-8')
				self.archi2.write('\n')
				self.archi2.write('-----NO HAY ERRORES DE RATIO DE LLUVIA\n')
				self.archi2.write('\n')
				self.archi2.close()
			else:
				cont=0
				errLST=[]
				errLST.append('\n')
				for elem in error:
					if cont==3:
						errLST.append(elem)
						errLST.append('\n')
						cont=0
					else:
						errLST.append(elem)
						cont+=1
				errorTemp = '  '
				errorTemp = errorTemp.join(errLST)
				self.archi2=open(nombreLog,'a', encoding='utf-8')
				self.archi2.write('------ERRORES DE RATIO DE LLUVIA----------------------------------------------\n')
				self.archi2.write(errorTemp)
				self.archi2.write('\n')
				self.archi2.close()

#		-----------------VERIFICA RAINFALL---------------------------------------------------------------------------------
			
			self.archi1.close()
			self.archi1=open(self.nombrearch,'r',encoding='utf-8')
			error=self.verificaRainfall()

			if error==[]:
				self.archi2=open(nombreLog,'a', encoding='utf-8')
				self.archi2.write('\n')
				self.archi2.write('-----NO HAY ERRORES DE LLUVIA\n')
				self.archi2.write('\n')
				self.archi2.close()
			else:
				cont=0
				errLST=[]
				errLST.append('\n')
				for elem in error:
					if cont==3:
						errLST.append(elem)
						errLST.append('\n')
						cont=0
					else:
						errLST.append(elem)
						cont+=1
				errorTemp = '  '
				errorTemp = errorTemp.join(errLST)
				self.archi2=open(nombreLog,'a', encoding='utf-8')
				self.archi2.write('------ERRORES DE LLUVIA------------------------------------------------------\n')
				self.archi2.write(errorTemp)
				self.archi2.write('\n')
				self.archi2.close()

#		-----------------VERIFICA PRESION----------------------------------------------------------------------------------
			
			self.archi1.close()
			self.archi1=open(self.nombrearch,'r',encoding='utf-8')
			error=self.verificaPresion()

			if error==[]:
				self.archi2=open(nombreLog,'a', encoding='utf-8')
				self.archi2.write('\n')
				self.archi2.write('-----NO HAY ERRORES DE PRESION\n')
				self.archi2.write('\n')
				self.archi2.close()
			else:
				cont=0
				errLST=[]
				errLST.append('\n')
				for elem in error:
					if cont==3:
						errLST.append(elem)
						errLST.append('\n')
						cont=0
					else:
						errLST.append(elem)
						cont+=1
				errorTemp = '  '
				errorTemp = errorTemp.join(errLST)
				self.archi2=open(nombreLog,'a', encoding='utf-8')
				self.archi2.write('------ERRORES DE PRESION----------------------------------------------------\n')
				self.archi2.write(errorTemp)
				self.archi2.write('\n')
				self.archi2.close()

#		-----------------VERIFICA TEMPERATURA INTERIOR---------------------------------------------------------------------
			
			self.archi1.close()
			self.archi1=open(self.nombrearch,'r',encoding='utf-8')
			error=self.verificaTinterior()

			if error==[]:
				self.archi2=open(nombreLog,'a', encoding='utf-8')
				self.archi2.write('\n')
				self.archi2.write('-----NO HAY ERRORES DE TEMPERATURA INTERIOR\n')
				self.archi2.write('\n')
				self.archi2.close()
			else:
				cont=0
				errLST=[]
				errLST.append('\n')
				for elem in error:
					if cont==3:
						errLST.append(elem)
						errLST.append('\n')
						cont=0
					else:
						errLST.append(elem)
						cont+=1
				errorTemp = '  '
				errorTemp = errorTemp.join(errLST)
				self.archi2=open(nombreLog,'a', encoding='utf-8')
				self.archi2.write('------ERRORES DE TEMPERATURA INTERIOR---------------------------------------\n')
				self.archi2.write(errorTemp)
				self.archi2.write('\n')
				self.archi2.close()


#		-----------------VERIFICA HUMEDAD INTERIOR-------------------------------------------------------------------------

			self.archi1.close()
			self.archi1=open(self.nombrearch,'r',encoding='utf-8')
			error=self.verificaHinterior()

			if error==[]:
				self.archi2=open(nombreLog,'a', encoding='utf-8')
				self.archi2.write('\n')
				self.archi2.write('-----NO HAY ERRORES DE HUMEDAD INTERIOR\n')
				self.archi2.write('\n')
				self.archi2.close()
			else:
				cont=0
				errLST=[]
				errLST.append('\n')
				for elem in error:
					if cont==3:
						errLST.append(elem)
						errLST.append('\n')
						cont=0
					else:
						errLST.append(elem)
						cont+=1
				errorTemp = '  '
				errorTemp = errorTemp.join(errLST)
				self.archi2=open(nombreLog,'a', encoding='utf-8')
				self.archi2.write('-----ERRORES DE HUMEDAD INTERIOR-------------------------------------------\n')
				self.archi2.write(errorTemp)
				self.archi2.write('\n')
				self.archi2.close()

#		-----------------VERIFICA WIND CHILL-------------------------------------------------------------------------------
			
			self.archi1.close()
			self.archi1=open(self.nombrearch,'r',encoding='utf-8')
			error=self.verificaWindChill()

			if error==[]:
				self.archi2=open(nombreLog,'a', encoding='utf-8')
				self.archi2.write('\n')
				self.archi2.write('-----NO HAY ERRORES DE WIND CHILL\n')
				self.archi2.write('\n')
				self.archi2.close()
			else:
				cont=0
				errLST=[]
				errLST.append('\n')
				for elem in error:
					if cont==3:
						errLST.append(elem)
						errLST.append('\n')
						cont=0
					else:
						errLST.append(elem)
						cont+=1
				errorTemp = '  '
				errorTemp = errorTemp.join(errLST)
				self.archi2=open(nombreLog,'a', encoding='utf-8')
				self.archi2.write('------ERRORES DE WIND CHILL--------------------------------------------------\n')
				self.archi2.write(errorTemp)
				self.archi2.write('\n')
				self.archi2.close()

#		-----------------VERIFICA HEAT INDEX-------------------------------------------------------------------------------
			
			self.archi1.close()
			self.archi1=open(self.nombrearch,'r',encoding='utf-8')
			error=self.verificaHeatIndex()

			if error==[]:
				self.archi2=open(nombreLog,'a', encoding='utf-8')
				self.archi2.write('\n')
				self.archi2.write('-----NO HAY ERRORES DE HEAT INDEX\n')
				self.archi2.write('\n')
				self.archi2.close()
			else:
				cont=0
				errLST=[]
				errLST.append('\n')
				for elem in error:
					if cont==3:
						errLST.append(elem)
						errLST.append('\n')
						cont=0
					else:
						errLST.append(elem)
						cont+=1
				errorTemp = '  '
				errorTemp = errorTemp.join(errLST)
				self.archi2=open(nombreLog,'a', encoding='utf-8')
				self.archi2.write('------ERRORES DE HEAT INDEX-------------------------------------------------\n')
				self.archi2.write(errorTemp)
				self.archi2.write('\n')
				self.archi2.close()

#		-----------------VERIFICA TEMPERATURA APARENTE---------------------------------------------------------------------
			
			self.archi1.close()
			self.archi1=open(self.nombrearch,'r',encoding='utf-8')
			error=self.verificaTaparente()

			if error==[]:
				self.archi2=open(nombreLog,'a', encoding='utf-8')
				self.archi2.write('\n')
				self.archi2.write('-----NO HAY ERRORES DE TEMPERATURA APARENTE\n')
				self.archi2.write('\n')
				self.archi2.close()
			else:
				cont=0
				errLST=[]
				errLST.append('\n')
				for elem in error:
					if cont==3:
						errLST.append(elem)
						errLST.append('\n')
						cont=0
					else:
						errLST.append(elem)
						cont+=1
				errorTemp = '  '
				errorTemp = errorTemp.join(errLST)
				self.archi2=open(nombreLog,'a', encoding='utf-8')
				self.archi2.write('------ERRORES DE TEMPERATURA APARENTE---------------------------------------\n')
				self.archi2.write(errorTemp)
				self.archi2.write('\n')
				self.archi2.close()


#		-----------------VERIFICA DIRECCION DEL VIENTO---------------------------------------------------------------------
			
			self.archi1.close()
			self.archi1=open(self.nombrearch,'r',encoding='utf-8')
			error=self.verificaDirViento()

			if error==[]:
				self.archi2=open(nombreLog,'a', encoding='utf-8')
				self.archi2.write('\n')
				self.archi2.write('-----NO HAY ERRORES DE DIRECCION DEL VIENTO\n')
				self.archi2.write('\n')
				self.archi2.close()
			else:
				cont=0
				errLST=[]
				errLST.append('\n')
				for elem in error:
					if cont==3:
						errLST.append(elem)
						errLST.append('\n')
						cont=0
					else:
						errLST.append(elem)
						cont+=1
				errorTemp = '  '
				errorTemp = errorTemp.join(errLST)
				self.archi2=open(nombreLog,'a', encoding='utf-8')
				self.archi2.write('------ERRORES DE DIRECCION DEL VIENTO-------------------------------------\n')
				self.archi2.write(errorTemp)
				self.archi2.write('\n')
				self.archi2.close()

#		-----------------VERIFICA LLUVIA DESDE LA MEDIANOCHE---------------------------------------------------------------
			
			self.archi1.close()
			self.archi1=open(self.nombrearch,'r',encoding='utf-8')
			error=self.verificaLLuviaMediaNoche()

			if error==[]:
				self.archi2=open(nombreLog,'a', encoding='utf-8')
				self.archi2.write('\n')
				self.archi2.write('-----NO HAY ERRORES DE LLUVIA DESDE LA MEDIANOCHE\n')
				self.archi2.write('\n')
				self.archi2.close()
			else:
				cont=0
				errLST=[]
				errLST.append('\n')
				for elem in error:
					if cont==3:
						errLST.append(elem)
						errLST.append('\n')
						cont=0
					else:
						errLST.append(elem)
						cont+=1
				errorTemp = '  '
				errorTemp = errorTemp.join(errLST)
				self.archi2=open(nombreLog,'a', encoding='utf-8')
				self.archi2.write('------ERRORES DE LLUVIA DESDE LA MEDIANOCHE----------------------------\n')
				self.archi2.write(errorTemp)
				self.archi2.write('\n')
				self.archi2.close()

			self.archi2=open(nombreLog,'r', encoding='utf-8')
			lineas=self.archi2.readlines()
			self.archi2.close()
			self.archi1.close()
			self.v2=Tk()
			self.v2.title('CumulusRepair'+' '+nombreLog)

			self.scrolledtext2=st.ScrolledText(self.v2)
			self.scrolledtext2.pack(expand=True, fill=BOTH)

			for linea in reversed(lineas):
				self.scrolledtext2.insert('1.0',linea)
			
			self.v2.mainloop()


		except TypeError:
			mb.showinfo('ERROR', 'ERROR de log. REVISE LINEA {}'.format(errorLin))
		except ValueError:
			mb.showinfo('ERROR', 'ERROR de log. REVISE LINEA {}'.format(errorLin))
		except AttributeError:
			mb.showinfo('ERROR', 'Abra un fichero LOG de cumulus.')
		except IndexError:
			mb.showinfo('ERROR', 'linea no existe.')
		except FileNotFoundError:
			mb.showinfo('ERROR', 'Abra un fichero LOG de cumulus.')


	def verificaFecha(self):		
		agnoD={'ene' : '01','feb' : '02','mar' : '03','abr' : '04','may' : '05','jun' : '06','jul' : '07','ago' : '08', 'sep' : '09','oct' : '10','nov' : '11','dic' : '12'}
		
		self.nomfichero=self.nombrearch[-13:]	  #Extraemos el mes y el año del nombre del log para verificarlos con los datos del LOG.
		agnoFic=self.nomfichero[4:6]
		mesFic=self.nomfichero[-13:-10]

#		print('nombre fichero=',self.nomfichero ,agnoFic, mesFic, agnoD.get(mesFic))
		diaMes=1
		error=[]
		contadorLinea=0
		lineas=self.archi1.readlines()
#		print(lineas[0])
		for linea in lineas:
			lin=linea.split('/')
			diaMal=lin[0]
			dia=int(diaMal[-2:])
			mesLog=lin[1]
			agnoSlice=lin[2]
			agnoLog=agnoSlice[0:2]
#			print('linea ',mesLog, agnoLog)
			contadorLinea+=1
			if agnoFic!=agnoLog:
				error.append('-ERROR-AÑO------')
				error.append(str(contadorLinea))
				error.append(agnoFic)
				error.append(agnoLog)

			if agnoD.get(mesFic)!=mesLog:
				error.append('ERROR-MES------')
				error.append(str(contadorLinea))
				error.append(agnoD.get(mesFic))
				error.append(mesLog)

			if contadorLinea==1 and dia!=1:
				error.append('ERROR-DIA------')
				error.append(str(contadorLinea))
				error.append(str(diaMes))				
				error.append(str(dia))
				diaMes=dia

			if (dia==diaMes) or (dia==diaMes+1):
				if dia==diaMes+1:
					diaMes+=1
			else:
				error.append('ERROR-DIA------')
				error.append(str(contadorLinea))
				error.append(str(diaMes))				
				error.append(str(dia))
				diaMes=dia
		
		return error		

	def verificaTemperatura(self):
		error=[]
		contadorLinea=0
		lineas=self.archi1.readlines()
		linea=lineas[0]
		line=linea.split(';')
		lin = [c.replace(',', '.') for c in line]
		tempAnt=float(lin[2])

		for linea in lineas:
			contadorLinea+=1
			line=linea.split(';')
			lin = [c.replace(',', '.') for c in line]
			temperatura=float(lin[2])
			difTemp = temperatura-tempAnt

			if temperatura<-10 or temperatura>48:
				error.append('ERROR-TEMPERATURA MAX.MIN.(-10 OR >48)')
				tempStr=str(temperatura)
				temperaturaR = tempStr.replace('.', ',')
				tempStr1=str(tempAnt)
				temperaturaN = tempStr1.replace('.', ',')
				error.append(str(contadorLinea))
				error.append(str(temperaturaR))
				error.append(str(temperaturaN))


			if (difTemp>=1 and difTemp<2) or (difTemp<=-1 and difTemp>-2):
				error.append('WARNING-TEMPERATURA (VARIACION ENTRE 1º Y 2º)')
				tempStr=str(temperatura)
				temperaturaR = tempStr.replace('.', ',')
				tempStr1=str(tempAnt)
				temperaturaN = tempStr1.replace('.', ',')
				error.append(str(contadorLinea))
				error.append(str(temperaturaR))
				error.append(str(temperaturaN))

			elif (difTemp>=2 and difTemp<5) or (difTemp<=-2 and difTemp>-5):
				error.append('WARNING-TEMPERATURA (VARIACION ENTRE 2 Y 5)')
				tempStr=str(temperatura)
				temperaturaR = tempStr.replace('.', ',')
				tempStr1=str(tempAnt)
				temperaturaN = tempStr1.replace('.', ',')
				error.append(str(contadorLinea))
				error.append(str(temperaturaR))
				error.append(str(temperaturaN))

			elif (difTemp>=5) or (difTemp<=-5):
				error.append('ERROR-TEMPERATURA (VARIACION MAYOR DE 5)')
				tempStr=str(temperatura)
				temperaturaR = tempStr.replace('.', ',')
				tempStr1=str(tempAnt)
				temperaturaN = tempStr1.replace('.', ',')
				error.append(str(contadorLinea))
				error.append(str(temperaturaR))
				error.append(str(temperaturaN))
			
			tempAnt=temperatura

		return error

	def verificaHumedad(self):
		errHumedad=[]
		contadorLinea=0
		lineas=self.archi1.readlines()
		linea=lineas[0]
		lin=linea.split(';')
		humAnt=int(lin[3])

		for linea in lineas:
			contadorLinea+=1
			lin=linea.split(';')
			humedad=int(lin[3])
			difHum = humedad-humAnt

			if (humedad>100) or (humedad<0):
				errHumedad.append('ERROR-HUMEDAD MAX.MIN.(NEG.OR >100)')
				humedadR=str(humedad)
				humedadN=str(humAnt)
				errHumedad.append(str(contadorLinea))
				errHumedad.append(str(humedadR))
				errHumedad.append(str(humedadN))

			if (difHum>5 and difHum<=10) or (difHum<-5 and difHum>=-10):
				errHumedad.append('WARNING-HUMEDAD (VARIACION ENTRE 5 Y 10)')
				humedadR=str(humedad)
				humedadN=str(humAnt)
				errHumedad.append(str(contadorLinea))
				errHumedad.append(str(humedadR))
				errHumedad.append(str(humedadN))

			if (difHum>10) or (difHum<-10):
				errHumedad.append('ERROR-HUMEDAD (VARIACION MAYOR DE 10)')
				humedadR=str(humedad)
				humedadN=str(humAnt)
				errHumedad.append(str(contadorLinea))
				errHumedad.append(str(humedadR))
				errHumedad.append(str(humedadN))
			
			humAnt=humedad

		return errHumedad

	def verificaDewPoint(self):
		error=[]
		contadorLinea=0
		lineas=self.archi1.readlines()
		linea=lineas[0]
		line=linea.split(';')
		lin = [c.replace(',', '.') for c in line]
		dewAnt=float(lin[4])

		for linea in lineas:
			contadorLinea+=1
			line=linea.split(';')
			lin = [c.replace(',', '.') for c in line]
			dewPoint=float(lin[4])
			difDew = dewPoint-dewAnt

			if (dewPoint>=30) or (dewPoint<=-30):
				error.append('ERROR-DEW POINT MAX.MIN.(+30 OR -30)')
				tempStr=str(dewPoint)
				dewPointR = tempStr.replace('.', ',')
				tempStr1=str(dewAnt)
				dewPointN = tempStr1.replace('.', ',')
				error.append(str(contadorLinea))
				error.append(str(dewPointR))
				error.append(str(dewPointN))


			if (difDew>5) or (difDew<-5):
				error.append('WARNING-DEW POINT (VARIACION MAYOR DE 5)')
				tempStr=str(dewPoint)
				dewPointR = tempStr.replace('.', ',')
				tempStr1=str(dewAnt)
				dewPointN = tempStr1.replace('.', ',')
				error.append(str(contadorLinea))
				error.append(str(dewPointR))
				error.append(str(dewPointN))
			
			dewAnt=dewPoint

		return error

	def verificaVelViento(self):
		error=[]
		contadorLinea=0
		lineas=self.archi1.readlines()
		linea=lineas[0]
		line=linea.split(';')
		lin = [c.replace(',', '.') for c in line]
		vientoAnt=float(lin[5])

		for linea in lineas:
			contadorLinea+=1
			line=linea.split(';')
			lin = [c.replace(',', '.') for c in line]
			viento=float(lin[5])
			difViento = viento-vientoAnt

			if viento<0 or viento>100:
				error.append('ERROR-VELOCIDAD VIENTO MAX.MIN.(NEGATIVA O MAYOR DE 100.)')
				tempStr=str(viento)
				vientoR = tempStr.replace('.', ',')
				tempStr1=str(vientoAnt)
				vientoN = tempStr1.replace('.', ',')
				error.append(str(contadorLinea))
				error.append(str(vientoR))
				error.append(str(vientoN))

			if (difViento>5) or (difViento<-5):
#				print('WARNING--TEMP<2,0>',contadorLinea,viento, vientoAnt)
				error.append('WARNING-VELOCIDAD VIENTO (VARIACION MAYOR DE 5)')
				tempStr=str(viento)
				vientoR = tempStr.replace('.', ',')
				tempStr1=str(vientoAnt)
				vientoN = tempStr1.replace('.', ',')
				error.append(str(contadorLinea))
				error.append(str(vientoR))
				error.append(str(vientoN))
			
			vientoAnt=viento

		return error

	def verificaMediaDeRafaga(self):
		error=[]
		contadorLinea=0
		lineas=self.archi1.readlines()
		linea=lineas[0]
		line=linea.split(';')
		lin = [c.replace(',', '.') for c in line]
		vientoAnt=float(lin[6])

		for linea in lineas:
			contadorLinea+=1
			line=linea.split(';')
			lin = [c.replace(',', '.') for c in line]
			viento=float(lin[6])
			difViento = viento-vientoAnt

			if viento < 0 or viento > 100:
				error.append('ERROR-MEDIA DE RAFAGA MAX.MIN.(NEGATIVA O MAYOR DE 100)')
				tempStr=str(viento)
				vientoR = tempStr.replace('.', ',')
				tempStr1=str(vientoAnt)
				vientoN = tempStr1.replace('.', ',')
				error.append(str(contadorLinea))
				error.append(str(vientoR))
				error.append(str(vientoN))

			if (difViento>20) or (difViento<-20):
				error.append('WARNING-MEDIA DE RAFAGA (VARIACION MAYOR DE 20)')
				tempStr=str(viento)
				vientoR = tempStr.replace('.', ',')
				tempStr1=str(vientoAnt)
				vientoN = tempStr1.replace('.', ',')
				error.append(str(contadorLinea))
				error.append(str(vientoR))
				error.append(str(vientoN))

			vientoAnt=viento

		return error

	def verificaDirMediaViento(self):
		error=[]
		contadorLinea=0
		lineas=self.archi1.readlines()

		for linea in lineas:
			contadorLinea+=1
			line=linea.split(';')
			viento=int(line[7])

			if viento<0 or viento>360:
				error.append('ERROR-DIRECCION MEDIA DEL VIENTO (NEGATIVA O MAYOR DE 360º)')
				error.append(str(contadorLinea))
				error.append(str(viento))
				error.append(str(viento))

		return error

	def verificaRateRainfall(self):
		error=[]
		contadorLinea=0
		lineas=self.archi1.readlines()
		linea=lineas[0]
		line=linea.split(';')
		lin = [c.replace(',', '.') for c in line]
		rateRainAnt=float(lin[8])

		for linea in lineas: 
			contadorLinea+=1
			line=linea.split(';')
			lin = [c.replace(',', '.') for c in line]
			rateRain=float(lin[8])

			if rateRain < 0 or rateRain > 250:
				error.append('ERROR-RATE RAINFALL MAX.MIN.(NEGATIVA O MAYOR DE 250)')
				tempStr=str(rateRain)
				rateRainR = tempStr.replace('.', ',')
				tempStr1=str(rateRainAnt)
				rateRainAntN = tempStr1.replace('.', ',')
				error.append(str(contadorLinea))
				error.append(str(rateRainR))
				error.append(str(rateRainAntN))

			difRateRain = rateRain-rateRainAnt

			if (difRateRain>50) or (difRateRain<-50):
				error.append('WARNING-RATE RAINFALL (VARIACION MAYOR DE 50)')
				tempStr=str(rateRain)
				rateRainR = tempStr.replace('.', ',')
				tempStr1=str(rateRainAnt)
				rateRainAntN = tempStr1.replace('.', ',')
				error.append(str(contadorLinea))
				error.append(str(rateRainR))
				error.append(str(rateRainAntN))

			rateRainAnt=rateRain

		return error

	def verificaRainfall(self):
		error=[]
		contadorLinea=0
		lineas=self.archi1.readlines()
		linea=lineas[0]
		line=linea.split(';')
		lin = [c.replace(',', '.') for c in line]
		rainfallAnt=float(lin[9])

		dialin=linea.split('/')
		diaMal=dialin[0]
		diaAnt=int(diaMal[-2:])

		for linea in lineas:			
			contadorLinea+=1
			line=linea.split(';')
			lin = [c.replace(',', '.') for c in line]
			rainfall=float(lin[9])

			dialin=linea.split('/')
			diaMal=dialin[0]
			dia=int(diaMal[-2:])

			if (rainfall<0 or rainfall>100) and (dia==diaAnt):
				error.append('ERROR-LLUVIA MIN.MAX.(NEGATIVO O MAYOR DE 100)')
				tempStr=str(rainfall)
				rainfallR = tempStr.replace('.', ',')
				tempStr1=str(rainfallAnt)
				rainfallN = tempStr1.replace('.', ',')
				error.append(str(contadorLinea))
				error.append(str(rainfallR))
				error.append(str(rainfallN))

			difRainfall = rainfall-rainfallAnt

			if (difRainfall>3 or difRainfall<-3) and (dia==diaAnt):
				error.append('WARNING-LLUVIA (VARIACION MAYOR DE 3)')
				tempStr=str(rainfall)
				rainfallR = tempStr.replace('.', ',')
				tempStr1=str(rainfallAnt)
				rainfallN = tempStr1.replace('.', ',')
				error.append(str(contadorLinea))
				error.append(str(rainfallR))
				error.append(str(rainfallN))

			rainfallAnt=rainfall
			diaAnt=dia

		return error

	def verificaPresion(self):
		error=[]
		contadorLinea=0
		lineas=self.archi1.readlines()
		linea=lineas[0]
		line=linea.split(';')
		lin = [c.replace(',', '.') for c in line]
		presionAnt=float(lin[10])

		for linea in lineas:
			contadorLinea+=1
			line=linea.split(';')
			lin = [c.replace(',', '.') for c in line]
			presion=float(lin[10])

			if presion<940 or presion>1050:
				error.append('ERROR-PRESION MIN.MAX.(MENOR DE 940 O MAYOR DE 1050)')
				tempStr=str(presion)
				presionR = tempStr.replace('.', ',')
				tempStr1=str(presionAnt)
				presionAntN = tempStr1.replace('.', ',')
				error.append(str(contadorLinea))
				error.append(str(presionR))
				error.append(str(presionAntN))

			difpresion = presion-presionAnt

			if (difpresion>1) or (difpresion<-1):
				error.append('WARNING-PRESION (VARIACION MAYOR DE 1)')
				tempStr=str(presion)
				presionR = tempStr.replace('.', ',')
				tempStr1=str(presionAnt)
				presionAntN = tempStr1.replace('.', ',')
				error.append(str(contadorLinea))
				error.append(str(presionR))
				error.append(str(presionAntN))

			presionAnt=presion

		return error

	def verificaTinterior(self):
		error=[]
		contadorLinea=0
		lineas=self.archi1.readlines()
		linea=lineas[0]
		line=linea.split(';')
		lin = [c.replace(',', '.') for c in line]
		tempAnt=float(lin[12])

		for linea in lineas:
			contadorLinea+=1
			line=linea.split(';')
			lin = [c.replace(',', '.') for c in line]
			temperatura=float(lin[12])
			difTemp = temperatura-tempAnt

			if temperatura<-10 or temperatura>48:
				error.append('ERROR-TEMPERATURA INTERIOR MAX.MIN.(-10 OR >48)')
				tempStr=str(temperatura)
				temperaturaR = tempStr.replace('.', ',')
				tempStr1=str(tempAnt)
				temperaturaN = tempStr1.replace('.', ',')
				error.append(str(contadorLinea))
				error.append(str(temperaturaR))
				error.append(str(temperaturaN))


			if (difTemp>=1 and difTemp<2) or (difTemp<=-1 and difTemp>-2):
				error.append('WARNING-TEMPERATURA INTERIOR (VARIACION ENTRE 1º Y 2º)')
				tempStr=str(temperatura)
				temperaturaR = tempStr.replace('.', ',')
				tempStr1=str(tempAnt)
				temperaturaN = tempStr1.replace('.', ',')
				error.append(str(contadorLinea))
				error.append(str(temperaturaR))
				error.append(str(temperaturaN))

			elif (difTemp>=2 and difTemp<5) or (difTemp<=-2 and difTemp>-5):
				error.append('WARNING-TEMPERATURA INTERIOR (VARIACION ENTRE 2 Y 5)')
				tempStr=str(temperatura)
				temperaturaR = tempStr.replace('.', ',')
				tempStr1=str(tempAnt)
				temperaturaN = tempStr1.replace('.', ',')
				error.append(str(contadorLinea))
				error.append(str(temperaturaR))
				error.append(str(temperaturaN))

			elif (difTemp>=5) or (difTemp<=-5):
				error.append('ERROR-TEMPERATURA INTERIOR (VARIACION MAYOR DE 5)')
				tempStr=str(temperatura)
				temperaturaR = tempStr.replace('.', ',')
				tempStr1=str(tempAnt)
				temperaturaN = tempStr1.replace('.', ',')
				error.append(str(contadorLinea))
				error.append(str(temperaturaR))
				error.append(str(temperaturaN))
			
			tempAnt=temperatura

		return error

	def verificaHinterior(self):
		errHumedad=[]
		contadorLinea=0
		lineas=self.archi1.readlines()
		linea=lineas[0]
		lin=linea.split(';')
		humAnt=int(lin[13])

		for linea in lineas:
			contadorLinea+=1
			lin=linea.split(';')
			humedad=int(lin[13])
			difHum = humedad-humAnt

			if (humedad>100) or (humedad<0):
				errHumedad.append('ERROR-HUMEDAD INTERIOR MAX.MIN.(NEGATIVA O MAYOR DE 100)')
				humedadR=str(humedad)
				humedadN=str(humAnt)
				errHumedad.append(str(contadorLinea))
				errHumedad.append(str(humedadR))
				errHumedad.append(str(humedadN))

			if (difHum>5) or (difHum<-5):
				errHumedad.append('WARNING-HUMEDAD INTERIOR (VARIACION MAS DE 5)')
				humedadR=str(humedad)
				humedadN=str(humAnt)
				errHumedad.append(str(contadorLinea))
				errHumedad.append(str(humedadR))
				errHumedad.append(str(humedadN))
			
			humAnt=humedad

		return errHumedad

	def verificaRafaga(self):
		error=[]
		contadorLinea=0
		lineas=self.archi1.readlines()
		linea=lineas[0]
		line=linea.split(';')
		lin = [c.replace(',', '.') for c in line]
		vientoAnt=float(lin[14])

		for linea in lineas:
			contadorLinea+=1
			line=linea.split(';')
			lin = [c.replace(',', '.') for c in line]
			viento=float(lin[14])
			difViento = viento-vientoAnt

			if viento < 0 or viento > 100:
				error.append('ERROR-RAFAGA MAX.MIN.(NEGATIVO O MAYOR DE 100)')
				tempStr=str(viento)
				vientoR = tempStr.replace('.', ',')
				tempStr1=str(vientoAnt)
				vientoN = tempStr1.replace('.', ',')
				error.append(str(contadorLinea))
				error.append(str(vientoR))
				error.append(str(vientoN))

			if (difViento>40) or (difViento<-40):
				error.append('WARNING-RAFAGA (VARIACION MAYOR DE 40)')
				tempStr=str(viento)
				vientoR = tempStr.replace('.', ',')
				tempStr1=str(vientoAnt)
				vientoN = tempStr1.replace('.', ',')
				error.append(str(contadorLinea))
				error.append(str(vientoR))
				error.append(str(vientoN))

			vientoAnt=viento

		return error

	def verificaWindChill(self):
		error=[]
		contadorLinea=0
		lineas=self.archi1.readlines()
		linea=lineas[0]
		line=linea.split(';')
		lin = [c.replace(',', '.') for c in line]
		tempAnt=float(lin[15])

		for linea in lineas:
			contadorLinea+=1
			line=linea.split(';')
			lin = [c.replace(',', '.') for c in line]
			temperatura=float(lin[15])
			difTemp = temperatura-tempAnt

			if temperatura<-10 or temperatura>50:
				error.append('ERROR-WIND CHILL MAX.MIN.(MENOR DE -10 O MAYOR DE 50)')
				tempStr=str(temperatura)
				temperaturaR = tempStr.replace('.', ',')
				tempStr1=str(tempAnt)
				temperaturaN = tempStr1.replace('.', ',')
				error.append(str(contadorLinea))
				error.append(str(temperaturaR))
				error.append(str(temperaturaN))

#			if (difTemp>=1 and difTemp<3) or (difTemp<=-1 and difTemp>-3):
#				error.append('WARNING-WIND CHILL (VARIACION ENTRE 1 Y 3 GRADOS)')
#				tempStr=str(temperatura)
#				temperaturaR = tempStr.replace('.', ',')
#				tempStr1=str(tempAnt)
#				temperaturaN = tempStr1.replace('.', ',')
#				error.append(str(contadorLinea))
#				error.append(str(temperaturaR))
#				error.append(str(temperaturaN))

			elif (difTemp>=5) or (difTemp<=-5):
				error.append('ERROR-WIND CHILL (VARIACION MAS DE 5 GRADOS)')
				tempStr=str(temperatura)
				temperaturaR = tempStr.replace('.', ',')
				tempStr1=str(tempAnt)
				temperaturaN = tempStr1.replace('.', ',')
				error.append(str(contadorLinea))
				error.append(str(temperaturaR))
				error.append(str(temperaturaN))
			
			tempAnt=temperatura

		return error

	def verificaHeatIndex(self):
		error=[]
		contadorLinea=0
		lineas=self.archi1.readlines()
		linea=lineas[0]
		line=linea.split(';')
		lin = [c.replace(',', '.') for c in line]
		tempAnt=float(lin[16])

		for linea in lineas:
			contadorLinea+=1
			line=linea.split(';')
			lin = [c.replace(',', '.') for c in line]
			temperatura=float(lin[16])
			difTemp = temperatura-tempAnt

			if temperatura<-10 or temperatura>50:
				error.append('ERROR-HEAT INDEX MAX.MIN.(-10 MAYOR DE 50)')
				tempStr=str(temperatura)
				temperaturaR = tempStr.replace('.', ',')
				tempStr1=str(tempAnt)
				temperaturaN = tempStr1.replace('.', ',')
				error.append(str(contadorLinea))
				error.append(str(temperaturaR))
				error.append(str(temperaturaN))


			if (difTemp>=1 and difTemp<3) or (difTemp<=-1 and difTemp>-3):
				error.append('WARNING-HEAT INDEX (VARIACION ENTRE 1 Y 3 GRADOS)')
				tempStr=str(temperatura)
				temperaturaR = tempStr.replace('.', ',')
				tempStr1=str(tempAnt)
				temperaturaN = tempStr1.replace('.', ',')
				error.append(str(contadorLinea))
				error.append(str(temperaturaR))
				error.append(str(temperaturaN))

			elif (difTemp>=3) or (difTemp<=-3):
				error.append('ERROR-HEAT INDEX (VARIACION MAYOR DE 3 GRADOS)')
				tempStr=str(temperatura)
				temperaturaR = tempStr.replace('.', ',')
				tempStr1=str(tempAnt)
				temperaturaN = tempStr1.replace('.', ',')
				error.append(str(contadorLinea))
				error.append(str(temperaturaR))
				error.append(str(temperaturaN))
			
			tempAnt=temperatura

		return error

	def verificaTaparente(self):
		error=[]
		contadorLinea=0
		lineas=self.archi1.readlines()
		linea=lineas[0]
		line=linea.split(';')
		lin = [c.replace(',', '.') for c in line]
		tempAnt=float(lin[21])

		for linea in lineas:
			contadorLinea+=1
			line=linea.split(';')
			lin = [c.replace(',', '.') for c in line]
			temperatura=float(lin[21])
			difTemp = temperatura-tempAnt

			if temperatura<-10 or temperatura>50:
				error.append('ERROR-TEMPERATURA APARENTE MAX.MIN.(MENOR DE -10 O MAYOR DE 50)')
				tempStr=str(temperatura)
				temperaturaR = tempStr.replace('.', ',')
				tempStr1=str(tempAnt)
				temperaturaN = tempStr1.replace('.', ',')
				error.append(str(contadorLinea))
				error.append(str(temperaturaR))
				error.append(str(temperaturaN))


			if (difTemp>=2 and difTemp<3) or (difTemp<=-2 and difTemp>-3):
				error.append('WARNING-TEMPERATURA APARENTE (VARIACION ENTRE 2 Y 3 GRADOS)')
				tempStr=str(temperatura)
				temperaturaR = tempStr.replace('.', ',')
				tempStr1=str(tempAnt)
				temperaturaN = tempStr1.replace('.', ',')
				error.append(str(contadorLinea))
				error.append(str(temperaturaR))
				error.append(str(temperaturaN))

			elif (difTemp>=3) or (difTemp<=-3):
				error.append('ERROR-TEMPERATURA APARENTE (VARIACION MAYOR DE 3 GRADOS)')
				tempStr=str(temperatura)
				temperaturaR = tempStr.replace('.', ',')
				tempStr1=str(tempAnt)
				temperaturaN = tempStr1.replace('.', ',')
				error.append(str(contadorLinea))
				error.append(str(temperaturaR))
				error.append(str(temperaturaN))
			
			tempAnt=temperatura

		return error

	def verificaDirViento(self):
		error=[]
		contadorLinea=0
		lineas=self.archi1.readlines()

		for linea in lineas:
			contadorLinea+=1
			line=linea.split(';')
			viento=int(line[24])

			if viento < 0 or viento > 360:
				error.append('ERROR-DIRECCION DEL VIENTO (NEGATIVA O MAYOR DE 360)')
				error.append(str(contadorLinea))
				error.append(str(viento))
				error.append(str(viento))

		return error

	def verificaLLuviaMediaNoche(self):
		try:
			error=[]
			contadorLinea=0
			lineas=self.archi1.readlines()
			linea=lineas[0]
			line=linea.split(';')
			lin = [c.replace(',', '.') for c in line]
			rainfallAnt=float(lin[26])

			dialin=linea.split('/')
			diaMal=dialin[0]
			diaAnt=int(diaMal[-2:])

			for linea in lineas:						
				contadorLinea+=1
				line=linea.split(';')

#				if len(line)>26:
#					raise ValueError

				lin = [c.replace(',', '.') for c in line]				
				rainfall=float(lin[26])

				dialin=linea.split('/')
				diaMal=dialin[0]
				dia=int(diaMal[-2:])

				if (rainfall < 0 or rainfall > 60) and (dia==diaAnt):
					error.append('ERROR-LLUVIA DESDE MEDIANOCHE MIN.MAX.(NEGATIVO O MAYOR DE 100)')
					tempStr=str(rainfall)
					rainfallR = tempStr.replace('.', ',')
					tempStr1=str(rainfallAnt)
					rainfallN = tempStr1.replace('.', ',')
					error.append(str(contadorLinea))
					error.append(str(rainfallR))
					error.append(str(rainfallN))

				difRainfall = rainfall-rainfallAnt

				if (difRainfall>=3 or difRainfall<=-3) and (dia==diaAnt):
					error.append('WARNING-LLUVIA DESDE MEDIANOCHE (VARIACION MAYOR DE 3)')
					tempStr=str(rainfall)
					rainfallR = tempStr.replace('.', ',')
					tempStr1=str(rainfallAnt)
					rainfallN = tempStr1.replace('.', ',')
					error.append(str(contadorLinea))
					error.append(str(rainfallR))
					error.append(str(rainfallN))

				rainfallAnt=rainfall
				diaAnt=dia

			return error


		except TypeError:
			mb.showinfo('ERROR', 'Error linea ', errorLin)
		except ValueError:
			mb.showinfo('ERROR', 'ValueError. ')
		except AttributeError:
			mb.showinfo('ERROR', 'Abra un fichero LOG de cumulus.')
		except IndexError:
			mb.showinfo('ERROR', 'linea no existe.')
		except FileNotFoundError:
			mb.showinfo('ERROR', 'Abra un fichero LOG de cumulus.')

ap1=Aplicacion()
