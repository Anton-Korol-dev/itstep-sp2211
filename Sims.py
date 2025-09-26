import random
class Human:
    def __init__(self, name="Human", job=None,
                home=None, car=None):
        self.name = name
        self.money = 100
        self.gladness = 50
        self.satiety = 50
        self.job = job
        self.car = car
        self.home = home

    def get_home(self):
        self.home = House()

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
        if self.home.food <=0:
            self.shopping("food")
        else:
            if self.satiety >=100:
                self.satiety = 100
                return
            self.satiety+=5
            self.home.food-=5

    def work(self):
        if self.car.drive():
            pass
        else:
            if self.car.fuel < 20:
                self.shopping("fuel")
                return
            else:
                self.to_repair()
            return
        self.money += self.job.salary
        self.gladness -= self.job.gladness_less
        self.satiety-=4

    def shopping(self, manage):
        if self.car.drive():
            pass
        else:
            if self.car.fuel < 20:
                manage = "fuel"
            else:
                self.to_repair()
                return
        if manage == "fuel":
            print("I bought fuel")
            self.money -= 100
            self.car.fuel += 100
        elif manage == "food":
            print("Bought food")
            self.money -= 50
            self.home.food += 50
            self.satiety += 5
        elif manage == "delicacies":
            print("Hooray! I bought delicacies")
            self.gladness += 10
            self.satiety += 2
            self.money -= 15

    def chill(self):
        self.gladness += 10
        self.home.mess += 5

    def clean_home(self):
        self.gladness -= 5
        self.home.mess = 0

    def to_repair(self):
        self.car.strength += 100
        self.money -= 50

    def days_indexes(self, day):
        day = f"Today the {day} of {self.name}'s life"
        print(f"{day:=^50}", "\n")
        human_indexes = self.name + "'s indexes"
        print(f"{human_indexes:^50}", "\n")
        print(f"Money - {self.money}")
        print(f"Satiety - {self.satiety}")
        print(f"Gladness - {self.gladness}")
        home_indexes = "Home indexes"
        print(f"{home_indexes:^50}", "\n")
        print(f"Food - {self.home.food}")
        print(f"Mess - {self.home.mess}")
        car_indexes = self.car.brand + " indexes"
        print(f"{car_indexes:^50}", "\n")
        print(f"Fuel - {self.car.fuel}")
        print(f"Strength - {self.car.strength}")

    def is_alive(self):
        if self.gladness <= 0:
            print("Depression...")
            return False
        if self.satiety <= 0:
            print("Dead...")
            return False
        if self.money < -500:
            print("Bankrupt...")
            return False
        return True
    
    def live(self, day):
        if self.is_alive() == False:
            return False
        if self.home == None:
            print("Settled in the house")
            self.get_home()
        if self.car == None:
            self.get_car()
            print(f"I bought a car {self.car.brand}")
        if self.job == None:
            self.get_job()
            if self.job != None:
                print(f"I got a job: {self.job.job} with salary {self.job.salary}")
            else:
                print("I can't get a job")
        self.days_indexes(day)
        dice = random.randint(1,4)
        if self.satiety < 20:
            print("I want to eat")
            self.eat()
        elif self.gladness < 20:
            if self.home.mess > 15:
                print("I want to chill, but there is so much mess...")
                self.clean_home()
            else:
                print("I want to chill")
                self.chill()
        elif self.money < 0:
            print("I need money...")
            self.work()
        elif dice == 1:
            print("Let`s chill!")
            self.chill()
        elif dice == 2:
            print("Time to work!")
            self.work()
        elif dice == 3:
            print("Cleaning time!")
            self.clean_home()
        elif dice == 4:
            print("I want delicacies!")
            self.shopping("delicacies")

class Auto:
    def __init__(self, brand_list):
        self.brand = random.choice(list(brand_list))
        self.strength = brand_list[self.brand]["strength"]
        self.fuel = brand_list[self.brand]["fuel"]
        self.consumption = brand_list[self.brand]["consumption"]
    
    def drive(self):
        if self.strength > 0 and self.fuel >= self.consumption:
            self.fuel -= self.consumption
            self.strength -= 1
            return True
        else:
            print("The car can't move")
            return False
class House:
    def __init__(self, brand_list):
        self.brand = random.choice(list(brand_list))
        self.fuel = brand_list[self.brand]["fuel"]
        self.strength = brand_list[self.brand]["strength"]
        self.consumption = brand_list[self.brand]["consumption"]
    
    def drive(self):
        if self.strength>0 and self.fuel>=self.consumption:
            self.fuel-=self.consumption
            self.strength-=1
            return True
        else:
            print("The car can't move")
            return False
        
class House:
    def __init__(self):
        self.food = 50
        self.mess = 0

job_list = {
    "Java developer":{"salary":50, "gladness_less":10},
    "Python developer":{"salary":40, "gladness_less":3},
    "C++ developer":{"salary":45, "gladness_less":25},
    "Rust developer":{"salary":70, "gladness_less":1}
}

brands_of_car = {
    "BMW":{"strength":100, "fuel":50, "consumption":6},
    "Lada":{"strength":40, "fuel":70, "consumption":10},
    "Volvo":{"strength":150, "fuel":60, "consumption":8},
    "Ferrari":{"strength":120, "fuel":80, "consumption":14}
}

class Job:
    def __init__(self, job_list):
        self.job = random.choice(list(job_list))
        self.salary = job_list[self.job]["salary"]
        self.gladness_less = job_list[self.job]["gladness_less"]

mark = Human(name="Mark")
for day in range(1,8):
    if mark.live(day) == False:
        break