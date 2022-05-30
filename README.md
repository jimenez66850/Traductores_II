# Traductores_II

El programa contiene 3 archivos de texto:
    program.txt
    AnalizadorLexico.txt
    ArbolSintactico.txt
y 2 archivos .py:
    tokens.py
    main.py

program.txt: 
    Dentro de este archivo, el usuario escribira el programa a analizar (dejaré un ejemplo dentro para compilar).

AnalizadorLéxico.txt:
    Dentro de este archivo, se encontrará una tabla con el resultado del analizador 
    lexico, formado con una tabla de la siguiente manera: 
        Contenido: [   ] Simbolo: [   ] Tipo: [    ]

ArbolSintactico.txt:
    Dentro de este archivo, se encontrará el árbol síntactico formado por el programa, donde cada tabulación depende del nivel del árbol.

tokens.py:
    Dentro de este archivo, se encuentran todas las clases implementadas dentro del programa.

main.py: 
    Dentro de este archivo, se encuentran todo el programa. 

Manejo de excepciones: 

Dentro del programa manejo 4 excepciones:
    
    OpOrError
    OpAndError
    InvalidString
    SyntaxError

    OpOrError:
        Este error ocurre a nivel lexico, este se presenta cuando el usuario solo ingreso un | en vez de los 2 necesarios para el operador or (||)
    
    OpAndError:
        Este error ocurre a nivel lexico, este se presenta cuando el usuario solo ingreso un & en vez de los 2 necesarios para el operador or (&&)
    
    InvalidString:
        Este error ocurre a nivel lexico, este se presenta cuando una cadena de texto no fue abierta o cerrada correctamente.
    
    SyntaxError: 
        Este error ocurre a nivel sintactico, este nos indica que hay un error en la sintaxis del programa, devuelto por la tabla sintactica. 

            








    