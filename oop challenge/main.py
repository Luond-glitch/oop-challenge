from pet import Pet

def main():
    my_pet = Pet("Simba")

    my_pet.get_status()

    # Interact with the pet
    my_pet.eat()
    my_pet.play()
    my_pet.sleep()
    my_pet.train("roll over")
    my_pet.train("fetch")

    # Show tricks and status again
    my_pet.show_tricks()
    my_pet.get_status()

if __name__ == "__main__":
    main()
