import numpy 
import matplotlib.pyplot as m
# a = 0
# with open('./data/data.npy', 'rb') as f:
#     a = numpy.load(f)

# b =0
# with open('./data/data2.npy', 'rb') as f:
#     b = numpy.load(f)

# m.plot(a, label="front leg")
# m.plot(b, label="back leg")
x = numpy.linspace(0, 2*numpy.pi, 1000)
m.plot(x)
m.legend()
m.show()