class IntegerToRomanConverter:
    # Mapping of integer values to their corresponding Roman numeral symbols
    _int_to_roman_map = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
    ]

    def __init__(self, number):
        if not isinstance(number, int):
            raise TypeError("Input must be an integer.")
        if number <= 0 or number > 3999:
            raise ValueError("Input must be between 1 and 3999 inclusive.")
        self.number = number

    def to_roman(self):
        num = self.number
        roman_numeral = ""
        for value, symbol in self._int_to_roman_map:
            while num >= value:
                roman_numeral += symbol
                num -= value
        return roman_numeral


# Example Usage:
if __name__ == "__main__":
    number = 1994
    converter = IntegerToRomanConverter(number)
    print(f"{number} in Roman numerals is: {converter.to_roman()}")
