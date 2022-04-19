import unittest

from states import vflip, rotate90, next_state, remove_duplicates
from states import set_possible_moves, get_required_action, get_original_action
from states import is_win, match_two_states, check_equal

class TestMenaceStateMethods(unittest.TestCase):

    def test_invariant(self):
        '''
        Test for checking invariant that difference in 
        count of X's and O's on board should be <= 1
        ''' 
        state = [1,2,2,0,0,1,0,0,0]
        self.assertTrue(abs(state.count(1) - state.count(2))<=1)


    def test_vlip(self):
        '''
        Test for Vertical flip of a state
        '''
        self.assertEqual(vflip([1,0,0,0,0,0,0,0,0]), [0,0,1,0,0,0,0,0,0])

    def test_rotate90(self):
        '''
        Test for rotate state by 90 degrees right
        '''
        self.assertEqual(rotate90([1,2,2,0,0,1,0,0,0]), [0, 0, 1, 0, 0, 2, 0, 1, 2])

    def test_next_state(self):
        '''
        Test for getting next state given current state and a move
        ''' 
        self.assertEqual(next_state([[1,2,1,2,1,2,1,0,0]], [], 2), [[1, 2, 1, 2, 1, 2, 1, 2, 0], [1, 2, 1, 2, 1, 2, 1, 0, 2]])

    def test_remove_duplicates(self):
        '''
        Test for removing duplicate states 
        from states list after flip and rotation
        '''
        self.assertEqual(remove_duplicates([[1,0,0,0,0,0,0,0,0], [0,0,1,0,0,0,0,0,0]]), [[1,0,0,0,0,0,0,0,0]])

    def test_set_possible_moves(self):
        '''
        Test for obtaining all possible moves
        ''' 
        self.assertEqual(set_possible_moves([[1,0,0,0,0,0,0,0,0]], 2), 
                        {(1, 0, 0, 0, 0, 0, 0, 0, 0): 
                        [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8]})

    def test_get_required_action(self):
        '''
        Test for getting required state given current state, 
        number of rotations and flips
        ''' 
        self.assertEqual(get_required_action(0, 3, 0), 6)

    def test_get_original_action(self):
        '''
        Test for getting back the original state, 
        number of rotations and flips done and current state
        ''' 
        self.assertEqual(get_original_action(6, 3, 0), 0)

    def test_is_win(self):
        '''
        Test for checking who won given a board state
        ''' 
        self.assertEqual(is_win([1,2,2,2,1,1,2,2,1]), 1)

    def test_match_two_states(self):
        '''
        Test for matching two states index by index
        ''' 
        self.assertEqual(match_two_states([1,2,2,0,0,1,0,0,0], [1,2,2,0,0,1,0,0,0]), True)

    def test_check_equal(self):
        '''
        Test to check whether two states are equal 
        after all possible flips and rotations
        ''' 
        self.assertEqual(check_equal([1,0,0,0,0,0,0,0,0], [0,0,1,0,0,0,0,0,0]), (True, 3, 0))

if __name__ == '__main__':
    unittest.main()