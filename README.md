# complex-fractals
Explore fractal effects when looking for roots in complex space.

## Formal Analysis
On the top left diagram, four different colours appear depending on what seed point you use to \
find a root. The light blue, green, orange and dark red correspond to the roots -i, +1, +i and -1, \
respectively. \

In certain areas of the diagram, a lot of different roots are found over a small range of seed \
points. This means changing the initial conditions (the seed point) by a tiny amount has a large \
effect on the eventual outcome. That is exactly what a chaotic system is. \

The top right diagram displays the number of iterations needed to get close to the root for \
each seed point (the colourbar gives the number of iterations corresponding to each colour). \
Along the lines where the imaginary part is equal to or the negative of the real part, you can \
see a distinct arrowhead-like shape repeating itself. As you zoom in on one small part of this \
line, you can see this same shape emerging again. Only this time, the shape is flipped across a \
line perpendicular to the line along which the arrowheads are distributed. This goes on \
indefinitely as you zoom in even further and is shown in the lower two subplots. Therefore, the \
images are fractal in nature.

[Sample programme output](sample_outputs/root_fractals.png)
