from __future__ import print_function
# ------------------------------------------------------------------------------------------------
# Copyright (c) 2016 Microsoft Corporation
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and
# associated documentation files (the "Software"), to deal in the Software without restriction,
# including without limitation the rights to use, copy, modify, merge, publish, distribute,
# sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all copies or
# substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT
# NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
# DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
# ------------------------------------------------------------------------------------------------

# Manual test of the command handlers.
# Creates a small maze, then allows the user to type commands directly to control the agent.
# A full list of the commands available can be found in the MissionHandlers.xsd - Schemas/MissionHndlers.html
# eg typing "tpy 255" will teleport the agent to a y-position of 255 (and then let him plummet to his death).
# typing "turn 0.5" will begin the agent spinning on the spot, etc.

from builtins import input
from builtins import range
import MalmoPython
import os
import random
import sys
import time
import json

def GetMissionXML( current_seed ):
    return '''<?xml version="1.0" encoding="UTF-8" ?>
    <Mission xmlns="http://ProjectMalmo.microsoft.com" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  
    <About>
        <Summary>Manual input test</Summary>
    </About>
     
    <ServerSection>
        <ServerHandlers>
            <FlatWorldGenerator generatorString="3;7,2*3,2;1;" />
            <ServerQuitWhenAnyAgentFinishes/>
        </ServerHandlers>
        
    </ServerSection>

    <AgentSection>
        <Name>James Bond</Name>
        <AgentStart>
            <Placement x="-203.5" y="4" z="217.5"  /> 
            <Inventory>
                <InventoryItem slot="0" type="flint_and_steel" />
                <InventoryItem slot="1" type="snowball" quantity="64" />
                <InventoryItem slot="2" type="egg" quantity="64" />
                <InventoryItem slot="3" type="bone" quantity="64" />
                <InventoryItem slot="4" type="wheat" quantity="64" />
                <InventoryItem slot="5" type="wooden_sword" />
            </Inventory>
        </AgentStart>
        <AgentHandlers>
            <ContinuousMovementCommands />
            <DiscreteMovementCommands />
            <InventoryCommands />
            <AbsoluteMovementCommands />
            <MissionQuitCommands quitDescription="give_up"/>
        </AgentHandlers>
    </AgentSection>

  </Mission>'''
  

if sys.version_info[0] == 2:
    sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)  # flush print output immediately
else:
    import functools
    print = functools.partial(print, flush=True)

validate = True
my_mission = MalmoPython.MissionSpec(GetMissionXML("random"),validate)
my_mission.observeRecentCommands()

agent_host = MalmoPython.AgentHost()
try:
    agent_host.parse( sys.argv )
except RuntimeError as e:
    print('ERROR:',e)
    print(agent_host.getUsage())
    exit(1)
if agent_host.receivedArgument("help"):
    print(agent_host.getUsage())
    exit(0)

if agent_host.receivedArgument("test"):
    my_mission.timeLimitInSeconds(20) # else mission runs forever

agent_host.setObservationsPolicy(MalmoPython.ObservationsPolicy.LATEST_OBSERVATION_ONLY)

my_mission_record = MalmoPython.MissionRecordSpec()

max_retries = 3
for retry in range(max_retries):
    try:
        agent_host.startMission( my_mission, my_mission_record )
        break
    except RuntimeError as e:
        if retry == max_retries - 1:
            print("Error starting mission:",e)
            exit(1)
        else:
            time.sleep(2)

print("Waiting for the mission to start", end=' ')
world_state = agent_host.getWorldState()
while not world_state.has_mission_begun:
    print(".", end="")
    time.sleep(0.1)
    world_state = agent_host.getWorldState()
print()

summon = ''
with open('commands.txt', 'r') as rfile:
    num_lines = len(rfile.readlines())
    rfile.close()

# main loop:
while world_state.is_mission_running:
    # if agent_host.receivedArgument("test"): # when running as an integration test
    #     nb = "movesouth 1"
    #     time.sleep(1)
    # else:
    #     nb = input('Enter command: ')
    
    with open('commands.txt', 'r') as rfile:
        lines = rfile.readlines()
        if len(lines) > num_lines:
            print('lets go')
            num_lines = len(lines)
            summon = lines[-1]
    
    if(summon != ''):
        if summon.startswith('FIREBALL'):
            agent_host.sendCommand('pitch 1')
            time.sleep(.15)
            agent_host.sendCommand('pitch 0')
            time.sleep(.4)
            agent_host.sendCommand('hotbar.1 1')
            agent_host.sendCommand('hotbar.1 0')
            agent_host.sendCommand("use 1")
            agent_host.sendCommand("use 0")
            time.sleep(.4)
            agent_host.sendCommand('pitch -1')
            time.sleep(.15)
            agent_host.sendCommand('pitch 0')
            summon = ''
        elif summon.startswith('BIRD'):
            agent_host.sendCommand("hotbar.3 1")
            agent_host.sendCommand("hotbar.3 0")
            agent_host.sendCommand("use 1")
            agent_host.sendCommand("use 0")
            summon = ''
        elif summon.startswith('DRAGON'):
            agent_host.sendCommand("hotbar.2 1")
            agent_host.sendCommand("hotbar.2 0")
            agent_host.sendCommand("use 1")
            agent_host.sendCommand("use 0")
            summon = ''
        elif summon.startswith('DOG'):
            agent_host.sendCommand("hotbar.4 1")
            agent_host.sendCommand("hotbar.4 0")
            agent_host.sendCommand("attack 1")
            time.sleep(1)
            agent_host.sendCommand("attack 0")
            summon = ''
        elif summon.startswith('HORSE'):
            agent_host.sendCommand("hotbar.5 1")
            agent_host.sendCommand("hotbar.5 0")
            agent_host.sendCommand("attack 1")
            time.sleep(1)
            agent_host.sendCommand("attack 0")
            summon = ''
        elif summon.startswith('TIGER'):
            agent_host.sendCommand("hotbar.6 1")
            agent_host.sendCommand("hotbar.6 0")
            agent_host.sendCommand("attack 1")
            time.sleep(1)
            agent_host.sendCommand("attack 0")

    else:
        agent_host.sendCommand("use 0")



    # if(nb == 'fire'):
    #     agent_host.sendCommand('hotbar.1 1')
    #     agent_host.sendCommand('hotbar.1 0')
    #     agent_host.sendCommand("use 1")
    #     agent_host.sendCommand("use 0")
    #     nb = ''
    # elif(nb == 'snow'):
    #     agent_host.sendCommand("hotbar.2 1")
    #     agent_host.sendCommand("hotbar.2 0")
    #     agent_host.sendCommand("use 1")
    #     agent_host.sendCommand("use 0")
    #     nb = ''
    # elif(nb == 'egg'):
    #     agent_host.sendCommand("hotbar.3 1")
    #     agent_host.sendCommand("hotbar.3 0")
    #     agent_host.sendCommand("use 1")
    #     agent_host.sendCommand("use 0")
    #     nb = ''
        
    # agent_host.sendCommand(nb)

    world_state = agent_host.getWorldState()

print("Mission has stopped.")
