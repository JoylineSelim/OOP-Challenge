from pet import Pet
import time

def main():
    print("✨ Welcome to the Virtual Pet Simulator! ✨")
    pet_name = input("What is your pet's name? 🐶: ")
    pet_type = input("What type of pet is it? (dog/cat/dragon/etc.): 🐉: ")

    my_pet = Pet(pet_name, pet_type)

    actions = ["eat", "sleep", "play", "dance", "train", "status", "tricks", "exit"]

    while True:
        print("\nAvailable actions: eat, sleep, play, dance, train, status, tricks, exit")
        choice = input(f"What would you like {my_pet.name} to do? ➡️ ").lower()

        if choice == "eat":
            my_pet.eat()
        elif choice == "sleep":
            my_pet.sleep()
        elif choice == "play":
            my_pet.play()
        elif choice == "dance":
            my_pet.dance()
        elif choice == "train":
            trick = input("Enter a trick to teach: 🎓 ")
            my_pet.train(trick)
        elif choice == "status":
            my_pet.get_status()
        elif choice == "tricks":
            my_pet.show_tricks()
        elif choice == "exit":
            print(f"👋 Goodbye! {my_pet.name} waves at you!")
            break
        else:
            print("❌ Invalid action. Please choose again.")

        time.sleep(1)  # Makes the game feel a little smoother

if __name__ == "__main__":
    main()

