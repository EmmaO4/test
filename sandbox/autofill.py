class Autofill:
    def __init__(self, format):
        self.set_format(format)

    def get_format(self):
        return self._format
    
    def set_format(self, format):
        if format not in ('p', 'd'):
            raise ValueError("Format must be 'p' (physical) or 'd' (digital).")
        self._format = format

    