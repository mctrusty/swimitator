import sys
sys.path.append("..\\swimitator")

import swim_lexer
import unittest

class TestSwimLexer(unittest.TestCase):
	'''Unit tests for swim_lexer'''
	
	def setUp(self):
		self.lexer = swim_lexer.lexer

	def test_empty_string_no_tokens(self):
		s=''
		result = swim_lexer.dump_tokens(s)
		self.assertEqual(result, '')
		
	def test_free_stroke_token(self):
		free = ('Fr', 'fr', 'Free', 'free')
		for fr in free:
			res = swim_lexer.dump_tokens(fr)
			self.assertEqual(res, 'STROKE')
		
	def test_back_stroke_token(self):
		back = ('Bk', 'bk', 'Back', 'back')
		for bk in back:
			res = swim_lexer.dump_tokens(bk)
			self.assertEqual(res, 'STROKE')
		
	def test_breast_stroke_token(self):
		breast = ('Br', 'br', 'Breast', 'breast')
		for br in breast:
			res = swim_lexer.dump_tokens(br)
			self.assertEqual(res, 'STROKE')
			
	def test_fly_stroke_token(self):
		fly = ('Fl', 'fl', 'fly', 'Fly')
		for fl in fly:
			res = swim_lexer.dump_tokens(fl)
			self.assertEqual(res, 'STROKE')
	
	def test_im_token(self):
		im = ('IM', 'im')
		for i in im:
			res = swim_lexer.dump_tokens(i)
			self.assertEqual(res, 'STROKE')
			
	def test_choice_token(self):
		choice = ('ch', 'Ch', 'choice', 'Choice')
		for ch in choice:
			res = swim_lexer.dump_tokens(ch)
			self.assertEqual(res, 'STROKE')
			
	def test_kick_token(self):
		kick = ('K', 'k', 'Kick', 'kick')
		for k in kick:
			res = swim_lexer.dump_tokens(k)
			self.assertEqual(res, 'KICK')

	def test_drill_token(self):
		drill = ('dr', 'Dr', 'drill', 'Drill')
		for dr in drill:
			res = swim_lexer.dump_tokens(dr)
			self.assertEqual(res, 'DRILL')

	def test_zone_token(self):
		zone = ('EN1', 'Zone 2' , 'zone 3')
		for z in zone:
			res = swim_lexer.dump_tokens(z)
			self.assertEqual(res, 'ZONE')

	
	def tearDown(self):
		self.lexer = None
		
if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestSwimLexer)
    unittest.TextTestRunner(verbosity=2).run(suite)