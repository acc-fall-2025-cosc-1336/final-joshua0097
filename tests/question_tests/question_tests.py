#write function tests here, don't add input('') statements here!
import unittest

#follow this example to add questions b, c, and d for testing including their functions
from src.question_c.question_c import get_most_likely_ancestor_consensus

class Test_Config(unittest.TestCase):

    def test_get_most_likely_ancestor_consensus_found_multiple(self):
        result = get_most_likely_ancestor_consensus("GATATATGCATATACTT", "ATAT")
        count, first_position, last_position = result
        self.assertEqual(count, 2)
        self.assertEqual(first_position, 4)
        self.assertEqual(last_position, 10)

                        

