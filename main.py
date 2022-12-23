import random


class Human:
    def __init__(self, name='Human', job=None, home=None, car=None):
        self.name = name
        self.money = 100
        self.gladness = 50
        self.satiety = 50
        self.job = job
        self.home = home
        self.car = car

    def get_home(self):
        self.home = Home()

    def get_car(self):
        self.car = Auto(brands_of_car)

    def get_job(self):
        if self.car.drive():
            pass
        else:
            self.to_repair()
            return
        self.job = Job(job_list)

    def eat(self):
        if self.home.food <= 0:
            self.shopping('food')
        else:
            if self.satiety > 100:
                self.satiety = 100
                return
            self.satiety += 5
            self.home.food -= 5

    def work(self):
        if self.car.drive():
            pass
        else:
            self.to_repair()
            return
        self.money += self.job.salary
        self.gladness += self.job.gladness
        self.satiety -= 5

    def shopping(self, manage):
        if self.car.drive():
            pass
        else:
            if self.car.fuel < 10:
                manage = 'fuel'
            else:
                self.to_repair()
                return
        if manage == 'fuel':
            print('I bought fuel....')
            self.money -= 50
            self.car.fuel += 100
        elif manage == 'food':
            print('Bought food....')
            self.money -= 20
            self.home.food += 20
        elif manage == 'delicacies':
            print('Happy!')
            self.gladness += 10
            self.satiety += 2
            self.money -= 15

    def chill(self):
        self.gladness += 15
        self.home.mess += 5

    def clean_home(self):
        self.home.mess = 0
        self.gladness -= 5

    def to_repair(self):
        self.car.strength += 100
        self.money -= 50

    def days_indexes(self, day):
        day = f'Today the {day} of {self.name} life:'
        print(f'{day:=^50}', "\n")
        human_indexes = self.name + "'s indexes"
        print(f'{human_indexes:^50}', '\n')
        print(f'Money - {self.money}')
        print(f'Satiety - {self.satiety}')
        print(f'Gladness - {self.gladness}')
        # home_indexes = 'Home indexes'
        print(f'{"Home indexes":=^50}', '\n')
        print(f'Food - {self.home.food}')
        print(f'Mess - {self.home.mess}')
        car_indexes = f'{self.car.brand} car indexes'
        print(f'{car_indexes:^50}', '\n')
        print(f'Fuel - {self.car.fuel}')
        print(f'Strength - {self.car.strength}')

    def is_alive(self):
        if self.gladness < 0:
            print('Depression..')
            return False
        if self.satiety <= 0:
            print('Dead....')
            return False
        if self.money < -100:
            print('Bankrupt...')
            return False

    def live(self, day):
        if self.is_alive() == False:
            return False
        if self.home is None:
            print('Settled in the home')
            self.get_home()
        if self.car is None:
            self.get_car()
            print(f'I bought a car {self.car.brand}')
        if self.job is None:
            self.get_job()
            print(f"I don't have a job, going to get a job {self.job.job}"
                  f"with salary {self.job.salary}")
        self.days_indexes(day)
        dice = random.randint(1, 4)
        if self.satiety < 20:
            print('Time go eat')
            self.eat()
        elif self.gladness < 20:
            if self.home.mess > 15:
                print('I want to chill, but there is so mess...')
                self.clean_home()
            else:
                print("Let's chill")
                self.chill()
        elif self.money < 10:
            print('Start working!')
            self.work()
        elif self.car.strength < 10:
            print('I need to repair my car')
            self.to_repair()
        elif dice == 1:
            print('Time chill')
            self.chill()
        elif dice == 2:
            print('Start working')
            self.work()
        elif dice == 3:
            print('Clean home')
            self.clean_home()
        elif dice == 4:
            print('Time shopping')
            self.shopping(manage='delicacies')


class Auto:
    def __init__(self, brand_list):
        self.brand = random.choice(list(brand_list))
        self.fuel = brand_list[self.brand]['fuel']
        self.strength = brand_list[self.brand]['strength']
        self.consumption = brand_list[self.brand]['consumption']

    def drive(self):
        if self.strength > 0 and self.fuel >= self.consumption:
            self.strength -= 1
            self.fuel -= self.consumption
            return True
        else:
            print('The car cannot move!')
            return False


class Home:
    def __init__(self):
        self.food = 0
        self.mess = 0


class Job:
    def __init__(self, job_list):
        self.job = random.choice(list(job_list))
        self.salary = job_list[self.job]['salary']
        self.gladness = job_list[self.job]['job_gladness']


job_list = {' lawyer': {'salary': 1500, 'job_gladness':1},
            ' shop assistant': {'salary': 15, 'job_gladness': 4},
            'fisherman': {'salary': 40, 'job_gladness': 20},
            'computer technician': {'salary': 1500, 'job_gladness': 9},
            '  judge': {'salary': 1200, 'job_gladness': 1},
            ' cook': {'salary': 1000, 'job_gladness': 11},}

brands_of_car = {'BMW': {'fuel': 90, 'strength':100,'consumption':13},
                 'Touta': {'fuel':80 ,'strength':60, 'consumption':7},
                 'ВАЗ': {'fuel':30 ,'strength':30, 'consumption':11},
                 'Mitsubishi': {'fuel': 150,'strength':140, 'consumption':5},
                'Lamborghini': {'fuel': 350,'strength':350, 'consumption':3},
                  'Mercedes-Benz': {'fuel': 300,'strength':400, 'consumption':4},
                  'Porha': {'fuel': 180,'strength':200, 'consumption':5},
                  'Alfa Romeo': {'fuel': 60, 'strength':80,'consumption':7},}

nick = Human(name='Nick')
for day in range(1, 8):
    if nick.live(day) == False:
        break