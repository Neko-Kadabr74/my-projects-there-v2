import time

def countdown(seconds):
    for i in range(seconds, 0, -1):
        print(f"exiting in {i}seconds.......", end-"\r")
        time.sleep(1)
        print("exiting, second ago!")
def main():
    entered_password = input("Enter your, or maybe someone else password. (tyoe 'kaboom' to exit): ")

    if entered_password == "kaboom":
        countdown(5)
        break
    elif entered_password == password:
        print("GRANTED ACCESS FOR... uhm... something..")
    else: 
        print("ACCESS TO SOMETHING WAS DENIED!") 

if __name__ == "__main__":
    main()