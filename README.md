<img src="images/Snake.png" width="1000" >

# Snake AI

My first trial Reinforcement Learning Project.

## Description
I was inspired by this [youtube video](https://www.youtube.com/watch?v=cO5g5qLrLSo&t=349s), where was shown basics of RL.
What suprised me the most was how easy you can create RL models but i didn't want to use gym module, i had clear plan in my head. What i was longing for is creation of my own enviroment for my project. I was aware that i couldn't be complicated so i chose good old Snake game. I can't imagine how many hours I spent as a kid playing it on my Nokia 6300.

Unfortunettly, even after countless hours of tinkiering with parametrs I couldn't get satisfying resault. The maximum score the AI obtained was six. Ususually it gets in loop and turns around.
What I tried was to add additional piunishment if NN loops but it didn't change anything.
Proposed solutions:

- add convolutional layers as for the state of game that AI obtains is just the array of one and zeros where each element correspond to the position of the snake or food on the grid.
- longer training, as for now the the longest that training's done was only one milion steps
- change the reward function, what I used was simple idea of Euclidian distance from the snakes head to the fruit.



## Installation 
Clone the repository
```
git clone https://github.com/rostekus/snake-ai
```
Setup
```
cd snake-ai
python3 setup.py install
```

## Usage
You can also play "human" version of game if you get bored at work just run:
```
python3 src/snake_game_human.py
```
or see how AI plays:
```
python3 src/snake.py
```

## Screenshots

![App Screenshot](/images/example.gif)


## License

[MIT](https://choosealicense.com/licenses/mit/)

## Author Info

- E-mail - [rmosorov@icloud.com](rmosorov@icloud.com)


