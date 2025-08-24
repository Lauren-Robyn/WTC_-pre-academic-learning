def main():
    while True:
         try:
          fraction = (input("Fraction: "))
          numerator,denominator = fraction.split("/")
          numerator = int(numerator)
          denominator = int(denominator)

          #handle division early
          if denominator == 0:
               continue
          #reject improper fractions
          if numerator < 0 or numerator > denominator:
               continue

          percentage = fuel(numerator, denominator)
          if percentage <= 1:
               print("E")
          elif percentage >= 99:
               print("F")
          else:
               print(f"{percentage}%")
          break

         except (ValueError, ZeroDivisionError):
               pass

def fuel(numerator, denominator):
     percentage = round((numerator / denominator)* 100)
     return percentage

main()