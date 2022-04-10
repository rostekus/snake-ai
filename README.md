<img src="images/Snake.png" width="1000" >

# Snake AI

My first trial Reinforcement Learning Project.

## Description
I was inspired by this [youtube video](https://www.youtube.com/watch?v=cO5g5qLrLSo&t=349s), where the basics of RL were shown. What suprised me the most was how easy you can create RL models. However, I didn't want to use gym module, I already had a clear plan in my head. What I was longing for is a creation of my own enviroment for my project. I was aware that it couldn't be complicated so i chose the good old Snake game. I can't imagine how many hours I’ve spent on playing it on my Nokia 6300 back in the day.
Unfortunately, even after countless hours of tinkering with parameters, I couldn't get satisfying results. The maximum score the AI obtained was 6. Usually it gets in loop and turns around. What I tried, was placing additional punishment if NN loops but it didn't change anything. Proposed solutions:

- add convolutional layers as for the state of game that AI obtains is just the array of one and zeros whereeach element corresponds to the position of the snake or food on the grid
- longer training, as for now the longest training that has been done consists of only one million steps
- change the reward function, what I used was simple idea of Euclidian distance from the snakes head to the fruit



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


