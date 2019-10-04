import gym
import pybullet_envs
import pybullet as p

import time

p.connect(p.DIRECT)
env = gym.make('AntBulletEnv-v0')
env.render(mode='human')

env.reset()
for _ in range(10000):
	time.sleep(1/60.)
	action = env.action_space.sample()
	obs, reward, done, _ = env.step(action)
        if done:
            break
