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
