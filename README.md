# Snakes and Ladders using Linked List
A 2D Graphical Snakes and Ladders Game using Linked List Data Structure

Type or paste the following commands in your command line to play this game.
Step 1:

```
pip install pygame
```

Step 2:

```
git clone https://github.com/GaneshSparkz/Snakes-and-Ladders-using-Linked-List.git
```

Step 3:

```
cd Snakes-and-Ladders-using-Linked-List
```

Step 4:

```
cd "Snakes and Ladders"
```

Step 5:

```
python snakes_and_ladders.py
```

DESCRIPTION

  ‘Snakes and Ladders’ is a multiplayer board game which has a board with hundred squares starting from 1 to 100. A number of Snakes and Ladders are pictured on the board pointing to some specific squares. This game is played using a dice which rolls from 1 to 6. Two different coloured pawns are used to represent each player. Each player starts with a token on the starting square (usually the "1" grid square in the bottom left corner, or simply, off the board next to the "1" grid square). Players take turns rolling a single die to move their token by the number of squares indicated by the die roll. Tokens follow a fixed route marked on the game board which usually follows a track from the bottom to the top of the playing area, passing once through every square. If, on completion of a move, a player's token lands on the lower-numbered end of a "ladder", the player moves the token up to the ladder's higher-numbered square. If the player lands on the higher-numbered square of a "snake", the token must be moved down to the snake's lower-numbered square. If a player rolls a 6, the player may, after moving, immediately take another turn; otherwise play passes to the next player in turn. The player who is first to bring their token to the last square of the track is the winner.
  
  This project is implemented in such a way that each player can roll the dice which appears on the screen by pressing the Space bar during his/her turn. A player can start the game (reach the first square) only if the dice shows 1. After starting, when a player rolls the dice, his/her coin automatically move number of steps indicated by the dice and reach the destination square. 

DEVELOPMENT TOOLS


PYTHON PROGRAMMING LANGUAGE

Python is a widely used general-purpose, high level programming language. It was initially designed by Guido van Rossum in 1991 and developed by Python Software Foundation. It was mainly developed for emphasis on code readability, and its syntax allows programmers to express concepts in fewer lines of code. Python is a programming language that lets you work quickly and integrate systems more efficiently. Python 3 is used to implement this project.

PYGAME LIBRARY

The pygame is a Free and Open Source python programming language library for making multimedia applications like games built on top of the excellent SDL library. Like SDL, pygame is highly portable and runs on nearly every platform and operating system. Millions of people have downloaded pygame itself, which is a whole lot of bits flying across the internets.
The functions used from pygame in this project are as follows:

•pygame.display.set_mode()

Initialize a window or screen for display
set_mode(resolution=(0,0),flags=0,depth=0) -> Surface
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 700
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
This function will create a display Surface. The arguments passed in are requests for a display type. The actual created display will be the best possible match supported by the system. The resolution argument is a pair of numbers representing the width and height. The flags argument is a collection of additional options. The depth argument represents the number of bits to use for colour. The Surface that gets returned can be drawn to like a regular Surface but changes will eventually be seen on the monitor.
 
•pygame.display.flip()

Update the full display Surface to the screen
flip() -> None
This will update the contents of the entire display. If your display mode is using the flags  pygame.HWSURFACE and pygame.DOUBLEBUF, this will wait for a vertical retrace and swap the surfaces. If you are using a different type of display mode, it will simply update the entire contents of the surface. When using a pygame.OPENGL display mode, this will perform a gl buffer swap.

•pygame.display.set_caption()

Set the current window caption
set_caption(title, icontitle=None) -> None
TITLE = "Snakes and Ladders"
pygame.display.set_caption(TITLE)
If the display has a window title, this function will change the name on the window. Some systems support an alternate shorter title to be used for minimized displays.

•pygame.Surface.blit()

draw one image onto another
blit(source, dest, area=None, special_flags = 0) -> Rect
screen.blit(dice, (50, 150))
Draws a source Surface onto this Surface. The draw can be positioned with the dest argument. Dest can either be pair of coordinates representing the upper left corner of the source. A Rect can also be passed as the destination and the topleft corner of the rectangle will be used as the position for the blit. The size of the destination rectangle does not effect the blit. An optional area rectangle can be passed as well. This represents a smaller portion of the source Surface to draw.

•pygame.font.SysFont()

create a Font object from the system fonts
SysFont(name, size, bold=False, italic=False) -> Font
font = pygame.font.SysFont("Maiandra GD", 24, bold=True)
Return a new Font object that is loaded from the system fonts. The font will match the requested bold and italic flags. If a suitable system font is not found this will fall back on loading the default pygame font. The font name can be a comma separated list of font names to look for.

•pygame.font.Font.render()

draw text on a new Surface
render(text, antialias, color, background=None) -> Surface
dice_msg1 = font.render("Press 'SPACE BAR'", True, (0, 0, 255))
This creates a new Surface with the specified text rendered on it. pygame provides no way to directly draw text on an existing Surface: instead you must use Font.render() to create an image (Surface) of the text, then blit this image onto another Surface. The text can only be a single line: newline characters are not rendered. Null characters ('x00') raise a TypeError. Both Unicode and char (byte) strings are accepted.

•pygame.image.load()

load new image from a file
load(filename) -> Surface
load(fileobj, namehint="") -> Surface
dice = pygame.image.load("dice.png")
Load an image from a file source. You can pass either a filename or a Python file-like object. Pygame will automatically determine the image type (e.g., GIF or bitmap) and create a new Surface object from the data. In some cases it will need to know the file extension (e.g., GIF images should end in ".gif"). If you pass a raw file-like object, you may also want to pass the original filename as the namehint argument.

•pygame.event.get()

get events from the queue
get() -> Eventlist
get(type) -> Eventlist
get(typelist) -> Eventlist
This will get all the messages and remove them from the queue. If a type or sequence of types is given, only those messages will be removed from the queue. If you are only taking specific events from the queue, be aware that the queue could eventually fill up with the events you are not interested.

THE RANDOM LIBRARY

This module implements pseudo-random number generators for various distributions. For integers, uniform selection from a range. For sequences, uniform selection of a random element, a function to generate a random permutation of a list in-place, and a function for random sampling without replacement.
The function used from random library in this project is
random.randint(a, b)
Return a random integer N such that a <= N <= b.
dice_value = random.randint(1, 6)

THE TIME LIBRARY

This module provides various time-related functions. Although this module is always available, not all functions are available on all platforms. Most of the functions defined in this module call platform C library functions with the same name. It may sometimes be helpful to consult the platform documentation, because the semantics of these functions varies among platforms.
The function used from time library in this project is
time.sleep(secs)
Suspend execution of the current thread for the given number of seconds. The argument may be a floating point number to indicate a more precise sleep time. The actual suspension time may be less than that requested because any caught signal will terminate the sleep() following execution of that signal’s catching routine. Also, the suspension time may be longer than requested by an arbitrary amount because of the scheduling of other activity in the system.
time.sleep(1)

LINKED LIST DATA STRUCTURE

A linked list is a linear data structure where each element is a separate object. Linked list elements are not stored at contiguous location; the elements are linked using pointers. Each node of a list is made up of two items - the data and a reference to the next node. The last node has a reference to null. The entry point into a linked list is called the head of the list. It should be noted that head is not a separate node, but the reference to the first node. If the list is empty then the head is a null reference. 
In this project, the Node(data type for linked list) is implemented as class Square which has the attributes position(data), next(pointer), snake(pointer), ladder(pointer), x, y(coordinates for graphics) and the Linked List is implemented as class Board whose object is a linked list of 100 Square objects(Nodes).
