scenarioFile = open('ScenarioSet.call','r')
readScenario = scenarioFile.read()
devideScenario = readScenario.split('[')

for scenario in devideScenario:
    lines = scenario.split('\n')
    for line in lines:
        if 'ScenarioName' in line:
            need = line.split('=')
            test = need[1]
            print(test)
            new = open(f'{test}.call','w')
            new.write('['+scenario)
        
scenarioFile.close()