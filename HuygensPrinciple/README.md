# HuygensPrinciple
An animation that demonstrates Huygens Priniple. Some technical accuracy was of course sacrificed for aesthetics.

The animation shows a single point source that emits a wave, the crest of which is shown as the white circle. After this first wave crest travels a bit, some points on it are then used as other point sources for new wave crests. As the waves travel outward, it becomes clear that the wavefront is still a circular wave centered at the original center. One could imagine that as more points on the original wavefront are treated as point sources, the approximation would be better and the superposition of the secondary wavefronts would be the same as the original wavefront.

![](HuygensPrinciple.gif)

The creation of this animation was significantly simplified with the use of mplanimations, as it only requires 62 lines of code. The drawback, however, is that the code may be difficult to read because I used many tricks that can certainly be unclear.
