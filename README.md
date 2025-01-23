# char-check-lab
## Character Check Lab
In this lab you will determine the types of characters in a string. You may work with others on this lab.

## Set Up
<ol>
	<li>Create new anaconda environment using these commands</li>
	<ul>
		<li>conda create --name character_check_lab python=3.13.1</li>
		<li>conda activate character_check_lab</li>
	</ul>
	<li>Pull starter code from GitHub Classroom</li>
	<li>Open in VS code and switch to the character_check_lab anaconda environment</li>
	<li>When the lab is complete, push code to GitHub Classroom</li>
</ol>

## Instructions
The check_character() function takes in two parameters, a string and an index. Fix the function so that it returns the type of the character at that index in the string. The type should be a letter, digit, white space, or unknown.  

## Example 
check_character('happy birthday', 2) should return "letter"  
check_character('happy birthday', 5) should return "white space"  
check_character('happy birthday 2 you', 15) should return "digit"  
check_character('happy birthday!', 14) should return "unknown"
