from environs import Env

# Read End
env: Env = Env()
env.read_env('.env')


class Config:
    SECRET_KEY: str = env("SECRET_KEY")

    POSTGRES_USER: str = env("POSTGRES_USER")
    POSTGRES_PASSWORD: str = env("POSTGRES_PASSWORD")

    SQLALCHEMY_DATABASE_URI: str = None

    JWT_SECRET_KEY: str = env("JWT_SECRET_KEY")
