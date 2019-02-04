'''
Explore fractal effects of finding roots using the Newton Raphson method in complex
space. Visualises output at different zoom levels.
'''

import matplotlib.pyplot as pyplot
import matplotlib.cm

from core_funcs import *

if __name__ == '__main__':
    x0, x1 = -2, 2
    y0, y1 = -2, 2
    N_POINTS = 400
    dx = (x1 - x0) / N_POINTS
    dy = (y1 - y0) / N_POINTS

    y_axis = numpy.arange(y0, y1, dy)
    x_axis = numpy.arange(x0, x1, dx)

    dat1 = numpy.zeros((len(y_axis), len(x_axis)))
    dat2 = numpy.zeros((len(y_axis), len(x_axis)))

    for iy, y in enumerate(y_axis):
        for ix, x in enumerate(x_axis):
            J = complex(x,y)
            dat1[iy, ix] = NRmethod(J)[0]
            dat2[iy, ix] = NRmethod(J)[1]

    # Zooming in now to explore fractal nature of this method.
    x0_2, x1_2 = 0.5, 1
    y0_2, y1_2 = 0.5, 1
    dx_2 = (x1_2 - x0_2) / N_POINTS
    dy_2 = (y1_2 - y0_2) / N_POINTS

    y_axis_2 = numpy.arange(y0_2, y1_2, dy_2)
    x_axis_2 = numpy.arange(x0_2, x1_2, dx_2)

    dat3 = numpy.zeros((len(y_axis_2), len(x_axis_2)))

    for iy, y in enumerate(y_axis_2):
        for ix, x in enumerate(x_axis_2):
            J = complex(x,y)
            dat3[iy, ix] = NRmethod(J)[1]

    # Zooming in further.
    x0_3, x1_3 = 0.713, 0.76
    y0_3, y1_3 = 0.713, 0.76
    dx_3 = (x1_3 - x0_3) / N_POINTS
    dy_3 = (y1_3 - y0_3) / N_POINTS

    y_axis_3 = numpy.arange(y0_3, y1_3, dy_3)
    x_axis_3 = numpy.arange(x0_3, x1_3, dx_3)

    dat4 = numpy.zeros((len(y_axis_3), len(x_axis_3)))

    for iy, y in enumerate(y_axis_3):
        for ix, x in enumerate(x_axis_3):
            J = complex(x,y)
            dat4[iy, ix] = NRmethod(J)[1]

    pyplot.figure()
    pyplot.subplot(2,2,1)
    pyplot.title('root found for seed points z')
    pyplot.ylabel('Im(z)')
    im = pyplot.imshow(dat1,extent=(x0,x1,y0,y1),origin='lower')
    pyplot.xticks([-2,-1,0,1,2]) # less clutter this way.
    pyplot.subplot(2,2,2)
    pyplot.title('Number of iterations needed')
    pyplot.ylabel('Im(z)')
    im = pyplot.imshow(dat2,extent=(x0,x1,y0,y1),origin='lower')
    pyplot.xticks([-2,-1,0,1,2])
    pyplot.colorbar(im,orientation='vertical')
    pyplot.subplot(2,2,3)
    pyplot.title('First zoom level')
    pyplot.xlabel('Re(z)') # this only on the lower subplots, in order to make it less cluttered.
    pyplot.ylabel('Im(z)')
    im = pyplot.imshow(dat3,extent=(x0_2,x1_2,y0_2,y1_2),origin='lower')
    pyplot.subplot(2,2,4)
    pyplot.title('Second zoom level')
    pyplot.xlabel('Re(z)')
    pyplot.ylabel('Im(z)')
    im = pyplot.imshow(dat4,extent=(x0_3,x1_3,y0_3,y1_3),origin='lower')
    pyplot.show()
