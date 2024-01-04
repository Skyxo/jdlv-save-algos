import jdlv
import data
import time
add_library('controlP5')

tab_width, tab_height, width, height = 800, 800, 1100, 800

def setup():
    size(width, height)
    cp5 = ControlP5(this)
    cp5.addButton('Start/Stop')\
       .setPosition(tab_width, 50)\
       .setSize(80,40)\
       .onClick(Pause)
       
    cp5.addButton('Reset')\
       .setPosition(tab_width, 90)\
       .setSize(80,40)\
       .onClick(Reset)
       
    cp5.addButton('+')\
       .setPosition(tab_width+80, 50)\
       .setSize(80,40)\
       .onClick(Plus)
       
    cp5.addButton('-')\
       .setPosition(tab_width+80, 90)\
       .setSize(80,40)\
       .onClick(Moins)
       
    cp5.addButton('>>>')\
       .setPosition(tab_width+160, 50)\
       .setSize(80,40)\
       .onClick(Next)
       
    cp5.addButton('<<<')\
       .setPosition(tab_width+160, 90)\
       .setSize(80,40)\
       .onClick(Previous)
       
    cp5.addButton('Ruche')\
       .setPosition(tab_width, 170)\
       .setSize(80,40)\
       .setValue(0)\
       .onClick(Placing)
       
    cp5.addButton('10')\
       .setPosition(tab_width+80, 170)\
       .setSize(80,40)\
       .setValue(1)\
       .onClick(Placing)
       
    cp5.addButton('Glider')\
       .setPosition(tab_width+160, 170)\
       .setSize(80,40)\
       .setValue(2)\
       .onClick(Placing)
       
    cp5.addButton('Glider C')\
       .setPosition(tab_width, 210)\
       .setSize(80,40)\
       .setValue(3)\
       .onClick(Placing)
       
    cp5.addButton('+90')\
       .setPosition(tab_width, 290)\
       .setSize(80,40)\
       .setValue(1)\
       .onClick(Rotate)
    
    cp5.addButton('-90')\
       .setPosition(tab_width+80, 290)\
       .setSize(80,40)\
       .setValue(-1)\
       .onClick(Rotate)
       
    cp5.addButton('Cancel')\
       .setPosition(tab_width, 330)\
       .setSize(80,40)\
       .onClick(CancelPlacing)
    
n = 50
tableau = jdlv.createTableau(n)
tab_data = []
periode = 0
pause = True
placing = [[0, 0]]
 
def draw():
    global tableau, n, pause, placing, tab_data, periode
    
    background(0)
    
    fill(255)
    text("Cellules en vie : {}".format(jdlv.compteur(tableau, n)), tab_width, 20)
    text("Periode : {}".format(periode), tab_width, 40)

    for i in range(len(tableau)):
        for o in range(len(tableau[i])):

            if tableau[i][o]:                
                rect(i*tab_width/n, o*tab_height/n, tab_width/n, tab_height/n)
            
    fill(105)
    for i in range(len(tableau)):
        for o in range(len(tableau[i])):
           if mouseX > i*tab_width/len(tableau)\
               and mouseX < i*tab_width/len(tableau)+tab_width/len(tableau)\
               and mouseY > o*tab_height/len(tableau)\
               and mouseY < o*tab_height/len(tableau)+tab_height/len(tableau):
             
                for coord in placing:
                    rect((coord[0]+i)*tab_width/n, (coord[1]+o)*tab_height/n, tab_width/n, tab_height/n)
                                  
    if not pause or keyPressed and keyCode == RIGHT:
        Next(keyPressed)
        
    if pause and keyPressed and keyCode == LEFT and len(tab_data) > 0:
        Previous(keyPressed)
        
def mouseDragged():
    global tableau, tab_data, periode
 
    for i in range(len(tableau)):
        if mouseX > i*tab_width/len(tableau) and mouseX < i*tab_width/len(tableau)+tab_width/len(tableau):
            for o in range(len(tableau[i])):
                if mouseY > o*tab_height/len(tableau) and mouseY < o*tab_height/len(tableau)+tab_height/len(tableau):
                
                    for coord in placing:
                        try:
                            if mouseButton == LEFT and not tableau[coord[0]+i][coord[1]+o]:
                                tableau[coord[0]+i][coord[1]+o] = 1
                            elif mouseButton == RIGHT and tableau[coord[0]+i][coord[1]+o]:
                                tableau[coord[0]+i][coord[1]+o] = 0
                        except:
                            pass
    
    tab_data = tab_data[0:periode]
    
def mouseClicked():
    mouseDragged()
    
def afficheConsole(tab):
    
    for i in range(len(tab)):
        print()
        for o in range(len(tab[i])):
            print(tab[i][o])
            
    
def Pause(event):
    global pause
    pause = False if pause else True
    
def Reset(event):
    global tableau, n, periode, tab_data, pause
    tableau = jdlv.createTableau(n)
    tab_data = [tableau]
    pause = True
    periode = 0
    
def Plus(event):
    global tableau, n
    n-=10
    tableau = jdlv.createTableau(n)
    
def Moins(event):
    global tableau, n
    n+=10
    tableau = jdlv.createTableau(n)
    
def Next(event):
    global tableau, tab_data, periode        
    
    periode+=1
    tab_data.append(tableau)
    tableau = jdlv.actualize(tableau)
    
def Previous(event):
    global tableau, tab_data, periode
    
    if periode-1 >= 0:
        periode-=1
        tableau = tab_data[periode]
    
def Placing(event):
    global placing
    value = int(event.getController().getValue())
    placing = data.placing[value]
    
def CancelPlacing(event):
    global placing
    placing = [[0, 0]]
    
def Rotate(event):
    global placing
    
    value = event.getController().getValue()
    
    r90 = [[0, -1*value],
           [1*value, 0]]
    
    for i in range(len(placing)):
        placing[i][0], placing[i][1] = jdlv.produit_matriciel(r90, [[placing[i][0]], [placing[i][1]]])
