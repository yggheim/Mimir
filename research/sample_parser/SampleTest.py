import unittest


####title: Successful checkout
####feature: cart/checkout
class ExampleTestCase(unittest.TestCase):
    def test_something(self):
        ####precondition: creating cart with items
        cart.add_item(123)

        ####step: click on checkout button
        checkout_button.click()
        something.click()

        ####check: we are on the checkout page
        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
