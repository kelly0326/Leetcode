class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        def c_to_k(c):
            k = c + 273.15
            print(k)
            return k
        def c_to_f(c):
            f = c * 1.80 + 32.00
            return f
        return c_to_k(celsius), c_to_f(celsius)