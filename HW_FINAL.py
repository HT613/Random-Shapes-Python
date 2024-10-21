import random
import tkinter as tk
import math

class Cube:
    def __init__(self, length=6, width=4, height=5):
        self.length = length
        self.width = width
        self.height = height
        
    def findArea(self):
        area = 2*((self.length*self.width)+(self.width*self.height)+(self.height*self.length))
        return area
    
    def display(self):
        return "Cube"

    def setLength(self, length):
        self.length = length

    def getLength(self):
        return self.length

    def setWidth(self, width):
        self.width = width

    def getWidth(self):
        return self.width

    def setHeight(self, height):
        self.height = height

    def getHeight(self):
        return self.height

    
class Circle:
    def __init__(self, radius=4.3):
        self.radius = radius
        
    def findArea(self):
        area = math.pi * math.pow(self.radius,2)
        return area
    
    def display(self):
        return "Circle"

    def setRadius(self, radius):
        self.radius = radius

    def getRadius(self):
        return self.radius
    
class Square:
    def __init__(self, side=4.0):
        self.side = side
        
    def findArea(self):
        area = 2 * self.side
        return area
        
    def display(self):
        return "Square"

    def setSide(self, side):
        self.side = side

    def getSide(self):
        return self.side
    
def prtToFile(shapes, filename):
    with open(filename, 'w') as file:
        for shape in shapes:
            file.write(f"{shape.display()}: {shape.findArea()}\n")


def prtToSc(shapes):
    print("Printing results on the screen:")
    print("-----------------------------")
    for shape in shapes:
        print(f"{shape.display()}: {shape.findArea()} square units")
    print("-----------------------------")


def prtToWindow(shapes):
    root = tk.Tk()
    root.geometry("500x200")
    root.title("Shapes and Their Areas")

    textArea = tk.Text(root, height=10, width=30)
    textArea.pack()

    for shape in shapes:
        textArea.insert(tk.END, f"{shape.display()}: {shape.findArea()}\n")

    # Bring the pop-up window to the front
    root.lift()

    root.mainloop()

def main():
    shapes = []  # Initialize shapes array outside the loop

    while True:
        # Clear the shapes array before generating new shapes
        shapes.clear()

        for i in range(10):
            choice = random.randint(0, 2)
            if choice == 0:
                shapes.append(Circle())
            elif choice == 1:
                shapes.append(Square())
            else:
                shapes.append(Cube())

        print("Choose method of outputting results:")
        print("1. Save the output to a file (FILE I/O)")
        print("2. Print output onto IDLE Shell")
        print("3. Display output onto pop-up window (Graphical User Interface)")
        print("4. Exit")

        option = input("Enter your choice (1, 2, 3, 4): ")

        if option == '1':
            filename = input("Please enter the name of the file to save the output in: ")
            prtToFile(shapes, filename)
        elif option == '2':
            prtToSc(shapes)
        elif option == '3':
            prtToWindow(shapes)
        elif option == '4':
            print("Exiting program.")
            break
        else:
            print("Oops! It appears you have entered an invalid input. Reminder, type in 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()
