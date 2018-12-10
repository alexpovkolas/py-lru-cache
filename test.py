import unittest
import lru_cache


# uncomment the line below and change the path specified
# sys.path.insert(0, r'path_to_solution_folder')


class InterfaceTestCase(unittest.TestCase):

    def test_cache(self):
        c = lru_cache.Cache()
        c.add("a", 1)
        c.add("b", 2)
        c.add("c", 3)
        c.add("d", 4)
        c.add("e", 5)
        c.add("f", 6)
        c.add("g", 7)
        self.assertEqual(c.size(), 5)
        self.assertEqual(c.get("a"), None)
        c.remove("g")
        self.assertEqual(c.get("g"), None)
        self.assertEqual(c.get("c"), 3)
        c.add("h", 8)
        self.assertEqual(c.get("c"), 3)
        self.assertEqual(c.contains("a"), False)
        self.assertEqual(c.contains("c"), True)
        c.clear()
        self.assertEqual(c.size(), 0)


if __name__ == '__main__':
    unittest.main()
