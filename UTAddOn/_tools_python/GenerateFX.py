from wand.color import Color
from wand.image import Image
from wand.drawing import Drawing
from wand.compat import nested
import math

# Generate the sprite images for the kill streaks and also the corresponding sprite definition files and effect kfx files.

def DrawImage(filename, text, size, color, colorb):
    with Drawing() as draw:
        with Image(width=512, height=128, background=Color('white')) as img:
            #draw.font_family = 'Gismonda'
            #draw.font_family = 'Unreal Tournament'
            draw.font_family = 'Verdana'
            draw.font_size = size
            draw.font_weight = 700 # bold -> https://developer.mozilla.org/en-US/docs/Web/CSS/font-weight#common_weight_name_mapping
            draw.push()
            draw.fill_color = Color("rgb(%d, %d, %d)" % (color[0], color[1], color[2]))
            draw.stroke_color = Color("rgb(%d, %d, %d)" % (colorb[0], colorb[1], colorb[2]))
            draw.text_alignment = 'center'
            draw.text(int(img.width/2),int(img.height/2+32), text)
            draw.pop()
            img.alpha_channel = True
            draw(img)
            img.save(filename='PNG32:../sprites/fx_' + filename + '.png')
            
    with open('../sprites/fx_' + filename + '_sprite.txt', 'w') as f:
        f.write('texture "UTAddOn/sprites/fx_' + filename + '.png"\n')
        f.write('\n')
        f.write('sprite 0 0 0 512 128\n')
        
    with open('../fx/' + filename + '.kfx', 'w') as f:
        f.write('fx[1] =\n')
        f.write('{\n')
        f.write('    {\n')
        f.write('        bTextureWrapMirrorWidth = 0\n')
        f.write('        bTextureWrapMirrorHeight = 0\n')
        f.write('        bDepthBuffer = 0\n')
        f.write('        bDrawOnBottom = 1\n')
        f.write('        bScaleLerp = 1\n')
        f.write('        bNoHitSource = 1\n')
        f.write('        translationRandomGlobal = 0.000000\n')
        f.write('        translation = { 0.000000 1.000000 0.000000 }\n')
        f.write('        scale = 10.0\n')
        f.write('        scaleDest = 0.1\n')
        f.write('        rotationOffsetRandom = 0\n')
        f.write('        shader = "progs/worldcolorfx"\n')
        f.write('        sprite = "UTAddOn/sprites/fx_' + filename + '"\n')
        f.write('        instances = 1\n')
        f.write('        lifeTime = 20\n')
        f.write('        animSpeed = 60\n')
        f.write('        whiteColor = { 0.700000 0.700000 0.700000 }\n')
        f.write('        blackColor = { 0.200000 0.200000 0.200000 }\n')
        f.write('        hueRandom = 0.000000\n')
        f.write('        saturationRandom = 0.000000\n')
        f.write('        brightnessRandom = 0.000000\n')
        f.write('        fadeOutTime = 15\n')
        f.write('        drawType = 0\n')
        f.write('        animType = 0\n')
        f.write('        priority = 99\n')
        f.write('    }\n')
        f.write('\n')   
        f.write(' }\n')

# ==========================================
        
fnames = ['KS_Kill','KS_DoubleKill','KS_MultiKill','KS_MegaKill','KS_UltraKill','KS_MonsterKill','KS_LudicrousKill','KS_HolyShit','KS_Ownage',]
texts = ['Kill','Double Kill','Multi Kill','Mega Kill','Ultra Kill','Monster Kill','Ludicrous Kill','Holy Shit','Ownage'];
sizes = [96,96,96,96,96,96,80,96,96]
c0 = [255, 255, 0]
cb0 = [200, 200, 200]
N = len(fnames)
step = int(math.floor(255 / N))
for i in range(N):
    c = [255, 255 - i*step, 0]
    cb = [i*step, i*step, 0]
    DrawImage(fnames[i], texts[i], sizes[i] * 0.7, c, cb)


        