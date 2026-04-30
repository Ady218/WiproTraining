import pytest

from src.calculations import Calculations

class TestCalculations:
    calc = Calculations()

    @pytest.fixture(scope='module', autouse=True)
    def setup(self):
        print('Fixtures')

    @pytest.mark.parametrize('n1,n2, exval',[(5, 5, 10),(-5, -5, -10),(0, 5, 5)])
    def test_add(self, n1, n2, exval):
        res = self.calc.add(n1, n2)
        assert res == exval, 'Addition Error'

    @pytest.mark.parametrize('n1,n2, exval', [(5, 5, 0), (-5, -5, 0), (0, 5, -5)])
    def test_sub(self, n1, n2, exval):
        res = self.calc.sub(n1, n2)
        assert res == exval, 'Sub Error'

    def test_mul(self):
        res = self.calc.mul(10, 5)
        assert res == 50, 'Multiplication Error'

    def test_div(self):
        res = self.calc.div(10, 5)
        assert res == 2, 'Division Error'

    @pytest.mark.skip(reason='NIY')
    def test_ne(self):
        res = self.calc.ne(5, 5)
        assert res == True, 'NE'

    @pytest.mark.xfail(reason='Exception not Handled')
    def test_diverr(self):
        # with pytest.raises(ZeroDivisionError):
        res = self.calc.div(10, 0)
        assert res == 0