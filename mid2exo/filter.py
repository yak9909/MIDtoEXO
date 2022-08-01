class Filter:
    def __init__(self, name, params):
        self.name = name
        self.params = params


class FilterType:
    def Position(x=0.0, y=0.0, z=0.0):
        return Filter(
            name="座標",
            params={
                "X": x,
                "Y": y,
                "Z": z
            }
        )
