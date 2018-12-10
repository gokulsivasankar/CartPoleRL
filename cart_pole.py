import gym  # OpenAI environment

env = gym.make('CartPole-v0')  # define the environment


def basic_policy(obs):  # defining a basic policy
    angle = obs[2]  # the third element from the observed data
    # move the cart left or right based on the angle of the pole
    return 0 if angle < 0 else 1


totals = []  # collect the rewards for each simulation
n_episodes = 100  # number of episodes
n_steps = 1000  # number of steps per episode

for episode in range(100):
    episode_rewards = 0  # reward = 0 at the start of each epsiode
    obs = env.reset()  # perform an initial observation of the env
    action = 1
    for steps in range(1000):
        action = basic_policy(obs)  # determine the action to be applied
        env.render()  # plot the environment
        obs, reward, done, info = env.step(action)  # simulate the system
        episode_rewards += reward  # add the reward to the previous
        if done:
            totals.append(episode_rewards)  # append episode reward to totals
            break

print(totals)
print('The longest time the pole was balanced: ', +str(max(totals)))
