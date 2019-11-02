# -*- coding: utf-8 -*-

# questionnaire.py
# Visual Cognitive Neuroscience Lab
# Brock University
#
# Created by Thomas Nelson <tn90ca@gmail.com>
#
# This script was developed for use by the Visual Cognitive Neuroscience Lab
# at Brock University.
# Modified by Brent Pitchford <bp11lj@brocku.ca> Oct. 28/2016 for Attention Lab

"""This script...

"""



from __future__ import absolute_import, division
from psychopy import locale_setup, gui, visual, core, data, event, logging, sound, monitors

from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding
import csv

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__)).decode(sys.getfilesystemencoding())
os.chdir(_thisDir)


# Store info about the experiment session
expName = 'STAI'  # from the Builder filename that created this script
expInfo = {'participant':'', 'session':'01'}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
endExpNow = False  # flag for 'escape' or other condition => quit the exp
# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename= _thisDir + os.sep + u'STAI' + os.sep + '%s' % (expInfo['participant'] + ".csv")




def run_time(subj_num):
    ####################################################################################################
    #                                         Program Constants                                        #
    ####################################################################################################
    # Set psychopy required names for things
    EXP_NAME     = "STAI"  # The name of the experiment for save files
    MONITOR_NAME = "testmonitor"     # The name of the monitor set in PsychoPy.


    # Set required colours for objects, text, etc
    BG_COLOUR     = [-1,-1,-1]  # Set a background colour, currently black
    TEXT_COLOUR   = [1, 1, 1]     # The text colour, currently white
    TEXT_COLOUR2  = [0, 0, 53]

    # Set required sizes for objects, text, etc
    TEXT_HEIGHT   = 1.2       # The height in visual degrees of instruction text
    TEXT_WRAP     = 35      # The character limit of each line of text before word wrap
    
    HEADER_LIST = ['Date','Participant', 'Questionnaire' , 'Response' , 'Score', 'RT']

    INS_MSG =    ("\nA number of statements which people have used to describe themselves are given."+
    "\nRead each statement and then choose the appropriate number of the statement to indicate how you generally feel.")

    questions_1 = ['I feel pleasant',
    'I feel nervous and restless ',
    'I feel satisfied with myself',
    'I wish I could be as happy as others seem to be',
    'I feel like a failure ',
    'I feel rested ',
    'I am calm, cool and collected ',
    'I feel that difficulties are piling up so that I cannot overcome them ',
    'I worry too much over something that really doesnt matter ',
    'I am happy ',
    'I have disturbing thoughts ',
    'I lack self-confidence ',
    'I feel secure ',
    'I make decisions easily ',
    'I feel inadequate ',
    'I am content ',
    'Some unimportant thought runs through my mind and bothers me ',
    'I take disappointments so keenly that I cant put them out of my mind ',
    'I am a steady person',
    'I get in a state of tension or turmoil as I think over my recent concerns and interests']
				   
                   
                   
    def set_psychopy():
        """
        
        """
        
        # Build the monitor with correct sizing for psychopy to calculate visual degrees
        mon = monitors.Monitor('testmonitor')
        mon.setDistance(57)  # Measure first to ensure this is correct
        mon.setWidth(41)     # Measure first to ensure this is correct
        3
        # Build the window for psychopy to run the experiment in
        win = visual.Window(fullscr=True, screen=0, allowGUI=False, allowStencil=False, monitor=mon, color=BG_COLOUR,
                            colorSpace='rgb', units='deg')
        
        # Set up an event clock for timing in trials
        event_clock = core.Clock()
        
        # Set up an event catcher to collect keyboard and mouse responses
        mouse    = event.Mouse(win=win)
        key_resp = event.BuilderKeyResponse()

        return win, mon, event_clock, key_resp, mouse
    # End def set_psychopy

    # Setup all required PsychoPy variables
    win, mon, event_clock, key_resp, mouse = set_psychopy()

    # Build all experiment stimuli
    ins  = visual.TextStim(win=win, name='msg', text=INS_MSG, height=1.0, wrapWidth=TEXT_WRAP,
                           color=TEXT_COLOUR, colorSpace='rgb', pos=[0,0])
    ans1 = visual.TextStim(win=win, name='msg', text='1 = Almost Never', height=0.8, wrapWidth=TEXT_WRAP,
                          color=TEXT_COLOUR, colorSpace='rgb', pos=[-9,-4])
    ans2 = visual.TextStim(win=win, name='msg', text='2 = Sometimes', height=0.8, wrapWidth=TEXT_WRAP,
                           color=TEXT_COLOUR, colorSpace='rgb', pos=[-2,-4])
    ans3 = visual.TextStim(win=win, name='msg', text='3 = Often ', height=0.8, wrapWidth=TEXT_WRAP,
                           color=TEXT_COLOUR, colorSpace='rgb', pos=[4,-4])
    ans4 = visual.TextStim(win=win, name='msg', text='4 = Almost Always', height=0.8, wrapWidth=TEXT_WRAP,
                           color=TEXT_COLOUR, colorSpace='rgb', pos=[10,-4])
    ans5 = visual.TextStim(win=win, name='msg', text='Skip this question', height=1.0, wrapWidth=TEXT_WRAP,
                           color=TEXT_COLOUR, colorSpace='rgb', pos=[-10,-10])
						   
    msg = visual.TextStim(win=win, name='msg', text="", height=1.0, wrapWidth=TEXT_WRAP,
                           color=TEXT_COLOUR, colorSpace='rgb', pos=[0,2])
    cls = visual.TextStim(win=win, name='msg', text="Press the enter key to submit your answer", height=1.0, wrapWidth=TEXT_WRAP,
                           color=TEXT_COLOUR, colorSpace='rgb', pos=[10,-10])

    # Present instructions for the experiment
    ins.setAutoDraw(True)
    win.flip()
    event.waitKeys()
    ins.setAutoDraw(False)
    win.flip()

    answers_1 = []
    for q in questions_1:
        msg.setText(q)
        ans1.setColor([1,1,1])
        ans2.setColor([1,1,1])
        ans3.setColor([1,1,1])
        ans4.setColor([1,1,1])
        ans5.setColor([1,1,1])
        msg.setAutoDraw(True)
        ans1.setAutoDraw(True)
        ans2.setAutoDraw(True)
        ans3.setAutoDraw(True)
        ans4.setAutoDraw(True)
        ans5.setAutoDraw(True)
        win.flip()
        event.clearEvents()
        response = None
        event_clock.reset()
        while True:
            win.flip()
            if event.getKeys(["1"]):
                response = 1
                cls.setAutoDraw(True)
                ans1.setColor([1,-1,-1])
                ans2.setColor([1,1,1])
                ans3.setColor([1,1,1])
                ans4.setColor([1,1,1])
                ans5.setColor([1,1,1])
            elif event.getKeys(["2"]):
                response = 2
                cls.setAutoDraw(True)
                ans1.setColor([1,1,1])
                ans2.setColor([1,-1,-1])
                ans3.setColor([1,1,1])
                ans4.setColor([1,1,1])
                ans5.setColor([1,1,1])
            elif event.getKeys(["3"]):
                response = 3
                cls.setAutoDraw(True)
                ans1.setColor([1,1,1])
                ans2.setColor([1,1,1])
                ans3.setColor([1,-1,-1])
                ans4.setColor([1,1,1])
                ans5.setColor([1,1,1])
            elif event.getKeys(["4"]):
                response = 4
                cls.setAutoDraw(True)
                ans1.setColor([1,1,1])
                ans2.setColor([1,1,1])
                ans3.setColor([1,1,1])
                ans4.setColor([1,-1,-1])
                ans5.setColor([1,1,1])
            elif event.getKeys(["space"]):
                response = 999
                cls.setAutoDraw(True)
                ans1.setColor([1,1,1])
                ans2.setColor([1,1,1])
                ans3.setColor([1,1,1])
                ans4.setColor([1,1,1])
                ans5.setColor([1,-1,-1])
            elif event.getKeys(['enter']) or event.getKeys(['return']):
                if response is not None:
                    cls.setAutoDraw(False)
                    rt = event_clock.getTime()
                    answers_1.append(response)
                    break
            elif event.getKeys(["escape"]):
                core.quit(0) # If escape key is hit then safely close program
    msg.setAutoDraw(False)
    ans1.setAutoDraw(False)
    ans2.setAutoDraw(False)
    ans3.setAutoDraw(False)
    ans4.setAutoDraw(False)
    cls.setAutoDraw(False)

#Use this section if you'd like to score responses
#    rev_q = [2, 9, 13, 18]
#    rev   = [5, 4, 3, 2, 1]

#    scored_answers_1 = []
#    for a in xrange(len(answers_1)):
#        if a in rev_q:
#            scored_answers_1.append(rev[answers_1[a]-1])
#        else:
#            scored_answers_1.append(answers_1[a])
   

    # Write output headers to subject save file
    with open(filename, 'w') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(HEADER_LIST)
    
    if not os.path.exists(filename):
        os.makedirs(filename)
    
    # Open the output file reader for writing
    csv_file = open(filename, 'a')
    writer   = csv.writer(csv_file)
    
    # Wrtie the answers to file
    for x in xrange(len(answers_1)):
        writer.writerow([expInfo['date'],expInfo['participant'],expInfo['expName'],answers_1[x],rt])
        

        
    csv_file.flush()
    csv_file.close()
# end def run_time
    
if __name__ == "__main__":
    run_time(001)
