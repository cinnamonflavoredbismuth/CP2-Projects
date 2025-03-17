#Cecily Strong Libraries Notes
import matplotlib.pyplot as plt # type: ignore
import numpy as np # type: ignore
from faker import Faker # type: ignore
#MatPlotLib
'''fig, ax = plt.subplots()             # Create a figure containing a single Axes.
ax.plot([1, 2, 3, 4], [1, 4, 2, 3])  # Plot some data on the Axes.
plt.show()'''

#Faker

fake = Faker()

fake.name()

fake.address()

fake.text()

for _ in range(10):
  print(fake.name())
