# Letter Substitution...???

Completed on Aug 11, 2017

I'm almost certain I wrote this for a challenge on the DailyProgrammer subreddit...

This program is intended to convert the letters a-z into ROT13,
but I've formatted the input to replace any one character with a string.

I've also used this to convert letters & numbers into morse code.

### Input Description

A file containing a list of letters to convert.
Each line in the file should follow this format:
```
input letter>OUTPUT LETTER(s)
```

Some same inputs: MorseCode.txt & ROT13.txt

After inputting the file, the program converts any line of input
via the substitution cipher.

### Output Description

After each line of input, the program converts that input.
For example:
```
cypher file: MorseCode.txt
Input string: hi
• • • • • •

Input string: sos
• • • --- --- --- • • •
```
