from week1 import Pet

def main():
    max_pet = Pet("Max")
    print(f"Creating pet: {max_pet.name} 🐶")

    max_pet.eat()
    max_pet.play()
    max_pet.sleep()
    max_pet.train("roll over")
    max_pet.train("play dead")
    max_pet.get_status()
    max_pet.show_tricks()

if __name__ == "__main__":
    main()
