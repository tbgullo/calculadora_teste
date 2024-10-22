def calculadora(expressao):
    try:
        # Dividimos a expressão em membros e operador
        membros = expressao.split()
        
        # Verificamos se a expressão tem exatamente três partes: número, operador e número
        if len(membros) != 3:
            print(None)
            return
        
        num1 = float(membros[0])  
        operador = membros[1]   
        num2 = float(membros[2]) 

        # Realiza a operação com base no operador fornecido
        if operador == '+':
            resultado = num1 + num2
        elif operador == '-':
            resultado = num1 - num2
        elif operador == '*':
            resultado = num1 * num2
        elif operador == '/':
            if num2 == 0:
                print(None) 
                return
            resultado = num1 / num2
        else:
            print(None)  
            return

        return resultado

    except Exception as e:
        print(None)  

