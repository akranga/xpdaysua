import unittest, app

class SimplisticTest(unittest.TestCase):

  def test_index(self):
    expected = {'message': 'Herllo, I am mr. Norris'}
    actual = app.index()
    self.assertEqual(expected, actual)


  def test_read_facts_file(self):
    expected = "All arrays Chuck Norris declares are of infinite size, because Chuck Norris knows no bounds."
    actual = app.read_facts_file()[0]
    self.assertEqual(expected, actual)



  def test_gimme_fact(self):
    expected = "All arrays Chuck Norris declares are of infinite size, because Chuck Norris knows no bounds."
    actual = app.gimme_fact('0')
    self.assertEqual(expected, actual)



  def test_gimme_random_fact(self):
    all_items = app.read_facts_file()
    actual = app.gimme_random_fact()
    self.assertTrue(actual in all_items)



if __name__ == '__main__':
  unittest.main()