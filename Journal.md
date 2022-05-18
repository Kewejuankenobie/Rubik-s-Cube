# This is a Running Journal of the Process

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

3/23 Have a 3x3x3 cube, but cubes have no perspective, and only one color, Define colors individually for faces
Cube is now multicolored, but not shown properly

3/24 Beginning work on recoloring pieces, may have to reformat how colors are seen in program (list instead of dic)

3/28 R and R' move now works as expected
3/29 Almost all moves work, need to fix bug where U, D, and E don't work on anything other than the first move.

3/30 Fixed bug with U, D, and E moves not working, plan on adding cube rotation moves next

4/4 Cube rotations added, can see each rotated side individually

4/5 Realized have to do key inputs with openGL, may switch engine from part pyGame part openGL to only openGL

4/6 Scratch previous day, added Tkinter window to recive input from a keyboard

4/7 Now have working virtual cube, but very resource intensive

4/11 Reduced ram usage from 4 Gigs to 37 Megabytes of ram

4/14 Commented some code and renamed variables for easier reading

4/25 Scramble button added

4/26 Can input strings of multiple moves (Full algorithms)

4/27 Now can Scramble the cube without undoing previous moves, starting to fix UI

4/28 Decided on a UI idea, need to remodel how the gui works to take into account multiple pages

5/2 Continuing from Before

5/3 Now can switch tabs when clicking the instructions button & move guide button

5/5 Added instructions on how to use the controller, decided on using PIL for the move guide

5/12 Got an image to show, need to resize properly and add other images, and a scroll bar to keep size of window down

5/13 Decided against scroll bar because it is too complicated for the timeframe I have

5/16 Made more instructions

5/17 Finished the instructions, moved the running journal from README.md to Running_Journal.md

5/18 Commented Code