class InterfaceMetroApp:
    def __init__(self, name):
        self.name = name
        self.stations = []
        self.lines = []

    VALID_STATIONS = (
        "A", "B", "C", "D", "E",
        "F", "G", "H", "I", "J",
        "K", "L", "M", "N", "O", "0"
    )

    def show_station_map(self):
        return (
            f"{'A - B - C - D - E':^50}\n"
            f"{'F - G - C - H - I':^50}\n"
            f"{'J - K - H - L - M':^50}\n"
            f"{'N - O - D - J - L':^50}"
        )

    def get_station(self, name):
        for station in self.stations:
            if station.name == name:
                return station

        return None

    def show_lines_menu(self):
        str_screen_1 = ''
        str_screen_1 += f"{50 * '='}\n{'LINHAS DO METRÔ'.center(50)}\n{50 * '='}\n"
        str_screen_1 += f"\n{'Escolha uma opção abaixo:'.center(50)}\n"
        str_screen_1 += f"{50 * '-'}\n"
        str_screen_1 += (
            "|1| Red Line \n"
            "|2| Blue Line \n"
            "|3| Green Line \n"
            "|4| Yellow Line \n"
            "|0| Sair\n"
        )
        str_screen_1 += f"{50 * '-'}\n"

        option = None
        while option != 0:
            try:
                print(str_screen_1)
                option = input("Digite uma opção válida: ")
                valid_options = ("0", "1", "2", "3", "4")

                if option not in valid_options:
                    raise ValueError("Insira uma opção válida.")

                else:
                    option = int(option)

                    if option != 0:
                        line = self.lines[option - 1]
                        print(line.show_stations())
                        input("Pressione Enter para continuar...")

            except ValueError as error:
                print(f"Erro: {error}")
                input("Pressione Enter para continuar...")
                continue

    def show_all_stations(self):
        for line in self.lines:
            print(f"{line.show_stations()}\n")

        input("Pressione Enter para continuar...")
        return

    def show_connections_menu(self):
        str_screen_3 = ''
        str_screen_3 += f"{50 * '='}\n{'CONEXÕES DA ESTAÇÃO'.center(50)}\n{50 * '='}\n"
        str_screen_3 += f"\n{'Escolha uma estação abaixo:'.center(50)}\n"
        str_screen_3 += f"{50 * '-'}\n"
        str_screen_3 += f"{self.show_station_map()}\n\n{'|0| Sair'.center(50)}\n"
        str_screen_3 += f"{50 * '-'}\n"

        option = None
        while option != '0':
            try:
                print(str_screen_3)
                option = input("Digite uma opção válida: ").upper()

                if option not in self.VALID_STATIONS:
                    raise ValueError("Insira uma opção válida.")

                else:
                    station = self.get_station(option)

                    if station:
                        print(station.show_connections())
                        input("Pressione Enter para continuar...")

            except ValueError as error:
                print(f"Erro: {error}")
                input("Pressione Enter para continuar...")
                continue

    def show_station_lines_menu(self):
        str_screen_4 = ''
        str_screen_4 += f"{50 * '='}\n{'LINHAS DA ESTAÇÃO'.center(50)}\n{50 * '='}\n"
        str_screen_4 += f"\n{'Escolha uma estação abaixo:'.center(50)}\n"
        str_screen_4 += f"{50 * '-'}\n"
        str_screen_4 += f"{self.show_station_map()}\n\n{'|0| Sair'.center(50)}\n"
        str_screen_4 += f"{50 * '-'}\n"

        option = None
        while option != '0':
            try:
                print(str_screen_4)
                option = input("Digite uma opção válida: ").upper()

                if option not in self.VALID_STATIONS:
                    raise ValueError("Insira uma opção válida.")

                else:
                    station = self.get_station(option)

                    if station:
                        print(station.show_lines())
                        input("Pressione Enter para continuar...")

            except ValueError as error:
                print(f"Erro: {error}")
                input("Pressione Enter para continuar...")
                continue

    def check_connection_menu(self):
        str_screen_5 = ''
        str_screen_5 += f"{50 * '='}\n{'VERIFICAR CONEXÃO'.center(50)}\n{50 * '='}\n"
        str_screen_5 += f"\n{'Escolha duas estações abaixo:'.center(50)}\n"
        str_screen_5 += f"{50 * '-'}\n"
        str_screen_5 += f"{self.show_station_map()}\n\n{'|0| Sair'.center(50)}\n"
        str_screen_5 += f"{50 * '-'}\n"

        option1 = None
        option2 = None

        while option1 != '0' and option2 != '0':
            try:
                print(str_screen_5)
                option1 = input("Digite uma estação: ").upper()
                option2 = input(
                    "Digite outra estação para verificar a conexão: "
                ).upper()

                if option1 not in self.VALID_STATIONS or option2 not in self.VALID_STATIONS:
                    raise ValueError("Insira duas opções válidas.")

                else:
                    station = self.get_station(option1)

                    if station:
                        print(station.is_connected(option2))
                        input("Pressione Enter para continuar...")

            except ValueError as error:
                print(f"Erro: {error}")
                input("Pressione Enter para continuar...")
                continue

    def find_path_menu(self):
        str_screen_6 = ''
        str_screen_6 += f"{50 * '='}\n{'ENCONTRAR O MELHOR CAMINHO'.center(50)}\n{50 * '='}\n"
        str_screen_6 += f"\n{'Escolha uma estação de origem e outra de destino:'.center(50)}\n"
        str_screen_6 += f"{50 * '-'}\n"
        str_screen_6 += f"{self.show_station_map()}\n\n{'|0| Sair'.center(50)}\n"
        str_screen_6 += f"{50 * '-'}\n"

        start_station = None
        destination_station = None

        while start_station != '0' and destination_station != '0':
            try:
                print(str_screen_6)

                start_station = input(
                    "Insira a estação de origem: "
                ).upper()

                destination_station = input(
                    "Insira a estação de destino: "
                ).upper()

                if (
                    start_station not in self.VALID_STATIONS
                    or destination_station not in self.VALID_STATIONS
                ):
                    raise ValueError("Insira uma opção válida.")

                else:
                    start = self.get_station(start_station)
                    destination = self.get_station(destination_station)

                    if start and destination:
                        metro = Metro("find_path")
                        best_path = metro.find_path(start, destination)

                        print(best_path)
                        input("Pressione Enter para continuar...")

            except ValueError as error:
                print(f"Erro: {error}")
                input("Pressione Enter para continuar...")
                continue

    def add_lines(self, lines):
        for line in lines:
            if isinstance(line, Line):
                self.lines.append(line)

    def add_stations(self, stations):
        for station in stations:
            if isinstance(station, Station):
                self.stations.append(station)

    def run(self):
        option = None

        while option != '0':
            try:
                self.show_menu()
                option = input("Digite uma opção válida: ")

                valid_options = ("0", "1", "2", "3", "4", "5", "6")

                if option not in valid_options:
                    raise ValueError("Insira uma opção válida.")

                else:
                    self.options_selected(int(option))

            except ValueError as error:
                print(f"Erro: {error}")
                input("Pressione Enter para continuar...")
                continue

    def show_menu(self):
        str_menu = ''
        str_menu += f"{50 * '='}\n{'METRO SEARCH APP'.center(50)}\n{50 * '='}"
        str_menu += f"\n\n{'Olá, seja bem-vindo ao Metro Search.'.center(50)}\n\n"
        str_menu += f"{'Escolha uma opção abaixo:'.center(50)}\n"
        str_menu += f"{50 * '-'}\n"
        str_menu += (
            "|1| Consultar linhas \n"
            "|2| Consultar estações \n"
            "|3| Consultar conexões \n"
            "|4| Consultar linhas de uma estação \n"
            "|5| Verificar conexão entre estações \n"
            "|6| Encontrar melhor trajeto \n"
            "|0| Sair\n"
        )
        str_menu += f"{50 * '-'}\n"

        print(str_menu)

    def options_selected(self, option):
        if option == 1:
            self.show_lines_menu()

        elif option == 2:
            self.show_all_stations()

        elif option == 3:
            self.show_connections_menu()

        elif option == 4:
            self.show_station_lines_menu()

        elif option == 5:
            self.check_connection_menu()

        elif option == 6:
            self.find_path_menu()


class Metro:
    def __init__(self, name):
        self.name = name

    # Método que recebe duas estações e, utilizando BFS, retorna o melhor caminho
    def find_path(self, start, destination):

        if start == destination:
            return (
                f"\n{'=' * 50}\n"
                f"{'MELHOR CAMINHO ENCONTRADO'.center(50)}\n"
                f"{'=' * 50}\n"
                f"Origem : {start.name}\n"
                f"Destino: {destination.name}\n"
                f"Rota   : {start.name}\n"
                f"Paradas: 0\n"
                f"{'=' * 50}"
            )

        visited = {start}
        predecessor = {}
        next_to_visit = [start]
        found = False

        while next_to_visit and not found:

            current_station = next_to_visit.pop(0)
            connections = current_station.connections

            for station in connections:
                if station not in visited:
                    visited.add(station)
                    predecessor[station] = current_station
                    next_to_visit.append(station)

                    if destination == station:
                        found = True
                        break

        if found:
            path = []
            current = destination

            while current != start:
                path.append(current)
                current = predecessor[current]

            path.append(start)
            path.reverse()

            final = [station.name for station in path]

            return (
                f"\n{'=' * 50}\n"
                f"{'MELHOR CAMINHO ENCONTRADO'.center(50)}\n"
                f"{'=' * 50}\n"
                f"Origem : {start.name}\n"
                f"Destino: {destination.name}\n"
                f"Rota   : {' --> '.join(final)}\n"
                f"Paradas: {len(final) - 1}\n"
                f"{'=' * 50}"
            )

        else:
            return (
                f"\n{'=' * 50}\n"
                f"{'CAMINHO NÃO ENCONTRADO'.center(50)}\n"
                f"{'=' * 50}\n"
                f"Origem : {start.name}\n"
                f"Destino: {destination.name}\n"
                f"Não existe caminho entre essas estações.\n"
                f"{'=' * 50}"
            )


class Line(Metro):
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color
        self.stations = []

    # Método que adiciona estações à linha de metrô
    def add_stations(self, stations):
        for station in stations:
            if isinstance(station, Station):
                self.stations.append(station)
            else:
                return "A estação informada não existe."

    # Método que retorna todas as estações de uma linha
    def show_stations(self):
        str_stations = [str(station.name) for station in self.stations]

        return (
            f"{'=' * 50}\n"
            f"{'Estações da ' + self.name:^50}\n"
            f"{'=' * 50}\n"
            f"{' --> '.join(str_stations):^50}\n"
            f"{'=' * 50}"
        )

    # Método que verifica se a estação existe na linha
    def has_station(self, station):
        str_stations = [str(station.name) for station in self.stations]

        if station.upper() in str_stations:
            return f"A linha {self.name} possui a estação {station.upper()}."
        else:
            return f"A linha {self.name} não possui a estação {station.upper()}."


class Station(Metro):
    def __init__(self, name):
        super().__init__(name)
        self.connections = []
        self.lines = []

    # Método que adiciona conexões entre as estações
    def add_connections(self, connections):
        for station in connections:
            if isinstance(station, Station):
                self.connections.append(station)
            else:
                return "Essa conexão não existe."

    # Método que integra a estação à linha
    def add_lines(self, lines):
        for line in lines:
            if isinstance(line, Line):
                self.lines.append(line)
            else:
                return "Essa linha não existe."

    # Método que retorna as conexões da estação
    def show_connections(self):
        str_connections = [connection.name for connection in self.connections]

        return (
            f"\n{'=' * 50}\n"
            f"{'CONEXÕES DA ESTAÇÃO ' + self.name:^50}\n"
            f"{'=' * 50}\n"
            f"{'Total de conexões: ' + str(len(str_connections)):^50}\n"
            f"{'Conectada a: ' + ' • '.join(str_connections):^50}\n"
            f"{'=' * 50}"
        )

    # Método que verifica se duas estações estão conectadas
    def is_connected(self, station):
        str_connections = [connection.name for connection in self.connections]

        if station.upper() in str_connections:
            return (
                f"\n{'=' * 50}\n"
                f"{'CONEXÃO ENTRE ESTAÇÕES':^50}\n"
                f"{'=' * 50}\n"
                f"{f'✓ {self.name} ↔ {station.upper}':^50}\n"
                f"{'As estações estão diretamente conectadas.':^50}\n"
                f"{'=' * 50}"
            )
        else:
            return (
                f"\n{'=' * 50}\n"
                f"{'CONEXÃO ENTRE ESTAÇÕES':^50}\n"
                f"{'=' * 50}\n"
                f"{f'✗ {self.name} ↛ {station.upper()}':^50}\n"
                f"{'As estações não estão diretamente conectadas.':^50}\n"
                f"{'=' * 50}"
            )

    # Método que retorna todas as linhas conectadas à estação
    def show_lines(self):
        str_lines = [line.name for line in self.lines]

        return (
            f"\n{'=' * 50}\n"
            f"{('LINHAS DA ESTAÇÃO ' + self.name):^50}\n"
            f"{'=' * 50}\n"
            f"{('Linhas: ' + ' • '.join(str_lines)):^50}\n"
            f"{('Estação de transferência' if len(str_lines) > 1 else 'Estação comum'):^50}\n"
            f"{'=' * 50}"
        )


if __name__ == '__main__':

    # CRIAÇÃO DAS LINHAS
    red = Line("Red Line", "red")
    blue = Line("Blue Line", "blue")
    green = Line("Green Line", "green")
    yellow = Line("Yellow Line", "yellow")

    # CRIAÇÃO DAS ESTAÇÕES
    a = Station("A")
    b = Station("B")
    c = Station("C")
    d = Station("D")
    e = Station("E")
    f = Station("F")
    g = Station("G")
    h = Station("H")
    i = Station("I")
    j = Station("J")
    k = Station("K")
    l = Station("L")
    m = Station("M")
    n = Station("N")
    o = Station("O")

    # ESTAÇÕES DAS LINHAS
    red.add_stations([a, b, c, d, e])
    blue.add_stations([f, g, c, h, i])
    green.add_stations([j, k, h, l, m])
    yellow.add_stations([n, o, d, j, l])

    # CONEXÕES DA RED LINE
    a.add_connections([b])
    b.add_connections([a, c])
    c.add_connections([b, d, g, h])
    d.add_connections([c, e, n])
    e.add_connections([d])

    # CONEXÕES DA BLUE LINE
    f.add_connections([g])
    g.add_connections([f, c])
    h.add_connections([g, i, c])
    i.add_connections([h])

    # CONEXÕES DA GREEN LINE
    j.add_connections([k, n, l])
    k.add_connections([j, h])
    l.add_connections([k, m, j])
    m.add_connections([l])

    # CONEXÕES DA YELLOW LINE
    n.add_connections([o, d, j])
    o.add_connections([n])

    # LINHAS DAS ESTAÇÕES
    a.add_lines([red])
    b.add_lines([red])
    c.add_lines([red, blue])
    d.add_lines([red, yellow])
    e.add_lines([red])

    f.add_lines([blue])
    g.add_lines([blue])
    h.add_lines([blue, green])
    i.add_lines([blue])

    j.add_lines([green, yellow])
    k.add_lines([green])
    l.add_lines([green, yellow])
    m.add_lines([green])

    n.add_lines([yellow])
    o.add_lines([yellow])

    test = InterfaceMetroApp("interface")

    test.add_lines([red, blue, green, yellow])
    test.add_stations([a, b, c, d, e, f, g, h, i, j, k, l, m, n, o])

    test.run()