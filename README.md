<h2>Brain-Fuck-Plus<div align="right"> V4 </div></h2>

<img src="Brain Fuck+ logo.png" alt="drawing" width="200"/>
<hr>

| key | Description                                                                                                         |
|-----|---------------------------------------------------------------------------------------------------------------------|
| , | get input characters.                                                                                                 |
| . | print data character.                                                                                                 |
| < | moves head/pointer left.                                                                                              |
| > | moves head/pointer right.                                                                                             |
| \[ | loops through the code untill the current head's/pointer's data is 0.                                                |
| ] | end of loop.                                                                                                          |
| - | subtract 1 from the curret head's/pointer's data, if it is 0 then it will go to 255.                                  |
| + | adds 1 to the curret head's/pointer's data, if it is 255 then it will go to 0.                                        |
| \` | get input string by setting each character's asci code down the "graph".                                             |
|num| repeats last key x times                                                                                              |
| # | set color of text in the terminal for fun!                                                                            |
| V | moves head/pointer down.                                                                                              |
| ^ | moves head/pointer up.                                                                                                |
| \\ | this will skip the next charicter.                                                                                   |
| $ | inbetween 2 $ it will try to read a formatted file to be then added to a library to be called on in the code latter on|
### Code examples

 ``` V`[.^]```

 this will get a string and print it back out, backwards!

<hr>

 ```V`^[^]V[.V]```

 this does the same thing but prints it normally!

<hr>

```$--[-5>+<]>-3.+12.-3.+3.+3.$```

this will read a file called "color" then try to add that to a library to then be called on.

<hr>

```-#```

this will change the text color to red!

<hr>

<h5>notes:</h5>
<p>it is best to lean normal Brain Fuck then come back to this, it will make it easier for you.</p>
<hr>
<a target="_blank" href="https://repl.it/github/cyleja1234/Brain-Fuck/blob/main/main.py"><img src="https://i.ibb.co/5XQm9kh/demo.png" alt="demo" border="0"></a>
