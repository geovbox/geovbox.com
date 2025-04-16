---
title: Simulation of Infectious Disease Spread Process Using Three Lines of Code (Discrete Element Method)
date: 2020-03-19
categories:
    - Discrete Element Communication
authors:
    - Li Changsheng
images:
slug: 20200317
---

> This model does not fit infectious disease transmission and is solely for learning about the discrete element method.

### 1. Restricting Movement

In the Hertz contact model of discrete elements, the stiffness coefficient of contact is related to the overlap amount of particles. Thus, it needs to be updated at each time step. When calculating the contact stiffness coefficient, incorporating the following three lines of pseudocode and modifying the color of contact particles can simulate the infectious disease spread process.

- Red: Infectious source
- Blue: Susceptible particles that become infected upon contact with red

```c
	if ((spheres[index_o].color == red) || (spheres[index_a].color == red))
	{
		spheres[index_o].color = red;
		spheres[index_a].color = red;
	}
```

- Assumption: A closed space contains 200 healthy blue particles, all of which move automatically, and contact leads to infection with no chance of recovery.
- Boundary Condition: A particle numbered 0 suddenly becomes infected with the red virus, and 10% (20 particles) start moving and activate other particles.
- Simulation Results:
  - Infection gradually spreads from the first case outward; the closer to the red particle numbered 0, the faster the infection occurs.
  - In the case of free movement without damping, only one particle survives.
  - When free movement occurs with damping, the left half of the particles has not yet been infected.
    {{< figure src="damp0.0.gif" title="Experiment 1 Damping=0.0" >}}
    {{< figure src="damp0.2.gif" title="Experiment 2 Damping=0.2" >}}

### 2. Herd Immunity

Professor Zhang from China University of Geosciences (Wuhan) suggested that 60% of the particles acquire immunity.

- Red: Infectious source
- Blue: Susceptible particles that become infected upon contact with red
- Green: Immune particles that are not infected by the red particles and do not transmit to others.

```c
	// Only if both are not green, consider mutual infection
	if ((spheres[index_o].color != green) && (spheres[index_a].color != green))
	{
		if ((spheres[index_o].color == red) || (spheres[index_a].color == red))
		{
			spheres[index_o].color = red;
			spheres[index_a].color = red;
		}
	}
```

- Experiment 3: In a closed space, there are 200 healthy blue particles, (60%) 120 of which have acquired immunity as green particles. All particles move automatically, with blue particles becoming infected upon contact with red and permanently turning red.
- Boundary Condition: A particle numbered 0 suddenly becomes infected with the red virus; 10% (20 particles) start moving and activate other particles.
- Simulation Results:
  - When all are susceptible, **199** particles become infected (red).
  - With 60% acquiring immunity, **14** particles become infected (red).
    {{< figure src="damp0.0.gif" title="Experiment 1 Everyone is Susceptible" >}}
    {{< figure src="immune60.gif" title="Experiment 3 60% Acquired Immunity" >}}

---

Translator: Zhu suqin

