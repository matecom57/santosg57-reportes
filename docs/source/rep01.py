file = 'memoria_todas_oct3025.txt'

fil = open(file, 'r')

datos = fil.readlines()

print(len(datos))

i=0
while i < len(datos):
  ss = datos[i]
  ss = ss.replace('\n', '')
  if '-----------' in ss:
    j = i+3
    ss = datos[j]
    ss = ss.replace('\n', '')
    print(ss)
    if 'total' in ss:
       
       k = ss.find('total')
       mem = datos[j+1]
       mem = mem.replace('\n', '')
       memoria = mem[k:(k+5)]
       print(memoria)
       i = j
  i = i+1








