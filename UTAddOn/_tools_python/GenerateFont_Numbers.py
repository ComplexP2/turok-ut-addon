from wand.color import Color
from wand.image import Image
from wand.drawing import Drawing
from wand.compat import nested
import math

# Generate numbers 0 to 9 as images for the hud

def DrawImage(filename, text, size, color, colorb):
    with Drawing() as draw:
        with Image(width=64, height=64, background=Color('white')) as img:
            draw.font_family = 'Eurostile'
            draw.font_size = size
            draw.font_weight = 700 # bold -> https://developer.mozilla.org/en-US/docs/Web/CSS/font-weight#common_weight_name_mapping
            draw.push()
            draw.fill_color = Color("rgb(%d, %d, %d)" % (color[0], color[1], color[2]))
            draw.stroke_color = Color("rgb(%d, %d, %d)" % (colorb[0], colorb[1], colorb[2]))
            draw.text_alignment = 'center'
            draw.text(int(img.width/2),int(img.height/2+24), text)
            draw.pop()
            img.alpha_channel = True
            draw(img)
            img.save(filename='PNG32:../textures/hud/num_' + filename + '.png')
        

# ==========================================
        
size = 74
c0 = [225, 225, 225]
cb0 = [200, 200, 200]
for i in range(10):
    DrawImage(str(i), str(i), size, c0, cb0)


        
