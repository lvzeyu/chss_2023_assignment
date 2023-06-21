class Person:
    def __init__(self, name, birth, current_year=2023):
        self.name = name
        self.birth = birth
        self.current_year = current_year
        
    def say_hello(self):
        print("Hello, my name is", self.name)
    
    def print_birth(self):
        print("{} was born in {}".format(self.name,self.birth))
    
    def age(self):
        return self.current_year - self.birth
    
    

class Address:
    def __init__(self, state, city, street):
        self.state = state
        self.city = city
        self.street = street

    def get_full_address(self):
        return self.state, self.city, self.street
    
def main():
    person1 = Person("John Doe", 30)
    person2 = Person("Jane Smith", 25)
    
    person1.say_hello()
    person2.say_hello()

if __name__ == "__main__":
    main()
    