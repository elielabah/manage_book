from pydantic import ConfigDict
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    port:int 
    host:str 
    environment:str 
    @property
    def debug(self):
        if self.environment=="development":
            return True
        return False
    model_config=ConfigDict(env_file=".env")
    
settings=Settings()    