def main():
    while True:
     try: 
         number = float(input("Enter a number. please.. >.>"): "")
         if number == 0:
            print("this number is equal to zero. :0")

         elif number in [10, 20, 30, 40, 50, 60, 70, 80, 90]:
            print("left digit is not zero.")
     
         else:
            print("this number is diffrent from zero ;|")
     except ValueError:
        print("Words are not numbers.")
if __name__ == "__main__":
    main()