import python_particle
import cython_particle

py_particle = python_particle.Particle(1.0, 2.0, 3.0)
cy_particle = cython_particle.Particle(1.0, 2.0, 3.0)

print(py_particle.get_momentum())
print(cy_particle.get_momentum())
