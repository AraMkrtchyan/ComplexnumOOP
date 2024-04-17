class ComplexNumber:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def add(self, other):
        real_sum = self.real + other.real
        imaginary_sum = self.imaginary + other.imaginary
        return ComplexNumber(real_sum, imaginary_sum)

    def subtract(self, other):
        real_diff = self.real - other.real
        imaginary_diff = self.imaginary - other.imaginary
        return ComplexNumber(real_diff, imaginary_diff)

    def multiply(self, other):
        real_prod = self.real * other.real - self.imaginary * other.imaginary
        imaginary_prod = self.real * other.imaginary + self.imaginary * other.real
        return ComplexNumber(real_prod, imaginary_prod)

    def divide(self, other):
        denominator = other.real ** 2 + other.imaginary ** 2
        real_div = (self.real * other.real + self.imaginary * other.imaginary) / denominator
        imaginary_div = (self.imaginary * other.real - self.real * other.imaginary) / denominator
        return ComplexNumber(real_div, imaginary_div)

    def __str__(self):
        return f"({self.real} + {self.imaginary}i)"

# Пример использования
num1 = ComplexNumber(3, 4)
num2 = ComplexNumber(1, 2)

print("Первое комплексное число:", num1)
print("Второе комплексное число:", num2)

sum_result = num1.add(num2)
print("Сумма:", sum_result)

diff_result = num1.subtract(num2)
print("Разность:", diff_result)

prod_result = num1.multiply(num2)
print("Произведение:", prod_result)

div_result = num1.divide(num2)
print("Деление:", div_result)