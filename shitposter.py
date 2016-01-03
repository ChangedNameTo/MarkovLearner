#!/usr/bin/python

import json, re, sys, urllib2

from HTMLParser import HTMLParser
from pymarkovchain import MarkovChain

def sanitize( com ):
    return re.sub( r"\<.+\>", "", com )

def train_on_thread( board, thread_id ):
    global mc
    
    response = urllib2.urlopen( 'http://a.4cdn.org/' + board + '/thread/' + str( thread_id ) + '.json' )
    data = json.loads( response.read() )
    
    for post in data['posts']:
        if 'com' in post:
            mc.generateDatabase( sanitize( post['com'] ) )

def analyze_board( board ):
    response = urllib2.urlopen( 'http://a.4cdn.org/' + board + '/threads.json' )
    data = json.loads( response.read() )
    thread_ids = list()
    
    # Doing all 10 pages takes a long time
    #for page in data:
        #for thread in page['threads']:
    
    for thread in data[0]['threads']:
        train_on_thread( board, thread['no'] )

def shitpost_loop( board ):
    read = ''
    
    while read != "exit":
        print( 'Enter a command. Enter ? for a list of valid commands.' )
        read = raw_input()
        
        if read.startswith( 'train' ):
            mc.generateDatabase( read )
        elif read == "?":
            print( "\nValid input is:\nexit - Exit the program.\nprint - Generate a shitpost.\ntrain - Learn how to shitpost (takes a while)." )
        elif read == "train":
            analyze_board( board )
        elif read == "exit":
            pass
        elif read == "print":
            print( mc.generateString() )
        else:
            print( "Invalid input." )

def main( args ):
    global mc
    
    mc = MarkovChain( "./shitpost_data" )
    
    print( "Enter the name of the board you would like to learn how to shitpost from." )
    board = raw_input()
    analyze_board( board )
    shitpost_loop( board )

if __name__ == "__main__":
    main( sys.argv[1:] )
