from enum import Enum

class Module(Enum):
    CLIENTS: str = 'clients'
    PRODUCTS: str = 'products'
    PROFILES: str = 'profiles'
    PROVIDERS: str = 'providers'
    RENTERS: str = 'renters'
    SERVICES: str = 'services'
    USERS: str = 'users'