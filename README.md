# Rubik-s-Cube
A virtual rubik's cube with the ability to solve, get a tutorial. Made in python.

Before running, Python 3.10.2 is required at a minimum

2/3 Figuring out how to represent cube tiles

2/7 Created a 3d representation of a cube with a 3d matrix containing text for corner, edge, center, and core

2/14 Fixed a bug where tiles added to the list automatically changed color and rotation

2/15 Re-added the rotation vectors to each piece so it will know how to rotate each piece in the 3d gui. Can't confirm until the 3d gui is built

2/17 Added the ability to obtain a layer on the puzzle (This is not a side) Also can rotate the Right side Clockwise

3/2 Now Can get sides and rotate them, but doesn't affect original matrix

3/8 Now Rotated sides affect original cube matrix. The cube can do every move now with text based input

3/10 Moved Puzzle into a seperate python file, debating what module to use for 3d Graphics
PyGame, x3d, pyopengl, matplotlib, vector

3/14 Decided on making a 3d engine using pyOpenGL, made 2 classes for points and vectors which will be used later
Rotate Sides by clearing screen and redrawing

3/15 No major updates to project, but did some testing on pyGame and OpenGL, ultimately decided to use this
Next want to make 27 wireframe cubes in a 3x3x3 pattern