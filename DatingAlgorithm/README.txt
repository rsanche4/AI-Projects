Inspired by the episode of Black Mirror "Hang the DJ", I decided to learn how dating apps work.
Written in Python, the program runs the algorithm with many users and selects the most compatible ones, and also returns their compatibility score.

What are users?
- Location (Putting dots in some grid)
- Personality (The Big 5 encoded)
- Age
- Weight
- Height
- Body Types (encoded)
- Education
- Smoke
- Drinking
- Ethnicity
- Religion
- sex
- Hobbies (encoded as a long lists of hobbies)

How is cscore determined?
Well, we look at all of this data points, and compare them like this:
- Close locations
- similar personalities
- similar age
- similar weight
- men taller than girl (or just a bit around the same height)
- similar body types
- similar education levels
- both smoke or not
- both drink or not
- similar ethnicity
- similar religion
- similar hobbies

Note: I did not take having kids into account, mental health, disorders, people lying about who they are, facial similarities, although that could be added as well for future reference.

How is the data encoded?
 location refers to x and y points on a grid
 sex : 1 for male, 2 for female
 personality = [O score, C, E, A, N] in the Big 5 Test
 weight is in pounds
 height is in feet
 body_type is encoded as:
       1 Slim/Slender
       2 Athletic/Fit
       3 About Average
       4 Muscular
       5 Curvy
       6 A few extra pounds
       7 Big and Beautiful
       8 Heavyset
 education
       1 Less than hs
       2 high school incomplete
       3 high school grad
       4 some college, no degree
       5 two year associate degree
       6 four year bachelor degree
       7 some postgrad or professional school
       8 postgrad or professional degree, including master's, phd, etc
 drinking means if the person drinks regularly
 ethnicity = [an array with all the options true below]
       1 Asian
       2 Black
       3 Hispanic/Latin
       4 Indian
       5 White
       6 Native American
       7 Middle Eastern
       8 Pacific Islander
       9 Other
 religion
       1 Adventist
       2 Agnostic
       3 Atheist
       4 Buddhist / Taoist
       5 Christian / Catholic
       6 Christian / LDS
       7 Christian / Protestant
       8 Christian / Other
       9 Hindu
       10 Jewish
       11 Muslim / Islam
       12 Spiritual but not religious
       13 Other
  hobbies = [list of all different hobbies]
 1 Water sports
 2 3D printing
 3 amateur radio
 4 scrapbook
 5 Amateur radio
 6 Acting
 7 Baton twirling
 8 Board games
 9 Book restoration
 10 Cabaret
 11 Calligraphy
 12 Candle making
 13 Computer programming
 14 Coffee roasting
 15 Cooking
 16 Coloring
 17 Cosplaying
 18 Couponing
 19 Creative writing
 20 Crocheting
 21 Cryptography
 22 Dance
 23 Digital arts
 24 Drama
 25 Drawing
 26 Do it yourself
 27 Electronics
 28 Embroidery
 29 Fashion
 30 Flower arranging
 31 Foreign language learning
 32 Gaming
 33 tabletop games
 34 role-playing games
 35 Gambling
 36 Genealogy
 37 Glassblowing
 38 Gunsmithing
 39 Homebrewing
 40 Ice skating
 41 Jewelry making
 42 Jigsaw puzzles
 43 Juggling
 44 Knapping
 45 Knitting
 46 Kabaddi
 47 Knife making
 48 Lacemaking
 49 Lapidary
 50 Leather crafting
 51 Lego building
 52 Lockpicking
 53 Machining
 54 Macrame
 55 Metalworking
 56 Magic
 57 Model building
 58 Listening to music
 59 Origami
 60 Painting
 61 Playing musical instruments
 62 Pet
 63 Poi
 64 Pottery
 65 Puzzles
 66 Quilting
 67 Reading
 68 Scrapbooking
 69 Sculpting
 70 Sewing
 71 Singing
 72 Sketching
 73 Soapmaking
 74 Sports
 75 Stand-up comedy
 76 Sudoku
 77 Table tennis
 78 Taxidermy
 79 Video gaming
 80 Watching movies
 81 Web surfing
 82 Whittling
 83 Wood carving
 84 Woodworking
 85 Worldbuilding
 86 Writing
 87 Yoga
 88 Yo-yoing
 89 Air sports
 90 Archery
 91 Astronomy
 92 Backpacking
 93 BASE jumping
 94 Baseball
 95 Basketball
 96 Beekeeping
 97 Bird watching
 98 Blacksmithing
 99 Board sports
 100 Bodybuilding
 101 Brazilian jiu-jitsu
 102 Community
 103 Cycling
 104 Dowsing
 105 Driving
 106 Fishing
 107 Flag Football
 108 Flying
 109 Flying disc
 110 Foraging
 111 Gardening
 112 Geocaching
 113 Ghost hunting
 114 Graffiti
 115 Handball
 116 Hiking
 117 Hooping
 118 Horseback riding
 119 Hunting
 120 Inline skating
 121 Jogging
 122 Kayaking
 123 Kite flying
 124 Kitesurfing
 125 LARPing
 126 Letterboxing
 127 Metal detecting
 128 Motor sports
 129 Mountain biking
 130 Mountaineering
 131 Mushroom hunting
 132 Mycology
 133 Netball
 134 Nordic skating
 135 Orienteering
 136 Paintball
 137 Parkour
 138 Photography
 139 Polo
 140 Rafting
 141 Rappelling
 142 Rock climbing
 143 Roller skating
 144 Rugby
 145 Running
 146 Sailing
 147 Sand art
 148 Scouting
 149 Scuba diving
 150 Sculling
 151 Rowing
 152 Shooting
 153 Shopping
 154 Skateboarding
 155 Skiing
 156 Skimboarding
 157 Skydiving
 158 Slacklining
 159 Snowboarding
 160 Stone skipping
 161 Surfing
 162 Swimming
 163 Taekwondo
 164 Tai chi
 165 Urban exploration
 166 Vacation
 167 Vehicle restoration