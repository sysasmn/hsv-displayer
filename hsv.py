import math 

def nearestinteger(f):  #note that this not work for negative numbers
    if (f < 0):
        print("nearestinteger() does not accept ", f)
        return -1
    d = math.modf(f)[0]

    if (d < 0.5):
        return math.floor(f)
    else:
        return math.ceil(f)

def hsvtorgb(h, s, v):
    #check these values are in the proper ranges
    #check h is undefined
    if h < 0 or h > 360: 
        print(h, s, v, "Bad Input")
        return []

    if s < 0 or s > 1:
        print(h, s, v, "bad Input")
        return []

    if v < 0 or v > 1:
        print(h,s,v,"Bad Input")
        return []

    c = v*s
    m = v-c
    h1 = h/60
    
    x = c * (1 - abs((h1 % 2) - 1))
    if 0 <= h1 and h1 <= 1:
        rgb1 = [c, x, 0] 
    
    elif 1 < h1 and h1 <= 2:
        rgb1 =  [x, c, 0]

    elif 2 < h1 and h1 <= 3:
        rgb1 = [0, c, x]

    elif 3 < h1 and h1 <= 4:
        rgb1 = [0, x, c]

    elif 4 < h1 and h1 <= 5:
        rgb1 = [x, 0, c]

    elif 5 < h1 <= 6:
        rgb1 = [c, 0, x]

    else:
        rgb1 =  [0, 0, 0] 

    return [nearestinteger((rgb1[0]+m)*255), nearestinteger((rgb1[1]+m)*255), nearestinteger((rgb1[2]+m)*255)]

def fixlength(h):
    #brings length up to 2 in case of a single digit hex number
    if len(h) == 1:
        return "0" + h.upper()
    
    return h.upper()

def rgbtohex(r,g,b):
    hexr = fixlength(hex(r)[2:])
    hexg = fixlength(hex(g)[2:])
    hexb = fixlength(hex(b)[2:])
    
    foo = "#"+hexr+hexg+hexb 
    #return [hex(r), hex(g), hex(b)]
    return foo

def hsvtohex(h, s, v):
    rgb = hsvtorgb(h, s, v)
    return rgbtohex(int(rgb[0]), int(rgb[1]), int(rgb[2]))

#print(hsvtorgb(60, 0.5,0.5))
#print(hsvtohex(60, 0.5,0.5))
