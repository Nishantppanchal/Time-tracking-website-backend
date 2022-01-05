from django.contrib.auth.tokens import PasswordResetTokenGenerator

class emailVerificationTokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return str(user.pk)