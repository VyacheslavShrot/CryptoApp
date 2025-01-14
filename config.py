from environs import Env

# Read End
env: Env = Env()
env.read_env('.env')


class Config:
    SECRET_KEY: str = env("SECRET_KEY")
