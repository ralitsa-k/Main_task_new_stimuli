#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v3.2.3),
    on Fri Mar 27 14:05:11 2020
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '3.2.3'
expName = 'trsut_define_game'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/apple/Documents/PhD/MAIN_TASKS/Construct_stimuli/Main_task_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=[2560, 1440], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[-1,-1,-1], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "demo"
demoClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text="Example. First block is social and will run for 5 trials, then will be the non-social block. \n\nLeft key is 'up', right key is 'down'.\n\nPress space to continue.  \n",
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_2 = keyboard.Keyboard()

# Initialize components for Routine "cue"
cueClock = core.Clock()
fix_cross = visual.ShapeStim(
    win=win, name='fix_cross', vertices='cross',
    size=(0.03, 0.03),
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=1.0, lineColorSpace='hsv',
    fillColor=1.0, fillColorSpace='hsv',
    opacity=1, depth=-1.0, interpolate=True)

# Initialize components for Routine "two_faces"
two_facesClock = core.Clock()
faces = visual.ImageStim(
    win=win,
    name='faces', units='height', 
    image='sin', mask=None,
    ori=0, pos=(0,0), size=(0.23, 0.6),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
loading = visual.MovieStim3(
    win=win, name='loading',
    noAudio = False,
    filename='giphy.gif',
    ori=0, pos=(0, 0), opacity=1,
    loop=True,
    size=(30, 30),
    depth=-2.0,
    )
Orangeframe = visual.ImageStim(
    win=win,
    name='Orangeframe', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.23, 0.6),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)

# Initialize components for Routine "response_screen"
response_screenClock = core.Clock()
key_resp_5 = keyboard.Keyboard()
whiteUD = visual.ImageStim(
    win=win,
    name='whiteUD', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.13, 0.04),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
fix_cross2 = visual.ShapeStim(
    win=win, name='fix_cross2', vertices='cross',
    size=(0.03, 0.03),
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-3.0, interpolate=True)

# Initialize components for Routine "feedback"
feedbackClock = core.Clock()
orange_UD = visual.ImageStim(
    win=win,
    name='orange_UD', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.13, 0.04),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
polygon_3 = visual.ShapeStim(
    win=win, name='polygon_3', vertices='cross',
    size=(0.03, 0.03),
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-2.0, interpolate=True)

# Initialize components for Routine "end_cross"
end_crossClock = core.Clock()
polygon = visual.ShapeStim(
    win=win, name='polygon', vertices='cross',
    size=(0.03, 0.03),
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-1.0, interpolate=True)

# Initialize components for Routine "cue"
cueClock = core.Clock()
fix_cross = visual.ShapeStim(
    win=win, name='fix_cross', vertices='cross',
    size=(0.03, 0.03),
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=1.0, lineColorSpace='hsv',
    fillColor=1.0, fillColorSpace='hsv',
    opacity=1, depth=-1.0, interpolate=True)

# Initialize components for Routine "two_faces"
two_facesClock = core.Clock()
faces = visual.ImageStim(
    win=win,
    name='faces', units='height', 
    image='sin', mask=None,
    ori=0, pos=(0,0), size=(0.23, 0.6),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
loading = visual.MovieStim3(
    win=win, name='loading',
    noAudio = False,
    filename='giphy.gif',
    ori=0, pos=(0, 0), opacity=1,
    loop=True,
    size=(30, 30),
    depth=-2.0,
    )
Orangeframe = visual.ImageStim(
    win=win,
    name='Orangeframe', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.23, 0.6),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)

# Initialize components for Routine "response_screen"
response_screenClock = core.Clock()
key_resp_5 = keyboard.Keyboard()
whiteUD = visual.ImageStim(
    win=win,
    name='whiteUD', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.13, 0.04),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
fix_cross2 = visual.ShapeStim(
    win=win, name='fix_cross2', vertices='cross',
    size=(0.03, 0.03),
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-3.0, interpolate=True)

# Initialize components for Routine "feedback"
feedbackClock = core.Clock()
orange_UD = visual.ImageStim(
    win=win,
    name='orange_UD', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.13, 0.04),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
polygon_3 = visual.ShapeStim(
    win=win, name='polygon_3', vertices='cross',
    size=(0.03, 0.03),
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-2.0, interpolate=True)

# Initialize components for Routine "end_cross"
end_crossClock = core.Clock()
polygon = visual.ShapeStim(
    win=win, name='polygon', vertices='cross',
    size=(0.03, 0.03),
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-1.0, interpolate=True)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "demo"-------
# update component parameters for each repeat
key_resp_2.keys = []
key_resp_2.rt = []
# keep track of which components have finished
demoComponents = [text, key_resp_2]
for thisComponent in demoComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
demoClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "demo"-------
while continueRoutine:
    # get current time
    t = demoClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=demoClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text* updates
    if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text.frameNStart = frameN  # exact frame index
        text.tStart = t  # local t and not account for scr refresh
        text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
        text.setAutoDraw(True)
    
    # *key_resp_2* updates
    waitOnFlip = False
    if key_resp_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_2.frameNStart = frameN  # exact frame index
        key_resp_2.tStart = t  # local t and not account for scr refresh
        key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
        key_resp_2.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_2.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_2.getKeys(keyList=['space'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            key_resp_2.keys = theseKeys.name  # just the last key pressed
            key_resp_2.rt = theseKeys.rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in demoComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "demo"-------
for thisComponent in demoComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text.started', text.tStartRefresh)
thisExp.addData('text.stopped', text.tStopRefresh)
# check responses
if key_resp_2.keys in ['', [], None]:  # No response was made
    key_resp_2.keys = None
thisExp.addData('key_resp_2.keys',key_resp_2.keys)
if key_resp_2.keys != None:  # we had a response
    thisExp.addData('key_resp_2.rt', key_resp_2.rt)
thisExp.addData('key_resp_2.started', key_resp_2.tStartRefresh)
thisExp.addData('key_resp_2.stopped', key_resp_2.tStopRefresh)
thisExp.nextEntry()
# the Routine "demo" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
Soc = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('pair_faces_Soc.csv'),
    seed=None, name='Soc')
thisExp.addLoop(Soc)  # add the loop to the experiment
thisSoc = Soc.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisSoc.rgb)
if thisSoc != None:
    for paramName in thisSoc:
        exec('{} = thisSoc[paramName]'.format(paramName))

for thisSoc in Soc:
    currentLoop = Soc
    # abbreviate parameter names if possible (e.g. rgb = thisSoc.rgb)
    if thisSoc != None:
        for paramName in thisSoc:
            exec('{} = thisSoc[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "cue"-------
    # update component parameters for each repeat
    z = randint(low = 60, high = 90) # values will range from 60 to 90
    
    thisExp.addData('random_duration_cue', z)
    
    
    if Soc.thisTrialN in [5]:
        Soc.finished = True 
    fix_cross.setFillColor(cueCol)
    fix_cross.setLineColor(cueCol)
    # keep track of which components have finished
    cueComponents = [fix_cross]
    for thisComponent in cueComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    cueClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "cue"-------
    while continueRoutine:
        # get current time
        t = cueClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=cueClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fix_cross* updates
        if fix_cross.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            fix_cross.frameNStart = frameN  # exact frame index
            fix_cross.tStart = t  # local t and not account for scr refresh
            fix_cross.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fix_cross, 'tStartRefresh')  # time at next scr refresh
            fix_cross.setAutoDraw(True)
        if fix_cross.status == STARTED:
            if frameN >= (fix_cross.frameNStart + z):
                # keep track of stop time/frame for later
                fix_cross.tStop = t  # not accounting for scr refresh
                fix_cross.frameNStop = frameN  # exact frame index
                win.timeOnFlip(fix_cross, 'tStopRefresh')  # time at next scr refresh
                fix_cross.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in cueComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "cue"-------
    for thisComponent in cueComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    Soc.addData('fix_cross.started', fix_cross.tStartRefresh)
    Soc.addData('fix_cross.stopped', fix_cross.tStopRefresh)
    # the Routine "cue" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "two_faces"-------
    # update component parameters for each repeat
    x = randint(low = 150, high = 200) 
    y = 250 - x
    thisExp.addData('random_duration_two_faces', x)
    faces.setImage(img_names)
    Orangeframe.setImage(polygonPos)
    # keep track of which components have finished
    two_facesComponents = [faces, loading, Orangeframe]
    for thisComponent in two_facesComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    two_facesClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "two_faces"-------
    while continueRoutine:
        # get current time
        t = two_facesClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=two_facesClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *faces* updates
        if faces.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            faces.frameNStart = frameN  # exact frame index
            faces.tStart = t  # local t and not account for scr refresh
            faces.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(faces, 'tStartRefresh')  # time at next scr refresh
            faces.setAutoDraw(True)
        if faces.status == STARTED:
            if frameN >= (faces.frameNStart + 250):
                # keep track of stop time/frame for later
                faces.tStop = t  # not accounting for scr refresh
                faces.frameNStop = frameN  # exact frame index
                win.timeOnFlip(faces, 'tStopRefresh')  # time at next scr refresh
                faces.setAutoDraw(False)
        
        # *loading* updates
        if loading.status == NOT_STARTED and frameN >= 70:
            # keep track of start time/frame for later
            loading.frameNStart = frameN  # exact frame index
            loading.tStart = t  # local t and not account for scr refresh
            loading.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(loading, 'tStartRefresh')  # time at next scr refresh
            loading.setAutoDraw(True)
        if loading.status == STARTED:
            if frameN >= (loading.frameNStart + x-70):
                # keep track of stop time/frame for later
                loading.tStop = t  # not accounting for scr refresh
                loading.frameNStop = frameN  # exact frame index
                win.timeOnFlip(loading, 'tStopRefresh')  # time at next scr refresh
                loading.setAutoDraw(False)
        
        # *Orangeframe* updates
        if Orangeframe.status == NOT_STARTED and frameN >= x:
            # keep track of start time/frame for later
            Orangeframe.frameNStart = frameN  # exact frame index
            Orangeframe.tStart = t  # local t and not account for scr refresh
            Orangeframe.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Orangeframe, 'tStartRefresh')  # time at next scr refresh
            Orangeframe.setAutoDraw(True)
        if Orangeframe.status == STARTED:
            if frameN >= (Orangeframe.frameNStart + y):
                # keep track of stop time/frame for later
                Orangeframe.tStop = t  # not accounting for scr refresh
                Orangeframe.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Orangeframe, 'tStopRefresh')  # time at next scr refresh
                Orangeframe.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in two_facesComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "two_faces"-------
    for thisComponent in two_facesComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    Soc.addData('faces.started', faces.tStartRefresh)
    Soc.addData('faces.stopped', faces.tStopRefresh)
    Soc.addData('loading.started', loading.tStartRefresh)
    Soc.addData('loading.stopped', loading.tStopRefresh)
    Soc.addData('Orangeframe.started', Orangeframe.tStartRefresh)
    Soc.addData('Orangeframe.stopped', Orangeframe.tStopRefresh)
    # the Routine "two_faces" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "response_screen"-------
    # update component parameters for each repeat
    key_resp_5.keys = []
    key_resp_5.rt = []
    img = 'upper_lower.png'
    whiteUD.setImage(img)
    # keep track of which components have finished
    response_screenComponents = [key_resp_5, whiteUD, fix_cross2]
    for thisComponent in response_screenComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    response_screenClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "response_screen"-------
    while continueRoutine:
        # get current time
        t = response_screenClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=response_screenClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *key_resp_5* updates
        waitOnFlip = False
        if key_resp_5.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_5.frameNStart = frameN  # exact frame index
            key_resp_5.tStart = t  # local t and not account for scr refresh
            key_resp_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_5, 'tStartRefresh')  # time at next scr refresh
            key_resp_5.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_5.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_5.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_5.status == STARTED:
            if frameN >= (key_resp_5.frameNStart + 90):
                # keep track of stop time/frame for later
                key_resp_5.tStop = t  # not accounting for scr refresh
                key_resp_5.frameNStop = frameN  # exact frame index
                win.timeOnFlip(key_resp_5, 'tStopRefresh')  # time at next scr refresh
                key_resp_5.status = FINISHED
        if key_resp_5.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_5.getKeys(keyList=['left', 'right'], waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed
                
                # check for quit:
                if "escape" == theseKeys:
                    endExpNow = True
                key_resp_5.keys = theseKeys.name  # just the last key pressed
                key_resp_5.rt = theseKeys.rt
                # a response ends the routine
                continueRoutine = False
        
        # *whiteUD* updates
        if whiteUD.status == NOT_STARTED and frameN >= 0.0:
            # keep track of start time/frame for later
            whiteUD.frameNStart = frameN  # exact frame index
            whiteUD.tStart = t  # local t and not account for scr refresh
            whiteUD.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(whiteUD, 'tStartRefresh')  # time at next scr refresh
            whiteUD.setAutoDraw(True)
        
        # *fix_cross2* updates
        if fix_cross2.status == NOT_STARTED and frameN >= 0.0:
            # keep track of start time/frame for later
            fix_cross2.frameNStart = frameN  # exact frame index
            fix_cross2.tStart = t  # local t and not account for scr refresh
            fix_cross2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fix_cross2, 'tStartRefresh')  # time at next scr refresh
            fix_cross2.setAutoDraw(True)
        if fix_cross2.status == STARTED:
            if frameN >= (fix_cross2.frameNStart + 90):
                # keep track of stop time/frame for later
                fix_cross2.tStop = t  # not accounting for scr refresh
                fix_cross2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(fix_cross2, 'tStopRefresh')  # time at next scr refresh
                fix_cross2.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in response_screenComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "response_screen"-------
    for thisComponent in response_screenComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_5.keys in ['', [], None]:  # No response was made
        key_resp_5.keys = None
    Soc.addData('key_resp_5.keys',key_resp_5.keys)
    if key_resp_5.keys != None:  # we had a response
        Soc.addData('key_resp_5.rt', key_resp_5.rt)
    Soc.addData('key_resp_5.started', key_resp_5.tStartRefresh)
    Soc.addData('key_resp_5.stopped', key_resp_5.tStopRefresh)
    Soc.addData('whiteUD.started', whiteUD.tStartRefresh)
    Soc.addData('whiteUD.stopped', whiteUD.tStopRefresh)
    Soc.addData('fix_cross2.started', fix_cross2.tStartRefresh)
    Soc.addData('fix_cross2.stopped', fix_cross2.tStopRefresh)
    # the Routine "response_screen" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "feedback"-------
    # update component parameters for each repeat
    
    
    if event.getKeys(['left']):
        img = 'up.png'
        
    if event.getKeys(['right']):
        img = 'down.png'
    orange_UD.setImage(img)
    # keep track of which components have finished
    feedbackComponents = [orange_UD, polygon_3]
    for thisComponent in feedbackComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    feedbackClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "feedback"-------
    while continueRoutine:
        # get current time
        t = feedbackClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=feedbackClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *orange_UD* updates
        if orange_UD.status == NOT_STARTED and frameN >= 0.0:
            # keep track of start time/frame for later
            orange_UD.frameNStart = frameN  # exact frame index
            orange_UD.tStart = t  # local t and not account for scr refresh
            orange_UD.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(orange_UD, 'tStartRefresh')  # time at next scr refresh
            orange_UD.setAutoDraw(True)
        if orange_UD.status == STARTED:
            if frameN >= (orange_UD.frameNStart + 90):
                # keep track of stop time/frame for later
                orange_UD.tStop = t  # not accounting for scr refresh
                orange_UD.frameNStop = frameN  # exact frame index
                win.timeOnFlip(orange_UD, 'tStopRefresh')  # time at next scr refresh
                orange_UD.setAutoDraw(False)
        
        # *polygon_3* updates
        if polygon_3.status == NOT_STARTED and frameN >= 0.0:
            # keep track of start time/frame for later
            polygon_3.frameNStart = frameN  # exact frame index
            polygon_3.tStart = t  # local t and not account for scr refresh
            polygon_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon_3, 'tStartRefresh')  # time at next scr refresh
            polygon_3.setAutoDraw(True)
        if polygon_3.status == STARTED:
            if frameN >= (polygon_3.frameNStart + 90):
                # keep track of stop time/frame for later
                polygon_3.tStop = t  # not accounting for scr refresh
                polygon_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(polygon_3, 'tStopRefresh')  # time at next scr refresh
                polygon_3.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in feedbackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "feedback"-------
    for thisComponent in feedbackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    Soc.addData('orange_UD.started', orange_UD.tStartRefresh)
    Soc.addData('orange_UD.stopped', orange_UD.tStopRefresh)
    Soc.addData('polygon_3.started', polygon_3.tStartRefresh)
    Soc.addData('polygon_3.stopped', polygon_3.tStopRefresh)
    # the Routine "feedback" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "end_cross"-------
    # update component parameters for each repeat
    r = randint(low = 90, high = 180) # values will range from 90 to 180
    
    thisExp.addData('random_duration_end_cross', r)
    # keep track of which components have finished
    end_crossComponents = [polygon]
    for thisComponent in end_crossComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    end_crossClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "end_cross"-------
    while continueRoutine:
        # get current time
        t = end_crossClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=end_crossClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *polygon* updates
        if polygon.status == NOT_STARTED and frameN >= 0.0:
            # keep track of start time/frame for later
            polygon.frameNStart = frameN  # exact frame index
            polygon.tStart = t  # local t and not account for scr refresh
            polygon.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon, 'tStartRefresh')  # time at next scr refresh
            polygon.setAutoDraw(True)
        if polygon.status == STARTED:
            if frameN >= (polygon.frameNStart + r):
                # keep track of stop time/frame for later
                polygon.tStop = t  # not accounting for scr refresh
                polygon.frameNStop = frameN  # exact frame index
                win.timeOnFlip(polygon, 'tStopRefresh')  # time at next scr refresh
                polygon.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in end_crossComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "end_cross"-------
    for thisComponent in end_crossComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    Soc.addData('polygon.started', polygon.tStartRefresh)
    Soc.addData('polygon.stopped', polygon.tStopRefresh)
    # the Routine "end_cross" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'Soc'


# set up handler to look after randomisation of conditions etc
nonSoc = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('pair_num_nonSoc.csv'),
    seed=None, name='nonSoc')
thisExp.addLoop(nonSoc)  # add the loop to the experiment
thisNonSoc = nonSoc.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisNonSoc.rgb)
if thisNonSoc != None:
    for paramName in thisNonSoc:
        exec('{} = thisNonSoc[paramName]'.format(paramName))

for thisNonSoc in nonSoc:
    currentLoop = nonSoc
    # abbreviate parameter names if possible (e.g. rgb = thisNonSoc.rgb)
    if thisNonSoc != None:
        for paramName in thisNonSoc:
            exec('{} = thisNonSoc[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "cue"-------
    # update component parameters for each repeat
    z = randint(low = 60, high = 90) # values will range from 60 to 90
    
    thisExp.addData('random_duration_cue', z)
    
    
    if Soc.thisTrialN in [5]:
        Soc.finished = True 
    fix_cross.setFillColor(cueCol)
    fix_cross.setLineColor(cueCol)
    # keep track of which components have finished
    cueComponents = [fix_cross]
    for thisComponent in cueComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    cueClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "cue"-------
    while continueRoutine:
        # get current time
        t = cueClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=cueClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fix_cross* updates
        if fix_cross.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            fix_cross.frameNStart = frameN  # exact frame index
            fix_cross.tStart = t  # local t and not account for scr refresh
            fix_cross.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fix_cross, 'tStartRefresh')  # time at next scr refresh
            fix_cross.setAutoDraw(True)
        if fix_cross.status == STARTED:
            if frameN >= (fix_cross.frameNStart + z):
                # keep track of stop time/frame for later
                fix_cross.tStop = t  # not accounting for scr refresh
                fix_cross.frameNStop = frameN  # exact frame index
                win.timeOnFlip(fix_cross, 'tStopRefresh')  # time at next scr refresh
                fix_cross.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in cueComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "cue"-------
    for thisComponent in cueComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    nonSoc.addData('fix_cross.started', fix_cross.tStartRefresh)
    nonSoc.addData('fix_cross.stopped', fix_cross.tStopRefresh)
    # the Routine "cue" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "two_faces"-------
    # update component parameters for each repeat
    x = randint(low = 150, high = 200) 
    y = 250 - x
    thisExp.addData('random_duration_two_faces', x)
    faces.setImage(img_names)
    Orangeframe.setImage(polygonPos)
    # keep track of which components have finished
    two_facesComponents = [faces, loading, Orangeframe]
    for thisComponent in two_facesComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    two_facesClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "two_faces"-------
    while continueRoutine:
        # get current time
        t = two_facesClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=two_facesClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *faces* updates
        if faces.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            faces.frameNStart = frameN  # exact frame index
            faces.tStart = t  # local t and not account for scr refresh
            faces.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(faces, 'tStartRefresh')  # time at next scr refresh
            faces.setAutoDraw(True)
        if faces.status == STARTED:
            if frameN >= (faces.frameNStart + 250):
                # keep track of stop time/frame for later
                faces.tStop = t  # not accounting for scr refresh
                faces.frameNStop = frameN  # exact frame index
                win.timeOnFlip(faces, 'tStopRefresh')  # time at next scr refresh
                faces.setAutoDraw(False)
        
        # *loading* updates
        if loading.status == NOT_STARTED and frameN >= 70:
            # keep track of start time/frame for later
            loading.frameNStart = frameN  # exact frame index
            loading.tStart = t  # local t and not account for scr refresh
            loading.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(loading, 'tStartRefresh')  # time at next scr refresh
            loading.setAutoDraw(True)
        if loading.status == STARTED:
            if frameN >= (loading.frameNStart + x-70):
                # keep track of stop time/frame for later
                loading.tStop = t  # not accounting for scr refresh
                loading.frameNStop = frameN  # exact frame index
                win.timeOnFlip(loading, 'tStopRefresh')  # time at next scr refresh
                loading.setAutoDraw(False)
        
        # *Orangeframe* updates
        if Orangeframe.status == NOT_STARTED and frameN >= x:
            # keep track of start time/frame for later
            Orangeframe.frameNStart = frameN  # exact frame index
            Orangeframe.tStart = t  # local t and not account for scr refresh
            Orangeframe.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Orangeframe, 'tStartRefresh')  # time at next scr refresh
            Orangeframe.setAutoDraw(True)
        if Orangeframe.status == STARTED:
            if frameN >= (Orangeframe.frameNStart + y):
                # keep track of stop time/frame for later
                Orangeframe.tStop = t  # not accounting for scr refresh
                Orangeframe.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Orangeframe, 'tStopRefresh')  # time at next scr refresh
                Orangeframe.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in two_facesComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "two_faces"-------
    for thisComponent in two_facesComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    nonSoc.addData('faces.started', faces.tStartRefresh)
    nonSoc.addData('faces.stopped', faces.tStopRefresh)
    nonSoc.addData('loading.started', loading.tStartRefresh)
    nonSoc.addData('loading.stopped', loading.tStopRefresh)
    nonSoc.addData('Orangeframe.started', Orangeframe.tStartRefresh)
    nonSoc.addData('Orangeframe.stopped', Orangeframe.tStopRefresh)
    # the Routine "two_faces" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "response_screen"-------
    # update component parameters for each repeat
    key_resp_5.keys = []
    key_resp_5.rt = []
    img = 'upper_lower.png'
    whiteUD.setImage(img)
    # keep track of which components have finished
    response_screenComponents = [key_resp_5, whiteUD, fix_cross2]
    for thisComponent in response_screenComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    response_screenClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "response_screen"-------
    while continueRoutine:
        # get current time
        t = response_screenClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=response_screenClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *key_resp_5* updates
        waitOnFlip = False
        if key_resp_5.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_5.frameNStart = frameN  # exact frame index
            key_resp_5.tStart = t  # local t and not account for scr refresh
            key_resp_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_5, 'tStartRefresh')  # time at next scr refresh
            key_resp_5.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_5.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_5.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_5.status == STARTED:
            if frameN >= (key_resp_5.frameNStart + 90):
                # keep track of stop time/frame for later
                key_resp_5.tStop = t  # not accounting for scr refresh
                key_resp_5.frameNStop = frameN  # exact frame index
                win.timeOnFlip(key_resp_5, 'tStopRefresh')  # time at next scr refresh
                key_resp_5.status = FINISHED
        if key_resp_5.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_5.getKeys(keyList=['left', 'right'], waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed
                
                # check for quit:
                if "escape" == theseKeys:
                    endExpNow = True
                key_resp_5.keys = theseKeys.name  # just the last key pressed
                key_resp_5.rt = theseKeys.rt
                # a response ends the routine
                continueRoutine = False
        
        # *whiteUD* updates
        if whiteUD.status == NOT_STARTED and frameN >= 0.0:
            # keep track of start time/frame for later
            whiteUD.frameNStart = frameN  # exact frame index
            whiteUD.tStart = t  # local t and not account for scr refresh
            whiteUD.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(whiteUD, 'tStartRefresh')  # time at next scr refresh
            whiteUD.setAutoDraw(True)
        
        # *fix_cross2* updates
        if fix_cross2.status == NOT_STARTED and frameN >= 0.0:
            # keep track of start time/frame for later
            fix_cross2.frameNStart = frameN  # exact frame index
            fix_cross2.tStart = t  # local t and not account for scr refresh
            fix_cross2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fix_cross2, 'tStartRefresh')  # time at next scr refresh
            fix_cross2.setAutoDraw(True)
        if fix_cross2.status == STARTED:
            if frameN >= (fix_cross2.frameNStart + 90):
                # keep track of stop time/frame for later
                fix_cross2.tStop = t  # not accounting for scr refresh
                fix_cross2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(fix_cross2, 'tStopRefresh')  # time at next scr refresh
                fix_cross2.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in response_screenComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "response_screen"-------
    for thisComponent in response_screenComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_5.keys in ['', [], None]:  # No response was made
        key_resp_5.keys = None
    nonSoc.addData('key_resp_5.keys',key_resp_5.keys)
    if key_resp_5.keys != None:  # we had a response
        nonSoc.addData('key_resp_5.rt', key_resp_5.rt)
    nonSoc.addData('key_resp_5.started', key_resp_5.tStartRefresh)
    nonSoc.addData('key_resp_5.stopped', key_resp_5.tStopRefresh)
    nonSoc.addData('whiteUD.started', whiteUD.tStartRefresh)
    nonSoc.addData('whiteUD.stopped', whiteUD.tStopRefresh)
    nonSoc.addData('fix_cross2.started', fix_cross2.tStartRefresh)
    nonSoc.addData('fix_cross2.stopped', fix_cross2.tStopRefresh)
    # the Routine "response_screen" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "feedback"-------
    # update component parameters for each repeat
    
    
    if event.getKeys(['left']):
        img = 'up.png'
        
    if event.getKeys(['right']):
        img = 'down.png'
    orange_UD.setImage(img)
    # keep track of which components have finished
    feedbackComponents = [orange_UD, polygon_3]
    for thisComponent in feedbackComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    feedbackClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "feedback"-------
    while continueRoutine:
        # get current time
        t = feedbackClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=feedbackClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *orange_UD* updates
        if orange_UD.status == NOT_STARTED and frameN >= 0.0:
            # keep track of start time/frame for later
            orange_UD.frameNStart = frameN  # exact frame index
            orange_UD.tStart = t  # local t and not account for scr refresh
            orange_UD.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(orange_UD, 'tStartRefresh')  # time at next scr refresh
            orange_UD.setAutoDraw(True)
        if orange_UD.status == STARTED:
            if frameN >= (orange_UD.frameNStart + 90):
                # keep track of stop time/frame for later
                orange_UD.tStop = t  # not accounting for scr refresh
                orange_UD.frameNStop = frameN  # exact frame index
                win.timeOnFlip(orange_UD, 'tStopRefresh')  # time at next scr refresh
                orange_UD.setAutoDraw(False)
        
        # *polygon_3* updates
        if polygon_3.status == NOT_STARTED and frameN >= 0.0:
            # keep track of start time/frame for later
            polygon_3.frameNStart = frameN  # exact frame index
            polygon_3.tStart = t  # local t and not account for scr refresh
            polygon_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon_3, 'tStartRefresh')  # time at next scr refresh
            polygon_3.setAutoDraw(True)
        if polygon_3.status == STARTED:
            if frameN >= (polygon_3.frameNStart + 90):
                # keep track of stop time/frame for later
                polygon_3.tStop = t  # not accounting for scr refresh
                polygon_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(polygon_3, 'tStopRefresh')  # time at next scr refresh
                polygon_3.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in feedbackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "feedback"-------
    for thisComponent in feedbackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    nonSoc.addData('orange_UD.started', orange_UD.tStartRefresh)
    nonSoc.addData('orange_UD.stopped', orange_UD.tStopRefresh)
    nonSoc.addData('polygon_3.started', polygon_3.tStartRefresh)
    nonSoc.addData('polygon_3.stopped', polygon_3.tStopRefresh)
    # the Routine "feedback" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "end_cross"-------
    # update component parameters for each repeat
    r = randint(low = 90, high = 180) # values will range from 90 to 180
    
    thisExp.addData('random_duration_end_cross', r)
    # keep track of which components have finished
    end_crossComponents = [polygon]
    for thisComponent in end_crossComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    end_crossClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "end_cross"-------
    while continueRoutine:
        # get current time
        t = end_crossClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=end_crossClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *polygon* updates
        if polygon.status == NOT_STARTED and frameN >= 0.0:
            # keep track of start time/frame for later
            polygon.frameNStart = frameN  # exact frame index
            polygon.tStart = t  # local t and not account for scr refresh
            polygon.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon, 'tStartRefresh')  # time at next scr refresh
            polygon.setAutoDraw(True)
        if polygon.status == STARTED:
            if frameN >= (polygon.frameNStart + r):
                # keep track of stop time/frame for later
                polygon.tStop = t  # not accounting for scr refresh
                polygon.frameNStop = frameN  # exact frame index
                win.timeOnFlip(polygon, 'tStopRefresh')  # time at next scr refresh
                polygon.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in end_crossComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "end_cross"-------
    for thisComponent in end_crossComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    nonSoc.addData('polygon.started', polygon.tStartRefresh)
    nonSoc.addData('polygon.stopped', polygon.tStopRefresh)
    # the Routine "end_cross" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'nonSoc'


# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
