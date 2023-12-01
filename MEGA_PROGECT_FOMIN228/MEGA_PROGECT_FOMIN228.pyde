bb = 300
ee = 25
x = 25
s = 150
y = 25
z = 875
l = 25
dirb = 3.2
dira = 2.9
dirc = 2.7
dird = 3
dirs = 2
def setup():
    size(900,900)
    background(0,5,5)
    frameRate(1000)
    textMode(CENTER)
def draw():
    global x,y,z,l,s,dirs,dira,dirb,dirc,dird,ee,bb
    background(1)
    fill(54,255,0)
    ellipse(bb,ee,35,35)
    ee = ee + 3
    if ee > 875:
        ee = 25
        bb = random(25,875)
    fill(255)
    rect(s,750,200,17)
    s = s + dirs
    if s > 700:
        dirs = -2
    if s < 0:
        dirs = 2
    ellipse(x,y,50,50)
    x = x + dira
    y = y + dirb
    if x > 875:
        dira = -3.2
    if x < 25:
        dira = 3.2
    if y > 1100:
        x = random(25,875)
        y = 25
    if y < 25:
        dirb = 2.9
    ellipse(z,l,50,50)
    z = z + dirc
    l = l + dird
    if z > 875:
        dirc = -2.7
    if z < 25:
        dirc = 2.7
    if l > 1100:
        l = 25
        z = random(25,875)
    if l < 25:
        dird = 3
    if x > s and x < s + 200 and y > 735 and y < 755:
        dirb = -2.9
    if z > s and z < s + 200 and l > 735 and l < 755:
        dird = -3   
    fill(62,83,116)
    textSize(70)
    text("wormax.io",280,200)
    textSize(120)
    fill(130)
    ellipse(450,340,340,180)
    fill(255,23,31)
    text("PLAY",305,380)
    fill(255)
    


    
    
