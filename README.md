# PyBullet RL Example
Simple PyBullet examples for RL people who have difficulties understanding how to use PyBullet like me

```python
import gym
import pybullet_envs
import pybullet as p

import time

# p.GUI for graphical version similar to the MuJoCo one
# it will shut down on my pc though
p.connect(p.DIRECT)

# check the link below for some common environments
# https://github.com/bulletphysics/bullet3/releases
env = gym.make('AntBulletEnv-v0')

# it is different from how MuJoCo renders environments
# it doesn't differ too much to me w/ and w/o mode='human'
env.render()

# you should call render() before reset()
env.reset()

for _ in range(10000):
	# call sleep() so that it can render at a normal speed
	time.sleep(1./60.)
	action = env.action_space.sample()
	obs, reward, done, _ = env.step(action)
	if done:
		break
```
