import os
import subprocess

def genre_prediction():
    subprocess.run(["python", "test_model.py"])

def audio_conversion():
    subprocess.run(["python", "final_translate.py"])

def menu():
    while True:
        print("\nSelect an option:")
        print("1. Predict Genre of Movie Summary")
        print("2. Convert Movie Summary to Audio")
        print("3. Exit")
        
        choice = input("Enter your choice (1/2/3): ")
        
        if choice == '1':
            genre_prediction()
        elif choice == '2':
            audio_conversion()
        elif choice == '3':
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    menu()
