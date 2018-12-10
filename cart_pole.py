import gym

env = gym.make('CartPole-v0')  # Define the environment


def basic_policy(obs):
    angle = obs[2]
    return 0 if angle < 0 else 1


totals = []

for episode in range(100):
    episode_rewards = 0
    obs = env.reset()
    action = 1
    for steps in range(1000):
        action = basic_policy(obs)
        env.render()
        obs, reward, done, info = env.step(action)
        episode_rewards += reward
        if done:
            totals.append(episode_rewards)
            break

print(totals)
print('The longest time the pole was balanced: ', +str(max(totals)))
