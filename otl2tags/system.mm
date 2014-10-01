<map version="0.8.0">
<node TEXT="Minimus Spine MS-1000 System">

<node TEXT="Basic Process">

<node TEXT="Cycle Pre-test">

<node TEXT="Check for lid closed">

<node TEXT="Method">

<node TEXT="Check state of lid switch"/>
</node>
<node TEXT="Success">

<node TEXT="Detection of lid closure"/>
</node>
<node TEXT="Failure modes">

<node TEXT="Lid not closed">

<node TEXT="Soft failure">

<node TEXT="Abort process"/>
</node>
<node TEXT="Control">

<node TEXT="Notify operator"/>
</node>
</node>
</node>
</node>
<node TEXT="Check for syringe">

<node TEXT="Method">

<node TEXT="Check state of syringe switch"/>
</node>
<node TEXT="Success">

<node TEXT="Detection of syringe"/>
</node>
<node TEXT="Failure modes">

<node TEXT="Syringe not detected">

<node TEXT="Soft failure">

<node TEXT="Abort process"/>
</node>
<node TEXT="Control">

<node TEXT="Notify operator"/>
</node>
</node>
</node>
</node>
<node TEXT="Verify UV LED and sensor">

<node TEXT="Method">

<node TEXT="Cycle LED output"/>
<node TEXT="Monitor UV input"/>
</node>
<node TEXT="Failure modes">

<node TEXT="UV LED not detected">

<node TEXT="Hard failure">

<node TEXT="Abort process"/>
<node TEXT="Log failure"/>
<node TEXT="Notify operator"/>
</node>
<node TEXT="Control">

<node TEXT="UV input levels"/>
</node>
</node>
</node>
</node>
<node TEXT="Verify blue LED and sensor">

<node TEXT="Method">

<node TEXT="Cycle LED output"/>
<node TEXT="Monitor blue input"/>
</node>
<node TEXT="Failure modes">

<node TEXT="Blue LED not detected">

<node TEXT="Hard failure">

<node TEXT="Abort process"/>
<node TEXT="Log failure"/>
<node TEXT="Notify operator"/>
</node>
<node TEXT="Control">

<node TEXT="Blue input levels"/>
</node>
</node>
</node>
</node>
</node>
<node TEXT="Concentrate Oxygen">

<node TEXT="Evacuate zeolite">

<node TEXT="Method">

<node TEXT="Select mode 1 (Evacuate Zeolite)"/>
<node TEXT="Monitor time and vacuum"/>
</node>
<node TEXT="Failure modes">

<node TEXT="Improper vaccum">

<node TEXT="Hard failure">

<node TEXT="Abort process"/>
<node TEXT="Log failure"/>
<node TEXT="Notify operator"/>
</node>
<node TEXT="Control">

<node TEXT="Vacuum limit not reached in time"/>
</node>
</node>
</node>
</node>
<node TEXT="Evacuate syringe">

<node TEXT="Method">

<node TEXT="Select mode 2 (Evacuate Zeolite and syringe)"/>
<node TEXT="Monitor time and vacuum"/>
</node>
<node TEXT="Failure modes">

<node TEXT="Improper vaccum">

<node TEXT="Soft failure">

<node TEXT="Abort process"/>
<node TEXT="Notify operator to check/replace syringe"/>
</node>
<node TEXT="Control">

<node TEXT="Vacuum limit not reached in time"/>
</node>
</node>
</node>
</node>
<node TEXT="Pressurize zeolite">

<node TEXT="Method">

<node TEXT="Select mode 3 (Pressurize Zeolite)"/>
<node TEXT="Monitor time and pressure"/>
<node TEXT="Monitor humidity"/>
</node>
<node TEXT="Failure modes">

<node TEXT="Improper pressure">

<node TEXT="Hard failure">

<node TEXT="Abort process"/>
<node TEXT="Log failure"/>
<node TEXT="Notify operator"/>
</node>
<node TEXT="Control">

<node TEXT="Pressure limit not reached in time"/>
</node>
</node>
<node TEXT="Improper humidity">

<node TEXT="Hard failure">

<node TEXT="Abort process"/>
<node TEXT="Log failure"/>
<node TEXT="Notify operator"/>
</node>
<node TEXT="Control">

<node TEXT="Humidiy too high"/>
</node>
</node>
</node>
</node>
<node TEXT="Pause for Adsorption">

<node TEXT="Method">

<node TEXT="Select mode 4 (Oxygen Hold)"/>
<node TEXT="Wait for set time and monitor pressure"/>
</node>
<node TEXT="Failure modes">

<node TEXT="Improper pressure">

<node TEXT="Hard failure">

<node TEXT="Abort process"/>
<node TEXT="Log failure"/>
<node TEXT="Notify operator"/>
</node>
<node TEXT="Control">

<node TEXT="Pressure not within limits"/>
</node>
</node>
</node>
</node>
</node>
<node TEXT="Fill Syringe">

<node TEXT="Pre-fill syringe (to purge parasitic spaces)">

<node TEXT="Method">

<node TEXT="Select mode 5 (Fill Syringe 1) for fixed time"/>
<node TEXT="Monitor time and UV sensor"/>
</node>
<node TEXT="Failure modes">

<node TEXT="Syringe did not fill properly">

<node TEXT="Soft failure">

<node TEXT="Abort process"/>
<node TEXT="Notify operator to check/replace syringe"/>
</node>
<node TEXT="Control">

<node TEXT="Monitor UV sensor and time"/>
<node TEXT="Zeolite pressure after fill"/>
</node>
</node>
</node>
</node>
<node TEXT="Re-evacuate syringe (to purge parasitic spaces)">

<node TEXT="Method">

<node TEXT="Select mode 6 (Purge Syringe)"/>
<node TEXT="Monitor time and vacuum"/>
</node>
<node TEXT="Failure modes">

<node TEXT="Improper vaccum">

<node TEXT="Soft failure">

<node TEXT="Abort process"/>
<node TEXT="Notify operator to check/replace syringe"/>
</node>
<node TEXT="Control">

<node TEXT="Vacuum limit not reached in time"/>
</node>
</node>
</node>
</node>
<node TEXT="Fill syringe">

<node TEXT="Method">

<node TEXT="Select mode 7 (Fill Syringe 2)"/>
<node TEXT="Monitor time and UV sensor"/>
</node>
<node TEXT="Failure modes">

<node TEXT="Syringe did not fill properly">

<node TEXT="Soft failure">

<node TEXT="Abort process"/>
<node TEXT="Notify operator to check/replace syringe"/>
</node>
<node TEXT="Control">

<node TEXT="Monitor UV sensor and time"/>
<node TEXT="Zeolite pressure after fill"/>
</node>
</node>
</node>
</node>
<node TEXT="Vent waste gasses">

<node TEXT="Method">

<node TEXT="Select mode 8 (Vent Excess Gasses)"/>
<node TEXT="Monitor pressure and time"/>
</node>
<node TEXT="Failure modes">

<node TEXT="Zeolite does not depressurize properly">

<node TEXT="Hard failure">

<node TEXT="Abort process"/>
<node TEXT="Log failure"/>
<node TEXT="Notify operator to check/replace syringe"/>
</node>
<node TEXT="Control">

<node TEXT="Pressure limit not reached in time"/>
</node>
</node>
</node>
</node>
<node TEXT="Equalize syringe pressure">

<node TEXT="Method">

<node TEXT="Select mode 9 (Equlize Syringe Pressure)"/>
<node TEXT="Monitor pressure and time"/>
<node TEXT="Sample blue light transmissivity for later use"/>
</node>
<node TEXT="Failure modes">

<node TEXT="Syringe pressure not equalized">

<node TEXT="Soft failure">

<node TEXT="Abort process"/>
<node TEXT="Replace syringe"/>
<node TEXT="Notify operator"/>
</node>
<node TEXT="Control">

<node TEXT="Pressure limit not reached in time"/>
</node>
</node>
</node>
</node>
<node TEXT="Seal pneumatic system">

<node TEXT="Method">

<node TEXT="Select mode 0 (All Off)"/>
</node>
<node TEXT="Failure modes">

<node TEXT="None"/>
</node>
</node>
</node>
<node TEXT="Generate Ozone">

<node TEXT="Ionize oxygen">

<node TEXT="Method">

<node TEXT="Adjust LED current for maximum gain"/>
<node TEXT="Turn on ionizer"/>
</node>
<node TEXT="Failure modes">

<node TEXT="Improper ionization">

<node TEXT="Soft failure">

<node TEXT="Abort process"/>
<node TEXT="Notify operator to replace syringe"/>
</node>
<node TEXT="Control">

<node TEXT="Monitor UV sensor and time"/>
</node>
</node>
</node>
</node>
<node TEXT="Check for NO2">

<node TEXT="Method">

<node TEXT="Measure change in blue light transmissivity"/>
</node>
<node TEXT="Failure modes">

<node TEXT="Detectable NO2">

<node TEXT="Soft failure">

<node TEXT="Abort process"/>
<node TEXT="Notify operator to replace syringe"/>
</node>
<node TEXT="Control">

<node TEXT="Monitor blue light sensor"/>
</node>
</node>
</node>
</node>
<node TEXT="Ozone usage timer">

<node TEXT="Method">

<node TEXT="Show on-screen timer to warn about ozone usage/decay"/>
</node>
<node TEXT="Failure modes">

<node TEXT="Ozone not administered in time">

<node TEXT="Soft failure">

<node TEXT="Abort process"/>
<node TEXT="Alert operator"/>
</node>
<node TEXT="Control">

<node TEXT="Monitor time"/>
</node>
</node>
<node TEXT="Device not notified of ozone use">

<node TEXT="Soft failure">

<node TEXT="Abort process"/>
<node TEXT="Alert operator"/>
</node>
<node TEXT="Control">

<node TEXT="Monitor time"/>
</node>
</node>
</node>
</node>
</node>
</node>
<node TEXT="Firmware">

<node TEXT="[X] 100% Prototype">

<node TEXT="[X] 100% Drivers">

<node TEXT="[X] 100% LCD">

<node TEXT="[X] 100% LCD control">

<node TEXT="[X] 100% brightness"/>
<node TEXT="[X] 100% backlight-off"/>
<node TEXT="[X] 100% backlight-on"/>
<node TEXT="[X] 100% cls"/>
<node TEXT="[X] 100% restorexy"/>
<node TEXT="[X] 100% savexy"/>
<node TEXT="[X] 100% setxy"/>
<node TEXT="[X] 100% setbgcolor"/>
<node TEXT="[X] 100% setcolor"/>
</node>
<node TEXT="[X] 100% text printing">

<node TEXT="[X] 100% lcdtype"/>
<node TEXT="[X] 100% lcdbgtype"/>
<node TEXT="[X] 100% lcdcrlf"/>
<node TEXT="[X] 100% lcdcr"/>
<node TEXT="[X] 100% lcd-terminal"/>
<node TEXT="[X] 100% clf"/>
<node TEXT="[X] 100% selectfont"/>
<node TEXT="[X] 100% textnorth"/>
<node TEXT="[X] 100% texteast"/>
<node TEXT="[X] 100% textsouth"/>
<node TEXT="[X] 100% textwest"/>
</node>
<node TEXT="[X] 100% graphics functions">

<node TEXT="[X] 100% arc"/>
<node TEXT="[X] 100% box"/>
<node TEXT="[X] 100% filled-box"/>
<node TEXT="[X] 100% circle"/>
<node TEXT="[X] 100% filled-circle"/>
<node TEXT="[X] 100% hline"/>
<node TEXT="[X] 100% lineto"/>
<node TEXT="[X] 100% pie"/>
<node TEXT="[X] 100% plot"/>
<node TEXT="[X] 100% plotxy"/>
<node TEXT="[X] 100% putsficon"/>
<node TEXT="[X] 100% vline"/>
</node>
<node TEXT="[X] 100% button function">

<node TEXT="[X] 100% anybutton?"/>
<node TEXT="[X] 100% button"/>
<node TEXT="[X] 100% buttondef"/>
<node TEXT="[X] 100% buttonstate"/>
<node TEXT="[X] 100% buttonsallup"/>
<node TEXT="[X] 100% buttonsdeleteall"/>
<node TEXT="[X] 100% touchprotocol"/>
</node>
</node>
<node TEXT="[X] 100% HV source">

<node TEXT="[X] 100% control"/>
</node>
<node TEXT="[X] 100% UV source">

<node TEXT="[X] 100% control"/>
</node>
<node TEXT="[X] 100% UV sensor">

<node TEXT="[X] 100% filtering"/>
<node TEXT="[X] 100% logging"/>
<node TEXT="[X] 100% scaling"/>
</node>
<node TEXT="[X] 100% pressure sensor">

<node TEXT="[X] 100% filtering"/>
<node TEXT="[X] 100% logging"/>
<node TEXT="[X] 100% scaling"/>
</node>
<node TEXT="[X] 100% vacuum sensor">

<node TEXT="[X] 100% filtering"/>
<node TEXT="[X] 100% logging"/>
<node TEXT="[X] 100% scaling"/>
</node>
<node TEXT="[X] 100% lid closure">

<node TEXT="[X] 100% detection"/>
</node>
<node TEXT="[X] 100% syringe detection">

<node TEXT="[X] 100% detection"/>
</node>
<node TEXT="[X] 100% Beeper">

<node TEXT="[X] 100% chirp"/>
<node TEXT="[X] 100% error beep"/>
</node>
<node TEXT="[X] 100% ADC">

<node TEXT="[X] 100% ADC IC interface"/>
<node TEXT="[X] 100% getsample"/>
<node TEXT="[X] 100% filtersample"/>
</node>
<node TEXT="[-] 33% Thumb drive">

<node TEXT="[X] 100% Vinculum serial driver"/>
<node TEXT="[_] 0% Logging"/>
<node TEXT="[_] 0% Firmware upgrade"/>
</node>
<node TEXT="[X] 100% Device log">

<node TEXT="[X] 100% logging"/>
<node TEXT="[X] 100% formatting"/>
<node TEXT="[X] 100% log rotation"/>
</node>
</node>
<node TEXT="[X] 100% Application">

<node TEXT="[X] 100% Screens">

<node TEXT="[X] 100% Startup"/>
<node TEXT="[X] 100% Oxygen Cycle">

<node TEXT="[X] 100% Evacuation"/>
<node TEXT="[X] 100% Oxygen Concentration"/>
<node TEXT="[X] 100% Fill Syringe"/>
</node>
<node TEXT="[X] 100% Ozone Cycle">

<node TEXT="[X] 100% Ionize Oxygen"/>
<node TEXT="[X] 100% Ozone Decay"/>
</node>
</node>
</node>
</node>
<node TEXT="[_] 56% Firmware Version 2">

<node TEXT="[_] 65% Drivers">

<node TEXT="[_] 62% LCD">

<node TEXT="[X] 100% LCD control">

<node TEXT="[X] 100% brightness"/>
<node TEXT="[X] 100% backlight-off"/>
<node TEXT="[X] 100% backlight-on"/>
<node TEXT="[X] 100% cls"/>
<node TEXT="[X] 100% restorexy"/>
<node TEXT="[X] 100% savexy"/>
<node TEXT="[X] 100% setxy"/>
<node TEXT="[X] 100% setbgcolor"/>
<node TEXT="[X] 100% setcolor"/>
</node>
<node TEXT="[X] 100% text printing">

<node TEXT="[X] 100% lcdtype"/>
<node TEXT="[X] 100% lcdbgtype"/>
<node TEXT="[X] 100% lcdcrlf"/>
<node TEXT="[X] 100% lcdcr"/>
<node TEXT="[X] 100% lcd-terminal"/>
<node TEXT="[X] 100% clf"/>
<node TEXT="[X] 100% selectfont"/>
<node TEXT="[X] 100% textnorth"/>
<node TEXT="[X] 100% texteast"/>
<node TEXT="[X] 100% textsouth"/>
<node TEXT="[X] 100% textwest"/>
</node>
<node TEXT="[X] 100% graphics functions">

<node TEXT="[X] 100% arc"/>
<node TEXT="[X] 100% box"/>
<node TEXT="[X] 100% filled-box"/>
<node TEXT="[X] 100% circle"/>
<node TEXT="[X] 100% filled-circle"/>
<node TEXT="[X] 100% hline"/>
<node TEXT="[X] 100% lineto"/>
<node TEXT="[X] 100% pie"/>
<node TEXT="[X] 100% plot"/>
<node TEXT="[X] 100% plotxy"/>
<node TEXT="[X] 100% putsficon"/>
<node TEXT="[X] 100% vline"/>
</node>
<node TEXT="[X] 100% button function">

<node TEXT="[X] 100% anybutton?"/>
<node TEXT="[X] 100% button"/>
<node TEXT="[X] 100% buttondef"/>
<node TEXT="[X] 100% buttonstate"/>
<node TEXT="[X] 100% buttonsallup"/>
<node TEXT="[X] 100% buttonsdeleteall"/>
<node TEXT="[X] 100% touchprotocol"/>
</node>
<node TEXT="[X] 100% button objects">

<node TEXT="[X] 100% build text button"/>
<node TEXT="[X] 100% destroy"/>
<node TEXT="[X] 100% show"/>
<node TEXT="[X] 100% hide"/>
</node>
<node TEXT="[_] 0% screen objects"/>
<node TEXT="[_] 0% window objects"/>
<node TEXT="[_] 0% graphing objects"/>
</node>
<node TEXT="[_] 50% HV source">

<node TEXT="[X] 100% control"/>
<node TEXT="[_] 0% failure detection (D00479 document compliance)"/>
</node>
<node TEXT="[_] 50% UV source">

<node TEXT="[X] 100% control"/>
<node TEXT="[_] 0% failure detection (D00479 document compliance)"/>
</node>
<node TEXT="[_] 75% UV sensor">

<node TEXT="[X] 100% filtering"/>
<node TEXT="[X] 100% logging"/>
<node TEXT="[X] 100% scaling"/>
<node TEXT="[_] 0% failure detection (D00479 document compliance)"/>
</node>
<node TEXT="[_] 75% pressure sensor">

<node TEXT="[X] 100% filtering"/>
<node TEXT="[X] 100% logging"/>
<node TEXT="[X] 100% scaling"/>
<node TEXT="[_] 0% failure detection (D00479 document compliance)"/>
</node>
<node TEXT="[_] 75% vacuum sensor">

<node TEXT="[X] 100% filtering"/>
<node TEXT="[X] 100% logging"/>
<node TEXT="[X] 100% scaling"/>
<node TEXT="[_] 0% failure detection (D00479 document compliance)"/>
</node>
<node TEXT="[_] 50% lid closure">

<node TEXT="[X] 100% detection"/>
<node TEXT="[_] 0% failure detection (D00479 document compliance)"/>
</node>
<node TEXT="[_] 50% syringe detection">

<node TEXT="[X] 100% detection"/>
<node TEXT="[_] 0% failure detection (D00479 document compliance)"/>
</node>
<node TEXT="[X] 100% Beeper">

<node TEXT="[X] 100% chirp"/>
<node TEXT="[X] 100% error beep"/>
</node>
<node TEXT="[X] 100% ADC">

<node TEXT="[X] 100% ADC IC interface"/>
<node TEXT="[X] 100% getsample"/>
<node TEXT="[X] 100% filtersample"/>
</node>
<node TEXT="[_] 33% Thumb drive">

<node TEXT="[X] 100% Vinculum serial driver"/>
<node TEXT="[_] 0% Logging"/>
<node TEXT="[_] 0% Firmware upgrade"/>
</node>
<node TEXT="[_] 60% Device log">

<node TEXT="[X] 100% logging"/>
<node TEXT="[X] 100% formatting"/>
<node TEXT="[X] 100% log rotation"/>
<node TEXT="[_] 0% printing"/>
<node TEXT="[_] 0% thumb drive save"/>
</node>
</node>
<node TEXT="[_] 47% Application">

<node TEXT="[_] 37% Screens">

<node TEXT="[X] 100% Startup"/>
<node TEXT="[_] 0% Hard failure"/>
<node TEXT="[_] 0% Soft failure"/>
<node TEXT="[_] 0% Setup">

<node TEXT="[_] 0% reports"/>
<node TEXT="[_] 0% detailed reports"/>
<node TEXT="[_] 0% language"/>
<node TEXT="[_] 0% time and date"/>
<node TEXT="[_] 0% diagnostics"/>
<node TEXT="[_] 0% logging to thumb drive"/>
<node TEXT="[_] 0% firmware upgrade"/>
</node>
<node TEXT="[_] 60% Oxygen Cycle">

<node TEXT="[_] 0% Syringe Insertion"/>
<node TEXT="[X] 100% Evacuation"/>
<node TEXT="[X] 100% Oxygen Concentration"/>
<node TEXT="[X] 100% Fill Syringe"/>
<node TEXT="[_] 0% Syringe Error"/>
</node>
<node TEXT="[_] 66% Ozone Cycle">

<node TEXT="[X] 100% Ionize Oxygen"/>
<node TEXT="[_] 0% Ionize Error"/>
<node TEXT="[X] 100% Ozone Decay"/>
</node>
</node>
<node TEXT="[_] 57% Processes">

<node TEXT="[X] 100% Monitor">

<node TEXT="Master process to control other processes."/>
</node>
<node TEXT="[X] 100% GUI">

<node TEXT="Show and handle user interface screens and buttons."/>
</node>
<node TEXT="[_] 31% Worker">

<node TEXT="Oxygen concentration and ozone generation."/>
<node TEXT="[X] 100% Idle">

<node TEXT="State: stIdle"/>
</node>
<node TEXT="[_] 0% Check Syringe">

<node TEXT="State: stCheckSyringe"/>
<node TEXT="[_] 0% Function">

<node TEXT="[_] 0% check syringe presense"/>
<node TEXT="[_] 0% cross-check sensors"/>
</node>
<node TEXT="[_] 0% Tests">

<node TEXT="[_] 0% lid switch"/>
<node TEXT="[_] 0% UV sensor"/>
<node TEXT="[_] 0% syringe switch"/>
<node TEXT="[_] 0% cross-check switches with UV sensor"/>
</node>
<node TEXT="[_] 0% Logging">

<node TEXT="[_] 0% lid opened"/>
<node TEXT="[_] 0% syringe removed"/>
<node TEXT="[_] 0% process start time"/>
<node TEXT="[_] 0% syringe check failure"/>
<node TEXT="[_] 0% sensor cross-check failure"/>
</node>
</node>
<node TEXT="[_] 33% Evacuate System">

<node TEXT="State: stEvacuate"/>
<node TEXT="[X] 100% Function"/>
<node TEXT="[_] 0% Tests">

<node TEXT="[_] 0% quick pressure"/>
<node TEXT="[_] 0% vacuum over time"/>
<node TEXT="[_] 0% vacuum hold"/>
<node TEXT="[_] 0% syringe switch"/>
<node TEXT="[_] 0% lid switch"/>
</node>
<node TEXT="[_] 0% Logging">

<node TEXT="[_] 0% lid opened"/>
<node TEXT="[_] 0% syringe removed"/>
<node TEXT="[_] 0% time to achieve vacuum"/>
<node TEXT="[_] 0% pressure sensor failure"/>
<node TEXT="[_] 0% vacuum sensor failure"/>
<node TEXT="[_] 0% vacuum failure"/>
<node TEXT="[_] 0% sensor cross-check failure"/>
</node>
</node>
<node TEXT="[_] 33% Evaucuate Syringe">

<node TEXT="State: stEvacSyringe"/>
<node TEXT="[X] 100% Function"/>
<node TEXT="[_] 0% Tests">

<node TEXT="[_] 0% syringe switch"/>
<node TEXT="[_] 0% lid switch"/>
<node TEXT="[_] 0% vacuum after evacuate"/>
</node>
<node TEXT="[_] 0% Logging">

<node TEXT="[_] 0% lid opened"/>
<node TEXT="[_] 0% syringe removed"/>
<node TEXT="[_] 0% syringe evacuation failure"/>
<node TEXT="[_] 0% sensor cross-check failure"/>
</node>
</node>
<node TEXT="[_] 33% Concentrate Oxygen">

<node TEXT="State: stOxygen"/>
<node TEXT="[X] 100% Function"/>
<node TEXT="[_] 0% Tests">

<node TEXT="[_] 0% syringe switch"/>
<node TEXT="[_] 0% lid switch"/>
<node TEXT="[_] 0% time to achieve pressure"/>
<node TEXT="[_] 0% pressure hold"/>
<node TEXT="[_] 0% pressure sensor failure"/>
</node>
<node TEXT="[_] 0% Logging">

<node TEXT="[_] 0% lid opened"/>
<node TEXT="[_] 0% syringe removed"/>
<node TEXT="[_] 0% time to achieve pressure"/>
<node TEXT="[_] 0% pressure failure"/>
<node TEXT="[_] 0% pressure sensor failure"/>
<node TEXT="[_] 0% sensor cross-check failure"/>
</node>
</node>
<node TEXT="[_] 33% Fill Syringe">

<node TEXT="State: stFillSyringe"/>
<node TEXT="[X] 100% Function"/>
<node TEXT="[_] 0% Tests">

<node TEXT="[_] 0% syringe switch"/>
<node TEXT="[_] 0% lid switch"/>
<node TEXT="[_] 0% Pressure after fill"/>
<node TEXT="[_] 0% UV sensor value for proper fill"/>
<node TEXT="[_] 0% UV sensor value for proper orientation"/>
</node>
<node TEXT="[_] 0% Logging">

<node TEXT="[_] 0% lid opened"/>
<node TEXT="[_] 0% syringe removed"/>
<node TEXT="[_] 0% pressure sensor failure"/>
<node TEXT="[_] 0% UV sensor failure"/>
<node TEXT="[_] 0% syringe orientation failure"/>
<node TEXT="[_] 0% syringe fill failure"/>
<node TEXT="[_] 0% sensor cross-check failure"/>
</node>
</node>
<node TEXT="[_] 50% Equalize Syringe Pressure">

<node TEXT="[X] 100% State: stFillSyringe"/>
<node TEXT="[X] 100% Function"/>
<node TEXT="[_] 0% Tests">

<node TEXT="[_] 0% syringe switch"/>
<node TEXT="[_] 0% lid switch"/>
<node TEXT="[_] 0% Pressure after equalization"/>
</node>
<node TEXT="[_] 0% Logging">

<node TEXT="[_] 0% lid opened"/>
<node TEXT="[_] 0% syringe removed"/>
<node TEXT="[_] 0% pressure failure"/>
<node TEXT="[_] 0% sensor cross-check failure"/>
</node>
</node>
<node TEXT="[_] 25% Izonize Oxygen">

<node TEXT="State: stIonize"/>
<node TEXT="[X] 100% Function"/>
<node TEXT="[_] 0% Tests">

<node TEXT="[_] 0% syringe switch"/>
<node TEXT="[_] 0% lid switch"/>
<node TEXT="[_] 0% UV sensor"/>
<node TEXT="[_] 0% UV change over time"/>
</node>
<node TEXT="[_] 0% Logging">

<node TEXT="[_] 0% lid opened"/>
<node TEXT="[_] 0% syringe removed"/>
<node TEXT="[_] 0% UV sensor failure"/>
<node TEXT="[_] 0% ionization failure"/>
<node TEXT="[_] 0% sensor cross-check failure"/>
</node>
</node>
<node TEXT="[_] 33% Ozone Decay">

<node TEXT="State: stDecay"/>
<node TEXT="[X] 100% Function"/>
<node TEXT="[_] 0% Tests"/>
<node TEXT="[_] 0% Logging"/>
</node>
<node TEXT="[_] 33% Process Complete">

<node TEXT="State: stComplete"/>
<node TEXT="[X] 100% Function"/>
<node TEXT="[_] 0% Tests"/>
<node TEXT="[_] 0% Logging"/>
</node>
<node TEXT="[_] 0% Process Soft Failure">

<node TEXT="State: stSoftFail"/>
</node>
<node TEXT="[_] 0% Process Hard Failure">

<node TEXT="State: stHardFail"/>
</node>
</node>
<node TEXT="[_] 0% Monitor">

<node TEXT="Monitor other tasks' stacks"/>
</node>
</node>
</node>
</node>
<node TEXT="Firmware Version 3">

<node TEXT="Features"/>
<node TEXT="Porting to new version 3 hardware"/>
</node>
</node>
<node TEXT="Electronics">

<node TEXT="Electronics Version 2 (current version)">

<node TEXT="Bugs">

<node TEXT="No pull-up on SDA">

<node TEXT="Fix: hand-add pull-up on SDA"/>
</node>
<node TEXT="No pull-up on SCL">

<node TEXT="Fix: hand-add pull-up on SCL"/>
</node>
<node TEXT="No pull-up on P0.14">

<node TEXT="Fix: hand-add pull-up on P0.14"/>
</node>
<node TEXT="Q10 burns out sometimes when pump is too near limits">

<node TEXT="Fix: continue to replace transistor on prototype"/>
</node>
</node>
<node TEXT="Changes">

<node TEXT="Converted blue LED output to drive UV LED"/>
</node>
</node>
<node TEXT="Electronics Version 3 (next version)">

<node TEXT="Controller">

<node TEXT="Changes">

<node TEXT="Add pull-up for SDA"/>
<node TEXT="Add pull-up for SCL"/>
<node TEXT="Change Q10">

<node TEXT="Larger package"/>
<node TEXT="3A minimum current"/>
</node>
<node TEXT="Replace UV lamp driver with UV LED driver"/>
<node TEXT="Change drive voltage of pressure sensors to 12VDC">

<node TEXT="This may not work"/>
<node TEXT="The single-ended voltages may be too high"/>
</node>
<node TEXT="Increase timing on -RST">

<node TEXT="Current TRC is 1ms"/>
<node TEXT="Should be at least 10ms"/>
</node>
</node>
<node TEXT="Enhancements">

<node TEXT="Current sensor for system diagnostics"/>
<node TEXT="Louder beeper"/>
<node TEXT="Ionization current sensor"/>
<node TEXT="Control for new HV power supply"/>
<node TEXT="Add 12V fan connector"/>
<node TEXT="CPU-adjustable constant current driver for UV LED"/>
</node>
</node>
<node TEXT="Ionizer"/>
</node>
</node>
<node TEXT="Pneumatics">

<node TEXT="[X] 100% Existing"/>
<node TEXT="[X] 100% Modifications">

<node TEXT="[X] 100% Change to new plumbing method so all gasses enter one port and leave another"/>
<node TEXT="[X] 100% Add luer fittings so gasses can enter and leave a the rear of the enclosure"/>
<node TEXT="[X] 100% Install and test new pump"/>
<node TEXT="[X] 100% Move valve closer to zeolite to reduce amount of residual nitrogen"/>
<node TEXT="[_] % Backpressure regulator"/>
</node>
</node>
<node TEXT="Enclosure"/>
<node TEXT="Problems">

<node TEXT="Low Ozone Concentration / Low Ionization">

<node TEXT="Symptoms">

<node TEXT="Low ozone readings on ozone meter"/>
<node TEXT="Poor performance on burning gloves"/>
<node TEXT="Inconsistent performanance on meter and gloves"/>
</node>
<node TEXT="Causes">

<node TEXT="Known">

<node TEXT="Inconsistent construction of syringe electrodes"/>
<node TEXT="Inconsistent levels of oxygen from zeolite">

<node TEXT="See Low/Inconsistent Oxygen Concentration"/>
</node>
<node TEXT="Poor and inconsistent ionizing field">

<node TEXT="Using a hacked-together high-voltage supply in an open-loop configuration"/>
</node>
</node>
<node TEXT="Possible">

<node TEXT="For low ozone readings">

<node TEXT="Faulty ozone meter"/>
</node>
</node>
</node>
<node TEXT="Solutions">

<node TEXT="Current">

<node TEXT="External ground electrode on syringe">

<node TEXT="Makes production faster and more consistent due to a larger ionizing field"/>
</node>
</node>
<node TEXT="To be implemented">

<node TEXT="Need a proper HV ionizer supply">

<node TEXT="We know it needs to be very short, very high-voltage, negative pulses"/>
<node TEXT="This type of power supply is very simple to create">

<node TEXT="Uses a flyback transformer"/>
<node TEXT="Output voltage is controlled by controlling the voltage on a capacitor"/>
<node TEXT="Output pulses can be put into the ???uS range"/>
<node TEXT="Would be under computer control so frequency and voltage can be controlled"/>
</node>
</node>
<node TEXT="Consistent method of placing the electrodes in/on the syringe">

<node TEXT="What needs to be determined">

<node TEXT="What is the correct amount of arc to cover on the ground electrode?"/>
<node TEXT="What is the correct length of the ionizing electrode?"/>
<node TEXT="What is the maximum voltage and pulse period we can use for ionizing?"/>
<node TEXT="These will have to be determined experimentally"/>
</node>
<node TEXT="How do we create consistent assembly in the mean time before manufacturing?"/>
</node>
</node>
</node>
<node TEXT="To Do">

<node TEXT="Prototype the new HV supply"/>
<node TEXT="Determine electrode configuration"/>
<node TEXT="Determine ionizing voltage, pulse width and frequency"/>
<node TEXT="Develop a way to simply hand-make syringes be for manufacturing"/>
</node>
</node>
<node TEXT="Inconsistent/Erroneous Ozone Measurement">

<node TEXT="Symptoms">

<node TEXT="Rise in UV transmissivity at the beginning of the ionization process"/>
<node TEXT="Inconsistent baseline readings"/>
</node>
<node TEXT="Causes">

<node TEXT="Known">

<node TEXT="Ionizer is engaged during meansurment">

<node TEXT="This causes more UV light to be reflected/refracted down the syringe"/>
<node TEXT="This diminishes as the level of ozone increases"/>
</node>
<node TEXT="Syringe placement in sterility tube">

<node TEXT="Causes refraction"/>
<node TEXT="Causes differing amounts of syringe body to be placed in the UV beam"/>
<node TEXT="Causes UV beam to be blocked by printing on the syring body"/>
</node>
</node>
<node TEXT="Possible">

<node TEXT="Heating of the UV sensor">

<node TEXT="May be due to entire machine heating"/>
<node TEXT="May be due to UV heating from UV LED"/>
</node>
<node TEXT="Oxidation of the syringe body"/>
<node TEXT="Oxidation of the lubricant"/>
</node>
</node>
<node TEXT="Solutions">

<node TEXT="Current"/>
<node TEXT="To be implemented">

<node TEXT="Syringe alignment 'donut'"/>
<node TEXT="Turn off ionizer during measurement">

<node TEXT="This takes about 100ms"/>
<node TEXT="Will increase ionization time by about 11%"/>
</node>
<node TEXT="Account for oxidization changes with math">

<node TEXT="The changes should be consistent enough for compensation down to 0.01% of full scale"/>
</node>
<node TEXT="Account for thermal influences with math"/>
<node TEXT="Add variable constant current source for UV LED">

<node TEXT="This will allow for maximizing dynamic range by adjusting full scale range for each syringe assembly"/>
<node TEXT="This will reduce noise from the switching power supply to below 50PPM"/>
</node>
<node TEXT="Enhance the optics">

<node TEXT="Perhaps both sensor and receive can be in an adjustable mounting"/>
<node TEXT="Mount should emulate or be comprised of a cylindrical aperture or tube"/>
<node TEXT="Mounts should be black"/>
<node TEXT="It seems unnecessary to switch from Teflon now or paint it black"/>
</node>
</node>
</node>
<node TEXT="Experimental Results as of 2008-10-02">

<node TEXT="Determine if there is heating of the sensor by the UV LED">

<node TEXT="Process">

<node TEXT="Start with the machine at room temperature"/>
<node TEXT="Open machine enclosure so machine heating effects will be removed for the experiment"/>
<node TEXT="Ionizer is off"/>
<node TEXT="Use an unlubricated syringe filled with air"/>
<node TEXT="Record the UV transmissivity measurement"/>
<node TEXT="remove syringe so the UV sensor will be overwhelmed"/>
<node TEXT="Wait 5 minutes"/>
<node TEXT="replace syringe"/>
<node TEXT="Record the UV transmissivity measurement"/>
<node TEXT="Evaluate the results"/>
</node>
<node TEXT="Results">

<node TEXT="Cannot create a uniform test"/>
<node TEXT="It does not appear that there is any heating at all from the UV light">

<node TEXT="The LED output is very low"/>
<node TEXT="The UV light is greatly filtered via the syringe and sterility enclosure"/>
</node>
</node>
</node>
<node TEXT="Determine how much machine heat affects UV sensor">

<node TEXT="Process">

<node TEXT="Start with the machine at room temperature"/>
<node TEXT="Ionizer is off"/>
<node TEXT="Use an unlubricated syringe filled with air"/>
<node TEXT="Allow the machine to heat up"/>
<node TEXT="Record the UV transmissivity measurements over time"/>
<node TEXT="Test may take a couple of hours so the machine can heat to maximum"/>
<node TEXT="Evaluate the results"/>
</node>
<node TEXT="Results"/>
</node>
<node TEXT="Determine if the standard lubricant is oxidizing">

<node TEXT="Process">

<node TEXT="Start with the machine at room temperature"/>
<node TEXT="Ionizer is off"/>
<node TEXT="Use a lubricated syringe filled with oxygen"/>
<node TEXT="Record the UV transmissivity measurements over time"/>
<node TEXT="Include any sensor heating effects, if they exist from the above experiments"/>
<node TEXT="Evaluate the results"/>
</node>
<node TEXT="Results">

<node TEXT="The syringe body / lubricant transmissivity does change about 2.3%"/>
</node>
</node>
<node TEXT="Determine if the special lubricant is oxidizing">

<node TEXT="Process">

<node TEXT="Start with the machine at room temperature"/>
<node TEXT="Ionizer is off"/>
<node TEXT="Use a specially lubricated syringe filled with oxygen"/>
<node TEXT="Record the UV transmissivity measurements over time"/>
<node TEXT="Include any sensor heating effects, if they exist from the above experiments"/>
<node TEXT="Evaluate the results"/>
</node>
<node TEXT="Results">

<node TEXT="The syringe body / lubricant transmissivity does change about 1.1%"/>
</node>
</node>
<node TEXT="Determine if the syringe body is oxidizing">

<node TEXT="Process">

<node TEXT="Start with the machine at room temperature"/>
<node TEXT="Ionizer is off"/>
<node TEXT="Use an unlubricated or cleaned syringe filled with oxygen"/>
<node TEXT="Record the UV transmissivity measurements over time"/>
<node TEXT="Include any sensor heating effects, if they exist from the above experiments"/>
<node TEXT="Evaluate the results"/>
</node>
<node TEXT="Results">

<node TEXT="The syringe body transmissivity does change about 0.1% to 0.2%"/>
</node>
</node>
</node>
<node TEXT="Experiments to Perform">

<node TEXT="Statistical Analysis on the Consistency of Syringe/Lubricant Oxidation"/>
<node TEXT="Determine temperature coeffients for UV sensor"/>
</node>
<node TEXT="Other">

<node TEXT="How to accurately compute ozone concentration?">

<node TEXT="Each syringe and syringe assembly has differing levels of transmissivity"/>
<node TEXT="Is there a fixed, proportional method that can be used?">

<node TEXT="OZ = beerslaw(UVoz)"/>
<node TEXT="UVoz = UVin/UVox"/>
<node TEXT="UVox: UV transmissivity reading through oxygen-fill syringe assembly"/>
<node TEXT="UVin: UV transmissivity reading in real-time"/>
<node TEXT="UVoz: UV transmissivity of ozone/oxygen mix"/>
</node>
</node>
</node>
</node>
<node TEXT="Low/Inconsistent Oxygen Concentration">

<node TEXT="Symptoms">

<node TEXT="Low oxygen output"/>
</node>
<node TEXT="Causes">

<node TEXT="Known">

<node TEXT="Build up of nitrogen inside enclosure"/>
<node TEXT="Zeolite compromised by moisture"/>
<node TEXT="A sneak path where air in the syringe and syringe tubing is entering the zeolite"/>
<node TEXT="Current tubing length between output of zeolite chamber and syringe valve"/>
</node>
<node TEXT="Possible">

<node TEXT="Time to compress the air into the zeolite chamber"/>
<node TEXT="Another path through which air is entering zeolite without going through the dessicant"/>
</node>
</node>
<node TEXT="Solutions">

<node TEXT="Replumb the system">

<node TEXT="So all air goes through the dessicant"/>
<node TEXT="So vacuuming the syringe does not allow outside air to enter zeolite"/>
<node TEXT="So the syringe valve is immediately next to the zeolite chamber"/>
<node TEXT="So all incoming air comes from the outside of the enclosure"/>
<node TEXT="So all outgoing air is exhausted to the outside of the enclosure"/>
</node>
</node>
<node TEXT="To Do">

<node TEXT="Test with the new, higher-volume pump to see if oxygen concentration improves"/>
<node TEXT="Determine if there are any other sneak paths where air that has not gone through the dessicant can enter the zeolite"/>
<node TEXT="Determine if it is even necessary to evacuate the zeolite or if venting it is sufficient"/>
</node>
</node>
<node TEXT="Poor System Ventilation">

<node TEXT="Symptoms">

<node TEXT="System gets too hot"/>
</node>
<node TEXT="Cause">

<node TEXT="Poor ventilation"/>
</node>
<node TEXT="Solution">

<node TEXT="Add small, muffin fan to rear of case"/>
<node TEXT="Add vent holes for air to circulate"/>
</node>
<node TEXT="To Do">

<node TEXT="Select an appropriate fan for the prototype"/>
<node TEXT="Select an appropriate fan for the redesign"/>
</node>
</node>
</node>
<node TEXT="Questions">

<node TEXT="Should sensor values be checked/cross-checked at each sample?">

<node TEXT="Yes, where possible"/>
</node>
</node>
<node TEXT="Sandbox"/>
</node>
</map>
