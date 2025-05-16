
class NumberProcessor:
  def_init_(self):
  self.numbers = []
def insert_number(self, count):
  for _ in range (count):
    number = int(input("Enter a number: "))
    self.numbers.append(number)
def find_index(self,x):
  if x in self.numbers:
    return self.numbers.index(x) + 1 #1-based index
    return -1

def main():
    processor = NumberProcessor()
    n = int(imput("Enter a positive integer N:"))
    processor.insert_numbers(n) 
    x = int(input("Enter the number to search for: "))
    result = processor.find.index(x)
    print("Index:" if result != -1 else "Not found:", result)
  if __name__ =="__main__":
    main()
