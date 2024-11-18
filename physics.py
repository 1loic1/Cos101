def calculate_force():
    mass=int(input('input mass:'))
    acceleration=int(input('input acceleration:'))
    force=mass * acceleration
    print(force)

def calculate_power():
    work=int(input('input work:'))
    time=int(input('input time'))
    power=work / time
    print(power)

def calculate_energy():
    power=int(input('input power'))
    time=int(input('input time'))
    energy=power * time
    print(energy)

def calculate_speed():
    distance=int(input('input distance'))
    time=int(input('input time'))
    speed=distance / time
    print(speed)

def calculate_time():
    distance=int(input('input distance'))
    speed=int(input('input speed'))
    time=distance / speed
    print(time)

def list():
    print('1.force')
    print('2.power')
    print('3.energy')
    print('4.speed')
    print('5.time')


    choice=int(input('what do you  want to learn:'))

    if choice == 1:
        calculate_force()

    elif choice == 2:
        calculate_power()

    elif choice == 3:
        calculate_energy()

    elif choice == 4:
        calculate_speed()

    elif choice == 5:
        calculate_time()

    else:
        print('invalid number')

list()