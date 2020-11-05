/**************** 
 * Xppsych Test *
 ****************/

// init psychoJS:
const psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: true,
  color: new util.Color([0, 0, 0]),
  units: 'height',
  waitBlanking: true
});

// store info about the experiment session:
let expName = 'XPPSYCH';  // from the Builder filename that created this script
let expInfo = {'participant': '', 'age': '', 'sex': '', 'occupation': ''};

// schedule the experiment:
psychoJS.schedule(psychoJS.gui.DlgFromDict({
  dictionary: expInfo,
  title: expName
}));

const flowScheduler = new Scheduler(psychoJS);
const dialogCancelScheduler = new Scheduler(psychoJS);
psychoJS.scheduleCondition(function() { return (psychoJS.gui.dialogComponent.button === 'OK'); }, flowScheduler, dialogCancelScheduler);

// flowScheduler gets run if the participants presses OK
flowScheduler.add(updateInfo); // add timeStamp
flowScheduler.add(experimentInit);
flowScheduler.add(WelcomeScreenRoutineBegin());
flowScheduler.add(WelcomeScreenRoutineEachFrame());
flowScheduler.add(WelcomeScreenRoutineEnd());
const SupraTrialsLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(SupraTrialsLoopBegin, SupraTrialsLoopScheduler);
flowScheduler.add(SupraTrialsLoopScheduler);
flowScheduler.add(SupraTrialsLoopEnd);
flowScheduler.add(Distractor1RoutineBegin());
flowScheduler.add(Distractor1RoutineEachFrame());
flowScheduler.add(Distractor1RoutineEnd());
flowScheduler.add(InstructionsScreenRoutineBegin());
flowScheduler.add(InstructionsScreenRoutineEachFrame());
flowScheduler.add(InstructionsScreenRoutineEnd());
const SupraTestsLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(SupraTestsLoopBegin, SupraTestsLoopScheduler);
flowScheduler.add(SupraTestsLoopScheduler);
flowScheduler.add(SupraTestsLoopEnd);
const DistractorTrialsLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(DistractorTrialsLoopBegin, DistractorTrialsLoopScheduler);
flowScheduler.add(DistractorTrialsLoopScheduler);
flowScheduler.add(DistractorTrialsLoopEnd);
flowScheduler.add(Instructions2RoutineBegin());
flowScheduler.add(Instructions2RoutineEachFrame());
flowScheduler.add(Instructions2RoutineEnd());
const SubliTrialsLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(SubliTrialsLoopBegin, SubliTrialsLoopScheduler);
flowScheduler.add(SubliTrialsLoopScheduler);
flowScheduler.add(SubliTrialsLoopEnd);
flowScheduler.add(InstructionsScreenRoutineBegin());
flowScheduler.add(InstructionsScreenRoutineEachFrame());
flowScheduler.add(InstructionsScreenRoutineEnd());
flowScheduler.add(Distractor1RoutineBegin());
flowScheduler.add(Distractor1RoutineEachFrame());
flowScheduler.add(Distractor1RoutineEnd());
const SubliTestsLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(SubliTestsLoopBegin, SubliTestsLoopScheduler);
flowScheduler.add(SubliTestsLoopScheduler);
flowScheduler.add(SubliTestsLoopEnd);
flowScheduler.add(EndScreenRoutineBegin());
flowScheduler.add(EndScreenRoutineEachFrame());
flowScheduler.add(EndScreenRoutineEnd());
flowScheduler.add(quitPsychoJS, '', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, '', false);

psychoJS.start({
  expName: expName,
  expInfo: expInfo,
  resources: [
    {'name': 'SubliminalTest.xlsx', 'path': 'SubliminalTest.xlsx'},
    {'name': 'SubliminalNameCue.xlsx', 'path': 'SubliminalNameCue.xlsx'},
    {'name': 'SupraliminalNameCue.xlsx', 'path': 'SupraliminalNameCue.xlsx'},
    {'name': 'SupraliminalTest.xlsx', 'path': 'SupraliminalTest.xlsx'}
  ]
});

psychoJS.experimentLogger.setLevel(core.Logger.ServerLevel.EXP);


var frameDur;
function updateInfo() {
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '2020.2.5';
  expInfo['OS'] = window.navigator.platform;

  // store frame rate of monitor if we can measure it successfully
  expInfo['frameRate'] = psychoJS.window.getActualFrameRate();
  if (typeof expInfo['frameRate'] !== 'undefined')
    frameDur = 1.0 / Math.round(expInfo['frameRate']);
  else
    frameDur = 1.0 / 60.0; // couldn't get a reliable measure so guess

  // add info from the URL:
  util.addInfoFromUrl(expInfo);
  
  return Scheduler.Event.NEXT;
}


var WelcomeScreenClock;
var polygon1;
var welcome;
var SupraStudyClock;
var polygon;
var ForenameSup;
var CueSup1;
var BlankSup;
var Distractor1Clock;
var polygon_2;
var dis1;
var InstructionsScreenClock;
var polygon_3;
var instruction;
var dis1key;
var SupraTestClock;
var polygon_4;
var suptest;
var key_resp;
var Phase2Clock;
var polygon_5;
var distractor1;
var key_resp_2;
var Instructions2Clock;
var polygon_7;
var textphase2;
var SubliStudyClock;
var polygon_6;
var ForenameSub;
var Mask1;
var Cue;
var Mask2;
var blank1;
var SubliTestClock;
var polygon_8;
var SubTest;
var key_resp_3;
var EndScreenClock;
var polygon_9;
var text;
var globalClock;
var routineTimer;
function experimentInit() {
  // Initialize components for Routine "WelcomeScreen"
  WelcomeScreenClock = new util.Clock();
  polygon1 = new visual.Rect ({
    win: psychoJS.window, name: 'polygon1', 
    width: [2, 2][0], height: [2, 2][1],
    ori: 0, pos: [0, 0],
    lineWidth: 1, lineColor: new util.Color([(- 1.0), (- 1.0), (- 1.0)]),
    fillColor: new util.Color([(- 1.0), (- 1.0), (- 1.0)]),
    opacity: 1, depth: 0, interpolate: true,
  });
  
  welcome = new visual.TextStim({
    win: psychoJS.window,
    name: 'welcome',
    text: 'WELCOME TO THIS EXPERIMENT!\n\nKindly read the series of forenames (items) as they appear on the screen.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  // Initialize components for Routine "SupraStudy"
  SupraStudyClock = new util.Clock();
  polygon = new visual.Rect ({
    win: psychoJS.window, name: 'polygon', 
    width: [2, 2][0], height: [2, 2][1],
    ori: 0, pos: [0, 0],
    lineWidth: 1, lineColor: new util.Color([(- 1.0), (- 1.0), (- 1.0)]),
    fillColor: new util.Color([(- 1.0), (- 1.0), (- 1.0)]),
    opacity: 1, depth: 0, interpolate: true,
  });
  
  ForenameSup = new visual.TextStim({
    win: psychoJS.window,
    name: 'ForenameSup',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  CueSup1 = new visual.TextStim({
    win: psychoJS.window,
    name: 'CueSup1',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -2.0 
  });
  
  BlankSup = new visual.TextStim({
    win: psychoJS.window,
    name: 'BlankSup',
    text: '.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.01,  wrapWidth: undefined, ori: 0,
    color: new util.Color([(- 1.0), (- 1.0), (- 1.0)]),  opacity: 1,
    depth: -3.0 
  });
  
  // Initialize components for Routine "Distractor1"
  Distractor1Clock = new util.Clock();
  polygon_2 = new visual.Rect ({
    win: psychoJS.window, name: 'polygon_2', 
    width: [2, 2][0], height: [2, 2][1],
    ori: 0, pos: [0, 0],
    lineWidth: 1, lineColor: new util.Color([(- 1.0), (- 1.0), (- 1.0)]),
    fillColor: new util.Color([(- 1.0), (- 1.0), (- 1.0)]),
    opacity: 1, depth: 0, interpolate: true,
  });
  
  dis1 = new visual.TextStim({
    win: psychoJS.window,
    name: 'dis1',
    text: '.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color([(- 1.0), (- 1.0), (- 1.0)]),  opacity: 1,
    depth: -1.0 
  });
  
  // Initialize components for Routine "InstructionsScreen"
  InstructionsScreenClock = new util.Clock();
  polygon_3 = new visual.Rect ({
    win: psychoJS.window, name: 'polygon_3', 
    width: [2, 2][0], height: [2, 2][1],
    ori: 0, pos: [0, 0],
    lineWidth: 1, lineColor: new util.Color([(- 1.0), (- 1.0), (- 1.0)]),
    fillColor: new util.Color([(- 1.0), (- 1.0), (- 1.0)]),
    opacity: 1, depth: 0, interpolate: true,
  });
  
  instruction = new visual.TextStim({
    win: psychoJS.window,
    name: 'instruction',
    text: 'The forenames (items) you read a while ago will reappear with other forenames not presented earlier. Determine whether the item is old (shown in the study phase) by pressing "O" or new (not shown in the study phase) by pressing "N".\n\n"O" Key - Old (present in the study phase)\n"N" Key - New (not present in the study phase)\n\nPress the spacebar to proceed.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  dis1key = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "SupraTest"
  SupraTestClock = new util.Clock();
  polygon_4 = new visual.Rect ({
    win: psychoJS.window, name: 'polygon_4', 
    width: [2, 2][0], height: [2, 2][1],
    ori: 0, pos: [0, 0],
    lineWidth: 1, lineColor: new util.Color([(- 1.0), (- 1.0), (- 1.0)]),
    fillColor: new util.Color([(- 1.0), (- 1.0), (- 1.0)]),
    opacity: 1, depth: 0, interpolate: true,
  });
  
  suptest = new visual.TextStim({
    win: psychoJS.window,
    name: 'suptest',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  key_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "Phase2"
  Phase2Clock = new util.Clock();
  polygon_5 = new visual.Rect ({
    win: psychoJS.window, name: 'polygon_5', 
    width: [2, 2][0], height: [2, 2][1],
    ori: 0, pos: [0, 0],
    lineWidth: 1, lineColor: new util.Color([(- 1.0), (- 1.0), (- 1.0)]),
    fillColor: new util.Color([(- 1.0), (- 1.0), (- 1.0)]),
    opacity: 1, depth: 0, interpolate: true,
  });
  
  distractor1 = new visual.TextStim({
    win: psychoJS.window,
    name: 'distractor1',
    text: 'What is 0 x 0 = ?',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  key_resp_2 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "Instructions2"
  Instructions2Clock = new util.Clock();
  polygon_7 = new visual.Rect ({
    win: psychoJS.window, name: 'polygon_7', 
    width: [2, 2][0], height: [2, 2][1],
    ori: 0, pos: [0, 0],
    lineWidth: 1, lineColor: new util.Color([(- 1.0), (- 1.0), (- 1.0)]),
    fillColor: new util.Color([(- 1.0), (- 1.0), (- 1.0)]),
    opacity: 1, depth: 0, interpolate: true,
  });
  
  textphase2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'textphase2',
    text: 'Kindly read the series of forenames (items) as they appear on the screen.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  // Initialize components for Routine "SubliStudy"
  SubliStudyClock = new util.Clock();
  polygon_6 = new visual.Rect ({
    win: psychoJS.window, name: 'polygon_6', 
    width: [2, 2][0], height: [2, 2][1],
    ori: 0, pos: [0, 0],
    lineWidth: 1, lineColor: new util.Color([(- 1.0), (- 1.0), (- 1.0)]),
    fillColor: new util.Color([(- 1.0), (- 1.0), (- 1.0)]),
    opacity: 1, depth: 0, interpolate: true,
  });
  
  ForenameSub = new visual.TextStim({
    win: psychoJS.window,
    name: 'ForenameSub',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  Mask1 = new visual.TextStim({
    win: psychoJS.window,
    name: 'Mask1',
    text: '###########',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -2.0 
  });
  
  Cue = new visual.TextStim({
    win: psychoJS.window,
    name: 'Cue',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -3.0 
  });
  
  Mask2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'Mask2',
    text: '###########',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -4.0 
  });
  
  blank1 = new visual.TextStim({
    win: psychoJS.window,
    name: 'blank1',
    text: '.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color([(- 1.0), (- 1.0), (- 1.0)]),  opacity: 1,
    depth: -5.0 
  });
  
  // Initialize components for Routine "InstructionsScreen"
  InstructionsScreenClock = new util.Clock();
  polygon_3 = new visual.Rect ({
    win: psychoJS.window, name: 'polygon_3', 
    width: [2, 2][0], height: [2, 2][1],
    ori: 0, pos: [0, 0],
    lineWidth: 1, lineColor: new util.Color([(- 1.0), (- 1.0), (- 1.0)]),
    fillColor: new util.Color([(- 1.0), (- 1.0), (- 1.0)]),
    opacity: 1, depth: 0, interpolate: true,
  });
  
  instruction = new visual.TextStim({
    win: psychoJS.window,
    name: 'instruction',
    text: 'The forenames (items) you read a while ago will reappear with other forenames not presented earlier. Determine whether the item is old (shown in the study phase) by pressing "O" or new (not shown in the study phase) by pressing "N".\n\n"O" Key - Old (present in the study phase)\n"N" Key - New (not present in the study phase)\n\nPress the spacebar to proceed.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  dis1key = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "Distractor1"
  Distractor1Clock = new util.Clock();
  polygon_2 = new visual.Rect ({
    win: psychoJS.window, name: 'polygon_2', 
    width: [2, 2][0], height: [2, 2][1],
    ori: 0, pos: [0, 0],
    lineWidth: 1, lineColor: new util.Color([(- 1.0), (- 1.0), (- 1.0)]),
    fillColor: new util.Color([(- 1.0), (- 1.0), (- 1.0)]),
    opacity: 1, depth: 0, interpolate: true,
  });
  
  dis1 = new visual.TextStim({
    win: psychoJS.window,
    name: 'dis1',
    text: '.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color([(- 1.0), (- 1.0), (- 1.0)]),  opacity: 1,
    depth: -1.0 
  });
  
  // Initialize components for Routine "SubliTest"
  SubliTestClock = new util.Clock();
  polygon_8 = new visual.Rect ({
    win: psychoJS.window, name: 'polygon_8', 
    width: [2, 2][0], height: [2, 2][1],
    ori: 0, pos: [0, 0],
    lineWidth: 1, lineColor: new util.Color([(- 1.0), (- 1.0), (- 1.0)]),
    fillColor: new util.Color([(- 1.0), (- 1.0), (- 1.0)]),
    opacity: 1, depth: 0, interpolate: true,
  });
  
  SubTest = new visual.TextStim({
    win: psychoJS.window,
    name: 'SubTest',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  key_resp_3 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "EndScreen"
  EndScreenClock = new util.Clock();
  polygon_9 = new visual.Rect ({
    win: psychoJS.window, name: 'polygon_9', 
    width: [2, 2][0], height: [2, 2][1],
    ori: 0, pos: [0, 0],
    lineWidth: 1, lineColor: new util.Color([(- 1.0), (- 1.0), (- 1.0)]),
    fillColor: new util.Color([(- 1.0), (- 1.0), (- 1.0)]),
    opacity: 1, depth: 0, interpolate: true,
  });
  
  text = new visual.TextStim({
    win: psychoJS.window,
    name: 'text',
    text: 'END OF EXPERIMENT\n\nThank you for participating!',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}


var t;
var frameN;
var WelcomeScreenComponents;
function WelcomeScreenRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'WelcomeScreen'-------
    t = 0;
    WelcomeScreenClock.reset(); // clock
    frameN = -1;
    routineTimer.add(7.000000);
    // update component parameters for each repeat
    // keep track of which components have finished
    WelcomeScreenComponents = [];
    WelcomeScreenComponents.push(polygon1);
    WelcomeScreenComponents.push(welcome);
    
    WelcomeScreenComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
  };
}


var frameRemains;
var continueRoutine;
function WelcomeScreenRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'WelcomeScreen'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = WelcomeScreenClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *polygon1* updates
    if (t >= 0.0 && polygon1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      polygon1.tStart = t;  // (not accounting for frame time here)
      polygon1.frameNStart = frameN;  // exact frame index
      
      polygon1.setAutoDraw(true);
    }

    frameRemains = 0.0 + 7 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if ((polygon1.status === PsychoJS.Status.STARTED || polygon1.status === PsychoJS.Status.FINISHED) && t >= frameRemains) {
      polygon1.setAutoDraw(false);
    }
    
    // *welcome* updates
    if (t >= 0.0 && welcome.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      welcome.tStart = t;  // (not accounting for frame time here)
      welcome.frameNStart = frameN;  // exact frame index
      
      welcome.setAutoDraw(true);
    }

    frameRemains = 0.0 + 7 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if ((welcome.status === PsychoJS.Status.STARTED || welcome.status === PsychoJS.Status.FINISHED) && t >= frameRemains) {
      welcome.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    WelcomeScreenComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function WelcomeScreenRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'WelcomeScreen'-------
    WelcomeScreenComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    return Scheduler.Event.NEXT;
  };
}


var SupraTrials;
var currentLoop;
function SupraTrialsLoopBegin(SupraTrialsLoopScheduler) {
  // set up handler to look after randomisation of conditions etc
  SupraTrials = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.RANDOM,
    extraInfo: expInfo, originPath: undefined,
    trialList: 'SupraliminalNameCue.xlsx',
    seed: undefined, name: 'SupraTrials'
  });
  psychoJS.experiment.addLoop(SupraTrials); // add the loop to the experiment
  currentLoop = SupraTrials;  // we're now the current loop

  // Schedule all the trials in the trialList:
  SupraTrials.forEach(function() {
    const snapshot = SupraTrials.getSnapshot();

    SupraTrialsLoopScheduler.add(importConditions(snapshot));
    SupraTrialsLoopScheduler.add(SupraStudyRoutineBegin(snapshot));
    SupraTrialsLoopScheduler.add(SupraStudyRoutineEachFrame(snapshot));
    SupraTrialsLoopScheduler.add(SupraStudyRoutineEnd(snapshot));
    SupraTrialsLoopScheduler.add(endLoopIteration(SupraTrialsLoopScheduler, snapshot));
  });

  return Scheduler.Event.NEXT;
}


function SupraTrialsLoopEnd() {
  psychoJS.experiment.removeLoop(SupraTrials);

  return Scheduler.Event.NEXT;
}


var SupraTests;
function SupraTestsLoopBegin(SupraTestsLoopScheduler) {
  // set up handler to look after randomisation of conditions etc
  SupraTests = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.RANDOM,
    extraInfo: expInfo, originPath: undefined,
    trialList: 'SupraliminalTest.xlsx',
    seed: undefined, name: 'SupraTests'
  });
  psychoJS.experiment.addLoop(SupraTests); // add the loop to the experiment
  currentLoop = SupraTests;  // we're now the current loop

  // Schedule all the trials in the trialList:
  SupraTests.forEach(function() {
    const snapshot = SupraTests.getSnapshot();

    SupraTestsLoopScheduler.add(importConditions(snapshot));
    SupraTestsLoopScheduler.add(SupraTestRoutineBegin(snapshot));
    SupraTestsLoopScheduler.add(SupraTestRoutineEachFrame(snapshot));
    SupraTestsLoopScheduler.add(SupraTestRoutineEnd(snapshot));
    SupraTestsLoopScheduler.add(endLoopIteration(SupraTestsLoopScheduler, snapshot));
  });

  return Scheduler.Event.NEXT;
}


function SupraTestsLoopEnd() {
  psychoJS.experiment.removeLoop(SupraTests);

  return Scheduler.Event.NEXT;
}


var DistractorTrials;
function DistractorTrialsLoopBegin(DistractorTrialsLoopScheduler) {
  // set up handler to look after randomisation of conditions etc
  DistractorTrials = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 5, method: TrialHandler.Method.RANDOM,
    extraInfo: expInfo, originPath: undefined,
    trialList: undefined,
    seed: undefined, name: 'DistractorTrials'
  });
  psychoJS.experiment.addLoop(DistractorTrials); // add the loop to the experiment
  currentLoop = DistractorTrials;  // we're now the current loop

  // Schedule all the trials in the trialList:
  DistractorTrials.forEach(function() {
    const snapshot = DistractorTrials.getSnapshot();

    DistractorTrialsLoopScheduler.add(importConditions(snapshot));
    DistractorTrialsLoopScheduler.add(Phase2RoutineBegin(snapshot));
    DistractorTrialsLoopScheduler.add(Phase2RoutineEachFrame(snapshot));
    DistractorTrialsLoopScheduler.add(Phase2RoutineEnd(snapshot));
    DistractorTrialsLoopScheduler.add(endLoopIteration(DistractorTrialsLoopScheduler, snapshot));
  });

  return Scheduler.Event.NEXT;
}


function DistractorTrialsLoopEnd() {
  psychoJS.experiment.removeLoop(DistractorTrials);

  return Scheduler.Event.NEXT;
}


var SubliTrials;
function SubliTrialsLoopBegin(SubliTrialsLoopScheduler) {
  // set up handler to look after randomisation of conditions etc
  SubliTrials = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.RANDOM,
    extraInfo: expInfo, originPath: undefined,
    trialList: 'SubliminalNameCue.xlsx',
    seed: undefined, name: 'SubliTrials'
  });
  psychoJS.experiment.addLoop(SubliTrials); // add the loop to the experiment
  currentLoop = SubliTrials;  // we're now the current loop

  // Schedule all the trials in the trialList:
  SubliTrials.forEach(function() {
    const snapshot = SubliTrials.getSnapshot();

    SubliTrialsLoopScheduler.add(importConditions(snapshot));
    SubliTrialsLoopScheduler.add(SubliStudyRoutineBegin(snapshot));
    SubliTrialsLoopScheduler.add(SubliStudyRoutineEachFrame(snapshot));
    SubliTrialsLoopScheduler.add(SubliStudyRoutineEnd(snapshot));
    SubliTrialsLoopScheduler.add(endLoopIteration(SubliTrialsLoopScheduler, snapshot));
  });

  return Scheduler.Event.NEXT;
}


function SubliTrialsLoopEnd() {
  psychoJS.experiment.removeLoop(SubliTrials);

  return Scheduler.Event.NEXT;
}


var SubliTests;
function SubliTestsLoopBegin(SubliTestsLoopScheduler) {
  // set up handler to look after randomisation of conditions etc
  SubliTests = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.RANDOM,
    extraInfo: expInfo, originPath: undefined,
    trialList: 'SubliminalTest.xlsx',
    seed: undefined, name: 'SubliTests'
  });
  psychoJS.experiment.addLoop(SubliTests); // add the loop to the experiment
  currentLoop = SubliTests;  // we're now the current loop

  // Schedule all the trials in the trialList:
  SubliTests.forEach(function() {
    const snapshot = SubliTests.getSnapshot();

    SubliTestsLoopScheduler.add(importConditions(snapshot));
    SubliTestsLoopScheduler.add(SubliTestRoutineBegin(snapshot));
    SubliTestsLoopScheduler.add(SubliTestRoutineEachFrame(snapshot));
    SubliTestsLoopScheduler.add(SubliTestRoutineEnd(snapshot));
    SubliTestsLoopScheduler.add(endLoopIteration(SubliTestsLoopScheduler, snapshot));
  });

  return Scheduler.Event.NEXT;
}


function SubliTestsLoopEnd() {
  psychoJS.experiment.removeLoop(SubliTests);

  return Scheduler.Event.NEXT;
}


var SupraStudyComponents;
function SupraStudyRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'SupraStudy'-------
    t = 0;
    SupraStudyClock.reset(); // clock
    frameN = -1;
    routineTimer.add(3.400000);
    // update component parameters for each repeat
    ForenameSup.setText(NameSup);
    CueSup1.setText(CueSup);
    // keep track of which components have finished
    SupraStudyComponents = [];
    SupraStudyComponents.push(polygon);
    SupraStudyComponents.push(ForenameSup);
    SupraStudyComponents.push(CueSup1);
    SupraStudyComponents.push(BlankSup);
    
    SupraStudyComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
  };
}


function SupraStudyRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'SupraStudy'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = SupraStudyClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *polygon* updates
    if (t >= 0.0 && polygon.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      polygon.tStart = t;  // (not accounting for frame time here)
      polygon.frameNStart = frameN;  // exact frame index
      
      polygon.setAutoDraw(true);
    }

    frameRemains = 0.0 + 3.4 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if ((polygon.status === PsychoJS.Status.STARTED || polygon.status === PsychoJS.Status.FINISHED) && t >= frameRemains) {
      polygon.setAutoDraw(false);
    }
    
    // *ForenameSup* updates
    if (t >= 0.0 && ForenameSup.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      ForenameSup.tStart = t;  // (not accounting for frame time here)
      ForenameSup.frameNStart = frameN;  // exact frame index
      
      ForenameSup.setAutoDraw(true);
    }

    frameRemains = 0.0 + 1.2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if ((ForenameSup.status === PsychoJS.Status.STARTED || ForenameSup.status === PsychoJS.Status.FINISHED) && t >= frameRemains) {
      ForenameSup.setAutoDraw(false);
    }
    
    // *CueSup1* updates
    if (t >= 1.2 && CueSup1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      CueSup1.tStart = t;  // (not accounting for frame time here)
      CueSup1.frameNStart = frameN;  // exact frame index
      
      CueSup1.setAutoDraw(true);
    }

    frameRemains = 1.2 + 1.2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if ((CueSup1.status === PsychoJS.Status.STARTED || CueSup1.status === PsychoJS.Status.FINISHED) && t >= frameRemains) {
      CueSup1.setAutoDraw(false);
    }
    
    // *BlankSup* updates
    if (t >= 2.4 && BlankSup.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      BlankSup.tStart = t;  // (not accounting for frame time here)
      BlankSup.frameNStart = frameN;  // exact frame index
      
      BlankSup.setAutoDraw(true);
    }

    frameRemains = 2.4 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if ((BlankSup.status === PsychoJS.Status.STARTED || BlankSup.status === PsychoJS.Status.FINISHED) && t >= frameRemains) {
      BlankSup.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    SupraStudyComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function SupraStudyRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'SupraStudy'-------
    SupraStudyComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    return Scheduler.Event.NEXT;
  };
}


var Distractor1Components;
function Distractor1RoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'Distractor1'-------
    t = 0;
    Distractor1Clock.reset(); // clock
    frameN = -1;
    routineTimer.add(2.000000);
    // update component parameters for each repeat
    // keep track of which components have finished
    Distractor1Components = [];
    Distractor1Components.push(polygon_2);
    Distractor1Components.push(dis1);
    
    Distractor1Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
  };
}


function Distractor1RoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'Distractor1'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = Distractor1Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *polygon_2* updates
    if (t >= 0.0 && polygon_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      polygon_2.tStart = t;  // (not accounting for frame time here)
      polygon_2.frameNStart = frameN;  // exact frame index
      
      polygon_2.setAutoDraw(true);
    }

    frameRemains = 0.0 + 2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if ((polygon_2.status === PsychoJS.Status.STARTED || polygon_2.status === PsychoJS.Status.FINISHED) && t >= frameRemains) {
      polygon_2.setAutoDraw(false);
    }
    
    // *dis1* updates
    if (t >= 0.0 && dis1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      dis1.tStart = t;  // (not accounting for frame time here)
      dis1.frameNStart = frameN;  // exact frame index
      
      dis1.setAutoDraw(true);
    }

    frameRemains = 0.0 + 2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if ((dis1.status === PsychoJS.Status.STARTED || dis1.status === PsychoJS.Status.FINISHED) && t >= frameRemains) {
      dis1.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    Distractor1Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function Distractor1RoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'Distractor1'-------
    Distractor1Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    return Scheduler.Event.NEXT;
  };
}


var _dis1key_allKeys;
var InstructionsScreenComponents;
function InstructionsScreenRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'InstructionsScreen'-------
    t = 0;
    InstructionsScreenClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    dis1key.keys = undefined;
    dis1key.rt = undefined;
    _dis1key_allKeys = [];
    // keep track of which components have finished
    InstructionsScreenComponents = [];
    InstructionsScreenComponents.push(polygon_3);
    InstructionsScreenComponents.push(instruction);
    InstructionsScreenComponents.push(dis1key);
    
    InstructionsScreenComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
  };
}


function InstructionsScreenRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'InstructionsScreen'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = InstructionsScreenClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *polygon_3* updates
    if (t >= 0.0 && polygon_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      polygon_3.tStart = t;  // (not accounting for frame time here)
      polygon_3.frameNStart = frameN;  // exact frame index
      
      polygon_3.setAutoDraw(true);
    }

    
    // *instruction* updates
    if (t >= 0.0 && instruction.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      instruction.tStart = t;  // (not accounting for frame time here)
      instruction.frameNStart = frameN;  // exact frame index
      
      instruction.setAutoDraw(true);
    }

    
    // *dis1key* updates
    if (t >= 0.0 && dis1key.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      dis1key.tStart = t;  // (not accounting for frame time here)
      dis1key.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { dis1key.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { dis1key.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { dis1key.clearEvents(); });
    }

    if (dis1key.status === PsychoJS.Status.STARTED) {
      let theseKeys = dis1key.getKeys({keyList: ['space'], waitRelease: false});
      _dis1key_allKeys = _dis1key_allKeys.concat(theseKeys);
      if (_dis1key_allKeys.length > 0) {
        dis1key.keys = _dis1key_allKeys[_dis1key_allKeys.length - 1].name;  // just the last key pressed
        dis1key.rt = _dis1key_allKeys[_dis1key_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    InstructionsScreenComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function InstructionsScreenRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'InstructionsScreen'-------
    InstructionsScreenComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('dis1key.keys', dis1key.keys);
    if (typeof dis1key.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('dis1key.rt', dis1key.rt);
        routineTimer.reset();
        }
    
    dis1key.stop();
    // the Routine "InstructionsScreen" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _key_resp_allKeys;
var SupraTestComponents;
function SupraTestRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'SupraTest'-------
    t = 0;
    SupraTestClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    suptest.setText(TestSup);
    key_resp.keys = undefined;
    key_resp.rt = undefined;
    _key_resp_allKeys = [];
    // keep track of which components have finished
    SupraTestComponents = [];
    SupraTestComponents.push(polygon_4);
    SupraTestComponents.push(suptest);
    SupraTestComponents.push(key_resp);
    
    SupraTestComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
  };
}


function SupraTestRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'SupraTest'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = SupraTestClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *polygon_4* updates
    if (t >= 0.0 && polygon_4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      polygon_4.tStart = t;  // (not accounting for frame time here)
      polygon_4.frameNStart = frameN;  // exact frame index
      
      polygon_4.setAutoDraw(true);
    }

    
    // *suptest* updates
    if (t >= 0.0 && suptest.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      suptest.tStart = t;  // (not accounting for frame time here)
      suptest.frameNStart = frameN;  // exact frame index
      
      suptest.setAutoDraw(true);
    }

    
    // *key_resp* updates
    if (t >= 0.0 && key_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp.tStart = t;  // (not accounting for frame time here)
      key_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp.clearEvents(); });
    }

    if (key_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp.getKeys({keyList: ['o', 'n'], waitRelease: false});
      _key_resp_allKeys = _key_resp_allKeys.concat(theseKeys);
      if (_key_resp_allKeys.length > 0) {
        key_resp.keys = _key_resp_allKeys[_key_resp_allKeys.length - 1].name;  // just the last key pressed
        key_resp.rt = _key_resp_allKeys[_key_resp_allKeys.length - 1].rt;
        // was this correct?
        if (key_resp.keys == AnswerSup) {
            key_resp.corr = 1;
        } else {
            key_resp.corr = 0;
        }
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    SupraTestComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function SupraTestRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'SupraTest'-------
    SupraTestComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // was no response the correct answer?!
    if (key_resp.keys === undefined) {
      if (['None','none',undefined].includes(AnswerSup)) {
         key_resp.corr = 1;  // correct non-response
      } else {
         key_resp.corr = 0;  // failed to respond (incorrectly)
      }
    }
    // store data for thisExp (ExperimentHandler)
    psychoJS.experiment.addData('key_resp.keys', key_resp.keys);
    psychoJS.experiment.addData('key_resp.corr', key_resp.corr);
    if (typeof key_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp.rt', key_resp.rt);
        routineTimer.reset();
        }
    
    key_resp.stop();
    // the Routine "SupraTest" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _key_resp_2_allKeys;
var Phase2Components;
function Phase2RoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'Phase2'-------
    t = 0;
    Phase2Clock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    key_resp_2.keys = undefined;
    key_resp_2.rt = undefined;
    _key_resp_2_allKeys = [];
    // keep track of which components have finished
    Phase2Components = [];
    Phase2Components.push(polygon_5);
    Phase2Components.push(distractor1);
    Phase2Components.push(key_resp_2);
    
    Phase2Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
  };
}


function Phase2RoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'Phase2'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = Phase2Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *polygon_5* updates
    if (t >= 0.0 && polygon_5.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      polygon_5.tStart = t;  // (not accounting for frame time here)
      polygon_5.frameNStart = frameN;  // exact frame index
      
      polygon_5.setAutoDraw(true);
    }

    
    // *distractor1* updates
    if (t >= 0.0 && distractor1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      distractor1.tStart = t;  // (not accounting for frame time here)
      distractor1.frameNStart = frameN;  // exact frame index
      
      distractor1.setAutoDraw(true);
    }

    
    // *key_resp_2* updates
    if (t >= 0.0 && key_resp_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_2.tStart = t;  // (not accounting for frame time here)
      key_resp_2.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_2.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_2.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_2.clearEvents(); });
    }

    if (key_resp_2.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_2.getKeys({keyList: ['0'], waitRelease: false});
      _key_resp_2_allKeys = _key_resp_2_allKeys.concat(theseKeys);
      if (_key_resp_2_allKeys.length > 0) {
        key_resp_2.keys = _key_resp_2_allKeys[_key_resp_2_allKeys.length - 1].name;  // just the last key pressed
        key_resp_2.rt = _key_resp_2_allKeys[_key_resp_2_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    Phase2Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function Phase2RoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'Phase2'-------
    Phase2Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('key_resp_2.keys', key_resp_2.keys);
    if (typeof key_resp_2.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_2.rt', key_resp_2.rt);
        routineTimer.reset();
        }
    
    key_resp_2.stop();
    // the Routine "Phase2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var Instructions2Components;
function Instructions2RoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'Instructions2'-------
    t = 0;
    Instructions2Clock.reset(); // clock
    frameN = -1;
    routineTimer.add(5.000000);
    // update component parameters for each repeat
    // keep track of which components have finished
    Instructions2Components = [];
    Instructions2Components.push(polygon_7);
    Instructions2Components.push(textphase2);
    
    Instructions2Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
  };
}


function Instructions2RoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'Instructions2'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = Instructions2Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *polygon_7* updates
    if (t >= 0.0 && polygon_7.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      polygon_7.tStart = t;  // (not accounting for frame time here)
      polygon_7.frameNStart = frameN;  // exact frame index
      
      polygon_7.setAutoDraw(true);
    }

    frameRemains = 0.0 + 5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if ((polygon_7.status === PsychoJS.Status.STARTED || polygon_7.status === PsychoJS.Status.FINISHED) && t >= frameRemains) {
      polygon_7.setAutoDraw(false);
    }
    
    // *textphase2* updates
    if (t >= 0.0 && textphase2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      textphase2.tStart = t;  // (not accounting for frame time here)
      textphase2.frameNStart = frameN;  // exact frame index
      
      textphase2.setAutoDraw(true);
    }

    frameRemains = 0.0 + 5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if ((textphase2.status === PsychoJS.Status.STARTED || textphase2.status === PsychoJS.Status.FINISHED) && t >= frameRemains) {
      textphase2.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    Instructions2Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function Instructions2RoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'Instructions2'-------
    Instructions2Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    return Scheduler.Event.NEXT;
  };
}


var SubliStudyComponents;
function SubliStudyRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'SubliStudy'-------
    t = 0;
    SubliStudyClock.reset(); // clock
    frameN = -1;
    routineTimer.add(3.300000);
    // update component parameters for each repeat
    ForenameSub.setText(NameSub);
    Cue.setText(CueSub);
    // keep track of which components have finished
    SubliStudyComponents = [];
    SubliStudyComponents.push(polygon_6);
    SubliStudyComponents.push(ForenameSub);
    SubliStudyComponents.push(Mask1);
    SubliStudyComponents.push(Cue);
    SubliStudyComponents.push(Mask2);
    SubliStudyComponents.push(blank1);
    
    SubliStudyComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
  };
}


function SubliStudyRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'SubliStudy'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = SubliStudyClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *polygon_6* updates
    if (t >= 0.0 && polygon_6.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      polygon_6.tStart = t;  // (not accounting for frame time here)
      polygon_6.frameNStart = frameN;  // exact frame index
      
      polygon_6.setAutoDraw(true);
    }

    frameRemains = 0.0 + 3.3 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if ((polygon_6.status === PsychoJS.Status.STARTED || polygon_6.status === PsychoJS.Status.FINISHED) && t >= frameRemains) {
      polygon_6.setAutoDraw(false);
    }
    
    // *ForenameSub* updates
    if (t >= 0.0 && ForenameSub.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      ForenameSub.tStart = t;  // (not accounting for frame time here)
      ForenameSub.frameNStart = frameN;  // exact frame index
      
      ForenameSub.setAutoDraw(true);
    }

    frameRemains = 0.0 + 1.2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if ((ForenameSub.status === PsychoJS.Status.STARTED || ForenameSub.status === PsychoJS.Status.FINISHED) && t >= frameRemains) {
      ForenameSub.setAutoDraw(false);
    }
    
    // *Mask1* updates
    if (t >= 1.2 && Mask1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Mask1.tStart = t;  // (not accounting for frame time here)
      Mask1.frameNStart = frameN;  // exact frame index
      
      Mask1.setAutoDraw(true);
    }

    if ((Mask1.status === PsychoJS.Status.STARTED || Mask1.status === PsychoJS.Status.FINISHED) && frameN >= (Mask1.frameNStart + 4)) {
      Mask1.setAutoDraw(false);
    }
    
    // *Cue* updates
    if (t >= 1.266 && Cue.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Cue.tStart = t;  // (not accounting for frame time here)
      Cue.frameNStart = frameN;  // exact frame index
      
      Cue.setAutoDraw(true);
    }

    if ((Cue.status === PsychoJS.Status.STARTED || Cue.status === PsychoJS.Status.FINISHED) && frameN >= (Cue.frameNStart + 2)) {
      Cue.setAutoDraw(false);
    }
    
    // *Mask2* updates
    if (t >= 1.3 && Mask2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Mask2.tStart = t;  // (not accounting for frame time here)
      Mask2.frameNStart = frameN;  // exact frame index
      
      Mask2.setAutoDraw(true);
    }

    frameRemains = 1.3 + 0.25 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if ((Mask2.status === PsychoJS.Status.STARTED || Mask2.status === PsychoJS.Status.FINISHED) && t >= frameRemains) {
      Mask2.setAutoDraw(false);
    }
    
    // *blank1* updates
    if (t >= 1.55 && blank1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      blank1.tStart = t;  // (not accounting for frame time here)
      blank1.frameNStart = frameN;  // exact frame index
      
      blank1.setAutoDraw(true);
    }

    frameRemains = 1.55 + 1.7 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if ((blank1.status === PsychoJS.Status.STARTED || blank1.status === PsychoJS.Status.FINISHED) && t >= frameRemains) {
      blank1.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    SubliStudyComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function SubliStudyRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'SubliStudy'-------
    SubliStudyComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    return Scheduler.Event.NEXT;
  };
}


var _key_resp_3_allKeys;
var SubliTestComponents;
function SubliTestRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'SubliTest'-------
    t = 0;
    SubliTestClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    SubTest.setText(TestSub);
    key_resp_3.keys = undefined;
    key_resp_3.rt = undefined;
    _key_resp_3_allKeys = [];
    // keep track of which components have finished
    SubliTestComponents = [];
    SubliTestComponents.push(polygon_8);
    SubliTestComponents.push(SubTest);
    SubliTestComponents.push(key_resp_3);
    
    SubliTestComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
  };
}


function SubliTestRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'SubliTest'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = SubliTestClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *polygon_8* updates
    if (t >= 0.0 && polygon_8.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      polygon_8.tStart = t;  // (not accounting for frame time here)
      polygon_8.frameNStart = frameN;  // exact frame index
      
      polygon_8.setAutoDraw(true);
    }

    
    // *SubTest* updates
    if (t >= 0.0 && SubTest.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      SubTest.tStart = t;  // (not accounting for frame time here)
      SubTest.frameNStart = frameN;  // exact frame index
      
      SubTest.setAutoDraw(true);
    }

    
    // *key_resp_3* updates
    if (t >= 0.0 && key_resp_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_3.tStart = t;  // (not accounting for frame time here)
      key_resp_3.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_3.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_3.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_3.clearEvents(); });
    }

    if (key_resp_3.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_3.getKeys({keyList: ['o', 'n'], waitRelease: false});
      _key_resp_3_allKeys = _key_resp_3_allKeys.concat(theseKeys);
      if (_key_resp_3_allKeys.length > 0) {
        key_resp_3.keys = _key_resp_3_allKeys[_key_resp_3_allKeys.length - 1].name;  // just the last key pressed
        key_resp_3.rt = _key_resp_3_allKeys[_key_resp_3_allKeys.length - 1].rt;
        // was this correct?
        if (key_resp_3.keys == AnswerSub) {
            key_resp_3.corr = 1;
        } else {
            key_resp_3.corr = 0;
        }
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    SubliTestComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function SubliTestRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'SubliTest'-------
    SubliTestComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // was no response the correct answer?!
    if (key_resp_3.keys === undefined) {
      if (['None','none',undefined].includes(AnswerSub)) {
         key_resp_3.corr = 1;  // correct non-response
      } else {
         key_resp_3.corr = 0;  // failed to respond (incorrectly)
      }
    }
    // store data for thisExp (ExperimentHandler)
    psychoJS.experiment.addData('key_resp_3.keys', key_resp_3.keys);
    psychoJS.experiment.addData('key_resp_3.corr', key_resp_3.corr);
    if (typeof key_resp_3.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_3.rt', key_resp_3.rt);
        routineTimer.reset();
        }
    
    key_resp_3.stop();
    // the Routine "SubliTest" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var EndScreenComponents;
function EndScreenRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'EndScreen'-------
    t = 0;
    EndScreenClock.reset(); // clock
    frameN = -1;
    routineTimer.add(4.000000);
    // update component parameters for each repeat
    // keep track of which components have finished
    EndScreenComponents = [];
    EndScreenComponents.push(polygon_9);
    EndScreenComponents.push(text);
    
    EndScreenComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
  };
}


function EndScreenRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'EndScreen'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = EndScreenClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *polygon_9* updates
    if (t >= 0.0 && polygon_9.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      polygon_9.tStart = t;  // (not accounting for frame time here)
      polygon_9.frameNStart = frameN;  // exact frame index
      
      polygon_9.setAutoDraw(true);
    }

    frameRemains = 0.0 + 4 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if ((polygon_9.status === PsychoJS.Status.STARTED || polygon_9.status === PsychoJS.Status.FINISHED) && t >= frameRemains) {
      polygon_9.setAutoDraw(false);
    }
    
    // *text* updates
    if (t >= 0.0 && text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text.tStart = t;  // (not accounting for frame time here)
      text.frameNStart = frameN;  // exact frame index
      
      text.setAutoDraw(true);
    }

    frameRemains = 0.0 + 4 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if ((text.status === PsychoJS.Status.STARTED || text.status === PsychoJS.Status.FINISHED) && t >= frameRemains) {
      text.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    EndScreenComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function EndScreenRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'EndScreen'-------
    EndScreenComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    return Scheduler.Event.NEXT;
  };
}


function endLoopIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        const thisTrial = snapshot.getCurrentTrial();
        if (typeof thisTrial === 'undefined' || !('isTrials' in thisTrial) || thisTrial.isTrials) {
          psychoJS.experiment.nextEntry(snapshot);
        }
      }
    return Scheduler.Event.NEXT;
    }
  };
}


function importConditions(currentLoop) {
  return function () {
    psychoJS.importAttributes(currentLoop.getCurrentTrial());
    return Scheduler.Event.NEXT;
    };
}


function quitPsychoJS(message, isCompleted) {
  // Check for and save orphaned data
  if (psychoJS.experiment.isEntryEmpty()) {
    psychoJS.experiment.nextEntry();
  }
  psychoJS.window.close();
  psychoJS.quit({message: message, isCompleted: isCompleted});
  
  return Scheduler.Event.QUIT;
}
