#Non-diffracting Bessel beam.

from LightPipes import *
import matplotlib.pyplot as plt

wavelength=632.8*nm
size=5.0*mm
N=500
phi=179.8*deg
n1=1.5
z=80*cm

F=Begin(size,wavelength,N)
F=GaussHermite(F, 2*mm)
F=Axicon(phi,n1,0,0,F)
F=Forvard(z,F)
I=Intensity(2,F)

plt.imshow(I)
plt.show()
