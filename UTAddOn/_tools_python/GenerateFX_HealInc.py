from wand.color import Color
from wand.image import Image
from wand.drawing import Drawing
from wand.compat import nested
import math

# Generate achievement fx sprites and corresponding kfx files

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
        f.write('        translation = { 0.000000 0.000000 0.000000 }\n')
        f.write('        scale = 8.5\n')
        f.write('        scaleDest = 0.01\n')
        f.write('        rotationOffsetRandom = 0\n')
        f.write('        shader = "progs/worldfx"\n')
        f.write('        sprite = "UTAddOn/sprites/fx_' + filename + '"\n')
        f.write('        instances = 1\n')
        f.write('        lifeTime = 40\n')
        f.write('        animSpeed = 30\n')
        f.write('        whiteColor = { 0.700000 0.700000 0.700000 }\n')
        f.write('        blackColor = { 0.200000 0.200000 0.200000 }\n')
        f.write('        hueRandom = 0.000000\n')
        f.write('        saturationRandom = 0.000000\n')
        f.write('        brightnessRandom = 0.000000\n')
        f.write('        fadeOutTime = 30\n')
        f.write('        drawType = 0\n')
        f.write('        animType = 0\n')
        f.write('        priority = 99\n')
        f.write('    }\n')
        f.write('\n')   
        f.write(' }\n')

# ==========================================
        
# Achievement FX - Health
fnames = []
texts = []
sizes = []
for i in range(5):
    fnames.append('MaxHealHealthInc' + str(i+1))
    texts.append('Max Health +' + str(i+1))
    sizes.append(96)
c0 = [0, 255, 125]
cb0 = [0, 80, 40]
N = len(fnames)
step = int(math.floor(255 / N))
for i in range(N):
    #c = [255, 255 - i*step, 0]
    #cb = [i*step, i*step, 0]
    c = c0
    cb = cb0
    DrawImage(fnames[i], texts[i], sizes[i] * 0.6, c, cb)

# Achievement FX - Armor
fnames = ['MaxHealArmorInc1', 'MaxHealArmorInc5']
texts = ['Max Armor +1', 'Max Armor +5']
sizes = [96, 96]
c0 = [0, 255, 255]
cb0 = [0, 40, 80]
N = len(fnames)
step = int(math.floor(255 / N))
for i in range(N):
    #c = [255, 255 - i*step, 0]
    #cb = [i*step, i*step, 0]
    c = c0
    cb = cb0
    DrawImage(fnames[i], texts[i], sizes[i] * 0.6, c, cb)

# Achievement FX - Ammo
fnames = []
texts = []
sizes = []
for i in range(6):
    fnames.append('AmmoGift' + str(i+1))
    texts.append('Ammo +' + str((i+1)*5) + '%')
    sizes.append(96)
c0 = [255, 0, 255]
cb0 = [180, 0, 140]
N = len(fnames)
step = int(math.floor(255 / N))
for i in range(N):
    #c = [255, 255 - i*step, 0]
    #cb = [i*step, i*step, 0]
    c = c0
    cb = cb0
    DrawImage(fnames[i], texts[i], sizes[i] * 0.6, c, cb)


# Achievement FX - Full Armor (50)
DrawImage('ArmorGift50', 'Full Armor', 96 * 0.6, [255, 255, 0], [200, 150, 0])

# Achievement FX - Full Ammo
DrawImage('AmmoGift100', 'Full Ammo', 96 * 0.6, [255, 0, 255], [180, 0, 140])