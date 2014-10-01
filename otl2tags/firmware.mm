<map version="0.8.0">
<node TEXT="Minimus Spine Firmware for Board V2.0">

<node TEXT="[_] 38% Firmware">

<node TEXT="[_] 69% Drivers">
<richcontent TYPE="NOTE"><html><head></head><body>blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blahblah</body></html></richcontent>

<node TEXT="[_] 20% LCD">

<node TEXT="[X] 100% text printing"/>
<node TEXT="[_] 0% screen objects"/>
<node TEXT="[_] 0% button objects"/>
<node TEXT="[_] 0% window objects"/>
<node TEXT="[_] 0% graphing objects"/>
</node>
<node TEXT="[X] 100% HV source"/>
<node TEXT="[X] 100% UV source"/>
<node TEXT="[_] 75% UV sensor">

<node TEXT="[X] 100% filtering"/>
<node TEXT="[X] 100% logging"/>
<node TEXT="[X] 100% scaling"/>
<node TEXT="[_] 0% error detection"/>
</node>
<node TEXT="[_] 75% pressure sensor">

<node TEXT="[X] 100% filtering"/>
<node TEXT="[X] 100% logging"/>
<node TEXT="[X] 100% scaling"/>
<node TEXT="[_] 0% error detection"/>
</node>
<node TEXT="[_] 75% vacuum sensor">

<node TEXT="[X] 100% filtering"/>
<node TEXT="[X] 100% logging"/>
<node TEXT="[X] 100% scaling"/>
<node TEXT="[_] 0% error detection"/>
</node>
<node TEXT="[_] 50% lid closure">

<node TEXT="[X] 100% detection"/>
<node TEXT="[_] 0% error detection"/>
</node>
<node TEXT="[_] 50% syringe detection">

<node TEXT="[X] 100% detection"/>
<node TEXT="[_] 0% error detection"/>
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
<node TEXT="[_] 8% Application">

<node TEXT="[_] 16% Screens">

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
<node TEXT="[_] 0% Oxygen Cycle">

<node TEXT="[_] 0% Syringe Insertion"/>
<node TEXT="[_] 0% Evacuation"/>
<node TEXT="[_] 0% Oxygen Concentration"/>
<node TEXT="[_] 0% Fill Syringe"/>
<node TEXT="[_] 0% Syringe Error"/>
</node>
<node TEXT="[_] 0% Ozone Cycle">

<node TEXT="[_] 0% Ionize Oxygen"/>
<node TEXT="[_] 0% Ionize Error"/>
<node TEXT="[_] 0% Ozone Decay"/>
</node>
</node>
<node TEXT="[_] 0% Processes">

<node TEXT="[_] 0% GUI"/>
<node TEXT="[_] 0% Worker">

<node TEXT="[_] 0% Idle">

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
<node TEXT="[_] 0% Evacuate System">

<node TEXT="State: stEvacuate"/>
<node TEXT="[_] 0% Function"/>
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
<node TEXT="[_] 0% Evaucuate Syringe">

<node TEXT="State: stEvacSyringe"/>
<node TEXT="[_] 0% Function"/>
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
<node TEXT="[_] 0% Concentrate Oxygen">

<node TEXT="State: stOxygen"/>
<node TEXT="[_] 0% Function"/>
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
<node TEXT="[_] 0% Fill Syringe">

<node TEXT="State: stFillSyringe"/>
<node TEXT="[_] 0% Function"/>
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
<node TEXT="[_] 0% Equalize Syringe Pressure">

<node TEXT="[_] 0% State: stFillSyringe"/>
<node TEXT="[_] 0% Function"/>
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
<node TEXT="[_] 0% Izonize Oxygen">

<node TEXT="State: stIonize"/>
<node TEXT="[_] 0% Function"/>
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
<node TEXT="[_] 0% Ozone Decay">

<node TEXT="State: stDecay"/>
<node TEXT="[_] 0% Function"/>
<node TEXT="[_] 0% Tests"/>
<node TEXT="[_] 0% Logging"/>
</node>
<node TEXT="[_] 0% Process Complete">

<node TEXT="State: stComplete"/>
<node TEXT="[_] 0% Function"/>
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
<node TEXT="[_] 0% Debug"/>
<node TEXT="[_] 0% Monitor"/>
</node>
</node>
</node>
<node TEXT="Devices to Test">

<node TEXT="Pressure sensor"/>
<node TEXT="Vacuum sensor"/>
<node TEXT="UV sensor"/>
<node TEXT="Lid switch"/>
<node TEXT="Syringe switch"/>
<node TEXT="Humidity sensor"/>
<node TEXT="Pump"/>
<node TEXT="Valve1"/>
<node TEXT="Valve2"/>
<node TEXT="Valve3"/>
<node TEXT="Valve4"/>
<node TEXT="Valve5"/>
</node>
<node TEXT="Sandbox">

<node TEXT="Worker States">

<node TEXT="Idle"/>
<node TEXT="Evacuate System"/>
<node TEXT="Evaucuate Syringe"/>
<node TEXT="Concentrate Oxygen"/>
<node TEXT="Fill Syringe"/>
<node TEXT="Izonize Oxygen"/>
<node TEXT="Ozone Decay"/>
<node TEXT="Process Complete"/>
<node TEXT="Process Soft Failure"/>
<node TEXT="Process Hard Failure"/>
</node>
<node TEXT="Questions">

<node TEXT="Should sensor values be checked/cross-checked at each sample?"/>
</node>
</node>
</node>
</map>
