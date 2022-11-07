import random

class Hat():
    def __init__(self, colores, cantidad):
        contenido1 = len(colores)
        contenido2 = len(cantidad)
        self.contents = []
        
        if(contenido1 != contenido2):
            return print('Valores distintos')

        i = -1
        j = 1
        for n in cantidad:
            i = i + 1
            j = 1
            while j <= n:
                j = j + 1
                self.contents.append(colores[i])
                # print(colores[i], "colores", j, "letra j")
            # print(self.contents)
    
    def draw(self, sacar):
        print(sacar, 'sacar')
        if sacar > len(self.contents):
            return self.contents 
            
        
        ncount = 1
        longitud = len(self.contents) - 1
        while ncount <= sacar:
            ncount = ncount  + 1

            print(ncount)

            if longitud <= 1:
                longitud = 1
                n1 = 0
                
            else:
                longitud = longitud - 1
                n1 = random.randint(1, longitud)

                
            if len(self.contents) <= 0:
                break                
            self.contents.pop(n1)
            # print(self.contents, 'despues')
            return self.contents
    
colores = [
    'black',
    'red',
    'green'
]

cantidad = [
    6, 4, 3
]

colores1 = [
    'red',
    'green'
]

cantidad1 = [
    2,1
]

hat = Hat(colores, cantidad)


def experiment(hat, expected_balls, num_balls_drawn, num_experiments, cantidad1):


    contador = 0    
    contador1 = 0    
    
    n = 1
    while n <= num_experiments:
        n = n + 1
        
        m = hat.draw(num_balls_drawn)    
        # print(m)
    
        bola = expected_balls[0]
        bola1 = expected_balls[1]
        
        if m.index(bola):
            print(m.index(bola), 'el color ', bola, 'existe')
            contador = contador + 1

        if m.index(bola1):
            print(m.index(bola1), 'el color ', bola1, 'existe')
            contador1 = contador1 + 1
            
                    
    # print(m / n)
experiment(hat, colores1, 5, 10, cantidad1)