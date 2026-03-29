from wand.color import Color
from wand.image import Image
from wand.drawing import Drawing
from wand.compat import nested
import math

# Generate hexagon armor effect fullscreen images

def DrawHexagon(draw, ctrX, ctrY, hSize):
    icX = 512 + ctrX
    icY = 256 + ctrY
    hh = hSize / 1.125
    a = 2 / math.sqrt(3) * hSize
    ah = a / 2
    points = [(icX+ah, icY+hh),(icX+a,icY),(icX+ah,icY-hh),(icX-ah,icY-hh),(icX-a,icY),(icX-ah,icY+hh)]
    draw.polygon(points)

def DrawImage(filename, hSize, fac, color, colorb):

    hFac = 1 / 1.125
    hh = hSize * hFac  # Scale height such that hexagons look equally sized on 16:9 screens
    a = 2 / math.sqrt(3) * hSize
    ah = a / 2

    # x-offset for uneven rows: 2*a-ah
    xOff_2 = 2 * a - ah
    # y-offset each row: hh
    yOff = hh

    with Drawing() as draw:
        with Image(width=1024, height=512, background=Color('white')) as img:

            draw.stroke_width = 2
            colF = Color("rgba(%d, %d, %d)" % (color[0], color[1], color[2]))
            colB = Color("rgba(%d, %d, %d)" % (colorb[0], colorb[1], colorb[2]))

            nRows2 = math.ceil(512 / (2*hh)) 
            nCols2 = math.ceil(1024 / (2*a))
            print(hh)
            print(a)
            print(nRows2)
            print(nCols2)

            for row in range(-nRows2, nRows2+1):
                
                xOffset = xOff_2 * (row % 2)
                yOffset = row * yOff

                for col in range(-nCols2, nCols2+1):
                    posX = xOffset + col * 2*xOff_2
                    posY = yOffset

                    dist = math.sqrt(math.pow(posX, 2.0) + math.pow(posY / hFac * 0.5, 2.0))
                    #dist = abs(posX)
                    # linear?
                    ff = math.pow(fac, 2)
                    alphaFac = 1 - math.exp(-1/ff * dist*dist)

                    colF.alpha = color[3] * alphaFac
                    colB.alpha = color[3] * alphaFac
                    draw.fill_color = colF
                    draw.stroke_color = colB

                    DrawHexagon(draw, posX, posY, hSize)
            

            img.alpha_channel = True
            draw(img)
            img.save(filename='PNG32:../textures/hud/' + filename + '.png')
        

# ==========================================
        
c0 = [255, 255, 0, 1.0]
cb0 = [255, 255, 0, 1.0]
DrawImage("tex_ArmorEffect1", 25, 800, c0, cb0)
DrawImage("tex_ArmorEffect2", 25, 400, c0, cb0)

        