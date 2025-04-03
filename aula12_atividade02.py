class Animal:
    def fazer_som(self):
        pass

class Cachorro(Animal):
    def fazer_som(self):
        print("Au Au!")

class Gato(Animal):
    def fazer_som(self):
        print("Miau!")

def fazer_barulho(animal):
    animal.fazer_som()


if __name__ == "__main__":

    meu_cachorro = Cachorro()
    meu_gato = Gato()

    fazer_barulho(meu_cachorro)
    fazer_barulho(meu_gato)