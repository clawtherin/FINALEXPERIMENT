#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2020.2.5),
    on November 06, 2020, at 05:19
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
psychopyVersion = '2020.2.5'
expName = 'XPPSYCH'  # from the Builder filename that created this script
expInfo = {'participant': '', 'age': '', 'sex': '', 'occupation': ''}
dlg = gui.DlgFromDict(dictionary=expInfo, sort_keys=False, title=expName)
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
    originPath='C:\\Users\\anonymous\\Documents\\data\\data\\XPPSYCH.py',
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
    size=[1366, 768], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
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

# Initialize components for Routine "WelcomeScreen"
WelcomeScreenClock = core.Clock()
polygon1 = visual.Rect(
    win=win, name='polygon1',
    width=(2, 2)[0], height=(2, 2)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[-1.000,-1.000,-1.000], lineColorSpace='rgb',
    fillColor=[-1.000,-1.000,-1.000], fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
welcome = visual.TextStim(win=win, name='welcome',
    text='WELCOME TO THIS EXPERIMENT!\n\nKindly read the series of forenames (items) as they appear on the screen.',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "SupraStudy"
SupraStudyClock = core.Clock()
polygon = visual.Rect(
    win=win, name='polygon',
    width=(2, 2)[0], height=(2, 2)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[-1.000,-1.000,-1.000], lineColorSpace='rgb',
    fillColor=[-1.000,-1.000,-1.000], fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
ForenameSup = visual.TextStim(win=win, name='ForenameSup',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
CueSup1 = visual.TextStim(win=win, name='CueSup1',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
BlankSup = visual.TextStim(win=win, name='BlankSup',
    text='.',
    font='Arial',
    pos=(0, 0), height=0.01, wrapWidth=None, ori=0, 
    color=[-1.000,-1.000,-1.000], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "Distractor1"
Distractor1Clock = core.Clock()
polygon_2 = visual.Rect(
    win=win, name='polygon_2',
    width=(2, 2)[0], height=(2, 2)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[-1.000,-1.000,-1.000], lineColorSpace='rgb',
    fillColor=[-1.000,-1.000,-1.000], fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
dis1 = visual.TextStim(win=win, name='dis1',
    text='.',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color=[-1.000,-1.000,-1.000], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "InstructionsScreen"
InstructionsScreenClock = core.Clock()
polygon_3 = visual.Rect(
    win=win, name='polygon_3',
    width=(2, 2)[0], height=(2, 2)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[-1.000,-1.000,-1.000], lineColorSpace='rgb',
    fillColor=[-1.000,-1.000,-1.000], fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
instruction = visual.TextStim(win=win, name='instruction',
    text='The forenames (items) you read a while ago will reappear with other forenames not presented earlier. Determine whether the item is old (shown in the study phase) by pressing "O" or new (not shown in the study phase) by pressing "N".\n\n"O" Key - Old (present in the study phase)\n"N" Key - New (not present in the study phase)\n\nPress the spacebar to proceed.',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
dis1key = keyboard.Keyboard()

# Initialize components for Routine "SupraTest"
SupraTestClock = core.Clock()
polygon_4 = visual.Rect(
    win=win, name='polygon_4',
    width=(2, 2)[0], height=(2, 2)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[-1.000,-1.000,-1.000], lineColorSpace='rgb',
    fillColor=[-1.000,-1.000,-1.000], fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
suptest = visual.TextStim(win=win, name='suptest',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
key_resp = keyboard.Keyboard()

# Initialize components for Routine "Phase2"
Phase2Clock = core.Clock()
polygon_5 = visual.Rect(
    win=win, name='polygon_5',
    width=(2, 2)[0], height=(2, 2)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[-1.000,-1.000,-1.000], lineColorSpace='rgb',
    fillColor=[-1.000,-1.000,-1.000], fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
distractor1 = visual.TextStim(win=win, name='distractor1',
    text='What is 0 x 0 = ?',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
key_resp_2 = keyboard.Keyboard()

# Initialize components for Routine "Instructions2"
Instructions2Clock = core.Clock()
polygon_7 = visual.Rect(
    win=win, name='polygon_7',
    width=(2, 2)[0], height=(2, 2)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[-1.000,-1.000,-1.000], lineColorSpace='rgb',
    fillColor=[-1.000,-1.000,-1.000], fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
textphase2 = visual.TextStim(win=win, name='textphase2',
    text='Kindly read the series of forenames (items) as they appear on the screen.',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "SubliStudy"
SubliStudyClock = core.Clock()
polygon_6 = visual.Rect(
    win=win, name='polygon_6',
    width=(2, 2)[0], height=(2, 2)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[-1.000,-1.000,-1.000], lineColorSpace='rgb',
    fillColor=[-1.000,-1.000,-1.000], fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
ForenameSub = visual.TextStim(win=win, name='ForenameSub',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
Mask1 = visual.TextStim(win=win, name='Mask1',
    text='###########',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
Cue = visual.TextStim(win=win, name='Cue',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
Mask2 = visual.TextStim(win=win, name='Mask2',
    text='###########',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
blank1 = visual.TextStim(win=win, name='blank1',
    text='.',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color=[-1.000,-1.000,-1.000], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);

# Initialize components for Routine "InstructionsScreen"
InstructionsScreenClock = core.Clock()
polygon_3 = visual.Rect(
    win=win, name='polygon_3',
    width=(2, 2)[0], height=(2, 2)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[-1.000,-1.000,-1.000], lineColorSpace='rgb',
    fillColor=[-1.000,-1.000,-1.000], fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
instruction = visual.TextStim(win=win, name='instruction',
    text='The forenames (items) you read a while ago will reappear with other forenames not presented earlier. Determine whether the item is old (shown in the study phase) by pressing "O" or new (not shown in the study phase) by pressing "N".\n\n"O" Key - Old (present in the study phase)\n"N" Key - New (not present in the study phase)\n\nPress the spacebar to proceed.',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
dis1key = keyboard.Keyboard()

# Initialize components for Routine "Distractor1"
Distractor1Clock = core.Clock()
polygon_2 = visual.Rect(
    win=win, name='polygon_2',
    width=(2, 2)[0], height=(2, 2)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[-1.000,-1.000,-1.000], lineColorSpace='rgb',
    fillColor=[-1.000,-1.000,-1.000], fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
dis1 = visual.TextStim(win=win, name='dis1',
    text='.',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color=[-1.000,-1.000,-1.000], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "SubliTest"
SubliTestClock = core.Clock()
polygon_8 = visual.Rect(
    win=win, name='polygon_8',
    width=(2, 2)[0], height=(2, 2)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[-1.000,-1.000,-1.000], lineColorSpace='rgb',
    fillColor=[-1.000,-1.000,-1.000], fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
SubTest = visual.TextStim(win=win, name='SubTest',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
key_resp_3 = keyboard.Keyboard()

# Initialize components for Routine "EndScreen"
EndScreenClock = core.Clock()
polygon_9 = visual.Rect(
    win=win, name='polygon_9',
    width=(2, 2)[0], height=(2, 2)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[-1.000,-1.000,-1.000], lineColorSpace='rgb',
    fillColor=[-1.000,-1.000,-1.000], fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
text = visual.TextStim(win=win, name='text',
    text='END OF EXPERIMENT\n\nThank you for participating!',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "WelcomeScreen"-------
continueRoutine = True
routineTimer.add(7.000000)
# update component parameters for each repeat
# keep track of which components have finished
WelcomeScreenComponents = [polygon1, welcome]
for thisComponent in WelcomeScreenComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
WelcomeScreenClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "WelcomeScreen"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = WelcomeScreenClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=WelcomeScreenClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *polygon1* updates
    if polygon1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        polygon1.frameNStart = frameN  # exact frame index
        polygon1.tStart = t  # local t and not account for scr refresh
        polygon1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(polygon1, 'tStartRefresh')  # time at next scr refresh
        polygon1.setAutoDraw(True)
    if polygon1.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > polygon1.tStartRefresh + 7-frameTolerance:
            # keep track of stop time/frame for later
            polygon1.tStop = t  # not accounting for scr refresh
            polygon1.frameNStop = frameN  # exact frame index
            win.timeOnFlip(polygon1, 'tStopRefresh')  # time at next scr refresh
            polygon1.setAutoDraw(False)
    
    # *welcome* updates
    if welcome.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        welcome.frameNStart = frameN  # exact frame index
        welcome.tStart = t  # local t and not account for scr refresh
        welcome.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(welcome, 'tStartRefresh')  # time at next scr refresh
        welcome.setAutoDraw(True)
    if welcome.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > welcome.tStartRefresh + 7-frameTolerance:
            # keep track of stop time/frame for later
            welcome.tStop = t  # not accounting for scr refresh
            welcome.frameNStop = frameN  # exact frame index
            win.timeOnFlip(welcome, 'tStopRefresh')  # time at next scr refresh
            welcome.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in WelcomeScreenComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "WelcomeScreen"-------
for thisComponent in WelcomeScreenComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('polygon1.started', polygon1.tStartRefresh)
thisExp.addData('polygon1.stopped', polygon1.tStopRefresh)
thisExp.addData('welcome.started', welcome.tStartRefresh)
thisExp.addData('welcome.stopped', welcome.tStopRefresh)

# set up handler to look after randomisation of conditions etc
SupraTrials = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('SupraliminalNameCue.xlsx'),
    seed=None, name='SupraTrials')
thisExp.addLoop(SupraTrials)  # add the loop to the experiment
thisSupraTrial = SupraTrials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisSupraTrial.rgb)
if thisSupraTrial != None:
    for paramName in thisSupraTrial:
        exec('{} = thisSupraTrial[paramName]'.format(paramName))

for thisSupraTrial in SupraTrials:
    currentLoop = SupraTrials
    # abbreviate parameter names if possible (e.g. rgb = thisSupraTrial.rgb)
    if thisSupraTrial != None:
        for paramName in thisSupraTrial:
            exec('{} = thisSupraTrial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "SupraStudy"-------
    continueRoutine = True
    routineTimer.add(3.400000)
    # update component parameters for each repeat
    ForenameSup.setText(NameSup)
    CueSup1.setText(CueSup)
    # keep track of which components have finished
    SupraStudyComponents = [polygon, ForenameSup, CueSup1, BlankSup]
    for thisComponent in SupraStudyComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    SupraStudyClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "SupraStudy"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = SupraStudyClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=SupraStudyClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *polygon* updates
        if polygon.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            polygon.frameNStart = frameN  # exact frame index
            polygon.tStart = t  # local t and not account for scr refresh
            polygon.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon, 'tStartRefresh')  # time at next scr refresh
            polygon.setAutoDraw(True)
        if polygon.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > polygon.tStartRefresh + 3.40-frameTolerance:
                # keep track of stop time/frame for later
                polygon.tStop = t  # not accounting for scr refresh
                polygon.frameNStop = frameN  # exact frame index
                win.timeOnFlip(polygon, 'tStopRefresh')  # time at next scr refresh
                polygon.setAutoDraw(False)
        
        # *ForenameSup* updates
        if ForenameSup.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ForenameSup.frameNStart = frameN  # exact frame index
            ForenameSup.tStart = t  # local t and not account for scr refresh
            ForenameSup.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ForenameSup, 'tStartRefresh')  # time at next scr refresh
            ForenameSup.setAutoDraw(True)
        if ForenameSup.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > ForenameSup.tStartRefresh + 1.2-frameTolerance:
                # keep track of stop time/frame for later
                ForenameSup.tStop = t  # not accounting for scr refresh
                ForenameSup.frameNStop = frameN  # exact frame index
                win.timeOnFlip(ForenameSup, 'tStopRefresh')  # time at next scr refresh
                ForenameSup.setAutoDraw(False)
        
        # *CueSup1* updates
        if CueSup1.status == NOT_STARTED and tThisFlip >= 1.2-frameTolerance:
            # keep track of start time/frame for later
            CueSup1.frameNStart = frameN  # exact frame index
            CueSup1.tStart = t  # local t and not account for scr refresh
            CueSup1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(CueSup1, 'tStartRefresh')  # time at next scr refresh
            CueSup1.setAutoDraw(True)
        if CueSup1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > CueSup1.tStartRefresh + 1.2-frameTolerance:
                # keep track of stop time/frame for later
                CueSup1.tStop = t  # not accounting for scr refresh
                CueSup1.frameNStop = frameN  # exact frame index
                win.timeOnFlip(CueSup1, 'tStopRefresh')  # time at next scr refresh
                CueSup1.setAutoDraw(False)
        
        # *BlankSup* updates
        if BlankSup.status == NOT_STARTED and tThisFlip >= 2.4-frameTolerance:
            # keep track of start time/frame for later
            BlankSup.frameNStart = frameN  # exact frame index
            BlankSup.tStart = t  # local t and not account for scr refresh
            BlankSup.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(BlankSup, 'tStartRefresh')  # time at next scr refresh
            BlankSup.setAutoDraw(True)
        if BlankSup.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > BlankSup.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                BlankSup.tStop = t  # not accounting for scr refresh
                BlankSup.frameNStop = frameN  # exact frame index
                win.timeOnFlip(BlankSup, 'tStopRefresh')  # time at next scr refresh
                BlankSup.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in SupraStudyComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "SupraStudy"-------
    for thisComponent in SupraStudyComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    SupraTrials.addData('polygon.started', polygon.tStartRefresh)
    SupraTrials.addData('polygon.stopped', polygon.tStopRefresh)
    SupraTrials.addData('ForenameSup.started', ForenameSup.tStartRefresh)
    SupraTrials.addData('ForenameSup.stopped', ForenameSup.tStopRefresh)
    SupraTrials.addData('CueSup1.started', CueSup1.tStartRefresh)
    SupraTrials.addData('CueSup1.stopped', CueSup1.tStopRefresh)
    SupraTrials.addData('BlankSup.started', BlankSup.tStartRefresh)
    SupraTrials.addData('BlankSup.stopped', BlankSup.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1 repeats of 'SupraTrials'


# ------Prepare to start Routine "Distractor1"-------
continueRoutine = True
routineTimer.add(2.000000)
# update component parameters for each repeat
# keep track of which components have finished
Distractor1Components = [polygon_2, dis1]
for thisComponent in Distractor1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Distractor1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Distractor1"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = Distractor1Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Distractor1Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *polygon_2* updates
    if polygon_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        polygon_2.frameNStart = frameN  # exact frame index
        polygon_2.tStart = t  # local t and not account for scr refresh
        polygon_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(polygon_2, 'tStartRefresh')  # time at next scr refresh
        polygon_2.setAutoDraw(True)
    if polygon_2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > polygon_2.tStartRefresh + 2-frameTolerance:
            # keep track of stop time/frame for later
            polygon_2.tStop = t  # not accounting for scr refresh
            polygon_2.frameNStop = frameN  # exact frame index
            win.timeOnFlip(polygon_2, 'tStopRefresh')  # time at next scr refresh
            polygon_2.setAutoDraw(False)
    
    # *dis1* updates
    if dis1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        dis1.frameNStart = frameN  # exact frame index
        dis1.tStart = t  # local t and not account for scr refresh
        dis1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(dis1, 'tStartRefresh')  # time at next scr refresh
        dis1.setAutoDraw(True)
    if dis1.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > dis1.tStartRefresh + 2-frameTolerance:
            # keep track of stop time/frame for later
            dis1.tStop = t  # not accounting for scr refresh
            dis1.frameNStop = frameN  # exact frame index
            win.timeOnFlip(dis1, 'tStopRefresh')  # time at next scr refresh
            dis1.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Distractor1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Distractor1"-------
for thisComponent in Distractor1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('polygon_2.started', polygon_2.tStartRefresh)
thisExp.addData('polygon_2.stopped', polygon_2.tStopRefresh)
thisExp.addData('dis1.started', dis1.tStartRefresh)
thisExp.addData('dis1.stopped', dis1.tStopRefresh)

# ------Prepare to start Routine "InstructionsScreen"-------
continueRoutine = True
# update component parameters for each repeat
dis1key.keys = []
dis1key.rt = []
_dis1key_allKeys = []
# keep track of which components have finished
InstructionsScreenComponents = [polygon_3, instruction, dis1key]
for thisComponent in InstructionsScreenComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
InstructionsScreenClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "InstructionsScreen"-------
while continueRoutine:
    # get current time
    t = InstructionsScreenClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=InstructionsScreenClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *polygon_3* updates
    if polygon_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        polygon_3.frameNStart = frameN  # exact frame index
        polygon_3.tStart = t  # local t and not account for scr refresh
        polygon_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(polygon_3, 'tStartRefresh')  # time at next scr refresh
        polygon_3.setAutoDraw(True)
    
    # *instruction* updates
    if instruction.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instruction.frameNStart = frameN  # exact frame index
        instruction.tStart = t  # local t and not account for scr refresh
        instruction.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instruction, 'tStartRefresh')  # time at next scr refresh
        instruction.setAutoDraw(True)
    
    # *dis1key* updates
    waitOnFlip = False
    if dis1key.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        dis1key.frameNStart = frameN  # exact frame index
        dis1key.tStart = t  # local t and not account for scr refresh
        dis1key.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(dis1key, 'tStartRefresh')  # time at next scr refresh
        dis1key.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(dis1key.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(dis1key.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if dis1key.status == STARTED and not waitOnFlip:
        theseKeys = dis1key.getKeys(keyList=['space'], waitRelease=False)
        _dis1key_allKeys.extend(theseKeys)
        if len(_dis1key_allKeys):
            dis1key.keys = _dis1key_allKeys[-1].name  # just the last key pressed
            dis1key.rt = _dis1key_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in InstructionsScreenComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "InstructionsScreen"-------
for thisComponent in InstructionsScreenComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('polygon_3.started', polygon_3.tStartRefresh)
thisExp.addData('polygon_3.stopped', polygon_3.tStopRefresh)
thisExp.addData('instruction.started', instruction.tStartRefresh)
thisExp.addData('instruction.stopped', instruction.tStopRefresh)
# check responses
if dis1key.keys in ['', [], None]:  # No response was made
    dis1key.keys = None
thisExp.addData('dis1key.keys',dis1key.keys)
if dis1key.keys != None:  # we had a response
    thisExp.addData('dis1key.rt', dis1key.rt)
thisExp.addData('dis1key.started', dis1key.tStartRefresh)
thisExp.addData('dis1key.stopped', dis1key.tStopRefresh)
thisExp.nextEntry()
# the Routine "InstructionsScreen" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
SupraTests = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('SupraliminalTest.xlsx'),
    seed=None, name='SupraTests')
thisExp.addLoop(SupraTests)  # add the loop to the experiment
thisSupraTest = SupraTests.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisSupraTest.rgb)
if thisSupraTest != None:
    for paramName in thisSupraTest:
        exec('{} = thisSupraTest[paramName]'.format(paramName))

for thisSupraTest in SupraTests:
    currentLoop = SupraTests
    # abbreviate parameter names if possible (e.g. rgb = thisSupraTest.rgb)
    if thisSupraTest != None:
        for paramName in thisSupraTest:
            exec('{} = thisSupraTest[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "SupraTest"-------
    continueRoutine = True
    # update component parameters for each repeat
    suptest.setText(TestSup)
    key_resp.keys = []
    key_resp.rt = []
    _key_resp_allKeys = []
    # keep track of which components have finished
    SupraTestComponents = [polygon_4, suptest, key_resp]
    for thisComponent in SupraTestComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    SupraTestClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "SupraTest"-------
    while continueRoutine:
        # get current time
        t = SupraTestClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=SupraTestClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *polygon_4* updates
        if polygon_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            polygon_4.frameNStart = frameN  # exact frame index
            polygon_4.tStart = t  # local t and not account for scr refresh
            polygon_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon_4, 'tStartRefresh')  # time at next scr refresh
            polygon_4.setAutoDraw(True)
        
        # *suptest* updates
        if suptest.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            suptest.frameNStart = frameN  # exact frame index
            suptest.tStart = t  # local t and not account for scr refresh
            suptest.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(suptest, 'tStartRefresh')  # time at next scr refresh
            suptest.setAutoDraw(True)
        
        # *key_resp* updates
        waitOnFlip = False
        if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp.frameNStart = frameN  # exact frame index
            key_resp.tStart = t  # local t and not account for scr refresh
            key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
            key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp.status == STARTED and not waitOnFlip:
            theseKeys = key_resp.getKeys(keyList=['o', 'n'], waitRelease=False)
            _key_resp_allKeys.extend(theseKeys)
            if len(_key_resp_allKeys):
                key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
                key_resp.rt = _key_resp_allKeys[-1].rt
                # was this correct?
                if (key_resp.keys == str(AnswerSup)) or (key_resp.keys == AnswerSup):
                    key_resp.corr = 1
                else:
                    key_resp.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in SupraTestComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "SupraTest"-------
    for thisComponent in SupraTestComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    SupraTests.addData('polygon_4.started', polygon_4.tStartRefresh)
    SupraTests.addData('polygon_4.stopped', polygon_4.tStopRefresh)
    SupraTests.addData('suptest.started', suptest.tStartRefresh)
    SupraTests.addData('suptest.stopped', suptest.tStopRefresh)
    # check responses
    if key_resp.keys in ['', [], None]:  # No response was made
        key_resp.keys = None
        # was no response the correct answer?!
        if str(AnswerSup).lower() == 'none':
           key_resp.corr = 1;  # correct non-response
        else:
           key_resp.corr = 0;  # failed to respond (incorrectly)
    # store data for SupraTests (TrialHandler)
    SupraTests.addData('key_resp.keys',key_resp.keys)
    SupraTests.addData('key_resp.corr', key_resp.corr)
    if key_resp.keys != None:  # we had a response
        SupraTests.addData('key_resp.rt', key_resp.rt)
    SupraTests.addData('key_resp.started', key_resp.tStartRefresh)
    SupraTests.addData('key_resp.stopped', key_resp.tStopRefresh)
    # the Routine "SupraTest" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'SupraTests'


# set up handler to look after randomisation of conditions etc
DistractorTrials = data.TrialHandler(nReps=5, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='DistractorTrials')
thisExp.addLoop(DistractorTrials)  # add the loop to the experiment
thisDistractorTrial = DistractorTrials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisDistractorTrial.rgb)
if thisDistractorTrial != None:
    for paramName in thisDistractorTrial:
        exec('{} = thisDistractorTrial[paramName]'.format(paramName))

for thisDistractorTrial in DistractorTrials:
    currentLoop = DistractorTrials
    # abbreviate parameter names if possible (e.g. rgb = thisDistractorTrial.rgb)
    if thisDistractorTrial != None:
        for paramName in thisDistractorTrial:
            exec('{} = thisDistractorTrial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "Phase2"-------
    continueRoutine = True
    # update component parameters for each repeat
    key_resp_2.keys = []
    key_resp_2.rt = []
    _key_resp_2_allKeys = []
    # keep track of which components have finished
    Phase2Components = [polygon_5, distractor1, key_resp_2]
    for thisComponent in Phase2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Phase2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Phase2"-------
    while continueRoutine:
        # get current time
        t = Phase2Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Phase2Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *polygon_5* updates
        if polygon_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            polygon_5.frameNStart = frameN  # exact frame index
            polygon_5.tStart = t  # local t and not account for scr refresh
            polygon_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon_5, 'tStartRefresh')  # time at next scr refresh
            polygon_5.setAutoDraw(True)
        
        # *distractor1* updates
        if distractor1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            distractor1.frameNStart = frameN  # exact frame index
            distractor1.tStart = t  # local t and not account for scr refresh
            distractor1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(distractor1, 'tStartRefresh')  # time at next scr refresh
            distractor1.setAutoDraw(True)
        
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
            theseKeys = key_resp_2.getKeys(keyList=['0'], waitRelease=False)
            _key_resp_2_allKeys.extend(theseKeys)
            if len(_key_resp_2_allKeys):
                key_resp_2.keys = _key_resp_2_allKeys[-1].name  # just the last key pressed
                key_resp_2.rt = _key_resp_2_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Phase2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Phase2"-------
    for thisComponent in Phase2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    DistractorTrials.addData('polygon_5.started', polygon_5.tStartRefresh)
    DistractorTrials.addData('polygon_5.stopped', polygon_5.tStopRefresh)
    DistractorTrials.addData('distractor1.started', distractor1.tStartRefresh)
    DistractorTrials.addData('distractor1.stopped', distractor1.tStopRefresh)
    # check responses
    if key_resp_2.keys in ['', [], None]:  # No response was made
        key_resp_2.keys = None
    DistractorTrials.addData('key_resp_2.keys',key_resp_2.keys)
    if key_resp_2.keys != None:  # we had a response
        DistractorTrials.addData('key_resp_2.rt', key_resp_2.rt)
    DistractorTrials.addData('key_resp_2.started', key_resp_2.tStartRefresh)
    DistractorTrials.addData('key_resp_2.stopped', key_resp_2.tStopRefresh)
    # the Routine "Phase2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 5 repeats of 'DistractorTrials'


# ------Prepare to start Routine "Instructions2"-------
continueRoutine = True
routineTimer.add(5.000000)
# update component parameters for each repeat
# keep track of which components have finished
Instructions2Components = [polygon_7, textphase2]
for thisComponent in Instructions2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Instructions2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Instructions2"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = Instructions2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Instructions2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *polygon_7* updates
    if polygon_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        polygon_7.frameNStart = frameN  # exact frame index
        polygon_7.tStart = t  # local t and not account for scr refresh
        polygon_7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(polygon_7, 'tStartRefresh')  # time at next scr refresh
        polygon_7.setAutoDraw(True)
    if polygon_7.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > polygon_7.tStartRefresh + 5-frameTolerance:
            # keep track of stop time/frame for later
            polygon_7.tStop = t  # not accounting for scr refresh
            polygon_7.frameNStop = frameN  # exact frame index
            win.timeOnFlip(polygon_7, 'tStopRefresh')  # time at next scr refresh
            polygon_7.setAutoDraw(False)
    
    # *textphase2* updates
    if textphase2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        textphase2.frameNStart = frameN  # exact frame index
        textphase2.tStart = t  # local t and not account for scr refresh
        textphase2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(textphase2, 'tStartRefresh')  # time at next scr refresh
        textphase2.setAutoDraw(True)
    if textphase2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > textphase2.tStartRefresh + 5-frameTolerance:
            # keep track of stop time/frame for later
            textphase2.tStop = t  # not accounting for scr refresh
            textphase2.frameNStop = frameN  # exact frame index
            win.timeOnFlip(textphase2, 'tStopRefresh')  # time at next scr refresh
            textphase2.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Instructions2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Instructions2"-------
for thisComponent in Instructions2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('polygon_7.started', polygon_7.tStartRefresh)
thisExp.addData('polygon_7.stopped', polygon_7.tStopRefresh)
thisExp.addData('textphase2.started', textphase2.tStartRefresh)
thisExp.addData('textphase2.stopped', textphase2.tStopRefresh)

# set up handler to look after randomisation of conditions etc
SubliTrials = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('SubliminalNameCue.xlsx'),
    seed=None, name='SubliTrials')
thisExp.addLoop(SubliTrials)  # add the loop to the experiment
thisSubliTrial = SubliTrials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisSubliTrial.rgb)
if thisSubliTrial != None:
    for paramName in thisSubliTrial:
        exec('{} = thisSubliTrial[paramName]'.format(paramName))

for thisSubliTrial in SubliTrials:
    currentLoop = SubliTrials
    # abbreviate parameter names if possible (e.g. rgb = thisSubliTrial.rgb)
    if thisSubliTrial != None:
        for paramName in thisSubliTrial:
            exec('{} = thisSubliTrial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "SubliStudy"-------
    continueRoutine = True
    routineTimer.add(3.300000)
    # update component parameters for each repeat
    ForenameSub.setText(NameSub)
    Cue.setText(CueSub)
    # keep track of which components have finished
    SubliStudyComponents = [polygon_6, ForenameSub, Mask1, Cue, Mask2, blank1]
    for thisComponent in SubliStudyComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    SubliStudyClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "SubliStudy"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = SubliStudyClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=SubliStudyClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *polygon_6* updates
        if polygon_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            polygon_6.frameNStart = frameN  # exact frame index
            polygon_6.tStart = t  # local t and not account for scr refresh
            polygon_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon_6, 'tStartRefresh')  # time at next scr refresh
            polygon_6.setAutoDraw(True)
        if polygon_6.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > polygon_6.tStartRefresh + 3.3-frameTolerance:
                # keep track of stop time/frame for later
                polygon_6.tStop = t  # not accounting for scr refresh
                polygon_6.frameNStop = frameN  # exact frame index
                win.timeOnFlip(polygon_6, 'tStopRefresh')  # time at next scr refresh
                polygon_6.setAutoDraw(False)
        
        # *ForenameSub* updates
        if ForenameSub.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ForenameSub.frameNStart = frameN  # exact frame index
            ForenameSub.tStart = t  # local t and not account for scr refresh
            ForenameSub.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ForenameSub, 'tStartRefresh')  # time at next scr refresh
            ForenameSub.setAutoDraw(True)
        if ForenameSub.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > ForenameSub.tStartRefresh + 1.2-frameTolerance:
                # keep track of stop time/frame for later
                ForenameSub.tStop = t  # not accounting for scr refresh
                ForenameSub.frameNStop = frameN  # exact frame index
                win.timeOnFlip(ForenameSub, 'tStopRefresh')  # time at next scr refresh
                ForenameSub.setAutoDraw(False)
        
        # *Mask1* updates
        if Mask1.status == NOT_STARTED and tThisFlip >= 1.2-frameTolerance:
            # keep track of start time/frame for later
            Mask1.frameNStart = frameN  # exact frame index
            Mask1.tStart = t  # local t and not account for scr refresh
            Mask1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Mask1, 'tStartRefresh')  # time at next scr refresh
            Mask1.setAutoDraw(True)
        if Mask1.status == STARTED:
            if frameN >= (Mask1.frameNStart + 4):
                # keep track of stop time/frame for later
                Mask1.tStop = t  # not accounting for scr refresh
                Mask1.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Mask1, 'tStopRefresh')  # time at next scr refresh
                Mask1.setAutoDraw(False)
        
        # *Cue* updates
        if Cue.status == NOT_STARTED and tThisFlip >= 1.266-frameTolerance:
            # keep track of start time/frame for later
            Cue.frameNStart = frameN  # exact frame index
            Cue.tStart = t  # local t and not account for scr refresh
            Cue.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Cue, 'tStartRefresh')  # time at next scr refresh
            Cue.setAutoDraw(True)
        if Cue.status == STARTED:
            if frameN >= (Cue.frameNStart + 2):
                # keep track of stop time/frame for later
                Cue.tStop = t  # not accounting for scr refresh
                Cue.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Cue, 'tStopRefresh')  # time at next scr refresh
                Cue.setAutoDraw(False)
        
        # *Mask2* updates
        if Mask2.status == NOT_STARTED and tThisFlip >= 1.3-frameTolerance:
            # keep track of start time/frame for later
            Mask2.frameNStart = frameN  # exact frame index
            Mask2.tStart = t  # local t and not account for scr refresh
            Mask2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Mask2, 'tStartRefresh')  # time at next scr refresh
            Mask2.setAutoDraw(True)
        if Mask2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Mask2.tStartRefresh + .250-frameTolerance:
                # keep track of stop time/frame for later
                Mask2.tStop = t  # not accounting for scr refresh
                Mask2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Mask2, 'tStopRefresh')  # time at next scr refresh
                Mask2.setAutoDraw(False)
        
        # *blank1* updates
        if blank1.status == NOT_STARTED and tThisFlip >= 1.55-frameTolerance:
            # keep track of start time/frame for later
            blank1.frameNStart = frameN  # exact frame index
            blank1.tStart = t  # local t and not account for scr refresh
            blank1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(blank1, 'tStartRefresh')  # time at next scr refresh
            blank1.setAutoDraw(True)
        if blank1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > blank1.tStartRefresh + 1.7-frameTolerance:
                # keep track of stop time/frame for later
                blank1.tStop = t  # not accounting for scr refresh
                blank1.frameNStop = frameN  # exact frame index
                win.timeOnFlip(blank1, 'tStopRefresh')  # time at next scr refresh
                blank1.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in SubliStudyComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "SubliStudy"-------
    for thisComponent in SubliStudyComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    SubliTrials.addData('polygon_6.started', polygon_6.tStartRefresh)
    SubliTrials.addData('polygon_6.stopped', polygon_6.tStopRefresh)
    SubliTrials.addData('ForenameSub.started', ForenameSub.tStartRefresh)
    SubliTrials.addData('ForenameSub.stopped', ForenameSub.tStopRefresh)
    SubliTrials.addData('Mask1.started', Mask1.tStartRefresh)
    SubliTrials.addData('Mask1.stopped', Mask1.tStopRefresh)
    SubliTrials.addData('Cue.started', Cue.tStartRefresh)
    SubliTrials.addData('Cue.stopped', Cue.tStopRefresh)
    SubliTrials.addData('Mask2.started', Mask2.tStartRefresh)
    SubliTrials.addData('Mask2.stopped', Mask2.tStopRefresh)
    SubliTrials.addData('blank1.started', blank1.tStartRefresh)
    SubliTrials.addData('blank1.stopped', blank1.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1 repeats of 'SubliTrials'


# ------Prepare to start Routine "InstructionsScreen"-------
continueRoutine = True
# update component parameters for each repeat
dis1key.keys = []
dis1key.rt = []
_dis1key_allKeys = []
# keep track of which components have finished
InstructionsScreenComponents = [polygon_3, instruction, dis1key]
for thisComponent in InstructionsScreenComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
InstructionsScreenClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "InstructionsScreen"-------
while continueRoutine:
    # get current time
    t = InstructionsScreenClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=InstructionsScreenClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *polygon_3* updates
    if polygon_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        polygon_3.frameNStart = frameN  # exact frame index
        polygon_3.tStart = t  # local t and not account for scr refresh
        polygon_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(polygon_3, 'tStartRefresh')  # time at next scr refresh
        polygon_3.setAutoDraw(True)
    
    # *instruction* updates
    if instruction.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instruction.frameNStart = frameN  # exact frame index
        instruction.tStart = t  # local t and not account for scr refresh
        instruction.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instruction, 'tStartRefresh')  # time at next scr refresh
        instruction.setAutoDraw(True)
    
    # *dis1key* updates
    waitOnFlip = False
    if dis1key.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        dis1key.frameNStart = frameN  # exact frame index
        dis1key.tStart = t  # local t and not account for scr refresh
        dis1key.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(dis1key, 'tStartRefresh')  # time at next scr refresh
        dis1key.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(dis1key.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(dis1key.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if dis1key.status == STARTED and not waitOnFlip:
        theseKeys = dis1key.getKeys(keyList=['space'], waitRelease=False)
        _dis1key_allKeys.extend(theseKeys)
        if len(_dis1key_allKeys):
            dis1key.keys = _dis1key_allKeys[-1].name  # just the last key pressed
            dis1key.rt = _dis1key_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in InstructionsScreenComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "InstructionsScreen"-------
for thisComponent in InstructionsScreenComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('polygon_3.started', polygon_3.tStartRefresh)
thisExp.addData('polygon_3.stopped', polygon_3.tStopRefresh)
thisExp.addData('instruction.started', instruction.tStartRefresh)
thisExp.addData('instruction.stopped', instruction.tStopRefresh)
# check responses
if dis1key.keys in ['', [], None]:  # No response was made
    dis1key.keys = None
thisExp.addData('dis1key.keys',dis1key.keys)
if dis1key.keys != None:  # we had a response
    thisExp.addData('dis1key.rt', dis1key.rt)
thisExp.addData('dis1key.started', dis1key.tStartRefresh)
thisExp.addData('dis1key.stopped', dis1key.tStopRefresh)
thisExp.nextEntry()
# the Routine "InstructionsScreen" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Distractor1"-------
continueRoutine = True
routineTimer.add(2.000000)
# update component parameters for each repeat
# keep track of which components have finished
Distractor1Components = [polygon_2, dis1]
for thisComponent in Distractor1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Distractor1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Distractor1"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = Distractor1Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Distractor1Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *polygon_2* updates
    if polygon_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        polygon_2.frameNStart = frameN  # exact frame index
        polygon_2.tStart = t  # local t and not account for scr refresh
        polygon_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(polygon_2, 'tStartRefresh')  # time at next scr refresh
        polygon_2.setAutoDraw(True)
    if polygon_2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > polygon_2.tStartRefresh + 2-frameTolerance:
            # keep track of stop time/frame for later
            polygon_2.tStop = t  # not accounting for scr refresh
            polygon_2.frameNStop = frameN  # exact frame index
            win.timeOnFlip(polygon_2, 'tStopRefresh')  # time at next scr refresh
            polygon_2.setAutoDraw(False)
    
    # *dis1* updates
    if dis1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        dis1.frameNStart = frameN  # exact frame index
        dis1.tStart = t  # local t and not account for scr refresh
        dis1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(dis1, 'tStartRefresh')  # time at next scr refresh
        dis1.setAutoDraw(True)
    if dis1.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > dis1.tStartRefresh + 2-frameTolerance:
            # keep track of stop time/frame for later
            dis1.tStop = t  # not accounting for scr refresh
            dis1.frameNStop = frameN  # exact frame index
            win.timeOnFlip(dis1, 'tStopRefresh')  # time at next scr refresh
            dis1.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Distractor1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Distractor1"-------
for thisComponent in Distractor1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('polygon_2.started', polygon_2.tStartRefresh)
thisExp.addData('polygon_2.stopped', polygon_2.tStopRefresh)
thisExp.addData('dis1.started', dis1.tStartRefresh)
thisExp.addData('dis1.stopped', dis1.tStopRefresh)

# set up handler to look after randomisation of conditions etc
SubliTests = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('SubliminalTest.xlsx'),
    seed=None, name='SubliTests')
thisExp.addLoop(SubliTests)  # add the loop to the experiment
thisSubliTest = SubliTests.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisSubliTest.rgb)
if thisSubliTest != None:
    for paramName in thisSubliTest:
        exec('{} = thisSubliTest[paramName]'.format(paramName))

for thisSubliTest in SubliTests:
    currentLoop = SubliTests
    # abbreviate parameter names if possible (e.g. rgb = thisSubliTest.rgb)
    if thisSubliTest != None:
        for paramName in thisSubliTest:
            exec('{} = thisSubliTest[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "SubliTest"-------
    continueRoutine = True
    # update component parameters for each repeat
    SubTest.setText(TestSub)
    key_resp_3.keys = []
    key_resp_3.rt = []
    _key_resp_3_allKeys = []
    # keep track of which components have finished
    SubliTestComponents = [polygon_8, SubTest, key_resp_3]
    for thisComponent in SubliTestComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    SubliTestClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "SubliTest"-------
    while continueRoutine:
        # get current time
        t = SubliTestClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=SubliTestClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *polygon_8* updates
        if polygon_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            polygon_8.frameNStart = frameN  # exact frame index
            polygon_8.tStart = t  # local t and not account for scr refresh
            polygon_8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon_8, 'tStartRefresh')  # time at next scr refresh
            polygon_8.setAutoDraw(True)
        
        # *SubTest* updates
        if SubTest.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            SubTest.frameNStart = frameN  # exact frame index
            SubTest.tStart = t  # local t and not account for scr refresh
            SubTest.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(SubTest, 'tStartRefresh')  # time at next scr refresh
            SubTest.setAutoDraw(True)
        
        # *key_resp_3* updates
        waitOnFlip = False
        if key_resp_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_3.frameNStart = frameN  # exact frame index
            key_resp_3.tStart = t  # local t and not account for scr refresh
            key_resp_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_3, 'tStartRefresh')  # time at next scr refresh
            key_resp_3.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_3.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_3.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_3.getKeys(keyList=['o', 'n'], waitRelease=False)
            _key_resp_3_allKeys.extend(theseKeys)
            if len(_key_resp_3_allKeys):
                key_resp_3.keys = _key_resp_3_allKeys[-1].name  # just the last key pressed
                key_resp_3.rt = _key_resp_3_allKeys[-1].rt
                # was this correct?
                if (key_resp_3.keys == str(AnswerSub)) or (key_resp_3.keys == AnswerSub):
                    key_resp_3.corr = 1
                else:
                    key_resp_3.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in SubliTestComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "SubliTest"-------
    for thisComponent in SubliTestComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    SubliTests.addData('polygon_8.started', polygon_8.tStartRefresh)
    SubliTests.addData('polygon_8.stopped', polygon_8.tStopRefresh)
    SubliTests.addData('SubTest.started', SubTest.tStartRefresh)
    SubliTests.addData('SubTest.stopped', SubTest.tStopRefresh)
    # check responses
    if key_resp_3.keys in ['', [], None]:  # No response was made
        key_resp_3.keys = None
        # was no response the correct answer?!
        if str(AnswerSub).lower() == 'none':
           key_resp_3.corr = 1;  # correct non-response
        else:
           key_resp_3.corr = 0;  # failed to respond (incorrectly)
    # store data for SubliTests (TrialHandler)
    SubliTests.addData('key_resp_3.keys',key_resp_3.keys)
    SubliTests.addData('key_resp_3.corr', key_resp_3.corr)
    if key_resp_3.keys != None:  # we had a response
        SubliTests.addData('key_resp_3.rt', key_resp_3.rt)
    SubliTests.addData('key_resp_3.started', key_resp_3.tStartRefresh)
    SubliTests.addData('key_resp_3.stopped', key_resp_3.tStopRefresh)
    # the Routine "SubliTest" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'SubliTests'


# ------Prepare to start Routine "EndScreen"-------
continueRoutine = True
routineTimer.add(4.000000)
# update component parameters for each repeat
# keep track of which components have finished
EndScreenComponents = [polygon_9, text]
for thisComponent in EndScreenComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
EndScreenClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "EndScreen"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = EndScreenClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=EndScreenClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *polygon_9* updates
    if polygon_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        polygon_9.frameNStart = frameN  # exact frame index
        polygon_9.tStart = t  # local t and not account for scr refresh
        polygon_9.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(polygon_9, 'tStartRefresh')  # time at next scr refresh
        polygon_9.setAutoDraw(True)
    if polygon_9.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > polygon_9.tStartRefresh + 4-frameTolerance:
            # keep track of stop time/frame for later
            polygon_9.tStop = t  # not accounting for scr refresh
            polygon_9.frameNStop = frameN  # exact frame index
            win.timeOnFlip(polygon_9, 'tStopRefresh')  # time at next scr refresh
            polygon_9.setAutoDraw(False)
    
    # *text* updates
    if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text.frameNStart = frameN  # exact frame index
        text.tStart = t  # local t and not account for scr refresh
        text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
        text.setAutoDraw(True)
    if text.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text.tStartRefresh + 4-frameTolerance:
            # keep track of stop time/frame for later
            text.tStop = t  # not accounting for scr refresh
            text.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text, 'tStopRefresh')  # time at next scr refresh
            text.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in EndScreenComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "EndScreen"-------
for thisComponent in EndScreenComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('polygon_9.started', polygon_9.tStartRefresh)
thisExp.addData('polygon_9.stopped', polygon_9.tStopRefresh)
thisExp.addData('text.started', text.tStartRefresh)
thisExp.addData('text.stopped', text.tStopRefresh)

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
