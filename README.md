# Anansi

This is a collection of different card and children's games all written in Python and distributed as a package that can be reused to simulate those game logics in other Python apps. It allows creators to create mini-games in their Python app.

## Games

* blackjack
* high_low

## Usage

`pip install git+ssh://git@github.com/tkmaseleme/anansi#egg=anansi`

### Blackjack

Create a Python file in your favorite text editor after installing the above, and the below and run the script.

```
from anansi import BlackJack

game = BlackJack
game.play
```

### High Low

```
from anansi import HighLow

game = HighLow
game.play()
```

## To Do

* Change print logic to return logic to allow for wider inclusion in other apps
* Create API documentation to allow for public use
* Publish publicly to PyPi
