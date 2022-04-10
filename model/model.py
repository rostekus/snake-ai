from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import (
    Dense,
    Flatten,
    BatchNormalization,
)
from tensorflow.keras.optimizers import Adam
from rl.agents import DQNAgent
from rl.policy import BoltzmannQPolicy
from rl.memory import SequentialMemory

from snakegame import Game


class Agent:
    def __init__(self, actions, states):
        self.actions = actions
        self.states = states
        self.model = self.build_model_conv(self.states, self.actions)
        self.dqn = self.build_agent(self.model, self.actions)
        self.dqn.compile(Adam(lr=1e-3), metrics=["mae", "accuracy"])

    def build_model(self, states, actions):
        model = Sequential()
        model.add(Flatten(input_shape=(1,) + states))

        model.add(Dense(24, activation="relu"))

        model.add(Dense(48, activation="relu"))
        model.add(BatchNormalization())
        model.add(Dense(24, activation="relu"))

        model.add(Dense(actions, activation="softmax"))

        print(model.summary())
        return model

    def build_agent(self, model, actions):
        policy = BoltzmannQPolicy()
        memory = SequentialMemory(limit=50000, window_length=1)
        dqn = DQNAgent(
            model=model,
            memory=memory,
            policy=policy,
            nb_actions=actions,
            nb_steps_warmup=1000,
            target_model_update=1e-2,
        )
        return dqn


if __name__ == "__main__":
    env = Game()

    states = env.observation_space.shape
    actions = env.action_space.n
    print(env.step(1))
    print(states, actions)
    agent = Agent(actions, states)
    agent.dqn.fit(env, nb_steps=10000000, visualize=False, verbose=1)
    agent.model.save("model.h5")
