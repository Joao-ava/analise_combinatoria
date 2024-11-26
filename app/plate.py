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
        return 0

    @staticmethod
    def count_ce() -> str:
        return str(Plate.count_plates(ceara))
    
    @staticmethod
    def count_pi() -> str:
        return str(Plate.count_plates(maranhao))
    
    @staticmethod
    def count_ma() -> str:
        return str(Plate.count_plates(piaui))


