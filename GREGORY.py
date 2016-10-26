# -*- coding: utf-8 -*-

from mechanize import Browser
from bs4 import BeautifulSoup
import timeit
import unicodedata
import encodings
import os,sys

busc=raw_input('QUE DESEAS BUSCAR?'+'\n')

inicio1=timeit.default_timer()
print 'BUSCANDO EN GOOGLE  ........'+'\n'
if busc=='pythan':
	obag='.python'
else:
	obag=busc
if busc=='pythen':
	obag='.python'
if busc=='pythin':
	obag='.python'
if busc=='python':
	obag='.python'
if busc=='pythun':
	obag='.python'


br = Browser()

br.set_handle_robots( False )
br.addheaders = [('User-agent', 'Chrome')]
br.open( "http://google.com" )

br.select_form( 'f' )
br.form[ 'q' ] = obag

br.submit()

b=''
for b1 in obag:
	if b1==' ':
		b=b+'+'
	else:
		b=b+b1

principal=''

soup = BeautifulSoup(br.response().read())
for i,link in enumerate(soup.find_all('a')):
    principal=principal+(str(link.get('href'))+'\n')

duno=0
for x in principal:
	if x=='\n':
		duno=duno+1


d0=0
google=''


for x in principal:
	if x=='\n':
		d0=d0+1
	if d0==18 and x!='\n':
		google=google+x
	if d0==19:
		break
googlelink1=google

google=''

d0=0
dun=duno-18
for y1 in principal:
	if y1=='\n':
		d0=d0+1
	if d0==dun and y1!='\n':
		google=google+y1
	if d0>dun:
		break
googlelink2=google

google=''


d0=0
dun=duno-17
for y2 in principal:
	if y2=='\n':
		d0=d0+1
	if d0==dun and y2!='\n':
		google=google+y2
	if d0>dun:
		break
googlelink3=google

google=''


d0=0
dun=duno-16
for y3 in principal:
	if y3=='\n':
		d0=d0+1
	if d0==dun and y3!='\n':
		google=google+y3
	if d0>dun:
		break
googlelink4=google

google=''



d0=0
dun=duno-15
for y4 in principal:
	if y4=='\n':
		d0=d0+1
	if d0==dun and y4!='\n':
		google=google+y4
	if d0>dun:
		break
googlelink5=google

google=''



d0=0
dun=duno-14
for y5 in principal:
	if y5=='\n':
		d0=d0+1
	if d0==dun and y5!='\n':
		google=google+y5
	if d0>dun:
		break
googlelink6=google

google=''





d0=0
dun=duno-13
for y6 in principal:
	if y6=='\n':
		d0=d0+1
	if d0==dun and y6!='\n':
		google=google+y6
	if d0>dun:
		break
googlelink7=google

google=''




d0=0
dun=duno-12
for y7 in principal:
	if y7=='\n':
		d0=d0+1
	if d0==dun and y7!='\n':
		google=google+y7
	if d0>dun:
		break
googlelink8=google

google=''



d0=0
dun=duno-11
for y8 in principal:
	if y8=='\n':
		d0=d0+1
	if d0==dun and y8!='\n':
		google=google+y8
	if d0>dun:
		break
googlelink9=google

google=''



d0=0
dun=duno-10
for y9 in principal:
	if y9=='\n':
		d0=d0+1
	if d0==dun and y9!='\n':
		google=google+y9
	if d0>dun:
		break
googlelink10=google

google=''



d0=0
d1=0
d2=0
d3=0
imgt=''
img=''
for y10 in principal:
	
	if y10=='\n':
		d0=d0+1
		d1=0
		d2=0
		if img=='/images?':
			googlelinkimg=imgt

			d3=1
			img=''
			imgt=''
		else:
			img=''
			imgt=''

	if d0==1 and y10!='\n':
		d1=d1+1
		img=img+y10
		if d1==7 and img=='/images':
			
			imgt=imgt+img
			
		if d1>=8:
			
			
			d0=0
			d2=1
			

	if d2==1:
		imgt=imgt+y10
			
	if d3==1:
		break


googlepaginas=['']*20
googlepagina1=''
googlepagina2=''
googlepagina3=''
googlepagina4=''
googlepagina5=''
googlepagina6=''
googlepagina7=''
googlepagina8=''
googlepagina9=''
googlepagina10=''
googlepagina11=''
googlepagina12=''
googlepagina13=''
googlepagina14=''
googlepagina15=''
googlepagina16=''
googlepagina17=''
googlepagina18=''
googlepagina19=''
googlepagina20=''


googletitulos=['']*20
googletitulo1=''
googletitulo2=''
googletitulo3=''
googletitulo4=''
googletitulo5=''
googletitulo6=''
googletitulo7=''
googletitulo8=''
googletitulo9=''
googletitulo10=''
googletitulo11=''
googletitulo12=''
googletitulo13=''
googletitulo14=''
googletitulo15=''
googletitulo16=''
googletitulo17=''
googletitulo18=''
googletitulo19=''
googletitulo20=''


googletextos=['']*20
googletextosfin=['']*20
googletexto1=''
googletexto2=''
googletexto3=''
googletexto4=''
googletexto5=''
googletexto6=''
googletexto7=''
googletexto8=''
googletexto9=''
googletexto10=''
googletexto11=''
googletexto12=''
googletexto13=''
googletexto14=''
googletexto15=''
googletexto16=''
googletexto17=''
googletexto18=''
googletexto19=''
googletexto20=''



d=0
filtro=''
br.open("http://google.com"+googlelink1)
soup1 = BeautifulSoup(br.response().read())


for j,hit in enumerate(soup1.findAll(attrs={'class' : 'r'})):
	try:
		ch=str(hit.a)

		comparador=''
		cuenta=0
		cuenta1=0

		for jala in ch:
			
			cuenta=cuenta+1
			if jala=='h' and cuenta>4:

				for jala1 in ch:
					cuenta1=cuenta1+1
					if cuenta1 >= cuenta and jala1!='&':
						comparador=comparador+jala1
					if jala1=='&':
						sab1=len(jala1)
						for x in range(1,(sab1+1)):
							jala1=''
						sab2=len(jala)
						for x in range(1,(sab2+1)):
							jala=''
						sab3=len(ch)
						for x in range(1,(sab3+1)):
							ch=''
						break
		
				
			
		bender=0
		fry=''
		if comparador=='':
			googlepaginas[d]='-'
			
			d=d+1
		
		for h in str(comparador):
			
			bender=bender+1
			fry=fry+h

			if  bender==4 and fry=='http':
				
				googlepaginas[d]=str(comparador)
				d=d+1
				
				break
			
			

			if bender==5:
				googlepaginas[d]='-'
			
				d=d+1
				
				break


		comparador=''
		
	except:
		pass


harr=''
harr1=0
harr2=''
googlepaginasfin=['']*20

for i in range(0,20):
	harr=googlepaginas[i]
	for j in harr:
		harr2=harr2+j
		harr1=harr1+1
		if harr2=='http://www.youtube.com' and harr1==22:
			googlepaginasfin[i]='-'
			harr2=''
			harr1=0
			break
		if harr1==23:
			googlepaginasfin[i]=googlepaginas[i]
			harr2=''
			harr1=0
			break
		if harr2=='-':
			googlepaginasfin[i]='-'
			harr2=''
			harr1=0
			break

print googlepaginasfin[:]

tit=''
num=0
num1=0
tit1=''
tit2=''
control=0
salida=''
ermest=0
sapeo=0
gab=''
for hit in enumerate(soup1.findAll(attrs={'class' : 'r'})):
	try:
		for x in str(hit):
			tit=tit+x
			num=num+1
		
		
		for y in range(1,(num)):
			if tit[num-y]=='"':
				break
			else:
				
				tit1=tit1+tit[num-y]
				num1=num1+1
		

		for z in range(1,num1):
			tit2=tit2+tit1[num1-z]
		may=tit2
		
		for a in may:
			if a=='>':
				control=1
			if a=='<':
				control=0
			if control==1 and a!='>':
				salida=salida+a
		pap=0
		guarda=''
		mmm=''
		qqq=unicode('imágene','utf-8')		
		for go in salida:
			pap=pap+1
			guarda=guarda+go
			if pap==8:
				
				mmm=guarda.lower()
				nnn=unicode(mmm,'utf-8')
								
				if nnn==qqq:
					gab=gab+str(ermest)

			if pap==9:
				break	
		googletitulos[ermest]=str(salida)
		ermest=ermest+1

		num=0
		num1=0
		tit=''
		tit1=''
		tit2=''
		salida=''
	except:
		pass
print '\n'
print googletitulos[:]
print gab







control1=0
salida1=''
branigan=0

for hit in enumerate(soup1.findAll(attrs={'class' : 'st'})):

	try:
			
		for c in str(hit):
			if c=='>':
				control1=1
			if c=='<':
				control1=0
			if control1==1 and c!='>' and c!='<' and c!=')':
				salida1=salida1+c

		
		googletextos[branigan]=str(salida1)
			
		branigan=branigan+1

		salida1=''
		control1=0
		zap=0
	except:
		pass

if gab=='':
	for o in range(0,20):
		googletextosfin[o]=googletextos[o]

else:
	for s in gab:

		for l in range(0,20):
			if googletextos[l]=='':
				break
			if int(l)<int(s):
				googletextosfin[l]=googletextos[l]
				
			if int(l)==int(s):

				googletextosfin[int(s)]='-'
				googletextosfin[int(s)+1]=googletextos[int(s)]
				
				
			if int(l)>int(s) :
				googletextosfin[l+1]=googletextos[int(l)]
			



		



print '\n'
print googletextosfin[:]
print '\n'
print 'BUSCANDO EN bing.......'+('\n'*3)

br.open( "http://bing.com" )
br.select_form( nr=0 )
br.form[ 'q' ] = obag
br.submit()
binghtml=''
inicio1=timeit.default_timer()
soup = BeautifulSoup(br.response().read())

for i,link in enumerate(soup.find_all('a')):

    binghtml=binghtml+(str(link.get('href'))+'\n')

a=''

for mod in obag:
	if mod==' ':
		a=a+'+'
	else:
		a=a+mod
lin1='/search?q='+a+'&go=&qs=ds&lf=1&qpvt='+a
lin2='/search?q='+a+'&go=&qs=ds&first=11&FORM=PERE'
lin3='/search?q='+a+'&go=&qs=ds&first=21&FORM=PERE1'
lin4='/search?q='+a+'&go=&qs=ds&first=31&FORM=PERE2'
lin5='/search?q='+a+'&go=&qs=ds&first=41&FORM=PERE3'
lin6='/images/search?q='+a+'&FORM=HDRSC2'
bingpagina1=''
bingpagina2=''
bingpagina3=''
bingpagina4=''
bingpagina5=''
bingimagenes=''


euro=''
for lin in binghtml:	
	if lin=='\n':


		if euro == lin1:
			bingpagina1=euro
			eouro=''
			
		if euro == lin2:
			bingpagina2=euro
			eouro=''
		
		if euro == lin3:
			bingpagina3=euro
			eouro=''
		
		if euro == lin4:
			bingpagina4=euro
			eouro=''

		
		if euro == lin5:
			bingpagina5=euro
			eouro=''

		if euro == lin6:
			bingimagenes=euro
			eouro=''
		else:
			euro=''
	else:
		euro=euro+lin
			
bingpaginas=['']*20
bingtitulos=['']*20
bingtextos=['']*20
br.open('http://bing.com'+bingpagina1)
soup1 = BeautifulSoup(br.response().read())
relog=0
for link in soup1.findAll(attrs={'class' : "b_algo"}):
	try:
		

		
		man=str(link.a)
		bingcont=0
		bingpag=''

		for guf in man:
			if guf=='"':
				bingcont=bingcont+1
			if bingcont==3 and guf!='"':
				bingpag=bingpag+guf
			if bingcont==4:
				
				bingpaginas[relog]=bingpag
				break

		men=str(link.a)
		bingtitulo=''
		aut=0
		for guf in men:
			if guf=='>':
				aut=1
			if guf=='<':
				aut=0
			if aut==1 and guf!='>':
				bingtitulo=bingtitulo+guf
		
		bingtitulos[relog]=bingtitulo
		bingtextos[relog]=link.text
		
		

	except:
		pass
	
	
	relog=relog+1				
print bingpaginas
print '\n'
print bingtitulos
print '\n'
print bingtextos


#
print '\n'
print 'BUSCANDO EN YAHOO .........'+'\n'

yahoob=''
for a in obag:
	if a==' ':
		yahoob=yahoob+'+'
	else:
		yahoob=yahoob+a

br=Browser()
br.set_handle_robots(False)
br.addheaders=[('User-agent','Chrome')]
br.open('https://espanol.search.yahoo.com/search?cs=bz&p='+yahoob+'&fr=fp-tts-706&fr2=ps&woeid=376229&fp=1')
br.submit
yahoohtml=''
soupyahoo = BeautifulSoup(br.response().read())
for link in (soupyahoo.find_all('a')):
	yahoohtml=yahoohtml+(str(link.get('href'))+'\n')


acumulador=''

yahooenlace1=''
yahooenlace2=''
yahooenlace3=''
yahooenlace4=''
yahooenlace5=''
yahooimagenes=''

contyahoo=0

tot=0
for mza0 in yahoohtml:
	if mza0=='\n':
		tot=tot+1

for mza in yahoohtml:
	
	if mza=='\n':
		contyahoo=contyahoo+1
		if contyahoo==27:
			yahooimagenes=acumulador
			acumulador=''
		if contyahoo==33:
			yahooenlace1=acumulador
			acumulador=''
		if contyahoo==(tot-9):
			yahooenlace2=acumulador
			acumulador=''
		if contyahoo==(tot-8):
			yahooenlace3=acumulador
			acumulador=''
		if contyahoo==(tot-7):
			yahooenlace4=acumulador
			acumulador=''
		if contyahoo==(tot-6):
			yahooenlace5=acumulador
			acumulador=''		
		else:
			acumulador=''




	else:
		acumulador=acumulador+mza

yahoopaginas=['']*20
yahootitulos=['']*20
yahootextos=['']*20
br.open(str(yahooenlace1))
yahooex=''
yahoocont=0
yahoosalida=''
yahoosalida1=''
yahookey=0
mm=''
yahooguia=0
souphtml=BeautifulSoup(br.response().read())
for link in souphtml.findAll(attrs={'class' : "yschttl spt"}):

	yahooex=''
	yahooex=str(link)
	for y in yahooex: 
		if y=='"':
			yahoocont=yahoocont+1
		if yahoocont==5 and y!='"':
			yahoosalida=yahoosalida+y
		if yahoocont==6:
			rat=0
			for m in yahoosalida:
				rat=rat+1
				mm=mm+m
				if rat==4 and mm=='http':
					#print yahoosalida
					yahoopaginas[yahooguia]=yahoosalida
					break
				if rat==4 and mm!='http':
					#print '-'
					yahoopaginas[yahooguia]='-'
					break
				
				
			yahoocont=0
			mm=''
			yahoosalida=''
			break


	for z in yahooex:
		if z=='>':
			yahookey=1
		if z=='<':
			yahookey=0
		if yahookey==1 and z!='>':
			yahoosalida1=yahoosalida1+z

	
	yahootitulos[yahooguia]=yahoosalida1

	yh1=unicode(' Búsqueda de video ','utf-8')
	yh5=unicode(' Resultados de imágenes','utf-8')
	yh2=0
	yh3=''

	for yh in yahoosalida1:
		if yh=='-':
			yh2=1
		if yh2==1 and yh!='-':
			yh3=yh3+yh
	
	yh4=unicode(yh3,'utf-8')
	if yh4==yh1:
		yahootextos[yahooguia]='-'
		
	if yh4==yh5:
		yahootextos[yahooguia]='-'
		




	yahoosalida1=''
	yahookey=0
	yahooguia=yahooguia+1





print '\n'
print yahoopaginas
print '\n'
print yahootitulos
print '\n'


yahoosalidatexto=''
textokey=0
yahootextsalida=''
yahoopaso=0
for link in souphtml.findAll(attrs={'class' : "abstr"}):
	
	yahoosalidatexto=str(link) 
	for x in yahoosalidatexto:
		if x=='>':
			textokey=1
		if x=='<':
			textokey=0
		if textokey==1 and x!='>':
			yahootextsalida=yahootextsalida+x

	

	if yahootextos[yahoopaso]=='-':
		yahootextos[yahoopaso+1]=yahootextsalida
		yahoopaso=yahoopaso+1
	else:
		yahootextos[yahoopaso]=yahootextsalida


	textokey=0
	yahoosalidatexto=''
	yahootextsalida=''
	yahoopaso=yahoopaso+1


print yahootextos

fin=timeit.default_timer()
tiempototal= fin-inicio1
print '___________________________________________________________'
print 'TIEMPO TOTAL TRANSCURRIDO:  %.3f'%tiempototal,'[SEGUNDOS]'
raw_input('ENTER PARA SALIR')
