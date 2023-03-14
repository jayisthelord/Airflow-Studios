import discord
from discord.ext import *
import random

@commands.command()
async def snake(ctx):
    await ctx.send("soon")

class SnakeGame:
    def __init__(self, rows=10, cols=10):
        self.rows = rows
        self.cols = cols
        self.snake = [(0,0)]
        self.food = self.generate_food()
        self.direction = 'right'
        self.game_over = False

    def generate_food(self):
        while True:
            food = (random.randint(0, self.rows-1), random.randint(0, self.cols-1))
            if food not in self.snake:
                return food

    def move_snake(self):
        head = self.snake[-1]
        if self.direction == 'up':
            new_head = (head[0]-1, head[1])
        elif self.direction == 'down':
            new_head = (head[0]+1, head[1])
        elif self.direction == 'left':
            new_head = (head[0], head[1]-1)
        elif self.direction == 'right':
            new_head = (head[0], head[1]+1)
        if new_head[0] < 0 or new_head[0] >= self.rows or new_head[1] < 0 or new_head[1] >= self.cols or new_head in self.snake:
            self.game_over = True
            return
        self.snake.append(new_head)
        if new_head == self.food:
            self.food = self.generate_food()
        else:
            self.snake.pop(0)

    def get_board(self):
        board = [[' ' for _ in range(self.cols)] for _ in range(self.rows)]
        for i, j in self.snake:
            board[i][j] = 'o'
        i, j = self.food
        board[i][j] = 'x'
        return '\n'.join([' '.join(row) for row in board])

    def turn_left(self):
        if self.direction != 'right':
            self.direction = 'left'

    def turn_right(self):
        if self.direction != 'left':
            self.direction = 'right'

    def turn_up(self):
        if self.direction != 'down':
            self.direction = 'up'

    def turn_down(self):
        if self.direction != 'up':
            self.direction = 'down'

@commands.command()
async def snake(ctx):
    """Starts a game of Snake"""
    game = SnakeGame()
    message = await ctx.send('Starting Snake game...')
    while not game.game_over:
        board = game.get_board()
        await message.edit(content=f'```{board}```Use the reactions to move. Game over: {game.game_over}')
        try:
            reaction, user = await bot.wait_for('reaction_add', check=lambda r, u: u == ctx.author and str(r.emoji) in ['⬅️', '➡️', '⬆️', '⬇️'], timeout=30.0)
            if str(reaction.emoji) == '⬅️':
                game.turn_left()
            elif str(reaction.emoji) == '➡️':
                game.turn_right()
            elif str(reaction.emoji) == '⬆️':
                game.turn_up()
            elif str(reaction.emoji) == '⬇️':
                game.turn_down()
            await reaction.remove(ctx.author)
        except:
            break
        game.move_snake()
    board = game.get_board()

async def setup(bot):
    bot.add_command(snake)
