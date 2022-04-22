# Rafael Sanchez
# Desc: Of a huge list of users, it finds 3 top users that have the highest compatibility, as well as their compatibility score.
import math
import random

class Person:
    def __init__(self, name="Jose", sex=1, location=(20, 20), personality=[50, 50, 50, 50, 50], age=25, height=6.0, body_type=3, education=6, smoke=False, drinks=False, ethnicity=[5, 3], religion=3, hobbies=[25, 165, 32]):
        self.name = name
        self.sex = sex
        self.location = location
        self.personality = personality
        self.age = age
        self.height = height
        self.body_type = body_type
        self.education = education
        self.smoke = smoke
        self.drinks = drinks
        self.ethnicity = ethnicity
        self.religion = religion
        self.hobbies = hobbies

    def printAll(self):
        format_sex = ''
        if self.sex==1:
            format_sex = 'Male'
        else:
            format_sex = 'Female'
        format_body_type = ''
        if self.body_type==1:
            format_body_type = 'Slim/Slender'
        elif self.body_type==2:
            format_body_type = 'Athletic/Fit'
        elif self.body_type==3:
            format_body_type = 'About Average'
        elif self.body_type==4:
            format_body_type = 'Muscular'
        elif self.body_type==5:
            format_body_type = 'Curvy'
        elif self.body_type==6:
            format_body_type = 'A few extra pounds'
        elif self.body_type==7:
            format_body_type = 'Big and Beautiful'
        elif self.body_type==8:
            format_body_type = 'Heavyset'
        format_edu = ''
        if self.body_type==1:
            format_edu = 'Less than hs'
        elif self.body_type==2:
            format_edu = 'High school incomplete'
        elif self.body_type==3:
            format_edu = 'High school grad'
        elif self.body_type==4:
            format_edu = 'Some college, no degree'
        elif self.body_type==5:
            format_edu = 'Two year associate degree'
        elif self.body_type==6:
            format_edu = 'Four year bachelor degree'
        elif self.body_type==7:
            format_edu = 'Some postgrad or professional school'
        elif self.body_type==8:
            format_edu = 'Postgrad or professional degree, including masters, phd, etc'
        format_smoke = ''
        if self.smoke:
            format_smoke = 'Smokes'
        else:
            format_smoke = 'Doesnt Smoke'
        format_drinks = ''
        if self.drinks:
            format_drinks = 'Drinks'
        else:
            format_drinks = 'Doesnt drink'
        format_eth = []
        for i in range(len(self.ethnicity)):
            if self.ethnicity[i]==1:
                format_eth.append('Asian')
            elif self.ethnicity[i]==2:
                format_eth.append('Black')
            elif self.ethnicity[i]==3:
                format_eth.append('Hispanic/Latin')
            elif self.ethnicity[i]==4:
                format_eth.append('Indian')
            elif self.ethnicity[i]==5:
                format_eth.append('White')
            elif self.ethnicity[i]==6:
                format_eth.append('Native American')
            elif self.ethnicity[i]==7:
                format_eth.append('Middle Eastern')
            elif self.ethnicity[i]==8:
                format_eth.append('Pacific Islander')
            elif self.ethnicity[i]==9:
                format_eth.append('Other')
        format_rel = ''
        if self.religion==1:
            format_rel = 'Adventist'
        elif self.religion==2:
            format_rel = 'Agnostic'
        elif self.religion==3:
            format_rel = 'Atheist'
        elif self.religion==4:
            format_rel = 'Buddhist / Taoist'
        elif self.religion==5:
            format_rel = 'Christian / Catholic'
        elif self.religion==6:
            format_rel = 'Christian / LDS'
        elif self.religion==7:
            format_rel = 'Christian / Protestant'
        elif self.religion==8:
            format_rel = 'Christian / Other'
        elif self.religion==9:
            format_rel = 'Hindu'
        elif self.religion==10:
            format_rel = 'Jewish'
        elif self.religion==11:
            format_rel = 'Muslim / Islam'
        elif self.religion==12:
            format_rel = 'Spiritual but not religious'
        elif self.religion==13:
            format_rel = 'Other'
        hobbies_arr = ['Water sports','3D printing','amateur radio','scrapbook','Amateur radio','Acting','Baton twirling','Board games','Book restoration','Cabaret','Calligraphy','Candle making','Computer programming','Coffee roasting','Cooking','Coloring','Cosplaying','Couponing','Creative writing','Crocheting','Cryptography','Dance','Digital arts','Drama','Drawing','Do it yourself','Electronics','Embroidery','Fashion','Flower arranging','Foreign language learning','Gaming','tabletop games','role-playing games','Gambling','Genealogy','Glassblowing','Gunsmithing','Homebrewing','Ice skating','Jewelry making','Jigsaw puzzles','Juggling','Knapping','Knitting','Kabaddi','Knife making','Lacemaking','Lapidary','Leather crafting','Lego building','Lockpicking','Machining','Macrame','Metalworking','Magic','Model building','Listening to music','Origami','Painting','Playing musical instruments','Pet','Poi','Pottery','Puzzles','Quilting','Reading','Scrapbooking','Sculpting','Sewing','Singing','Sketching','Soapmaking','Sports','Stand-up comedy','Sudoku','Table tennis','Taxidermy','Video gaming','Watching movies','Web surfing','Whittling','Wood carving','Woodworking','Worldbuilding','Writing','Yoga','Yo-yoing','Air sports','Archery','Astronomy','Backpacking','BASE jumping','Baseball','Basketball','Beekeeping','Bird watching','Blacksmithing','Board sports','Bodybuilding','Brazilian jiu-jitsu','Community','Cycling','Dowsing','Driving','Fishing','Flag Football','Flying','Flying disc','Foraging','Gardening','Geocaching','Ghost hunting','Graffiti','Handball','Hiking','Hooping','Horseback riding','Hunting','Inline skating','Jogging','Kayaking','Kite flying','Kitesurfing','LARPing','Letterboxing','Metal detecting','Motor sports','Mountain biking','Mountaineering','Mushroom hunting','Mycology','Netball','Nordic skating','Orienteering','Paintball','Parkour','Photography','Polo','Rafting','Rappelling','Rock climbing','Roller skating','Rugby','Running','Sailing','Sand art','Scouting','Scuba diving','Sculling','Rowing','Shooting','Shopping','Skateboarding','Skiing','Skimboarding','Skydiving','Slacklining','Snowboarding','Stone skipping','Surfing','Swimming','Taekwondo','Tai chi','Urban exploration','Vacation','Vehicle restoration']
        
        format_hob = []
        for hob_ind in self.hobbies:
            format_hob.append(hobbies_arr[hob_ind-1])
        print(self.name, ' | Sex ', format_sex, ' | Location ', self.location, ' | Big 5 ', self.personality, ' | Age ', self.age, ' | Height ', format(self.height, '.1f'), ' | Body type ', format_body_type, ' | Education ', format_edu, ' | ', format_smoke, ' | ',format_drinks, ' | ', format_eth, ' | ', format_rel, ' | Hobbies ', format_hob)

def match_score(b, g):
    score = 0
    dist = math.dist(b.location, g.location)
    MAX_DIST = 10 # miles
    # idea is that location is a big factor, thus the number should make a bigger difference in the score, so we amplify it. Same idea with other data
    AMPLIFIER_data_1 = 100
    data_1 = MAX_DIST - dist
    if data_1 > 0:
        score += (data_1*AMPLIFIER_data_1)
    
    for i in range(0, len(b.personality)):
        dif = abs(b.personality[i]-g.personality[i])
        MAX_DIF = 98
        AMPLIFIER_data_2 = 8
        if dif <= MAX_DIF:
            data_2 = MAX_DIF - dif
            score += data_2*AMPLIFIER_data_2

    MAX_AGE = 20
    age_dif = abs(b.age-g.age)
    AMPLIFIER_data_3 = 20
    if age_dif <= MAX_AGE:
        data_3 = MAX_AGE - age_dif
        score += data_3*AMPLIFIER_data_3
    
    MAX_HEIGHT = 2.0
    height_dif = abs(b.height-g.height)
    AMPLIFIER_data_4 = 100
    if height_dif <= MAX_HEIGHT:
        data_4 = MAX_HEIGHT-height_dif
        score += data_4*AMPLIFIER_data_4

    MAX_BODY = 90
    if b.body_type==g.body_type:
        data_5 = MAX_BODY
        score += data_5

    MAX_EDU = 8
    edu_dif = abs(b.education-g.education)
    data_6 = MAX_EDU-edu_dif
    AMPLIFIER_data_6 = 25
    score += data_6*AMPLIFIER_data_6

    MAX_SMOKE = 75
    if b.smoke==g.smoke:
        data_7 = MAX_SMOKE
        score += data_7

    MAX_DRINK = 75
    if b.drinks==g.drinks:
        data_8 = MAX_DRINK
        score += data_8

    res_boy = b.ethnicity
    res_boy.sort()
    res_girl = g.ethnicity
    res_girl.sort()
    MAX_ETH = 75
    if res_boy==res_girl:
        data_10 = MAX_ETH
        score += data_10

    MAX_REL = 75
    if b.religion==g.religion:
        data_11 = MAX_REL
        score += data_11

    for hobby_b in b.hobbies:
        for hobby_g in g.hobbies:
            if hobby_b==hobby_g:
                data_12 = 50
                score += data_12

    total = 6110
    percentage = (score/total)*100
    BOOST = 9.0
    percentage += BOOST
    if percentage <= 100:
        return percentage
    else:
        return 100.0

def generate_person(pname, psex):
    MAX_WID = 25
    MAX_HEI = 25
    return Person(name=pname, sex=psex, location=(random.randint(10, MAX_WID-10), random.randint(10, MAX_HEI-10)), personality=[random.randint(0, 100), random.randint(0, 100), random.randint(0, 100), random.randint(0, 100), random.randint(0, 100)], age=random.randint(18, 65), height=random.uniform(4.5, 7), body_type=random.randint(1, 8), education=random.randint(1, 8), smoke=random.randint(0, 1), drinks=random.randint(0, 1), ethnicity=[random.randint(1, 9)], religion=random.randint(1, 13),  hobbies=[random.randint(1, 167), random.randint(1, 167), random.randint(1, 167), random.randint(1, 167), random.randint(1, 167)])

people = []
for i in range(1000):
    if i%2==0:
        lines = open('male_names.txt').read().splitlines()
        myline =random.choice(lines)
        people.append(generate_person(myline, 1))
    else:
        lines = open('female_names.txt').read().splitlines()
        myline =random.choice(lines)
        people.append(generate_person(myline, 2))

scores_arr = []
people_index = []
for i in range(1000):
    for j in range(1000):
        if i!=j and people[i].sex==1 and people[j].sex==2:
            scores_arr.append((match_score(people[i], people[j]), people[i], people[j]))

scores_arr.sort(key=lambda tup: tup[0], reverse=True)
print("")
print("*****************1st Compatible Couple*****************")
print('Score', format(scores_arr[0][0], ".1f"), '%')
print("")
scores_arr[0][1].printAll()
print("")
scores_arr[0][2].printAll()
print("")
print("*****************2nd Compatible Couple*****************")
print('Score', format(scores_arr[1][0], ".1f"), '%')
print("")
scores_arr[1][1].printAll()
print("")
scores_arr[1][2].printAll()
print("")
print("*****************3rd Compatible Couple*****************")
print('Score', format(scores_arr[2][0], ".1f"), '%')
print("")
scores_arr[2][1].printAll()
print("")
scores_arr[2][2].printAll()
print("")
