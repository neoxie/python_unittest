import unittest
from widget import Widget


class WidgetTestCase(unittest.TestCase):
    def setUp(self):
        self.widget = Widget('The widget')
        print('run setUp before each of test cases')

    def test_default_widget_size(self):
        self.assertEqual(self.widget.size(), (50, 50),
                         'incorrect default size')

    def test_widget_resize(self):
        self.widget.resize(100, 150)
        self.assertEqual(self.widget.size(), (100, 150),
                         'wrong size after resize')

    @unittest.skip("demonstrating skipping")
    def test_nothing(self):
        self.fail("shouldn't happen")

    @unittest.expectedFailure
    def test_fail(self):
        self.assertEqual(1, 0, "broken")

    def tearDown(self):
        self.widget.dispose()
        print('run tearDown before after of test cases')


def suite():
    suite = unittest.TestSuite()
    suite.addTest(WidgetTestCase('test_default_widget_size'))
    suite.addTest(WidgetTestCase('test_widget_resize'))
    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())
