# Pong-in-pygame

# EN
# About the Game  

This is a classic Pong — a game inspired by the original arcade machines.  
The goal of the game is to hit the ball with the paddle and prevent it from passing by.  
Each time the ball crosses the opponent’s field, you earn a point.  
The game continues until one of the players scores 11 points, after which the winner is announced.  

The game is implemented using the Pygame library and follows the principles of object-oriented programming (OOP),  
which makes the code clean, scalable, and easy to read.  

---

## Game Features  

- Two players: Control two paddles with the keyboard to hit the ball.  
- Scoreboard: The score is displayed on the screen to track the progress of the match.  
- Boundaries: The playfield is limited by the top and bottom borders. The ball bounces off them, adding dynamics to the game.  
- Victory screen: When a player reaches 11 points, the game stops, and a message announcing the winner appears.  

---

## Controls  

Player 1 (left paddle):  
- W — up  
- S — down  

Player 2 (right paddle):  
- ↑ (arrow up) — up  
- ↓ (arrow down) — down  

Additional:  
- P — start or resume the game  
- Q — quit the game  

---

## Technical Details  

The project is written in Python using the Pygame library.  
The main components of the game are divided into modules for better code organization:  

- main.py — the main file that runs the game and contains the main game loop.  
- borders.py — responsible for creating and drawing the game field borders.  
- paddle.py — contains the Paddle class for paddles, implements their movement and boundary checks.  
- ball.py — contains the Ball class for the ball, responsible for its movement and collisions.  
- settings.py — a class for storing all game settings, including sizes, colors, and speeds.  
- game_stats.py — responsible for game statistics, such as player scores.  
- scoreboard.py — manages score display and winner messages.


# RU
# Об игре  

Это классический Pong — игра, вдохновлённая оригинальными аркадными автоматами.  
Цель игры — отбивать мяч ракеткой и не позволить ему пролететь мимо.  
Каждый раз, когда мяч пересекает поле соперника, тебе начисляется очко.  
Игра продолжается до тех пор, пока один из игроков не наберёт 11 очков, после чего объявляется победитель.  

Игра реализована с использованием библиотеки Pygame и следует принципам объектно-ориентированного программирования (ООП),  
что делает её код чистым, масштабируемым и легко читаемым.  

---

## Особенности игры  

- Два игрока: Управляйте двумя ракетками с помощью клавиш, чтобы отбивать мяч.  
- Счёт: На экране отображается счёт, позволяя следить за ходом матча.  
- Границы: Игровое поле ограничено верхней и нижней границами. Мяч отскакивает от них, добавляя динамики в игру.  
- Победный экран: При достижении 11 очков игра останавливается, и на экране появляется сообщение о победителе.  

---

## Управление  

Игрок 1 (левая ракетка):  
- W — вверх  
- S — вниз  

Игрок 2 (правая ракетка):  
- ↑ (стрелка вверх) — вверх  
- ↓ (стрелка вниз) — вниз  

Дополнительно:  
- P — начать или возобновить игру  
- Q — выйти из игры  

---

## Технические детали  

Проект написан на языке Python с использованием библиотеки Pygame.  
Основные компоненты игры разделены на модули для лучшей организации кода:  

- main.py — главный файл, который запускает игру и содержит основной игровой цикл.  
- borders.py — отвечает за создание и отрисовку границ игрового поля.  
- paddle.py — содержит класс Paddle для ракеток. Реализует их движение и проверку границ.  
- ball.py — содержит класс Ball для мяча. Отвечает за его движение и столкновения.  
- settings.py — класс для хранения всех настроек игры, включая размеры, цвета и скорости.  
- game_stats.py — отвечает за статистику игры, такую как счёт игроков.  
- scoreboard.py — управляет отображением счёта и сообщения о победителе.
