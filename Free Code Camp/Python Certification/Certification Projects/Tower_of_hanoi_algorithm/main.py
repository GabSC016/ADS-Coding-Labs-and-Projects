def hanoi_solver(number_of_disks):

    # Cria as listas

    origem_list = []
    auxiliar_list = []
    destino_list = []

    for number in range(number_of_disks,0,-1):
        origem_list.append(number)
    
    steps = [f'{origem_list} {auxiliar_list} {destino_list}']

    # Função recursiva

    def mover(number_of_disks, origem, auxiliar, destino, path_list):

        if number_of_disks == 1:

            disk = origem.pop()
            destino.append(disk)

            step = f'{origem_list} {auxiliar_list} {destino_list}'
            steps.append(step)
        
        else:

            mover(number_of_disks - 1, origem, destino, auxiliar, path_list)

            disk = origem.pop()
            destino.append(disk)

            step = f'{origem_list} {auxiliar_list} {destino_list}'
            steps.append(step)

            mover(number_of_disks - 1, auxiliar, origem, destino, path_list) 

    # Programa    
    
    mover(number_of_disks, origem_list, auxiliar_list, destino_list, steps)
    
    final_string = '\n'.join(steps)

    return final_string