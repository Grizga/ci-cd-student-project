python
importpytest
import sys
importos
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

fromsrc.calculator import Calculator

classTestCalculator:
defsetup_method(self):
self.calc = Calculator()

deftest_add(self):
assertself.calc.add(2, 3) == 5
assertself.calc.add(-1, 1) == 0

deftest_subtract(self):
assertself.calc.subtract(5, 3) == 2
assertself.calc.subtract(0, 5) == -5

deftest_multiply(self):
assertself.calc.multiply(3, 4) == 12
assertself.calc.multiply(0, 5) == 0

deftest_divide(self):
assertself.calc.divide(6, 3) == 2
assertself.calc.divide(5, 2) == 2.5

deftest_divide_by_zero(self):
withpytest.raises(ValueError):
self.calc.divide(5, 0)

deftest_power(self):
assertself.calc.power(2, 3) == 8
assertself.calc.power(5, 0) == 1
