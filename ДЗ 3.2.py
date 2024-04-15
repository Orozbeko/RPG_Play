class Computer:
    def __init__(self, cpu, memory):
        self.__cpu = cpu
        self.__memory = memory

    def get_cpu(self):
        return self.__cpu

    def set_cpu(self, cpu):
        self.__cpu = cpu

    def get_memory(self):
        return self.__memory

    def set_memory(self, memory):
        self.__memory = memory

    def make_computations(self):
        return self.__cpu + self.__memory

    def __str__(self):
        return f"Computer(CPU: {self.__cpu}, Memory: {self.__memory})"

    def __eq__(self, other):
        return self.__memory == other.get_memory()

    def __lt__(self, other):
        return self.__memory < other.get_memory()

    def __le__(self, other):
        return self.__memory <= other.get_memory()

    def __gt__(self, other):
        return self.__memory > other.get_memory()

    def __ge__(self, other):
        return self.__memory >= other.get_memory()

    def __ne__(self, other):
        return self.__memory != other.get_memory()


class Phone:
    def __init__(self):
        self.__sim_cards_list = []

    def get_sim_cards_list(self):
        return self.__sim_cards_list

    def set_sim_cards_list(self, sim_cards_list):
        self.__sim_cards_list = sim_cards_list

    def call(self, sim_card_number, call_to_number):
        sim_card = self.__sim_cards_list[sim_card_number - 1]
        print(f"Идет звонок на номер {call_to_number} с сим-карты-{sim_card_number} - {sim_card}")


class SmartPhone(Computer, Phone):
    def __init__(self, cpu, memory):
        Computer.__init__(self, cpu, memory)
        Phone.__init__(self)

    def use_gps(self, location):
        print(f"Путь до локаций: {location}")

    def __str__(self):
        return f"SmartPhone(CPU: {self.get_cpu()}, Memory: {self.get_memory()}, Sim Cards: {self.get_sim_cards_list()})"


computer1 = Computer("Intel i5", 512)
phone1 = Phone()
smartphone1 = SmartPhone("Snapdragon 855", 64)
smartphone2 = SmartPhone("Apple A13", 128)


phone1.set_sim_cards_list(["Beeline", "Megacom", "O!</span>"])

print(computer1)
print(phone1)
print(smartphone1)
print(smartphone2)





