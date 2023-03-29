from Token import Token

class Automata:
    letras = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s", "t", "u","v","w","x","y","z", "-"]
    numeros = ["1","2","3","4","5","6","7","8","9","0", "."]
    tabla_tokens = []
    cadena = ""
    fila = 0
    columna = 0
    estado_actual = 0
    estado_anterior = 0
    estados_aceptacion = [9]

    def guardar_token(self, lexema):
        nuevo_token = Token(self.fila, self.columna, lexema)
        self.tabla_tokens.append(nuevo_token)

    def analizar(self, cadena):
        operaciones = []
        token = ""
        tipo_operacion = ""

        while len(cadena) > 0:
            char = cadena[0]

            #ignorando espacios en blanco
            if char == "\n":
                self.fila += 1
                self.columna = 0
                cadena = cadena[1:]
                continue
            elif char == " ":
                self.columna += 1
                cadena = cadena[1:]
                continue

            if self.estado_actual == 0:
                if char == "{":
                    self.guardar_token(char)
                    self.estado_anterior = 0
                    self.estado_actual = 1

            elif self.estado_actual == 1:
                if char == '"':
                    self.guardar_token(char)
                    self.estado_anterior = 1
                    self.estado_actual = 2
                elif char == "{":
                    self.guardar_token(char)
                    self.estado_anterior = 1
                    self.estado_actual = 10

            elif self.estado_actual == 2:
                if char.lower() in self.letras:
                    token += char
                    self.estado_anterior = 2
                    self.estado_actual = 3
            
            elif self.estado_actual == 3:
                if char.lower() in self.letras:
                    token += char
                    self.estado_anterior = 3
                    self.estado_actual = 3
                elif char == '"':
                    self.guardar_token(token)
                    token = ""
                    self.guardar_token(char)
                    self.estado_anterior = 3
                    self.estado_actual = 4
            
            elif self.estado_actual == 4:
                if char == ":":
                    self.guardar_token(char)
                    self.estado_anterior = 4
                    self.estado_actual = 5

            elif self.estado_actual == 5:
                if char == '"':
                    self.guardar_token(char)
                    self.estado_anterior = 5
                    self.estado_actual = 6

            elif self.estado_actual == 6:
                if char.lower() in self.letras:
                    token += char
                    self.estado_anterior = 6
                    self.estado_actual = 7

            elif self.estado_actual == 7:
                if char.lower() in self.letras:
                    token += char
                    self.estado_anterior = 7
                    self.estado_actual = 7
                elif char == '"':
                    self.guardar_token(token)
                    token = ""
                    self.guardar_token(char)
                    self.estado_anterior = 7
                    self.estado_actual = 8

            elif self.estado_actual == 8:
                if char == "}":
                    self.guardar_token(char)
                    self.estado_anterior = 8
                    self.estado_actual = 9
                elif char == ",":
                    self.guardar_token(char)
                    self.estado_anterior = 8
                    self.estado_actual = 1

            elif self.estado_actual == 10:
                if char == '"':
                    self.guardar_token(char)
                    self.estado_anterior = 10
                    self.estado_actual = 11

            elif self.estado_actual == 11:
                if char.lower() in self.letras:
                    token += char
                    self.estado_anterior = 11
                    self.estado_actual = 12

            elif self.estado_actual == 12:
                if char.lower() in self.letras:
                    token += char
                    self.estado_anterior = 12
                    self.estado_actual = 12
                elif char == '"':
                    self.guardar_token(token)
                    token = ''
                    self.guardar_token(char)
                    self.estado_anterior = 12
                    self.estado_actual = 13

            elif self.estado_actual == 13:
                if char == ':':
                    self.guardar_token(char)
                    self.estado_anterior = 13
                    self.estado_actual = 14

            elif self.estado_actual == 14:
                if char == '"':
                    self.guardar_token(char)
                    self.estado_anterior = 14
                    self.estado_actual = 15

                if char.lower() in self.numeros:
                    token += char
                    self.estado_anterior = 14
                    self.estado_actual = 18
                
                if char == '[':
                    self.guardar_token(char)
                    self.estado_anterior = 14
                    self.estado_actual = 19

            elif self.estado_actual == 15:
                if char.lower() in self.letras:
                    token += char
                    self.estado_anterior = 15
                    self.estado_actual = 16

            elif self.estado_actual == 16:
                if char.lower() in self.letras:
                    token += char
                    self.estado_anterior = 16
                    self.estado_actual = 16
                elif char == '"':
                    self.guardar_token(token)
                    #guardando el tipo de operacion
                    tipo_operacion = token
                    token = ""
                    self.guardar_token(char)
                    self.estado_anterior = 16
                    self.estado_actual = 17
                    #aqui iria la clase recursiva de las operaciones
                    #en donde las opera y las guarda de una vez
                    #en la lista de cadena

            elif self.estado_actual == 17:
                if char == ",":
                    self.guardar_token(char)
                    self.estado_anterior = 17
                    self.estado_actual = 10
                    
            elif self.estado_actual == 18:
                if char.lower() in self.numeros:
                    token += char
                    self.estado_anterior = 18
                    self.estado_actual = 18
                elif char == ",":
                    self.guardar_token(token)
                    operaciones.append(token)
                    token = ""
                    self.guardar_token(char)
                    self.estado_anterior = 18
                    self.estado_actual = 10
                elif char == "]":
                    self.guardar_token(token)
                    operaciones.append(token)
                    token = ""
                    self.guardar_token(char)
                    self.estado_anterior = 18
                    self.estado_actual = 20
                elif char == "}":
                    self.guardar_token(token)
                    operaciones.append(token)
                    token = ""
                    self.guardar_token(char)
                    self.estado_anterior = 18
                    self.estado_actual = 21
                    #Aqui denuevo va la recursividad
                    #return esa vaina va a estar horrible

            elif self.estado_actual == 19:
                if char == '"':
                    self.guardar_token(char)
                    self.estado_anterior = 19
                    self.estado_actual = 11

            elif self.estado_actual == 20:
                if char == ",":
                    self.guardar_token(char)
                    self.estado_anterior = 20
                    self.estado_actual = 10
                    #otra vez la operacion la puta madre
                    #retunr operacion y tal
                elif char == "]":
                    self.guardar_token(char)
                    self.estado_anterior = 20
                    self.estado_actual = 20
                elif char == "}":
                    self.guardar_token(char)
                    self.estado_anterior = 20
                    self.estado_actual = 21
                    #operaciones everywhere
                    #retunr asjjas

            elif self.estado_actual == 21:
                if char == ",":
                    self.guardar_token(char)
                    self.estado_anterior = 21
                    self.estado_actual = 1
                elif char == "}":
                    self.guardar_token(char)
                    self.estado_anterior = 21
                    self.estado_actual = 9

            self.columna += 1
            cadena = cadena[1:]

        #OPERACIONES DENUVEO Y TAL
        # RETURN AJSJASJAS
        # 
    def detectar_operacion(self):
        for token in self.tabla_tokens:
            if token.lexema == "Suma":
                print("se encontro una suma")
            elif token.lexema == "Resta":
                print("se encontro una resta")
            elif token.lexema == "Multiplicacion":
                print("se encontro una multiplicacion")
            elif token.lexema == "Division":
                print("se encontro una division")
            elif token.lexema == "Potencia":
                print("se encontro una potencia")
            elif token.lexema == "Raiz":
                print("se encontro una raiz")
            elif token.lexema == "Seno":
                print("se encontro un seno")
            elif token.lexema == "Coseno":
                print("se encontro un coseno")
            elif token.lexema == "Tangente":
                print("se encontro una tangente")

    def imprimir_tokens(self):
        print('-'*31)
        print("| {:<4} | {:<7} | {:<10} |".format('Fila','Columna','Lexema'))    
        print('-'*31)
        for token in self.tabla_tokens:
            print ("| {:<4} | {:<7} | {:<10} |".format(token.fila, token.columna, token.lexema))
        self.tabla_tokens = []
        self.cadena = " "
        self.fila = 0
        self.columna = 0
        self.estado_actual = 0
        self.estado_anterior = 0
        self.estados_aceptacion = [9]
        self.token = " "

    def imprimir_lexemas(self):
        for token in self.tabla_tokens:
            print(token.lexema)
        self.tabla_tokens = []
        self.cadena = ""
        self.fila = 0
        self.columna = 0
        self.estado_actual = 0
        self.estado_anterior = 0
        self.estados_aceptacion = [9]
        self.token = ""

