# Cyber Minecraft Pi Project Part 1
# Documentation https://github.com/raspberrypilearning/getting-started-with-minecraft-pi/blob/master/worksheet.md
# 0. Remove ~/Desktop/mcpi-app and ~/Desktop/mcpi-python and reclone both.  Do not save files in these folders.
# 1. Create folder on /home/pi/Desktop for your python code.  Use you name, intials, or StevePi name.
# 2. Run this file: python3 cyberAssignment.py or set geany to run python3
# 3. Use the following format to create a Minecraft object that looks like something we see in the world or universe.
# * Code must be posted somewhere on your github site.
# * You can not use any pre-existing project code in the "project" directory. 
# * ( https://github.com/tritechsc/mcpi-python/tree/master/projects)
# * Communicate what you are making prior to starting with Mr. Coleman
# 4. Use 5 total functions. One of the functions may clear the area with air.
# 5. Use 1 or more mc.setBlock(x,y, z, block.IRON_BLOCK.id) commands. block.IRON_BLOCK.id can be replaced with a number.
# * wool = 35; n = 5 (This is an example of how to use wool.)
# 6. Use 1 or more mc.setBlocks(x,y, z,h,k,l, wool,n) commands.
# 7. Use 1 for loop, 1 while loop and 1 if condition.
# * * * * * * * 
# * * install ascii  -> sudo apt install ascii  -> then run ascii
# 8.  Modify mcpi-app to mcpi-1234567 where 1234567 is your StevePi name. 
# * Clone https://github.com/tritechsc/mcpi-app.git to /home/pi/Desktop.
# *. Copy mcpi-app to mcpi-1234567 where username is 1234567. User name must be 7 characters.
# * cp -fR mcpi-app mcpi-1234567
# 9. Modify mincraft-pi to display a unique 7 charater name as follows:
'''copy minecraft-pi to a location to edit cp -fR mcpi-app mcpi-1234567
hexdump -ve '1/1 "%.2X"' minecraft-pi > mcpi.txt
sed -i "s/53746576655069/31323334353637/g" mcpi.txt
xxd -r -p mcpi.txt > minecraft-pi.bin
rm minecraft-pi
cp minecraft-pi.bin minecraft-pi
chown pi:pi minecraft-pi
chmod a+x minecraft-pi
'''
# 10. Change the skin of the char.png image in your ~/Desktop/mcpi-1234567 directory using GIMP.
# * Export the file as a char.png
# * Example char-turtle-DON.xcf will be exported as char.png. Upload your gimp file to github.
# * Change your skin by moving char.png to /home/pi/Desktop/mcpi-1234567/data/images/mob/char.png 
# * Look in the ~/Desktop/mcpi-1234567/CODE+IMAGES folder. 
# 11. Move p3-mcpi-start.sh or p4-mcpi-start.sh to your desktop.
# 12. Modify p3-mcpi-start.sh or p4-mcpi-start.sh so it works with your unique mcpi-1234567 directory
# 13. Add bash_aliases to ~/.bash_aliases as the pi user.
# 14. Modifiy ~/.bashrc to enable ll for ls -l as a root users.
from mcpi.minecraft import Minecraft
from mcpi import block
from   time import sleep

def init():
 #ipString = "192.168.1.73"
 ipString = "127.0.0.1"
 #mc = Minecraft.create("127.0.0.1", 4711)
 mc = Minecraft.create(ipString, 4711)
 mc.setting("world_immutable",True)
 #x, y, z = mc.player.getPos()  
 return mc

def one(mc,x,y,z):
 print("FUNCTION ONE")
 mc.setBlock(x,y, z, block.IRON_BLOCK.id)

def two(mc,x,y,z):
 print("FUNCTION TWO")
 mc.setBlocks(x-10,y,z+1,x+10,y+10,z+1+10,35,7)
def three(mc,x,y,z):
 print("FUNCTION THREE")
 mc.setBlocks(x-10,y,z+1,x+10,y+10,z+1+10,35,3)
 mc.setBlocks(x-10,y,z+1,x+10,y+10,z+1+10,35,9)
 
def main():
 mc = init()
 x,y,z = mc.player.getPos()
 mc.player.setPos(x,y,z)
 one(mc,x,y,z)
 two(mc,x,y+5,z)
 three(mc,x,y+10,z)
 mc.player.setPos(x,y+10,z-2)

if __name__ == "__main__":
 main()

