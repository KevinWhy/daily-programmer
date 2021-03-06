# Cryptarithms
https://www.reddit.com/r/dailyprogrammer/comments/6v29zk/170821_challenge_328_easy_latin_squares/

Completed on Jan 9, 2018

> Cryptarithms are a kind of mathematical puzzle.
> Each puzzle consists of a basic equation of arithmetic
> (involving addition, subtraction, division, etc.) with words,
> where each letter represents a different digit.
> The goal of the puzzle is to find the correct number substitution for each letter
> in order to make a valid equation.
> 
> This classic example (taken from the wikipedia page) was first published in 1924:
> 
> ```
>     S E N D
> +   M O R E
> _______________
>   M O N E Y
> ```
> 
> The solution to this puzzle is:
> 
> ```
> O = 0,
> M = 1,
> Y = 2,
> E = 5,
> N = 6,
> D = 7,
> R = 8,
> and S = 9.
> ```
> 
> (i.e. 9567 + 1085 = 10652)
> 
> Note: Leading zeroes are not allowed in a valid solution.

## Input Description

Some strings & their sum.

Example: "SEND + MORE == MONEY"

## Output Description

What each letter represents.

Example:
```
mapping found: {"D"=>7, "E"=>5, "M"=>1, "N"=>6, "O"=>0, "R"=>8, "S"=>9, "Y"=>2}
         9567 + 1085 = 10652
```

This is not an optimized solution, but it can solve the bonus (aka: more challenging inputs):

### Bonus / Challenge Input 1

> "TEN + HERONS + REST + NEAR + NORTH + SEA + SHORE + AS + TAN + TERNS + SOAR + TO + ENTER + THERE + AS + HERONS + NEST + ON + STONES + AT + SHORE + THREE + STARS + ARE + SEEN + TERN + SNORES + ARE + NEAR == SEVVOTH"

Output:
```
mapping found: {"A"=>2, "E"=>5, "H"=>3, "N"=>7, "O"=>4, "R"=>6, "S"=>1, "T"=>9, "V"=>8}
         957 + 356471 + 6519 + 7526 + 74693 + 152 + 13465 + 21 + 927 + 95671 + 1426 + 94 + 57956 + 93565 + 21 + 356471 + 7519 + 47 + 194751 + 29 + 13465 + 93655 + 19261 + 265 + 1557 + 9567 + 174651 + 265 + 7526 = 1588493
```

### Bonus / Challenge Input 2

> "SO + MANY + MORE + MEN + SEEM + TO + SAY + THAT + THEY + MAY + SOON + TRY + TO + STAY + AT + HOME +  SO + AS + TO + SEE + OR + HEAR + THE + SAME + ONE + MAN + TRY + TO + MEET + THE + TEAM + ON + THE + MOON + AS + HE + HAS + AT + THE + OTHER + TEN == TESTS"

Output:
```
mapping found: {"A"=>7, "E"=>0, "H"=>5, "M"=>2, "N"=>6, "O"=>1, "R"=>8, "S"=>3, "T"=>9, "Y"=>4}
         31 + 2764 + 2180 + 206 + 3002 + 91 + 374 + 9579 + 9504 + 274 + 3116 + 984 + 91 + 3974 + 79 + 5120 + 31 + 73 + 91 + 300 + 18 + 5078 + 950 + 3720 + 160 + 276 + 984 + 91 + 2009 + 950 + 9072 + 16 + 950 + 2116 + 73 + 50 + 573 + 79 + 950 + 19508 + 906 = 90393
```

### Bonus / Challenge Input 3

> "THIS + A + FIRE + THEREFORE + FOR + ALL + HISTORIES + I + TELL + A + TALE + THAT + FALSIFIES + ITS + TITLE + TIS + A + LIE + THE + TALE + OF + THE + LAST + FIRE + HORSES + LATE + AFTER + THE + FIRST + FATHERS + FORESEE + THE + HORRORS + THE + LAST + FREE + TROLL + TERRIFIES + THE + HORSES + OF + FIRE + THE + TROLL + RESTS + AT + THE + HOLE + OF + LOSSES + IT + IS + THERE + THAT + SHE + STORES + ROLES + OF + LEATHERS + AFTER + SHE + SATISFIES + HER + HATE + OFF + THOSE + FEARS + A + TASTE + RISES + AS + SHE + HEARS + THE + LEAST + FAR + HORSE + THOSE + FAST + HORSES + THAT + FIRST + HEAR + THE + TROLL + FLEE + OFF + TO + THE + FOREST + THE + HORSES + THAT + ALERTS + RAISE + THE + STARES + OF + THE + OTHERS + AS + THE + TROLL + ASSAILS + AT + THE + TOTAL + SHIFT + HER + TEETH + TEAR + HOOF + OFF + TORSO + AS + THE + LAST + HORSE + FORFEITS + ITS + LIFE + THE + FIRST + FATHERS + HEAR + OF + THE + HORRORS + THEIR + FEARS + THAT + THE + FIRES + FOR + THEIR + FEASTS + ARREST + AS + THE + FIRST + FATHERS + RESETTLE + THE + LAST + OF + THE + FIRE + HORSES + THE + LAST + TROLL + HARASSES + THE + FOREST + HEART + FREE + AT + LAST + OF + THE + LAST + TROLL + ALL + OFFER + THEIR + FIRE + HEAT + TO + THE + ASSISTERS + FAR + OFF + THE + TROLL + FASTS + ITS + LIFE + SHORTER + AS + STARS + RISE + THE + HORSES + REST + SAFE + AFTER + ALL + SHARE + HOT + FISH + AS + THEIR + AFFILIATES + TAILOR + A + ROOFS + FOR + THEIR + SAFE == FORTRESSES"

Output:
```
mapping found: {"A"=>1, "E"=>0, "F"=>5, "H"=>8, "I"=>7, "L"=>2, "O"=>6, "R"=>3, "S"=>4, "T"=>9}
         9874 + 1 + 5730 + 980305630 + 563 + 122 + 874963704 + 7 + 9022 + 1 + 9120 + 9819 + 512475704 + 794 + 97920 + 974 + 1 + 270 + 980 + 9120 + 65 + 980 + 2149 + 5730 + 863404 + 2190 + 15903 + 980 + 57349 + 5198034 + 5630400 + 980 + 8633634 + 980 + 2149 + 5300 + 93622 + 903375704 + 980 + 863404 + 65 + 5730 + 980 + 93622 + 30494 + 19 + 980 + 8620 + 65 + 264404 + 79 + 74 + 98030 + 9819 + 480 + 496304 + 36204 + 65 + 20198034 + 15903 + 480 + 419745704 + 803 + 8190 + 655 + 98640 + 50134 + 1 + 91490 + 37404 + 14 + 480 + 80134 + 980 + 20149 + 513 + 86340 + 98640 + 5149 + 863404 + 9819 + 57349 + 8013 + 980 + 93622 + 5200 + 655 + 96 + 980 + 563049 + 980 + 863404 + 9819 + 120394 + 31740 + 980 + 491304 + 65 + 980 + 698034 + 14 + 980 + 93622 + 1441724 + 19 + 980 + 96912 + 48759 + 803 + 90098 + 9013 + 8665 + 655 + 96346 + 14 + 980 + 2149 + 86340 + 56350794 + 794 + 2750 + 980 + 57349 + 5198034 + 8013 + 65 + 980 + 8633634 + 98073 + 50134 + 9819 + 980 + 57304 + 563 + 98073 + 501494 + 133049 + 14 + 980 + 57349 + 5198034 + 30409920 + 980 + 2149 + 65 + 980 + 5730 + 863404 + 980 + 2149 + 93622 + 81314404 + 980 + 563049 + 80139 + 5300 + 19 + 2149 + 65 + 980 + 2149 + 93622 + 122 + 65503 + 98073 + 5730 + 8019 + 96 + 980 + 144749034 + 513 + 655 + 980 + 93622 + 51494 + 794 + 2750 + 4863903 + 14 + 49134 + 3740 + 980 + 863404 + 3049 + 4150 + 15903 + 122 + 48130 + 869 + 5748 + 14 + 98073 + 1557271904 + 917263 + 1 + 36654 + 563 + 98073 + 4150 = 5639304404
```
