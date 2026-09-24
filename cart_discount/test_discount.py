import unittest 
from unittest import TestCase
from price_discount import discount  

class TestDiscount(TestCase):

    def test_discount_returns_lowest_price_for_three_prices(self):
        prices = [10, 4, 20]
        expected_discount = 4
        self.assertEqual(expected_discount, discount(prices))

    def test_discount_returns_zero_for_two_prices(self):
        prices = [10, 4]
        expected_discount = 0
        self.assertEqual(expected_discount, discount(prices))

    def test_discount_returns_lowest_price_for_more_than_three_prices(self):
        prices = [10, 4, 20, 7]
        expected_discount = 4
        self.assertEqual(expected_discount, discount(prices))

    #('Outline: decide whether an empty cart returns 0 or raises an error.')
    def test_discount_with_empty_list(self):
        self.fail('finish this test')

    #('Outline: decide whether one item returns 0 or raises an error.')
    def test_discount_with_one_price(self):
        self.fail('finish this test')

    #('Outline: decide whether duplicate lowest prices still return one price.')
    def test_discount_with_duplicate_lowest_prices(self):
        self.fail('finish this test')

    #('Outline: decide whether decimal prices are supported.')
    def test_discount_with_decimal_prices(self):
        self.fail('finish this test')

    #('Outline: decide how free, negative, or refunded items are handled.')
    def test_discount_with_zero_or_negative_price(self):
        self.fail('finish this test')

    #('Outline: decide whether non-numeric prices raise TypeError or ValueError.')
    def test_discount_with_non_numeric_price(self):
        self.fail('finish this test')

    #('Outline: decide whether None instead of a list raises TypeError.')
    def test_discount_with_none(self):
        self.fail('finish this test')


if __name__ == '__main__':
    unittest.main()