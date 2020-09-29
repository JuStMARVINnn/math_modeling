line1 = float(input("Первая сторона : "))
line2 = float(input("Вторая сторона : "))
line3 = float(input("Третья сторона : "))

if (line1 + line2 > line3 and
    line1 + line3 > line2 and
    line2 + line3 > line1):
    print("Треугольник существует")
    
    if line1 == line2 == line3:
        print("Треугольник равносторонний")
    elif (line1 == line2 or
          line2 == line3 or
          line1 == line3):
        print("Треугольник равнобедренный")
    else:
        print("Треугольник разносторонний")
        
else:
    print("Треугольник не существует")