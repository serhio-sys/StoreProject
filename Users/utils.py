from django.contrib.auth.tokens import PasswordResetTokenGenerator

class GeneratorTokena(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp: int):
        return str(user.pk)+str(timestamp)+str(user.is_active)

email_activate_token = GeneratorTokena()