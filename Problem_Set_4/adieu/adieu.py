import inflect

engine_object = inflect.engine()
names=[]
while True:
      try:
        name = input("Name: ").title()
        names.append(name)
        result = engine_object.join(names)
      except EOFError:
                    print (f"\nAdieu, adieu, to {result}")
                    break