import unittest # unittesting
import sys # import sys()
from io import StringIO #

class TestHelloWorld(unittest.TestCase):
    def testExample(self):
        """Test that helloworld.py prints 'HELLO WORLD'"""
        # Capture stdout
        captured_output = StringIO()
        sys.stdout = captured_output
        
        # Execute the helloworld.py code
        # python3 -c "exec(open('helloworld.py').read())"
        exec(open('helloworld.py').read())
        
        # Reset stdout
        sys.stdout = sys.__stdout__
        
        # Check the output
        self.assertEqual(captured_output.getvalue().strip(), "HELLO WORLD")


if __name__ == '__main__':
    unittest.main()

