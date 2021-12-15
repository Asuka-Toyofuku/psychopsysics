#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.2.3),
    on Wed Dec 15 06:53:25 2021
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2021.2.3'
expName = 'myproject'  # from the Builder filename that created this script
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
    originPath='/Users/toyofukuasuka/Downloads/psychophysics/myexperiment/myproject_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=(1024, 768), fullscr=True, screen=0, 
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

# Setup eyetracking
ioDevice = ioConfig = ioSession = ioServer = eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "explanation"
explanationClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='Hello!\n\nPress “p” if the word has a positive meaning.\nPress “n” if the word has a negative meaning.\nPress “q” if the word has a neutral meaning.\n\nPress Space to continue.',
    font='Open Sans',
    pos=(0, 0), height=0.07, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp = keyboard.Keyboard()

# Initialize components for Routine "trial_ex"
trial_exClock = core.Clock()
text_4 = visual.TextStim(win=win, name='text_4',
    text='Let’s practise first.\n\nPress space to begin.',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_5 = keyboard.Keyboard()

# Initialize components for Routine "trial"
trialClock = core.Clock()
fixtation = visual.TextStim(win=win, name='fixtation',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
words = visual.TextStim(win=win, name='words',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
key_response = keyboard.Keyboard()

# Initialize components for Routine "part1"
part1Clock = core.Clock()
text_2 = visual.TextStim(win=win, name='text_2',
    text='PART 01\n\npress space to start.',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_4 = keyboard.Keyboard()

# Initialize components for Routine "trial"
trialClock = core.Clock()
fixtation = visual.TextStim(win=win, name='fixtation',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
words = visual.TextStim(win=win, name='words',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
key_response = keyboard.Keyboard()

# Initialize components for Routine "trial"
trialClock = core.Clock()
fixtation = visual.TextStim(win=win, name='fixtation',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
words = visual.TextStim(win=win, name='words',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
key_response = keyboard.Keyboard()

# Initialize components for Routine "part2"
part2Clock = core.Clock()
text_5 = visual.TextStim(win=win, name='text_5',
    text='PART 02\n\nPress space to begin.',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_6 = keyboard.Keyboard()

# Initialize components for Routine "trial_color"
trial_colorClock = core.Clock()
fix_2 = visual.TextStim(win=win, name='fix_2',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
word_2 = visual.TextStim(win=win, name='word_2',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
key_resp_2 = keyboard.Keyboard()

# Initialize components for Routine "trial_color"
trial_colorClock = core.Clock()
fix_2 = visual.TextStim(win=win, name='fix_2',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
word_2 = visual.TextStim(win=win, name='word_2',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
key_resp_2 = keyboard.Keyboard()

# Initialize components for Routine "ending"
endingClock = core.Clock()
text_3 = visual.TextStim(win=win, name='text_3',
    text='This is the end of the experiment.\nThank you so much.\n\nPress ‘space’ to end.',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_3 = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "explanation"-------
continueRoutine = True
# update component parameters for each repeat
key_resp.keys = []
key_resp.rt = []
_key_resp_allKeys = []
# keep track of which components have finished
explanationComponents = [text, key_resp]
for thisComponent in explanationComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
explanationClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "explanation"-------
while continueRoutine:
    # get current time
    t = explanationClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=explanationClock)
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
        theseKeys = key_resp.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_allKeys.extend(theseKeys)
        if len(_key_resp_allKeys):
            key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
            key_resp.rt = _key_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in explanationComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "explanation"-------
for thisComponent in explanationComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text.started', text.tStartRefresh)
thisExp.addData('text.stopped', text.tStopRefresh)
# check responses
if key_resp.keys in ['', [], None]:  # No response was made
    key_resp.keys = None
thisExp.addData('key_resp.keys',key_resp.keys)
if key_resp.keys != None:  # we had a response
    thisExp.addData('key_resp.rt', key_resp.rt)
thisExp.addData('key_resp.started', key_resp.tStartRefresh)
thisExp.addData('key_resp.stopped', key_resp.tStopRefresh)
thisExp.nextEntry()
# the Routine "explanation" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "trial_ex"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_5.keys = []
key_resp_5.rt = []
_key_resp_5_allKeys = []
# keep track of which components have finished
trial_exComponents = [text_4, key_resp_5]
for thisComponent in trial_exComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
trial_exClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "trial_ex"-------
while continueRoutine:
    # get current time
    t = trial_exClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=trial_exClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_4* updates
    if text_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_4.frameNStart = frameN  # exact frame index
        text_4.tStart = t  # local t and not account for scr refresh
        text_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_4, 'tStartRefresh')  # time at next scr refresh
        text_4.setAutoDraw(True)
    if text_4.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_4.tStartRefresh + 10.0-frameTolerance:
            # keep track of stop time/frame for later
            text_4.tStop = t  # not accounting for scr refresh
            text_4.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_4, 'tStopRefresh')  # time at next scr refresh
            text_4.setAutoDraw(False)
    
    # *key_resp_5* updates
    waitOnFlip = False
    if key_resp_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
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
    if key_resp_5.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_5.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_5_allKeys.extend(theseKeys)
        if len(_key_resp_5_allKeys):
            key_resp_5.keys = _key_resp_5_allKeys[-1].name  # just the last key pressed
            key_resp_5.rt = _key_resp_5_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in trial_exComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "trial_ex"-------
for thisComponent in trial_exComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_4.started', text_4.tStartRefresh)
thisExp.addData('text_4.stopped', text_4.tStopRefresh)
# check responses
if key_resp_5.keys in ['', [], None]:  # No response was made
    key_resp_5.keys = None
thisExp.addData('key_resp_5.keys',key_resp_5.keys)
if key_resp_5.keys != None:  # we had a response
    thisExp.addData('key_resp_5.rt', key_resp_5.rt)
thisExp.addData('key_resp_5.started', key_resp_5.tStartRefresh)
thisExp.addData('key_resp_5.stopped', key_resp_5.tStopRefresh)
thisExp.nextEntry()
# the Routine "trial_ex" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
practice01 = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('/Users/toyofukuasuka/psychophysics/trial_words 2.xlsx'),
    seed=None, name='practice01')
thisExp.addLoop(practice01)  # add the loop to the experiment
thisPractice01 = practice01.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisPractice01.rgb)
if thisPractice01 != None:
    for paramName in thisPractice01:
        exec('{} = thisPractice01[paramName]'.format(paramName))

for thisPractice01 in practice01:
    currentLoop = practice01
    # abbreviate parameter names if possible (e.g. rgb = thisPractice01.rgb)
    if thisPractice01 != None:
        for paramName in thisPractice01:
            exec('{} = thisPractice01[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "trial"-------
    continueRoutine = True
    routineTimer.add(2.600000)
    # update component parameters for each repeat
    fixtation.setText('+')
    words.setText(word)
    key_response.keys = []
    key_response.rt = []
    _key_response_allKeys = []
    # keep track of which components have finished
    trialComponents = [fixtation, words, key_response]
    for thisComponent in trialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "trial"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = trialClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=trialClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fixtation* updates
        if fixtation.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fixtation.frameNStart = frameN  # exact frame index
            fixtation.tStart = t  # local t and not account for scr refresh
            fixtation.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fixtation, 'tStartRefresh')  # time at next scr refresh
            fixtation.setAutoDraw(True)
        if fixtation.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fixtation.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                fixtation.tStop = t  # not accounting for scr refresh
                fixtation.frameNStop = frameN  # exact frame index
                win.timeOnFlip(fixtation, 'tStopRefresh')  # time at next scr refresh
                fixtation.setAutoDraw(False)
        
        # *words* updates
        if words.status == NOT_STARTED and tThisFlip >= 1.1-frameTolerance:
            # keep track of start time/frame for later
            words.frameNStart = frameN  # exact frame index
            words.tStart = t  # local t and not account for scr refresh
            words.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(words, 'tStartRefresh')  # time at next scr refresh
            words.setAutoDraw(True)
        if words.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > words.tStartRefresh + 1.5-frameTolerance:
                # keep track of stop time/frame for later
                words.tStop = t  # not accounting for scr refresh
                words.frameNStop = frameN  # exact frame index
                win.timeOnFlip(words, 'tStopRefresh')  # time at next scr refresh
                words.setAutoDraw(False)
        
        # *key_response* updates
        waitOnFlip = False
        if key_response.status == NOT_STARTED and tThisFlip >= 1.1-frameTolerance:
            # keep track of start time/frame for later
            key_response.frameNStart = frameN  # exact frame index
            key_response.tStart = t  # local t and not account for scr refresh
            key_response.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_response, 'tStartRefresh')  # time at next scr refresh
            key_response.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_response.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_response.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_response.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > key_response.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                key_response.tStop = t  # not accounting for scr refresh
                key_response.frameNStop = frameN  # exact frame index
                win.timeOnFlip(key_response, 'tStopRefresh')  # time at next scr refresh
                key_response.status = FINISHED
        if key_response.status == STARTED and not waitOnFlip:
            theseKeys = key_response.getKeys(keyList=['p', 'n', 'q'], waitRelease=False)
            _key_response_allKeys.extend(theseKeys)
            if len(_key_response_allKeys):
                key_response.keys = _key_response_allKeys[-1].name  # just the last key pressed
                key_response.rt = _key_response_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trial"-------
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    practice01.addData('fixtation.started', fixtation.tStartRefresh)
    practice01.addData('fixtation.stopped', fixtation.tStopRefresh)
    practice01.addData('words.started', words.tStartRefresh)
    practice01.addData('words.stopped', words.tStopRefresh)
    # check responses
    if key_response.keys in ['', [], None]:  # No response was made
        key_response.keys = None
    practice01.addData('key_response.keys',key_response.keys)
    if key_response.keys != None:  # we had a response
        practice01.addData('key_response.rt', key_response.rt)
    practice01.addData('key_response.started', key_response.tStartRefresh)
    practice01.addData('key_response.stopped', key_response.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'practice01'


# ------Prepare to start Routine "part1"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_4.keys = []
key_resp_4.rt = []
_key_resp_4_allKeys = []
# keep track of which components have finished
part1Components = [text_2, key_resp_4]
for thisComponent in part1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
part1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "part1"-------
while continueRoutine:
    # get current time
    t = part1Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=part1Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_2* updates
    if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_2.frameNStart = frameN  # exact frame index
        text_2.tStart = t  # local t and not account for scr refresh
        text_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
        text_2.setAutoDraw(True)
    if text_2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_2.tStartRefresh + 10.0-frameTolerance:
            # keep track of stop time/frame for later
            text_2.tStop = t  # not accounting for scr refresh
            text_2.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_2, 'tStopRefresh')  # time at next scr refresh
            text_2.setAutoDraw(False)
    
    # *key_resp_4* updates
    waitOnFlip = False
    if key_resp_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_4.frameNStart = frameN  # exact frame index
        key_resp_4.tStart = t  # local t and not account for scr refresh
        key_resp_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_4, 'tStartRefresh')  # time at next scr refresh
        key_resp_4.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_4.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_4.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_4.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_4.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_4_allKeys.extend(theseKeys)
        if len(_key_resp_4_allKeys):
            key_resp_4.keys = _key_resp_4_allKeys[-1].name  # just the last key pressed
            key_resp_4.rt = _key_resp_4_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in part1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "part1"-------
for thisComponent in part1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_2.started', text_2.tStartRefresh)
thisExp.addData('text_2.stopped', text_2.tStopRefresh)
# check responses
if key_resp_4.keys in ['', [], None]:  # No response was made
    key_resp_4.keys = None
thisExp.addData('key_resp_4.keys',key_resp_4.keys)
if key_resp_4.keys != None:  # we had a response
    thisExp.addData('key_resp_4.rt', key_resp_4.rt)
thisExp.addData('key_resp_4.started', key_resp_4.tStartRefresh)
thisExp.addData('key_resp_4.stopped', key_resp_4.tStopRefresh)
thisExp.nextEntry()
# the Routine "part1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trial_pos = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('/Users/toyofukuasuka/psychophysics/01postive_neutral_words.xlsx'),
    seed=None, name='trial_pos')
thisExp.addLoop(trial_pos)  # add the loop to the experiment
thisTrial_po = trial_pos.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_po.rgb)
if thisTrial_po != None:
    for paramName in thisTrial_po:
        exec('{} = thisTrial_po[paramName]'.format(paramName))

for thisTrial_po in trial_pos:
    currentLoop = trial_pos
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_po.rgb)
    if thisTrial_po != None:
        for paramName in thisTrial_po:
            exec('{} = thisTrial_po[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "trial"-------
    continueRoutine = True
    routineTimer.add(2.600000)
    # update component parameters for each repeat
    fixtation.setText('+')
    words.setText(word)
    key_response.keys = []
    key_response.rt = []
    _key_response_allKeys = []
    # keep track of which components have finished
    trialComponents = [fixtation, words, key_response]
    for thisComponent in trialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "trial"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = trialClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=trialClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fixtation* updates
        if fixtation.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fixtation.frameNStart = frameN  # exact frame index
            fixtation.tStart = t  # local t and not account for scr refresh
            fixtation.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fixtation, 'tStartRefresh')  # time at next scr refresh
            fixtation.setAutoDraw(True)
        if fixtation.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fixtation.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                fixtation.tStop = t  # not accounting for scr refresh
                fixtation.frameNStop = frameN  # exact frame index
                win.timeOnFlip(fixtation, 'tStopRefresh')  # time at next scr refresh
                fixtation.setAutoDraw(False)
        
        # *words* updates
        if words.status == NOT_STARTED and tThisFlip >= 1.1-frameTolerance:
            # keep track of start time/frame for later
            words.frameNStart = frameN  # exact frame index
            words.tStart = t  # local t and not account for scr refresh
            words.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(words, 'tStartRefresh')  # time at next scr refresh
            words.setAutoDraw(True)
        if words.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > words.tStartRefresh + 1.5-frameTolerance:
                # keep track of stop time/frame for later
                words.tStop = t  # not accounting for scr refresh
                words.frameNStop = frameN  # exact frame index
                win.timeOnFlip(words, 'tStopRefresh')  # time at next scr refresh
                words.setAutoDraw(False)
        
        # *key_response* updates
        waitOnFlip = False
        if key_response.status == NOT_STARTED and tThisFlip >= 1.1-frameTolerance:
            # keep track of start time/frame for later
            key_response.frameNStart = frameN  # exact frame index
            key_response.tStart = t  # local t and not account for scr refresh
            key_response.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_response, 'tStartRefresh')  # time at next scr refresh
            key_response.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_response.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_response.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_response.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > key_response.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                key_response.tStop = t  # not accounting for scr refresh
                key_response.frameNStop = frameN  # exact frame index
                win.timeOnFlip(key_response, 'tStopRefresh')  # time at next scr refresh
                key_response.status = FINISHED
        if key_response.status == STARTED and not waitOnFlip:
            theseKeys = key_response.getKeys(keyList=['p', 'n', 'q'], waitRelease=False)
            _key_response_allKeys.extend(theseKeys)
            if len(_key_response_allKeys):
                key_response.keys = _key_response_allKeys[-1].name  # just the last key pressed
                key_response.rt = _key_response_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trial"-------
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trial_pos.addData('fixtation.started', fixtation.tStartRefresh)
    trial_pos.addData('fixtation.stopped', fixtation.tStopRefresh)
    trial_pos.addData('words.started', words.tStartRefresh)
    trial_pos.addData('words.stopped', words.tStopRefresh)
    # check responses
    if key_response.keys in ['', [], None]:  # No response was made
        key_response.keys = None
    trial_pos.addData('key_response.keys',key_response.keys)
    if key_response.keys != None:  # we had a response
        trial_pos.addData('key_response.rt', key_response.rt)
    trial_pos.addData('key_response.started', key_response.tStartRefresh)
    trial_pos.addData('key_response.stopped', key_response.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trial_pos'


# set up handler to look after randomisation of conditions etc
trials_neg = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('/Users/toyofukuasuka/psychophysics/01negative_neutral_words.xlsx'),
    seed=None, name='trials_neg')
thisExp.addLoop(trials_neg)  # add the loop to the experiment
thisTrials_neg = trials_neg.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrials_neg.rgb)
if thisTrials_neg != None:
    for paramName in thisTrials_neg:
        exec('{} = thisTrials_neg[paramName]'.format(paramName))

for thisTrials_neg in trials_neg:
    currentLoop = trials_neg
    # abbreviate parameter names if possible (e.g. rgb = thisTrials_neg.rgb)
    if thisTrials_neg != None:
        for paramName in thisTrials_neg:
            exec('{} = thisTrials_neg[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "trial"-------
    continueRoutine = True
    routineTimer.add(2.600000)
    # update component parameters for each repeat
    fixtation.setText('+')
    words.setText(word)
    key_response.keys = []
    key_response.rt = []
    _key_response_allKeys = []
    # keep track of which components have finished
    trialComponents = [fixtation, words, key_response]
    for thisComponent in trialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "trial"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = trialClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=trialClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fixtation* updates
        if fixtation.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fixtation.frameNStart = frameN  # exact frame index
            fixtation.tStart = t  # local t and not account for scr refresh
            fixtation.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fixtation, 'tStartRefresh')  # time at next scr refresh
            fixtation.setAutoDraw(True)
        if fixtation.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fixtation.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                fixtation.tStop = t  # not accounting for scr refresh
                fixtation.frameNStop = frameN  # exact frame index
                win.timeOnFlip(fixtation, 'tStopRefresh')  # time at next scr refresh
                fixtation.setAutoDraw(False)
        
        # *words* updates
        if words.status == NOT_STARTED and tThisFlip >= 1.1-frameTolerance:
            # keep track of start time/frame for later
            words.frameNStart = frameN  # exact frame index
            words.tStart = t  # local t and not account for scr refresh
            words.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(words, 'tStartRefresh')  # time at next scr refresh
            words.setAutoDraw(True)
        if words.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > words.tStartRefresh + 1.5-frameTolerance:
                # keep track of stop time/frame for later
                words.tStop = t  # not accounting for scr refresh
                words.frameNStop = frameN  # exact frame index
                win.timeOnFlip(words, 'tStopRefresh')  # time at next scr refresh
                words.setAutoDraw(False)
        
        # *key_response* updates
        waitOnFlip = False
        if key_response.status == NOT_STARTED and tThisFlip >= 1.1-frameTolerance:
            # keep track of start time/frame for later
            key_response.frameNStart = frameN  # exact frame index
            key_response.tStart = t  # local t and not account for scr refresh
            key_response.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_response, 'tStartRefresh')  # time at next scr refresh
            key_response.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_response.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_response.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_response.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > key_response.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                key_response.tStop = t  # not accounting for scr refresh
                key_response.frameNStop = frameN  # exact frame index
                win.timeOnFlip(key_response, 'tStopRefresh')  # time at next scr refresh
                key_response.status = FINISHED
        if key_response.status == STARTED and not waitOnFlip:
            theseKeys = key_response.getKeys(keyList=['p', 'n', 'q'], waitRelease=False)
            _key_response_allKeys.extend(theseKeys)
            if len(_key_response_allKeys):
                key_response.keys = _key_response_allKeys[-1].name  # just the last key pressed
                key_response.rt = _key_response_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trial"-------
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_neg.addData('fixtation.started', fixtation.tStartRefresh)
    trials_neg.addData('fixtation.stopped', fixtation.tStopRefresh)
    trials_neg.addData('words.started', words.tStartRefresh)
    trials_neg.addData('words.stopped', words.tStopRefresh)
    # check responses
    if key_response.keys in ['', [], None]:  # No response was made
        key_response.keys = None
    trials_neg.addData('key_response.keys',key_response.keys)
    if key_response.keys != None:  # we had a response
        trials_neg.addData('key_response.rt', key_response.rt)
    trials_neg.addData('key_response.started', key_response.tStartRefresh)
    trials_neg.addData('key_response.stopped', key_response.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trials_neg'


# ------Prepare to start Routine "part2"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_6.keys = []
key_resp_6.rt = []
_key_resp_6_allKeys = []
# keep track of which components have finished
part2Components = [text_5, key_resp_6]
for thisComponent in part2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
part2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "part2"-------
while continueRoutine:
    # get current time
    t = part2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=part2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_5* updates
    if text_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_5.frameNStart = frameN  # exact frame index
        text_5.tStart = t  # local t and not account for scr refresh
        text_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_5, 'tStartRefresh')  # time at next scr refresh
        text_5.setAutoDraw(True)
    if text_5.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_5.tStartRefresh + 10.0-frameTolerance:
            # keep track of stop time/frame for later
            text_5.tStop = t  # not accounting for scr refresh
            text_5.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_5, 'tStopRefresh')  # time at next scr refresh
            text_5.setAutoDraw(False)
    
    # *key_resp_6* updates
    waitOnFlip = False
    if key_resp_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_6.frameNStart = frameN  # exact frame index
        key_resp_6.tStart = t  # local t and not account for scr refresh
        key_resp_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_6, 'tStartRefresh')  # time at next scr refresh
        key_resp_6.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_6.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_6.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_6.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_6.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_6_allKeys.extend(theseKeys)
        if len(_key_resp_6_allKeys):
            key_resp_6.keys = _key_resp_6_allKeys[-1].name  # just the last key pressed
            key_resp_6.rt = _key_resp_6_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in part2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "part2"-------
for thisComponent in part2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_5.started', text_5.tStartRefresh)
thisExp.addData('text_5.stopped', text_5.tStopRefresh)
# check responses
if key_resp_6.keys in ['', [], None]:  # No response was made
    key_resp_6.keys = None
thisExp.addData('key_resp_6.keys',key_resp_6.keys)
if key_resp_6.keys != None:  # we had a response
    thisExp.addData('key_resp_6.rt', key_resp_6.rt)
thisExp.addData('key_resp_6.started', key_resp_6.tStartRefresh)
thisExp.addData('key_resp_6.stopped', key_resp_6.tStopRefresh)
thisExp.nextEntry()
# the Routine "part2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trial_col_pos = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('/Users/toyofukuasuka/psychophysics/02postive_neutral_words.xlsx'),
    seed=None, name='trial_col_pos')
thisExp.addLoop(trial_col_pos)  # add the loop to the experiment
thisTrial_col_po = trial_col_pos.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_col_po.rgb)
if thisTrial_col_po != None:
    for paramName in thisTrial_col_po:
        exec('{} = thisTrial_col_po[paramName]'.format(paramName))

for thisTrial_col_po in trial_col_pos:
    currentLoop = trial_col_pos
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_col_po.rgb)
    if thisTrial_col_po != None:
        for paramName in thisTrial_col_po:
            exec('{} = thisTrial_col_po[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "trial_color"-------
    continueRoutine = True
    routineTimer.add(2.600000)
    # update component parameters for each repeat
    fix_2.setText('+')
    word_2.setColor(color_of_words, colorSpace='rgb')
    word_2.setContrast(1.0)
    word_2.setText(word)
    key_resp_2.keys = []
    key_resp_2.rt = []
    _key_resp_2_allKeys = []
    # keep track of which components have finished
    trial_colorComponents = [fix_2, word_2, key_resp_2]
    for thisComponent in trial_colorComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    trial_colorClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "trial_color"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = trial_colorClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=trial_colorClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fix_2* updates
        if fix_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fix_2.frameNStart = frameN  # exact frame index
            fix_2.tStart = t  # local t and not account for scr refresh
            fix_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fix_2, 'tStartRefresh')  # time at next scr refresh
            fix_2.setAutoDraw(True)
        if fix_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fix_2.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                fix_2.tStop = t  # not accounting for scr refresh
                fix_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(fix_2, 'tStopRefresh')  # time at next scr refresh
                fix_2.setAutoDraw(False)
        
        # *word_2* updates
        if word_2.status == NOT_STARTED and tThisFlip >= 1.1-frameTolerance:
            # keep track of start time/frame for later
            word_2.frameNStart = frameN  # exact frame index
            word_2.tStart = t  # local t and not account for scr refresh
            word_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(word_2, 'tStartRefresh')  # time at next scr refresh
            word_2.setAutoDraw(True)
        if word_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > word_2.tStartRefresh + 1.5-frameTolerance:
                # keep track of stop time/frame for later
                word_2.tStop = t  # not accounting for scr refresh
                word_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(word_2, 'tStopRefresh')  # time at next scr refresh
                word_2.setAutoDraw(False)
        
        # *key_resp_2* updates
        waitOnFlip = False
        if key_resp_2.status == NOT_STARTED and tThisFlip >= 1.1-frameTolerance:
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
        if key_resp_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > key_resp_2.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                key_resp_2.tStop = t  # not accounting for scr refresh
                key_resp_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(key_resp_2, 'tStopRefresh')  # time at next scr refresh
                key_resp_2.status = FINISHED
        if key_resp_2.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_2.getKeys(keyList=['p', 'n', 'q'], waitRelease=False)
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
        for thisComponent in trial_colorComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trial_color"-------
    for thisComponent in trial_colorComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trial_col_pos.addData('fix_2.started', fix_2.tStartRefresh)
    trial_col_pos.addData('fix_2.stopped', fix_2.tStopRefresh)
    trial_col_pos.addData('word_2.started', word_2.tStartRefresh)
    trial_col_pos.addData('word_2.stopped', word_2.tStopRefresh)
    # check responses
    if key_resp_2.keys in ['', [], None]:  # No response was made
        key_resp_2.keys = None
    trial_col_pos.addData('key_resp_2.keys',key_resp_2.keys)
    if key_resp_2.keys != None:  # we had a response
        trial_col_pos.addData('key_resp_2.rt', key_resp_2.rt)
    trial_col_pos.addData('key_resp_2.started', key_resp_2.tStartRefresh)
    trial_col_pos.addData('key_resp_2.stopped', key_resp_2.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trial_col_pos'


# set up handler to look after randomisation of conditions etc
trial_col_neg = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('/Users/toyofukuasuka/psychophysics/02negative_neutral_words .xlsx'),
    seed=None, name='trial_col_neg')
thisExp.addLoop(trial_col_neg)  # add the loop to the experiment
thisTrial_col_neg = trial_col_neg.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_col_neg.rgb)
if thisTrial_col_neg != None:
    for paramName in thisTrial_col_neg:
        exec('{} = thisTrial_col_neg[paramName]'.format(paramName))

for thisTrial_col_neg in trial_col_neg:
    currentLoop = trial_col_neg
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_col_neg.rgb)
    if thisTrial_col_neg != None:
        for paramName in thisTrial_col_neg:
            exec('{} = thisTrial_col_neg[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "trial_color"-------
    continueRoutine = True
    routineTimer.add(2.600000)
    # update component parameters for each repeat
    fix_2.setText('+')
    word_2.setColor(color_of_words, colorSpace='rgb')
    word_2.setContrast(1.0)
    word_2.setText(word)
    key_resp_2.keys = []
    key_resp_2.rt = []
    _key_resp_2_allKeys = []
    # keep track of which components have finished
    trial_colorComponents = [fix_2, word_2, key_resp_2]
    for thisComponent in trial_colorComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    trial_colorClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "trial_color"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = trial_colorClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=trial_colorClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fix_2* updates
        if fix_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fix_2.frameNStart = frameN  # exact frame index
            fix_2.tStart = t  # local t and not account for scr refresh
            fix_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fix_2, 'tStartRefresh')  # time at next scr refresh
            fix_2.setAutoDraw(True)
        if fix_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fix_2.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                fix_2.tStop = t  # not accounting for scr refresh
                fix_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(fix_2, 'tStopRefresh')  # time at next scr refresh
                fix_2.setAutoDraw(False)
        
        # *word_2* updates
        if word_2.status == NOT_STARTED and tThisFlip >= 1.1-frameTolerance:
            # keep track of start time/frame for later
            word_2.frameNStart = frameN  # exact frame index
            word_2.tStart = t  # local t and not account for scr refresh
            word_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(word_2, 'tStartRefresh')  # time at next scr refresh
            word_2.setAutoDraw(True)
        if word_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > word_2.tStartRefresh + 1.5-frameTolerance:
                # keep track of stop time/frame for later
                word_2.tStop = t  # not accounting for scr refresh
                word_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(word_2, 'tStopRefresh')  # time at next scr refresh
                word_2.setAutoDraw(False)
        
        # *key_resp_2* updates
        waitOnFlip = False
        if key_resp_2.status == NOT_STARTED and tThisFlip >= 1.1-frameTolerance:
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
        if key_resp_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > key_resp_2.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                key_resp_2.tStop = t  # not accounting for scr refresh
                key_resp_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(key_resp_2, 'tStopRefresh')  # time at next scr refresh
                key_resp_2.status = FINISHED
        if key_resp_2.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_2.getKeys(keyList=['p', 'n', 'q'], waitRelease=False)
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
        for thisComponent in trial_colorComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trial_color"-------
    for thisComponent in trial_colorComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trial_col_neg.addData('fix_2.started', fix_2.tStartRefresh)
    trial_col_neg.addData('fix_2.stopped', fix_2.tStopRefresh)
    trial_col_neg.addData('word_2.started', word_2.tStartRefresh)
    trial_col_neg.addData('word_2.stopped', word_2.tStopRefresh)
    # check responses
    if key_resp_2.keys in ['', [], None]:  # No response was made
        key_resp_2.keys = None
    trial_col_neg.addData('key_resp_2.keys',key_resp_2.keys)
    if key_resp_2.keys != None:  # we had a response
        trial_col_neg.addData('key_resp_2.rt', key_resp_2.rt)
    trial_col_neg.addData('key_resp_2.started', key_resp_2.tStartRefresh)
    trial_col_neg.addData('key_resp_2.stopped', key_resp_2.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trial_col_neg'


# ------Prepare to start Routine "ending"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_3.keys = []
key_resp_3.rt = []
_key_resp_3_allKeys = []
# keep track of which components have finished
endingComponents = [text_3, key_resp_3]
for thisComponent in endingComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
endingClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "ending"-------
while continueRoutine:
    # get current time
    t = endingClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=endingClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_3* updates
    if text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_3.frameNStart = frameN  # exact frame index
        text_3.tStart = t  # local t and not account for scr refresh
        text_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
        text_3.setAutoDraw(True)
    if text_3.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_3.tStartRefresh + 7.0-frameTolerance:
            # keep track of stop time/frame for later
            text_3.tStop = t  # not accounting for scr refresh
            text_3.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_3, 'tStopRefresh')  # time at next scr refresh
            text_3.setAutoDraw(False)
    
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
        theseKeys = key_resp_3.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_3_allKeys.extend(theseKeys)
        if len(_key_resp_3_allKeys):
            key_resp_3.keys = _key_resp_3_allKeys[-1].name  # just the last key pressed
            key_resp_3.rt = _key_resp_3_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in endingComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "ending"-------
for thisComponent in endingComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_3.started', text_3.tStartRefresh)
thisExp.addData('text_3.stopped', text_3.tStopRefresh)
# check responses
if key_resp_3.keys in ['', [], None]:  # No response was made
    key_resp_3.keys = None
thisExp.addData('key_resp_3.keys',key_resp_3.keys)
if key_resp_3.keys != None:  # we had a response
    thisExp.addData('key_resp_3.rt', key_resp_3.rt)
thisExp.addData('key_resp_3.started', key_resp_3.tStartRefresh)
thisExp.addData('key_resp_3.stopped', key_resp_3.tStopRefresh)
thisExp.nextEntry()
# the Routine "ending" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

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
