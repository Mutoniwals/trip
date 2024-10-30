from shaps import shap,rectangle,triangle,circle
shape = shap()
rect = rectangle(4,8)
tria = triangle(5,10)
circle = circle(10)


print(shape.compute_area())
print(rect.compute_area())
print(tria.compute_area())
print(circle.compute_area())