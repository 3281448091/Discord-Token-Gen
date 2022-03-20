import random
import secrets

class FDiscord:

    def __init__(self):
        self.random_username = [
            "SuperMCPlayer",
            "AmongSUSSYBAKALOLOL",
            "SuperBowl",
            "Valorant",
            "JustinYT",
            "ImposterIsMe",
            "EldenRings",
            "PaTheG",
        ]

        self.random_email = [
            secrets.token_hex(10)
        ]

    def _get_fake_username(self):
        return random.choice(self.random_username)
    def _get_fake_email(self):
        # TODO
        return random.choice(self.random_email)

