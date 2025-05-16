from module5_mod import NumberProcessor
def main():
    processor = NumberProcessor()
    n = int(imput("Enter a positive integer N:"))
    processor.insert_numbers(n) 
    x = int(input("Enter the number to search for: "))
    result = processor.find.index(x)
    print("Index:" if result != -1 else "Not found:", result)
  if __name__ =="__main__":
    main()