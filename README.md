<h1 align="center"> Tictactoe in a Terminal Built with Python </h1>
<p align="center">
   <img width="700" height="400" src="assets/tic_tac_toe_for_terminal.jpg">
   </p>

| Team | GitHub |Country
|:-----------:|:-----------:|:-----------:|
| Jeffer Max        |[@M21x1](https://github.com/M21x1)           |	<img width="30" height="20" src="assets/Flag_of_Peru.png">


<p>Tictactoe or Noughts and Crosses is a two player, they take turns, game where the only rule to win is to draw the same sign vertically, horizontally or diagonally on a three by three grid. </p>
<p> We will build the program using 5 modules:</p>
<ul>
  <li>The grid printer</li>
  <li>The input getter</li>
  <li>The switch player</li>
  <li>The winner determiner</li>
  <li>The game developer</li>
</ul>

<h2>How things work</h2>

<p>The above list can be daunting but no worries..I was too, hehe.</p> 
<br>
<p>First, the grid printer is a function that uses a dictionary to print out an initial frame where the players will be placing their signs.</p>
<br>
<p>Second, the input getter is where the terminal will ask a player to input a sign, imposing some restriction to not cause an error in the game like the input must be a number between 1 - 3.</p>
<br>
<p>Third, the switch player is the most simple function of them all, it just changes turns between players.</p>
<br>
<p>Fourth, the winner determiner is like a filter to check horizontally, vertically and diagonally if one of the player got three consecutive signs.</p>
<br>
<p>Finally, the game developer relates the four functions described and initializes the game.</p>
<br>
<img width="700" height="400" src="assets/screen_terminal_game.jpg">
<br>

