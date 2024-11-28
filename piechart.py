import matplotlib.pyplot as plt
students = [20,100,70,50,90]
grade = ['Rice','Beans','cereals','Cocoa','Garri']
exp = [0,0,0.2,0,0]
plt.pie(students, labels = grade, startangle = 90)
plt.show()