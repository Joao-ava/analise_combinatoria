from app.core import word_distance, Word


ceara = [
    ('HTX', 'HZA'),
    ('NQL', 'NRE'),
    ('NUM', 'NVF'),
    ('OCB', 'OCU'),
    ('OHX', 'OIQ'),
    ('ORN', 'OSV'),
    ('OZA', 'OZA'),
    ('PMA', 'POZ'),
    ('RIA', 'RIN'),
    ('SAN', 'SBV'),
]

maranhao = [
    ('HOL', 'HQE'),
    ('NHA', 'NHT'),
    ('NMP', 'NNI'),
    ('NWS', 'NXQ'),
    ('OIR', 'OJQ'),
    ('OXQ', 'OXZ'),
    ('PSA', 'PTZ'),
    ('ROA', 'ROZ'),
]

piaui = [
    ('LVF', 'LWQ'),
    ('NHU', 'NIX'),
    ('ODU', 'OEI'),
    ('OUA', 'OUE'),
    ('OVW', 'OVY'),
    ('PIA', 'PIZ'),
    ('QRN', 'QRZ'),
    ('RSG', 'RST'),
]


class Plate:
    @staticmethod
    def find_state(plate: str) -> str:
        prefix = plate[:3]  
        for start, end in ceara:
            if start <= prefix <= end:
                return 'Ceará'
        
        for start, end in maranhao:
            if start <= prefix <= end:
                return 'Maranhão'
        
        for start, end in piaui:
            if start <= prefix <= end:
                return 'Piauí'
        
        return 'De nenhum dos estados'

    @staticmethod
    def count_plates(plate_range) -> int:
        """
        Calcula o número total de placas possíveis para um intervalo de prefixos.

        :param plate_range: Lista de tuplas contendo os intervalos (ex.: [('HTX', 'HZA')]).
        :return: Número total de placas possíveis.
        """
        total_plates = 0
        for start, end in plate_range:
            prefix_count = word_distance(Word(start), Word(end)) + 1
            total_plates += prefix_count * 26000
        return total_plates

    @staticmethod
    def count_ce() -> str:
        return str(Plate.count_plates(ceara))
    
    @staticmethod
    def count_ma() -> str:
        return str(Plate.count_plates(maranhao))
    
    @staticmethod
    def count_pi() -> str:
        return str(Plate.count_plates(piaui))

def word_distance(start: str, end: str) -> int:
    """
    Calcula a "distância alfabética" entre dois prefixos de placas.

    :param start: Prefixo inicial (ex.: 'HTX'):)
    :param end: Prefixo final (ex.: 'HZA'):)
    :return: Número de posições alfabéticas entre os dois prefixos.
    """
    return ord(end[0]) - ord(start[0]) + \
           (ord(end[1]) - ord(start[1])) * 26 + \
           (ord(end[2]) - ord(start[2])) * 26 * 26
    
