'''
Created on Jan 2, 2017

@author: Kyle
'''
import sfml as sf
import os
 

#constants
game_size = sf.Vector2(800,600)

#colors
black = sf.Color.BLACK
white = sf.Color.WHITE
red = sf.Color.RED
blue = sf.Color.BLUE
green = sf.Color.GREEN
yellow = sf.Color.YELLOW


#setup window
w,h = game_size
window = sf.RenderWindow(sf.VideoMode(w,h),"Start Window")

#load Font|check font filepath
os.chdir("C:\Users\Kyle\Documents\LiClipse Workspace")
font = sf.Font.from_file("arial.ttf")
if os.path.exists("arial.ttf") == True:
    print "found font file path"
else:
    print "could not find font file path"

def get_mouse_pos():
    mousepos = sf.window.Mouse.get_position()
    return mousepos

def mouse_clicked():
    if sf.Mouse.is_button_pressed(sf.Mouse.LEFT) == True:
        return True

def make_button(x,y,w,h,rotate,color,outlineThickness,outlinecolor,scale = (1,1)):
    new_btn = sf.RectangleShape()
    new_btn.position = (sf.Vector2(x,y))
    new_btn.size = (sf.Vector2(w,h))
    new_btn.fill_color = (color)
    new_btn.outline_thickness = outlineThickness
    new_btn.outline_color = outlinecolor
    new_btn.rotation = (rotate)
    new_btn.ratio = (scale)
    return new_btn

# the make_tile procedure creates a button at posx,posy
# the tag allows for properties to be assigned dinamicly
# for example you could create a function to assign every btn tagged dog a dog image

#assign default variables Use make_tile to create a quick button
tileWidth = 20
tileHeight = 20
tileRotation = 0
tileColor = black
def make_tile(posx,posy):
    new_tile = make_button(posx, posy, tileWidth, tileHeight, tileRotation, tileColor, 1, black, (1,1))
    return new_tile

def make_text(text_x,x,y,font,color,size):
    txt = sf.Text(text_x)
    txt.font = font
    txt.character_size = size
    txt.position = (x,y)
    txt.color = color
    return txt
#returns list(float-x,float-y,float-w,float-h)

        
#===============================================================================
# def SurfaceDimentions(surface):
#     
#     height = surface.height
#     width = surface.width
#     return width,height    
#===============================================================================
def bounded(object):
    
    x = object.position[0]
    y = object.position[1]
    
    d,c,w,h = object.local_bounds
    
    bounds = [x,y,x+w,y+h]
    return bounds
  
    
def isClicked(object):
    
    ob_li = bounded(object)
    Ox = ob_li[0]
    Oy = ob_li[1]
    Ow = ob_li[2]
    Oh = ob_li[3]
    
    mousepos = get_mouse_pos()
    Cx = mousepos[0]-249
    Cy = mousepos[1]-243
    
    # if click within object
    if Cx > Ox and Cy > Oy and Cx < Ow and Cx < Ow and Cy < Oh:
        return True
        print "True"
    else:
        return False

total = 0
ilist = []
    
def handle_disvar(value):
    val = ilist[-1]
    ilist[-1] = value
    ilist[-2] = val
    print ilist
    return ilist
    
    print ilist

def merge_list(list):# for i in nli[] do total + add// add = i * var   var+1 
    times = 1
    total = 0
    rlist = list
    
    rlist.reverse()
        
    for item in rlist:
        total = total + item * times
        times = times * 10
    rlist.reverse()
    return total
def clear_list(list):
    length = list.__len__()
   
    while length > 0:
        list.pop(length-1)
        length = length - 1
        
    
x= window.width - window.width
y= window.height - window.height
#create objects
newBTN = make_button(x+400, y+400, 300, 50, 0, red, 2, black)
newTXT = make_text("0", bounded(newBTN)[0], bounded(newBTN)[1], font, blue, 18)

playing_btn = make_button(0, 0, 50, 50, 0, green, 2, blue)
playing_txt = make_text(": Playing", 60, 10, font, green, 30)

paused_btn = make_button(0, 0, 50, 50, 0, red, 2, blue)
paused_txt = make_text(": Paused", 60, 10, font, red, 30)

#group UI elements with calcUI controlling multipule elements
calcUI_X=x+100
calcUI_Y=y+100

new_btn = make_button(720, 20, 50, 50,0,red,1,black)        
num1_btn = make_button(calcUI_X+2,    calcUI_Y+2,    40-2,40-2, 0, white,2,black)
num2_btn = make_button(calcUI_X+40+2, calcUI_Y+2,    40-2,40-2, 0, white,2,black)
num3_btn = make_button(calcUI_X+80+2, calcUI_Y+2,    40-2,40-2, 0, white,2,black)
num4_btn = make_button(calcUI_X+2,    calcUI_Y+40+2, 40-2,40-2, 0, white,2,black)
num5_btn = make_button(calcUI_X+40+2, calcUI_Y+40+2, 40-2,40-2, 0, white,2,black)
num6_btn = make_button(calcUI_X+80+2, calcUI_Y+40+2, 40-2,40-2, 0, white,2,black)
num7_btn = make_button(calcUI_X+2,    calcUI_Y+80+2, 40-2,40-2, 0, white,2,black)
num8_btn = make_button(calcUI_X+40+2, calcUI_Y+80+2, 40-2,40-2, 0, white,2,black)
num9_btn = make_button(calcUI_X+80+2, calcUI_Y+80+2, 40-2,40-2, 0, white,2,black)
num0_btn = make_button(calcUI_X+40+2, calcUI_Y+120+2,40-2,40-2, 0, white,2,black)
oprclear_btn = make_button(calcUI_X+2, calcUI_Y+120+2, 40-2, 40-2, 0, white, 2, black)
oprequl_btn = make_button(calcUI_X+80+2, calcUI_Y+120+2, 40-2, 40-2, 0, white, 2, black)
oprplus_btn = make_button(calcUI_X+80+2+40, calcUI_Y+120+2, 40-2, 40-2, 0, white, 2, black)
dis_btn = make_button(calcUI_X+2, calcUI_Y-20, 118, 20, 0, white, 2, black)
dis_total_btn = make_button(calcUI_X+150, calcUI_Y, 150, 50, 0, white, 2, black)

#group map elements
mapUI_X=x+400
mapUI_Y=y+400
mapUI_offset=5



#Designate Text
num_txt = make_text("", bounded(dis_btn)[0], bounded(dis_btn)[1], font, black, 18)
dis_total_txt = make_text("", bounded(dis_total_btn)[0], bounded(dis_total_btn)[1], font, black, 20)
num1_txt = make_text("1",bounded(num1_btn)[0]+10,bounded(num1_btn)[1],font,black,30)
num2_txt = make_text("2",bounded(num2_btn)[0]+10,bounded(num2_btn)[1],font,black,30)
num3_txt = make_text("3",bounded(num3_btn)[0]+10,bounded(num3_btn)[1],font,black,30)
num4_txt = make_text("4",bounded(num4_btn)[0]+10,bounded(num4_btn)[1],font,black,30)
num5_txt = make_text("5",bounded(num5_btn)[0]+10,bounded(num5_btn)[1],font,black,30)
num6_txt = make_text("6",bounded(num6_btn)[0]+10,bounded(num6_btn)[1],font,black,30)
num7_txt = make_text("7",bounded(num7_btn)[0]+10,bounded(num7_btn)[1],font,black,30)
num8_txt = make_text("8",bounded(num8_btn)[0]+10,bounded(num8_btn)[1],font,black,30)
num9_txt = make_text("9",bounded(num9_btn)[0]+10,bounded(num9_btn)[1],font,black,30)
num0_txt = make_text("0",bounded(num0_btn)[0]+10,bounded(num0_btn)[1],font,black,30)
oprclear_txt = make_text("C", bounded(oprclear_btn)[0]+10, bounded(oprclear_btn)[1], font, red, 30)
oprequl_txt = make_text("=", bounded(oprequl_btn)[0]+10, bounded(oprequl_btn)[1], font, blue, 30)
oprplus_txt = make_text("+", bounded(oprplus_btn)[0]+10, bounded(oprplus_btn)[1], font, green, 30)



def make_map(row):
    rowtemp = 0
    maplist = []
    while rowtemp < row:
        maplist.append(["#","#","#","#","#"])  
        rowtemp = rowtemp+1
    return maplist
        
map = make_map(5)

def del_from_map(x,y):
    map[y-1].pop(x-1)
    map[y-1].insert(x-1,"#")
    #for i in map:
        #print i
    #print "--------------"

def add_to_map(x,y,elem):
    map[y-1].pop(x-1)
    map[y-1].insert(x-1,elem)                 
    #for i in map:
    #    print i
    #print "--------------"

# designate tile
water_tile = make_tile(300, 50)
water_tile_tag = "black"
test_tile = make_tile(300, 10)
test_tile_tag = "red"

def prossess_tile(tile_tag,tile):
    if tile_tag == "red":
        tile.fill_color = (red)
        window.draw(tile)
    if tile_tag == "blue":
        tile.fill_color = (blue)
        window.draw(tile)
    if tile_tag == "black":
        tile.fill_color = (black)
        
def setup_window_btn():  
    #draw() buttons
    window.draw(new_btn)
    window.draw(num1_btn)
    window.draw(num2_btn) 
    window.draw(num3_btn)
    window.draw(num4_btn)
    window.draw(num5_btn)
    window.draw(num6_btn)
    window.draw(num7_btn)
    window.draw(num8_btn)
    window.draw(num9_btn)
    window.draw(num0_btn)
    window.draw(oprclear_btn)
    window.draw(oprequl_btn)
    window.draw(oprplus_btn)
    window.draw(dis_btn)
    window.draw(dis_total_btn)

def setup_window_txt():
    #draw() numbers
    window.draw(num1_txt)
    window.draw(num2_txt)
    window.draw(num3_txt)
    window.draw(num4_txt)
    window.draw(num5_txt)
    window.draw(num6_txt)
    window.draw(num7_txt)
    window.draw(num8_txt)
    window.draw(num9_txt)
    window.draw(num0_txt)
    window.draw(oprclear_txt)
    window.draw(oprequl_txt)
    window.draw(oprplus_txt)
    window.draw(num_txt)
    window.draw(dis_total_txt)

curentposx = 1
curentposy = 1  

def up(playerX,playerY):
    del_from_map(playerX,playerY)
    add_to_map(playerX, playerY+1, "P")
    

clock = sf.Clock()
is_playing = False

t1 = sf.system.milliseconds(250)
oprPhase = 0
oprsave_var = 0
while window.is_open:
    
    for event in window.events:
        if type(event) is sf.CloseEvent:
            window.close()
            print "window closed"
        if type(event) is sf.KeyEvent and event.pressed and event.code is sf.Keyboard.SPACE:
            if not is_playing:
                is_playing = True
                clock.restart()
            else:
                is_playing = False
                clock.restart()
    #update positions/variables
        if is_playing:
            
            num_txt.string = str(merge_list(ilist))
                        
                    
                            
    window.clear(white)
    
    #action when playing
    if is_playing:
        setup_window_btn()
        setup_window_txt()
        window.draw(playing_btn)
        window.draw(playing_txt)
                
        window.draw(test_tile)
        prossess_tile(test_tile_tag, test_tile)
        
        window.draw(water_tile)
        prossess_tile(water_tile_tag, water_tile)
        
        #if mouse.clicked then check mouse pos, if 
        if sf.Mouse.is_button_pressed(sf.Mouse.LEFT):
            
            if isClicked(num1_btn) == True:
                ilist.append(1)     
            if isClicked(num2_btn) == True:
                ilist.append(2)
            if isClicked(num3_btn) == True:
                ilist.append(3)    
            if isClicked(num4_btn) == True:
                ilist.append(4)        
            if isClicked(num5_btn) == True:
                ilist.append(5)         
            if isClicked(num6_btn) == True:
                ilist.append(6)        
            if isClicked(num7_btn) == True:
                ilist.append(7)     
            if isClicked(num8_btn) == True:
                ilist.append(8)       
            if isClicked(num9_btn) == True:
                ilist.append(9)        
            if isClicked(num0_btn) == True:
                ilist.append(0)
            if isClicked(oprclear_btn)==True:
                clear_list(ilist)
            if isClicked(oprplus_btn)==True:
                oprPhase = 1
                oprType = "plus"
                oprsave_var = merge_list(ilist)
                clear_list(ilist)
                print "saved: " + str(oprsave_var)
            if isClicked(oprequl_btn)==True:
                if oprType == "plus":
                    result = oprsave_var + merge_list(ilist)
                    dis_total_txt.string = str(result)
                    print "result: " + str(result)
                    clear_list(ilist)
                    oprsave_var = 0
                    oprPhase = 0
            if isClicked(test_tile)==True:
                for i in map:
                    print i
                water_tile_tag = "black"
            if isClicked(water_tile)==True:
                #add_to_map(1,1,"$")
                up(curentposx,curentposy)
                water_tile_tag = "white"
                
            sf.system.sleep(t1)
                
    #action when paused
    else:
        window.draw(paused_btn)
        window.draw(paused_txt)
    window.display()
            