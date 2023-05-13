## Workshop exercises

### Core exercise

The following exercises will help you get started with GitHub Copilot. You must have completed the [setup instructions](<./1. setup.md>) before starting these steps.


<details>
<summary>1a. Building a Rock Paper Scissors game with GitHub Copilot</summary>

### Step by step instructions

1. Ensure you can see the files in the **Explorer view**. If not, click the **Explorer View icon** on the left sidebar of your editor.

<img width="398" alt="Code Explorer View" src="../assets/Code Explorer View.png">

2. Open the ```main.py``` file if it's not already open in the editor.
3. Let's start by adding the following comment to provide some context for the code we're about to write:
```# Write a rock, paper, scissors game``` :leftwards_arrow_with_hook:

4. On the next line we're going to prompt GitHub Copilot to suggest code for us by typing the following:

```# import random module``` :leftwards_arrow_with_hook:

5. When you press **Enter** after typing the previous comment, GitHub Copilot will suggest some code for you. Select the first suggestion by pressing **TAB** then **Enter** again.


<img width="529" alt="Copilot Suggestion - Import Random" src="../assets/Copilot Suggestion - Import Random.png">

6. Now we're going to prompt GitHub Copilot to suggest code for us by typing the following:

```# define main function that handles all the logic``` :leftwards_arrow_with_hook:

7. When you press **Enter** after typing the previous comment, GitHub Copilot will again suggest some code for you. Select the first suggestion by pressing **TAB** then **Enter** again.
8. **Pause briefly** while Copilot creates up to 10 suggestions for you. You should see the Copilot icon in the lower right corner of the editor spinning. When Copilot displays the first suggestion, we're going to open the GitHub Copilot suggestion panel by pressing **CTRL + ENTER**. 
9. Scroll down the list of suggestions that GitHub Copilot has made and choose the one that looks like the best option for our Rock, Paper, Scissors game. When you see the suggestion you want, click **Accept Solution** to have that code snippet inserted into your code file.

<img width="906" alt="Copilot Suggestion - Accept Solution" src="../assets/Copilot Suggestion - Accept Solution.png">


10. On the line following the last snippet, let's prompt GitHub Copilot to suggest the final line of code for us by typing the following:

```# call main function``` :leftwards_arrow_with_hook:

11. When you press Enter after typing the previous comment, GitHub Copilot will suggest some code for you. Select the first suggestion by pressing TAB then Enter again.

<img width="498" alt="Copilot Suggestion - def main" src="../assets/Copilot Suggestion - def main.png">


**Now we're ready to see if this code executes** :thumbsup:

> **NOTE:** To run the Python code, you'll need to have Python installed on your computer.

13. In the Terminal window in your Codespace, type the following command and press **Enter** to run the code:

```python3 main.py``` :leftwards_arrow_with_hook:

Here's an example of what the completed game might look like.

<img width="645" alt="Running the game" src="../assets/Running the game.png">

---

>Hopefully your Paper, Rock, Scissors game is working! Remember, GitHub Copilot is probabilistic so you may not get the exact same code suggestions as we did. If you're not happy with the suggestions, you can always press **CTRL + Z** to undo the changes and try again.

You're now ready to start the [challenge exercises](<./3. challenge exercises.md>) to see how you can leverage the power of GitHub Copilot to solve a number of challenges yourself.

======================== END OF EXERCISE ========================

</details>



 -- or -- 
>IF you chose to use VSCode as your IDE **AND** you chose to install the CodeTour extension, **OR** you're using the Codespaces experience and want to use the CodeTour extension instead of reading through the instructions, you should use the following steps instead.

<details>

<summary>1b. Building a Rock Paper Scissors game with GitHub Copilot (CodeTour option)</summary>

### Starting the CodeTour

1. Ensure you can see the files in the **Explorer view**. If not, click the **Explorer View icon** on the left sidebar of your editor.

<img width="398" alt="Code Explorer View" src="../assets/Code Explorer View.png">

2. At the bottom of the Explorer view panel, click **CodeTour** to expand the CodeTour panel.

<img width="427" alt="Expand CodeTour panel" src="../assets/Expand CodeTour panel.png">


3. In the CodeTour panel, press the “**Play button**” to start the tour.

<img width="428" alt="Play the CodeTour" src="../assets/Play the CodeTour.png">

4. Your CodeTour will begin! Follow the CodeTour’s steps in the main code window to learn how to use GitHub Copilot.

<img width="674" alt="CodeTour Starts" src="../assets/CodeTour Starts.png">

5. When you've completed each step, click the **Next** button to move to the next step in the CodeTour.

<img width="674" alt="CodeTour Navigation" src="../assets/CodeTour Navigation.png">

6. Work your way through each of the steps in the CodeTour to complete this exercise.

</details>

#### What's next?
You're now ready to start the [challenge exercises](<./3. challenge exercises.md>) to see how you can leverage the power of GitHub Copilot to solve a number of challenges yourself.
