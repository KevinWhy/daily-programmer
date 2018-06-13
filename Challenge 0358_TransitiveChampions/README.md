# Everyone's A Winner! (aka: Transitive Champions)
https://www.reddit.com/r/dailyprogrammer/comments/8ewq2e/20180425_challenge_358_intermediate_everyones_a/

Completed on May 23, 2018

> Today's challenge comes from the website fivethirtyeight.com,
> which runs a weekly Riddler column.
> Today's dailyprogrammer challenge was the riddler on 2018-04-06.
> > From Matt Gold, a chance, perhaps, to redeem your busted bracket:
> > 
> > On Monday, Villanova won the NCAA men’s basketball national title.
> > But I recently overheard some boisterous Butler fans calling themselves the
> > "transitive national champions,” because Butler beat Villanova earlier in the season.
> > Of course, other teams also beat Butler during the season and their fans could
> > therefore make exactly the same claim.
> > 
> > How many transitive national champions were there this season?
> > Or, maybe more descriptively, how many teams weren’t transitive national champions?
> > 
> > (All of this season’s college basketball results are here.
> > To get you started, Villanova lost to Butler, St. John’s, Providence and Creighton
> > this season, all of whom can claim a transitive title.
> > But remember, teams beat those teams, too.)


### Input Description

Webpage with this season's games: https://www.masseyratings.com/scores.php?s=298892&sub=12801&all=1

I didn't read input dynamically from the webpage.
The program accepts a file containing a list of basketball games.

Assumption: The last game = the championship match

### Output Description

A list of transitive champions, or:
The teams that beat the championship team / another transitive champion.

Output using "BacketballGames.txt" (aka: Games from this season):

```
Number of Teams: 1362
Champion Team:
--------------------------
         Villanova

Number of Transitive Champions: 1184
Transitive Champions:
--------------------------
        S Maine
        Lycoming
        York NY
        Southern Utah
        Keene St
        Albany GA
        Mercer
        PR Bayamon
        Anderson IN
        Troy
        Nova SE
        Paine
        Midwest TX St
        Elizabethtown
        Manhattan
        S Virginia
        Florida Tech
        Covenant
        Seton Hall
        Penn St
        Cazenovia
        CS San Bern.
        UCLA
        Georgia C&S
        Emerson
        Fresno Pacific
        Black Hills St
        Fitchburg St
        Alcorn St
        PSU Mont Alto
        UNLV
        Holy Names
        Virginia
        Drake
        St Francis PA
        Dominican CA
        Brooklyn Col
        FL Southern
        Central St OH
        Palm Beach Atl
        Duke
        Utica
        Cairn
        American Univ
        Lasell
        UVA-Wise
        Colorado
        CS Chico
        Virginia Tech
        Mt St Mary NY
        Manhattanville
        Kentucky Chr
        Philander Smith
        S Wesleyan
        Lesley
        Kennesaw
        NC Pembroke
        ME Presque Isle
        Eckerd
        Maryville TN
        Ashland
        Washington MD
        Purdue
        St Bonaventure
        PSU-DuBois
        Frostburg St
        Lincoln Chr
        Pace
        Salisbury
        Concord
        St Cloud
        Geneseo St
        Post
        Hendrix
        Trinity TX
        Truman St
        Chadron St
        Rollins
        E Illinois
        Delta St
        Carleton MN
        Univ of Southwest
        Shippensburg
        Westminster UT
        Southeastern FL
        S Dakota St
        Oregon
        Anderson SC
        Chattanooga
        Cal St-LA
        Coppin St
        Harvard
        Notre Dame CA
        PSU-Harrisburg
        Neumann
        Jackson St
        St Augustine's
        Spalding
        Lock Haven
        SC Aiken
        Wisconsin
        Indianapolis
        St Joseph's LI
        Dallas Bap
        SUNY New Paltz
        Bluffton
        St Anselm
        Thomas ME
        Maranatha Bap
        MIT
        Luther IA
        Westminster PA
        Providence
        Xavier
        Tusculum
        Florida St
        Ferris St
        Hilbert
        Vanderbilt
        Shaw NC
        Sioux Falls
        R Stockton
        Spring Hill
        Bowdoin
        Jamestown
        Manchester
        Utah
        Lehigh
        Charleston WV
        West Florida
        Chatham
        Oakland City
        Daemen
        Webster Univ
        N Dakota St
        Ft Lewis
        Indiana St
        Monmouth NJ
        WI Milwaukee
        CS San Marcos
        St Peter's
        Marist
        North Park
        Gordon
        E Texas Bap
        Buffalo St
        Houston Bap
        Albright
        Assumption
        Franciscan OH
        Marshall
        Loyola NO
        Fort Valley St
        Lindenwood
        Moravian
        Dubuque
        Iowa St
        Michigan St
        DePaul
        New Mexico St
        St Mary's MN
        Keystone
        Fairfield
        Chowan
        Texas St
        Yeshiva
        North Alabama
        J&W FL
        PSU-Behrend
        Wheaton MA
        Texas
        C Oklahoma
        Indiana PA
        Northeastern
        Oglethorpe
        St Mary's TX
        Wayne St MI
        Charleston So
        St Vincent
        Mt St Vincent
        W Texas A&M
        UC Irvine
        WI Eau Claire
        La Verne
        Univ Ozarks
        Kenyon
        Edgewood
        Southern Miss
        SW Baptist
        Abilene Chr
        Millersville
        Berea
        Stevens Tech
        Bethel TN
        George Mason
        Michigan Tech
        PSU-Schuylkill
        North Dakota
        Hiram
        Grandview
        Mississippi St
        Clarke
        MA Liberal Arts
        Cheyney St
        Adrian
        St Joseph's PA
        Whitman
        SW Minnesota
        TX Lutheran
        Davenport
        Pacific Union
        Rivier
        Calvin
        Clark Atlanta
        St John Fisher
        St Martin's
        S Carolina St
        Colorado Chr
        E Nazarene
        North Carolina
        Vanguard
        Iowa Wesleyan
        OK Baptist
        UC Santa Cruz
        Arkansas Tech
        Worcester St
        Pomona Pitzer
        Florida Intl
        Wayne St NE
        Quincy
        UT Dallas
        Ohio St
        Richmond
        MN Duluth
        Detroit
        Air Force
        Cal Baptist
        McNeese St
        UTRGV
        Hamline
        Belhaven MS
        Boston College
        Simpson IA
        CS Fullerton
        Pitt-Bradford
        Hampton
        Syracuse
        Mt Ida
        Maryland
        Chr Brothers
        N Kentucky
        Humboldt St
        MO St Louis
        Millikin
        Concordia Mhd
        Oregon St
        Anna Maria
        ETSU
        Holy Cross
        Embry-Riddle FL
        MO Southern
        Peace
        Missouri KC
        Lewis & Clark
        Princeton
        Roger Williams
        Boise St
        Emmanuel MA
        Santa Clara
        Cent Arkansas
        Alabama A&M
        Young Harris
        Incarnate Word
        Willamette
        Milwaukee Eng
        Bethel KS
        Bryn Athyn
        NM Highlands
        Wilberforce
        Bridgewater VA
        Augustana SD
        C Washington
        Minnesota
        North Greenville
        Graceland
        St Mary's MD
        CS Sacramento
        Cornerstone
        Bethel MN
        Univ Sciences
        Rutgers-Newark
        Frank & Marsh
        Brockport St
        Catawba
        Hanover
        California PA
        Baldwin-Wallace
        NE Kearney
        Spring Arbor
        San Jose St
        SUNY Fredonia
        WV Tech
        Guilford
        Butler
        Bentley
        Charlotte
        Randall
        Ohio Valley
        E Connecticut
        Swarthmore
        Northwestern
        Rowan
        Central Conn
        Roosevelt
        Harris-Stowe
        Murray St
        Bradley
        Coastal Car
        Memphis
        LSU
        Arizona St
        Rhodes
        Albion
        CS Poly Pomona
        Michigan
        UT Tyler
        Colorado Col
        Seton Hill
        Loy Marymount
        Jacksonville
        Thomas GA
        La Sierra
        Notre Dame
        Georgia St
        Evergreen St
        Northern St SD
        CS Stanislaus
        S Francisco St
        Babson
        Northern Iowa
        Case Western
        Rochester MI
        Lawrence
        Texas A&M
        Wilkes
        Findlay
        Fayetteville St
        Queens NC
        Waldorf
        Hobart & Smith
        Ark Monticello
        TX Southern
        Hawaii
        Wright St
        Geneva
        IL Springfield
        Olivet MI
        AK Anchorage
        Belmont Abbey
        Southern Nazarene
        Urbana
        Point Loma
        Auburn
        St Francis NY
        JC Smith
        Austin Peay
        Gettysburg
        Lynn
        Oakland
        Silver Lake
        NC A&T
        Mary ND
        Lane
        F Dickinson
        S Dakota Tech
        Emmanuel GA
        Freed-Hardeman
        Summit
        Northern Arizona
        WI Stevens Pt
        Wyoming
        Centenary
        Blackburn
        Wooster
        St Norbert
        Hope Intl
        Carson-Newman
        IL Wesleyan
        Miami OH
        LeMoyne-Owen
        Regis MA
        Cornell
        S Arkansas
        Arizona
        Marquette
        Southern Univ
        Bob Jones
        UC Santa Barbara
        Boston Univ
        Castleton
        Fordham
        Dallas Chr
        Emory & Henry
        Ohio
        Louisiana Col
        Bryant
        Georgia Tech
        Wagner
        Seattle
        Beloit
        ULL
        Portland Bible
        SUNY Oneonta
        Florida A&M
        Berkeley NYC
        Russell Sage
        PSU-Brandywine
        W Oregon
        CS Dom. Hills
        Messiah
        Pittsburg St
        Marymount VA
        Washington MO
        Newberry
        WI Whitewater
        KY Wesleyan
        Rochester NY
        Grand Canyon
        Roanoke
        Amherst
        Mars Hill
        Centenary NJ
        W Michigan
        Dallas Univ
        Washington
        Francis Marion
        Villa Maria
        Tuskegee
        Mississippi Col
        King's PA
        Oklahoma
        J&W RI
        St Mary's CA
        Framingham St
        Millsaps
        NE Omaha
        MO Western
        NY Maritime
        Centre
        Grove City
        LSU Shreveport
        Wofford
        Lincoln Mem
        Morgan St
        Kent
        Roberts Wslyn
        SUNY Potsdam
        Plattsburgh St
        Wingate
        Toledo
        Colorado Mines
        Dist Columbia
        Arizona Chr
        Wash & Lee
        Westfield St
        Great Lakes Chr
        Kansas St
        Dominican NY
        Farmingdale
        Methodist
        Hawaii Hilo
        Arkansas-FS
        Ripon
        Dixie St
        Widener
        Indiana
        Cornell IA
        Cent Methodist
        RI College
        Rogers St
        Evansville
        W Carolina
        MS Valley St
        Col Charleston
        Stony Brook
        UT Arlington
        Vassar
        Chapman
        Otterbein
        Bucknell
        Whittier
        Akron
        New Haven
        MN Mankato
        Colorado St
        Maryville MO
        Staten Island
        Clark MA
        Drew
        Vermont
        S Indiana
        Henderson St
        NW Oklahoma St
        St Scholastica
        Colby-Sawyer
        Medaille
        Piedmont
        Endicott
        Merrimack
        Illinois St
        Cal Lutheran
        MA Lowell
        C Michigan
        ME Ft Kent
        Plymouth St
        Bard
        Connecticut
        Cameron
        Stonehill
        Colgate
        Berry
        Thomas More
        WI Superior
        La Salle
        Lander
        Bellarmine
        Winona St
        Mt St Mary's
        E Stroudsburg
        New Rochelle
        Central IA
        Winthrop
        VA Wesleyan
        Oklahoma Chr
        Penn Col Tech
        Alma
        Alfred
        Earlham
        Concordia NE
        Drury
        Metro St
        St John's
        W Washington
        N Central MN
        St Michael's
        Curry
        Pitt-Johnstown
        SUNYIT
        SE Oklahoma
        NYU
        NC Central
        Glenville St
        South Carolina
        Canisius
        Valparaiso
        Houston
        Fairmont St
        Dominican IL
        Rensselaer
        Benedictine IL
        Molloy
        Samford
        Wilmington OH
        Drexel
        Nichols
        AL Huntsville
        Tennessee Tech
        Massachusetts
        Crown MN
        WKU
        Western St CO
        Averett
        Presbyterian
        Wm Jewell
        Ithaca
        Morrisville St
        AK Fairbanks
        Appalachian St
        Augsburg
        Rosemont
        UT San Antonio
        Tulsa
        Merchant Marine
        King TN
        East Central OK
        WV Wesleyan
        Bowie St
        N England Col
        Mississippi
        McDaniel Col
        Alabama St
        Denver
        PSU-Berks
        Kentucky St
        Bethany Luth
        Fresno St
        William & Mary
        Nicholls St
        Pac Lutheran
        CT College
        Cincinnati
        Missouri S&T
        Robert Morris
        SUNY Canton
        WI River Falls
        Flagler
        E Michigan
        Bethany WV
        Mobile
        California
        West Chester
        West Georgia
        S Illinois
        Rockford
        Elmhurst
        Brandeis
        Wheeling Jesuit
        Wright St-Lake
        VMI
        Ursinus
        Long Beach St
        Miles
        Lakeland
        TAM C. Christi
        Buena Vista
        St Elizabeth
        Mt Olive
        Corban
        Weber St
        Chestnut Hill
        Florida National
        Moorhead St
        Mt Aloysius
        Grinnell
        Emory
        Pepperdine
        Denison
        Stetson
        Lebanon Val
        Rutgers
        S New Hampshire
        Adams St
        Sacred Heart
        TX A&M Commerce
        Penn
        Tiffin
        MN Morris
        Iowa
        Temple
        Trine
        Florida Col
        Cal Maritime
        Lake Forest
        Siena
        Montreat
        Eliz. City St
        Thomas Aquinas
        Birmingham So
        Five Towns
        St Leo
        Ohio Northern
        South Florida
        Randolph Col
        IPFW
        SUNY-Delhi
        Menlo
        Wheaton IL
        Muhlenberg
        St Olaf
        Texas A&M Intl
        Pfeiffer
        FL Gulf Coast
        Walsh
        Wartburg
        Northwest WA
        Fisher
        Suffolk
        Dickinson
        Warner Pacific
        Howard Payne
        Tarleton St
        Mt Vernon Naz
        Hawaii Pacific
        Goldey Beacom
        Benedict
        Longwood
        Finlandia
        Ark Pine Bluff
        Juniata
        Lubbock Chr
        Valley City St
        Georgia
        Fort Hays St
        Ald-Broaddus
        Nazareth
        Aquinas
        Hartwick
        Redlands
        Huntingdon
        UMBC
        Tougaloo
        Loyola-Chicago
        Bluefield VA
        Rocky Mtn
        La Roche
        Dean
        Rose-Hulman
        WI Oshkosh
        Husson
        Le Tourneau
        UTEP
        South Dakota
        S Connecticut
        UCF
        Purdue Northwest
        Rochester Tech
        MA Boston
        NYIT
        C Missouri
        Johnson St
        Central Bap
        Oberlin
        Newman
        Delaware St
        Puget Sound
        Mesa St
        Kean
        St Edward's
        Tulane
        MacMurray
        Carthage
        W Salem St
        MD E Shore
        Stanford
        Oral Roberts
        St Francis IL
        Muskingum
        Davidson
        ME Maritime
        Wm Paterson
        Malone
        Newbury
        Barton
        OK Wesleyan
        Edinboro
        OK City
        Liberty
        Col of Idaho
        Bloomfield
        WI Parkside
        Allen
        Becker
        San Diego St
        West Liberty
        NE Oklahoma
        Stevenson
        Hardin-Simmons
        Duquesne
        Lancaster Bib
        IL Tech
        Hampden-Sydney
        Catholic
        Mercy
        Wittenberg
        TCU
        American Intl
        UNC Wilmington
        W Coast Bap
        Lafayette
        Oklahoma S&A
        Shepherd
        Bates
        Georgian Court
        D'Youville
        Lake Erie
        Trevecca Naz
        Columbus St
        Stillman
        Augusta
        Col Springs
        Adelphi
        Presentation
        Illinois Col
        John Jay
        Scranton
        Nebraska
        Brevard
        Hope
        Utah Valley
        WI Lutheran
        Caldwell
        J&W CO
        Oklahoma St
        Tennessee
        Chicago
        Missouri St
        Mt St Joseph
        Concordia SP
        Missouri
        Cabrini
        Concordia IL
        NE Wesleyan
        Northland
        Purchase
        Card Stritch
        Gonzaga
        Iona
        Union TN
        New Mexico
        ULM
        Idaho St
        Chris Newport
        East Carolina
        Concordia CA
        Delaware
        Creighton
        Ark Little Rock
        Ga Southern
        Prairie View
        Cedarville
        Towson
        Augustana IL
        Harding
        Dayton
        WI Green Bay
        Voorhees
        PSU York
        Franklin Pierce
        Upper Iowa
        Yale
        IL Chicago
        Bridgeport
        SMU
        WI Platteville
        Washington St
        New Orleans
        Valley Forge
        Sam Houston St
        Johnson TN
        MTSU
        Ramapo
        NW Nazarene
        Rice
        Academy of Art
        Warren Wilson
        NC State
        Monmouth IL
        St Joseph's NY
        Pine Manor
        Norfolk St
        Savannah St
        Baylor
        Elon
        Pacific
        Hartford
        Lincoln MO
        Nyack
        Kalamazoo
        Tennessee St
        Eastern Univ
        Wilmington DE
        Hillsdale
        PSU-Abington
        Dartmouth
        W New Mexico
        Virginia Union
        Cleveland St
        Bowling Green
        Medgar Evers
        Mitchell
        ME Farmington
        Elmira
        Pacific OR
        SW Univ TX
        Utah St
        Bridgewater MA
        Greensboro
        Tufts
        Albertus Magnus
        Wichita St
        Belmont
        UC San Diego
        St Thomas FL
        Mary Washington
        Hunter
        College of NJ
        W New England
        MN Crookston
        Radford
        Chicago St
        Washburn
        Union NY
        Angelo St
        Wayland
        Lee TN
        BYU
        Chaminade
        Wells
        NW Missouri
        Notre Dame OH
        CSU-Pueblo
        Pitt-Greensburg
        E Washington
        Macalester
        MA Dartmouth
        Lenoir Rhyne
        Portland St
        USC
        NJIT
        McKendree
        SW Adventist
        E Mennonite
        Emporia St
        Erskine
        Mercyhurst
        Salem MA
        St Lawrence
        Idaho
        Mt Union
        Miami FL
        Gust Adolphus
        SUNY-Cobleskill
        Cortland St
        Wilson
        Sul Ross
        S Vermont
        Colby
        Portland
        Rhode Island
        Clayton St
        WI Stout
        OH Dominican
        Washington Advt
        Louisville
        N Colorado
        Arkansas
        Hofstra
        Navy
        James Madison
        Springfield
        Montclair St
        DePauw
        Bluefield WV
        San Francisco
        CS Monterey Bay
        Nevada
        Baruch
        Simon Fraser
        Tampa
        Concordia MI
        DeSales
        Sewanee
        Alvernia
        Schreiner
        City Col NY
        Capital
        West Virginia
        Green Mtn
        Old Westbury
        Westminster MO
        Lewis
        Saginaw Val
        Haverford
        Viterbo
        Lehman
        Felician
        Johns Hopkins
        Lyndon St
        CW Post
        Judson IL
        Mansfield
        Army
        Bloomsburg
        Gallaudet
        Concordia OR
        Sonoma St
        Wake Forest
        FDU Madison
        Wash & Jeff
        Grambling
        CSU East Bay
        Lake Superior
        FL Atlantic
        Principia
        Morningside
        Ball St
        Virginia St
        Buffalo
        UC Merced
        NJ City
        Ouachita
        Marian WI
        Mayville St
        Lincoln PA
        St Rose
        Pittsburgh
        San Diego
        Delaware Val
        U New England
        Old Dominion
        Worcester Tech
        LaGrange
        Allegheny
        Susquehanna
        North Georgia
        Montana St
        Florida
        New Hampshire
        W Connecticut
        CS Bakersfield
        Lamar
        Slippery Rock
        Northwest Chr
        SIUE
        Eureka
        Greenville
        Norwich
        Rider
        Middlebury
        Elms
        Carroll WI
        SE Missouri St
        TX A&M K'ville
        E Kentucky
        Georgetown
        Loras
        Jacksonville St
        Wentworth Tech
        Heidelberg
        Niagara
        Binghamton
        Coe
        Illinois
        UAB
        South Alabama
        IUPUI
        NC Wesleyan
        UC Davis
        Carnegie Mellon
        Northwood MI
        Franklin IN
        High Point
        M Hardin-Baylor
        UNC Asheville
        Concordia TX
        Campbell
        Alabama
        Columbia
        Lees-McRae
        York PA
        Salve Regina
        St Thomas MN
        Arcadia
        Whitworth
        Auburn M'gomery
        Rockhurst
        Aurora
        SW Oklahoma
        Bethune-Cookman
        W Illinois
        Gwynedd-Mercy
        Regis CO
        Grand Valley St
        G Washington
        Sarah Lawrence
        Montana
        Kansas
        Barry
        CS Northridge
        MT St-Billings
        E New Mexico
        Gannon
        Concordia NY
        PSU Wilkes-Barre
        Limestone
        Caltech
        Shorter
        Quinnipiac
        Wesley DE
        Loyola MD
        Gardner Webb
        Clarkson
        Seattle Pacific
        SC Upstate
        Texas Tech
        Holy Family
        Albany Pharmacy
        Kutztown
        Houghton
        Trinity CT
        Salem WV
        Valdosta St
        Misericordia
        St Joseph's ME
        Long Island
        Wabash
        Skidmore
        Davis & Elkins
        Cal Poly
        Montevallo
        Lipscomb
        North Florida
        UNC Greensboro
        T Jefferson
        Northwestern MN
        WI LaCrosse
        Northwestern LA
        Thiel
        Morehouse
        North Texas
        Occidental
        Rutgers-Camden
        St John's MN
        Kentucky
        Linfield
        Queens NY
        Marywood
        TN Martin
        Albany NY
        Defiance
        Ohio Wesleyan
        Lynchburg
        Alfred St
        Austin Col
        Transylvania
        St Louis
        Ferrum
        N Central IL
        Coker
        Citadel
        SE Louisiana
        VA Commonwealth
        Permian Basin
        Unity
        Georgia SW
        Biola
        WV State
        Livingstone
        SF Austin
        Fontbonne
        Youngstown St
        Coast Guard
        Waynesburg
        Wesleyan CT
        Knox
        Williams
        Oswego St
        PSU-Altoona
        Marietta
        Westmont
        N Michigan
        Azusa Pacific
        Hood
        West Alabama
        Louisiana Tech
        Arkansas St
        Wheelock
        Hamilton
        Morehead St
        Howard
        John Carroll
        Luther MN
        Bemidji St
        Clemson
        Maine
        Immaculata
        Shenandoah
        McMurry
        Le Moyne
        Minot St
        Panhandle St
        N Illinois
        Concordia WI
        Clarion
        Randolph Macon
        George Fox
        UC Riverside
        Claremont M.S.
        Shawnee St
        Furman
        Keuka
        Claflin
        Point
        Brown
```
