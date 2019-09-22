def phspprg(width, height, rectangles, sorting="width"):
  
    if sorting not in ["width", "height" ]:
        raise ValueError("The algorithm only supports sorting by width or height but {} was given.".format(sorting))
    if sorting == "width":
        wh = 0
    else:
        wh = 1
    logger.debug('The original array: {}'.format(rectangles))
    result = [None] * len(rectangles) # resulta = [None]
    remaining = deepcopy(rectangles) #Lo que hace es tener en una lista auxiliar, referenciado a los valores iniciales
    for idx, r in enumerate(remaining): #Enumerate, bota un contador y el valor --> (0, rectangle[0])(1, rectangle[1])
        if r[0] > r[1]:
            remaining[idx][0], remaining[idx][1] = remaining[idx][1], remaining[idx][0] #Lo giro 90 grados
    #logger.debug('Swapped some widths and height with the following result: {}'.format(remaining))
    
    sorted_indices = sorted(range(len(remaining)), key=lambda x: -remaining[x][wh]) # sorted_indices = [1, 0]
    '''
    La función sorted puede tener un parametro llamado "key", este manda a la hora de ordenar, 
    si key = len, le decimos que ordene las ids ---> range(n), pero según quien es mayor ---> remaining[x],
    botaría números de 0 a n, ordenados de acuerdo a su peso
    en este caso le decimos que ordene según " - remaining[x][wh] "
    o sea, que de remaining, agarre el primer valor de cada valor, que viene a ser la coordenada " x ",
    pero que lo ponga negativo, o sea, que sea decreciente o reverso, esto podría cambiarse por
    el tercer parámetro que tiene sorted, sería sorted(iterable, key, reverse), sería poner reverse = True
    y tendría el mismo resultado, o eso creo :p
    '''
    #logger.debug('The sorted indices: {}'.format(sorted_indices))
    sorted_rect = [remaining[idx] for idx in sorted_indices] #Acá, según el orden que envía sorted_indices, este agarra  
    #el mismo orden, pero, agarra ya las coordenadas, teniendo un orden a la hora de tratar de ordenar los rectángulos
    #logger.debug('The sorted array is: {}'.format(sorted_rect))
    x, y, w, h, H = 0, 0, 0, 0, 0
    while sorted_indices: #cola  [1, 0]
        idx = sorted_indices.pop(0) #sprted queda con [0] porque le quitas el 1 idx = 1
        r = remaining[idx]  # remain[1] = [10,20] 
        #En el if
        #Acá le está diciendo que, si es que el rectángulo ingresado es mayor a la placa, que lo dibuje igual, y que avise
        #cuando queda de ancho (w), y cuanto es la nueva altura(h), también avisa en donde empieza el siguiente rect (x, y)
        if r[1] > width or r[1] > height:#si la altura es mayor al ancho
            result[idx] = Rectangle(x, y, r[0], r[1])
            x, y, w, h, H = r[0], H, width - r[0], r[1], H + r[1] 
        else: #si la altura es menor al ancho, podemos rotarlo
            result[idx] = Rectangle(x, y, r[1], r[0]) #lo rotamos
            x, y, w, h, H = r[1], H, width - r[1], r[0], H + r[0]#cuando queda de ancho (w), y cuanto es la nueva altura(h),
                                                                 #también avisa en donde empieza el siguiente rect (x, y)
     #       print(x, y, w, h, H)                                      
        recursive_packing(x, y, w, h, 1, remaining, sorted_indices, result)
        x, y = 0, H
    #logger.debug('The resulting rectangles are: {}'.format(result))

    return H, result
