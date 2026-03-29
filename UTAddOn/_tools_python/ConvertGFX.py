from wand.image import Image
from wand.color import Color

# Use the original weapon images of the game (extracted game zip file: game.kpf -> game.zip (copy&rename) -> game_zip (extracted dir)) 
# and generate weapon images for the hud (including grayed-out versions)

def resizeImg(sourceFile, destFile, width, height):
    with Image(width=width, height=height) as outerImg:
        with Image(filename=sourceFile) as img:
            if(img.width > 128 | img.height > 64):
                print("Image too big! Re-scaling not implemented!")
                raise
            img.transform(resize="%dx%d>" % (width, height))
            img.flip()
            outerImg.format = img.format.lower()
            newLeft = int((width - img.width) / 2)
            newTop = int((height - img.height) / 2)
            outerImg.composite(img, left=newLeft, top=newTop)
            outerImg.save(filename=destFile + ".png")

            outerImg.transform_colorspace('gray')
            outerImg.gamma(0.1)
            outerImg.blur(radius=1, sigma=1)
            outerImg.save(filename=destFile + "_bw.png")

fnames = ["h_w_alien", "h_w_autoshot", "h_w_bow", "h_w_charge", "h_w_fusion",\
        "h_w_glauncher", "h_w_knife", "h_w_minigun", "h_w_mlauncher", "h_w_pistol",\
        "h_w_pulse", "h_w_rifle", "h_w_scepter", "h_w_shotgun"]

srcPathRel = "../../../../game_zip/gfx/hud/"
destPathRel = "../textures/hud/"
N = len(fnames)
for i in range(N):
    resizeImg(srcPathRel + fnames[i] + ".tga", "PNG32:" + destPathRel + fnames[i], 128, 64)
