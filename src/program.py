
from __future__ import division

import os
from os.path import abspath, dirname, join
import shutil
import sys
import time
import signal
from random import randint

from subprocess import call,Popen, PIPE, STDOUT

import pygame
from pygame.locals import *


print( "BOOT" )

def signal_term_handler( signal , frame ):
    global flagRun
    print "SIGTERM"
    flagRun = False
 
signal.signal( signal.SIGTERM , signal_term_handler )


runsFile = "runs.dat" 
runs = 1
if os.path.isfile( runsFile ):
    with open( runsFile , "r" ) as f:
        runs = int( f.read( ).replace( "\n" , "" ) ) + 1
        f.close( )

with open( runsFile , "w" ) as f:
    f.write( str( runs ) )
    f.close( )

print( "RUN " + str( runs ) )

################################################################
class projector :

    screen = None 
    screenrect = None 
    img = None    
    imgRect = None

    def __init__( self ):

        disp_no = os.getenv( "DISPLAY" )

        if disp_no:
            print( "X display = {0}" + format( disp_no ) )
        
        drivers = [ "fbcon" , "directfb" , "svgalib" ]

        found = False

        for driver in drivers:
            if not os.getenv( "SDL_VIDEODRIVER" ):
                os.putenv( "SDL_VIDEODRIVER" , driver )

            try:
                #print( driver )
                pygame.display.init( )
                pygame.font.init()

            except pygame.error:
                print( "Driver: {0} failed." + format( driver ) )
                continue

            found = True
            break
    
        if not found:
            raise Exception( "No video driver found!" )
        
        size = ( pygame.display.Info( ).current_w , pygame.display.Info( ).current_h )

        self.screenrect = ( 0 , 0 , size[ 0 ] , size[ 1 ] ) 

        #print( "resolution : %d x %d" % (size[ 0 ] , size[ 1 ] ) )

        #self.screen = pygame.display.set_mode( size ,  pygame.HWSURFACE|pygame.DOUBLEBUF |pygame.FULLSCREEN)
        self.screen = pygame.display.set_mode( size )

        pygame.mouse.set_visible( False )

        self.img = pygame.image.load( "resources/latest.jpg" ).convert()

        resourceorigrect = self.img.get_rect( )

        wr = resourceorigrect.size[ 0 ]
        hr = resourceorigrect.size[ 1 ]
        ws = self.screenrect[2]
        hs = self.screenrect[3]

        ar = wr/hr
        #print(ar)

        h=hs
        w=h*ar
        x=(w-ws)/2
        y=0
        if w<ws:
            print("w>ws")
            w=ws
            h=w/ar
            x=0
            y=(h-hs)/2

        self.imgRect=(

            int(round(x)),
            int(round(y)),
            int(round(w)),
            int(round(h))
        )

        self.img = pygame.transform.scale(self.img, (self.imgRect[2],self.imgRect[3]))
        print(self.screenrect)
        print(self.imgRect)

    def __del__( self ):

        print( "QUIT" )
        pygame.quit( )


    def update( self ):

        black = ( 0 , 0 , 0 )
        col = ( 128 , 0 , 0 )
        self.screen.fill( col )



        self.screen.blit( self.img , ( 0 , 0 ) ,
            ( self.imgRect[ 0 ] , self.imgRect[1] , 
                self.screenrect[ 2 ] , self.screenrect[ 3 ]) )

        pygame.display.flip( )

################################################################

projector = projector( )

frame = 1

flagRun = True

clock = pygame.time.Clock()

print( "LOOP" )

while flagRun:

    projector.update( )
    time.sleep( 3 )

    #clock.tick( 30 )



