import turtle, time, random
import window


def reset_game():
    print("Game Over")
    wn.update()
    time.sleep(3)
    # Reset
    score.reset()
    pipe1_bottom.reset(280, random.randint(-600, -200))
    pipe1_top.reset(pipe1_bottom)
    pipe2_bottom.reset(pipe1_bottom.xcor() + 280, random.randint(-600, -200))
    pipe2_top.reset(pipe2_bottom)
    player.reset()


wn = window.wn

score = window.Score()
score.write()

player = window.Player()

pipe1_bottom = window.Pipe_bottom(280, random.randint(-600, -200), "green")
pipe1_top = window.Pipe_top(pipe1_bottom)
pipe2_bottom = window.Pipe_bottom(pipe1_bottom.xcor() + 280, random.randint(-600, -200),"brown")
pipe2_top = window.Pipe_top(pipe2_bottom)

# Keyboard binding
wn.listen()
wn.onkeypress(player.go_up, "space")

# Main Game Loop
while True:
    # Pause
    time.sleep(0.03)
    # Update the screen
    wn.update()
    # Move player
    player.move()
    # Move the pipes
    recreate_pipe1 = pipe1_bottom.move()
    pipe1_top.move()
    recreate_pipe2 = pipe2_bottom.move()
    pipe2_top.move()
    # Recreate pipes
    if recreate_pipe1:
        pipe1_bottom.reset(280, random.randint(-600, -200))
        pipe1_top.reset(pipe1_bottom)
    elif recreate_pipe2:
        pipe2_bottom.reset(pipe1_bottom.xcor() + 280, random.randint(-600, -200))
        pipe2_top.reset(pipe2_bottom)
    # Check for collisions with pipes
    # Pipe 1
    if ((player.xcor() + 10) > (pipe1_top.xcor() - 30)) and + ((player.xcor() -10 ) < (pipe1_top.xcor() + 30)):
        if ((player.ycor() + 10) > (pipe1_top.ycor() - 320)) or ((player.ycor() - 10) < (pipe1_bottom.ycor() + 320)):
            reset_game()
    # Check for collisions with pipes
    # Pipe 2
    if ((player.xcor() + 10) > (pipe2_top.xcor() - 30)) and + ((player.xcor() -10 ) < (pipe2_top.xcor() + 30)):
        if ((player.ycor() + 10) > (pipe2_top.ycor() - 320)) or ((player.ycor() - 10) < (pipe2_bottom.ycor() + 320)):
            reset_game()
    # Check score
    inlet = False
    if (((player.xcor() - 10) == (pipe1_top.xcor() + 30)) or ((player.xcor() - 10) == (pipe2_top.xcor() + 30))):
        score.add_score()

wn.mainloop()
