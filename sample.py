
age = 450


class User:  # z dużej litery klasy

    def __init__(self, age, name):
        print(
            'jstem inicjalizatorem, który wywołuje się zawsze podczas konstrukcji obiektu')
        self.age = age
        self.name = name

        self.ageInFuture = age + 1

    def print_age(self, message):
        print(message, "wiek: ", self.age, self.name)


user1 = User(30, 'Arek')
user2 = User(20, 'Mirek')


user1.print_age("dodatkowy tekst")
user2.print_age("dodtakowy tekst inny")

print(user1.ageInFuture)
