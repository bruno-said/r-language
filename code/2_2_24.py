import math
import matplotlib as mpl
import matplotlib.pyplot as plt

def f ( x ):
  return ( 1 + x ** 9 ) / ( 1 + x ** 15 )

limit = -1;

x = [];

for i in range( 3 ):
  x.append( limit + ( 10 ** ( - ( i + 1 ) ) ) )

for i in range( 3 ):
  x.append( limit - ( 10 ** ( i - 3 ) ) )

print( x )

y = []

for i in range( len( x ) ):
  y.append( f ( x[ i ] ) )

print( 'x      | y = f(x)' )
print( '-----------------' )

for i in range( len( x ) ):
  print( '{:.4f} | {:.6f}'.format( x[ i ], y[ i ] ) )

mpl.rcParams.update({
  'font.family': 'Times New Roman',
  'font.size': 10
})

plt.scatter( x, y )
plt.title( 'Verificando o limite de f(x) quando x tende a 0' )
plt.ylabel( 'f(x)' )
plt.xlabel( 'x' )
plt.grid()
plt.show()