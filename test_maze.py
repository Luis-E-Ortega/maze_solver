import unittest
from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]), 
            num_rows,
        )
    def test_maze_create_cells_small(self):
        num_cols = 2
        num_rows = 2
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )
    def test_maze_create_cells_wide(self):
        num_cols = 20
        num_rows = 5
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )
    def test_maze_create_cells_tall(self):
        num_cols = 5
        num_rows = 20
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows
        )
    def test_maze_break_entrance_and_exit_basic(self):
        num_cols = 5
        num_rows = 4
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)

        # Test entrance
        self.assertEqual(m1._cells[0][0].has_top_wall, False)

        # Test exit
        self.assertEqual(m1._cells[num_cols-1][num_rows-1].has_bottom_wall, False)
    
    def test_maze_initialization_with_wall_breaks(self):
        maze = Maze (0, 0, 2, 2, 10, 10, seed=0)

        self.assertEqual(maze.num_cols, 2)
        self.assertEqual(maze.num_rows, 2)
        self.assertEqual(maze.seed, 0)

        self.assertEqual(len(maze._cells), 2)
        self.assertEqual(len(maze._cells[0]), 2)
    
    def test_maze_reset_cells_visited(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        for col in m1._cells:
            for cell in col:
                self.assertEqual(
                    cell.visited,
                    False,
                )



if __name__ == "__main__":
    unittest.main()
